#! /usr/bin/python
# -*- coding: utf-8 -*-

""" This file is a part of an application named viral_seq_classifier
    If you have any questions and/or comments, don't hesitate to 
    contact me by email wojciech.galan@gmail.com
    
    CopyLeft (C) 2016  Wojciech Gałan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>"""

import argparse
import os
import random
import cPickle as pickle

from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import commonFunctions

from SeqContainer import Container

# temp solution for current attribs
# todo allow any attribs
attribs = ('gi', 'host', 'host_lineage', 'length', 'lineage', 'molecule', 'nuc_frequencies', 'relative_nuc_frequencies_one_strand', 'relative_trinuc_freqs_one_strand')
# todo allow parameters for classifiers
classifier_dict = {
    'svm':SVC(),
    'knn':KNeighborsClassifier(),
    'qda':QuadraticDiscriminantAnalysis()
}

def getAttributesClassesIdsFeatures( att_list, objects, classes_infecting, classes_systematics=None ):
	'''Przyjmuje:
		- att_list - lista nazw atrybutów obiektów
		- objects - obiekty klasy UnifiedSequence, dla których wszystkie z atrybutów są notNone. De facto attributes i objects, to jedna z par klucz: wartość zwrócona przez processSetsOfNotNoneAttrs
		- classes_infecting - słownik postaci { nr_klasy:slownik_z_opisem }
			gdzie slownik_z_opisem jest postaci { 'Bacteria':1, 'Archaea':1 } - liczba określa jak głęboko w host_lineage szukać
			Przykład - 2 klasy - pierwsza zawiera wirusy zakażające Eukaryota, druga Bacteria i Archaea. classes_info będzie wyglądać:
			{ 0:{ 'Eukaryota':1 }, 1:{ 'Bacteria':1, 'Archaea':1 } }
		- classes_systematics - słownik postaci { nr_klasy:slownik_z_opisem }
			gdzie slownik_z_opisem jest postaci { 'Dependoparvovirus':4 } - liczba określa jak głęboko w lineage szukać
			Najpierw sprawdzana jest systematics - ze zbioru obiektów wybierane (i usówane) są wirusy należące do danej grupy, dopiero potem spośród pozostałych wirusów wybierane są wirusy zakażające określone organizmy.
	Zwraca:
		- np.array 2D z atrybutów
		- np.array z oznaczeń klas
		- lista id wirusów
		- lista stringów atrybutów. Jest to ważne, gryż niektóre atrybuty odpowiadające nazwom atrybutów wejściowyciowych (attributes) w rzeczywistości są słownikami
	UWAGA:
		- użytkownik musi sam zadbać o to, by classes_infecting były wewnętrznie rozłączne, tzn, nie było sytuacji, że mamy klasę infecting Eucaryota i infecting Deuterostomia. To samo ma  miejsce w przypadku classes_systematics'''
	vals_list = []
	cls_list = []
	gi_list = []
	feat_list = []
	container = Container( objects[:] )
	#pdb.set_trace()
	assert all( sorted(container.seqs[0].__dict__) == sorted(x.__dict__) for x in container.seqs )
	if classes_systematics:
		gi_to_remove = []
		for cls_num, cls_description in sorted( classes_systematics.iteritems(), key = lambda x:x[0] ):
			viruses = container.getVirusesOfLineage( cls_description.values()[0], cls_description.keys()[0] )
			for k, v in sorted( cls_description.items(), key = lambda x:x[0] )[1:]:
				viruses += container.getVirusesOfLineage( v, k )
			for virus in viruses:
				l = []
				for att in sorted( att_list ):
					if att not in [ 'host_lineage', 'lineage', 'gi', 'host' ]:
						if type( virus.__dict__[ att ] ) == dict:
							l.extend( virus.__dict__[ att ][x] for x in sorted( virus.__dict__[ att ] ) )
						else:
							l.append( virus.__dict__[ att ] )
				vals_list.append( l )
				cls_list.append( cls_num )
				gi_list.append( virus.gi )
			print "class %d contains %d elements" %( cls_num, len( viruses ) )
			#usówam wybrane sekwencje z kontenera
			gi_to_remove.extend([ virus.gi for virus in viruses ])
		container.removeIds( gi_to_remove )
	if classes_infecting:
		#pdb.set_trace()
		for cls_num, cls_description in sorted( classes_infecting.iteritems(), key = lambda x:x[0] ):
			how_much = 0
			sorted_cls_description_items = sorted( cls_description.items(), key = lambda x:x[0] )
			viruses_infecting_class = container.getVirusesInfectingSpeciviedGroup( sorted_cls_description_items[0][1], sorted_cls_description_items[0][0] )
			#pdb.set_trace()
			for k, v in sorted_cls_description_items[1:]:
				viruses_infecting_class += container.getVirusesInfectingSpeciviedGroup( v, k )
			for virus in viruses_infecting_class:
				l = []
				for att in sorted( att_list ):
					if att not in [ 'host_lineage', 'lineage', 'gi', 'host' ]:
						if type( virus.__dict__[ att ] ) == dict:
							l.extend( virus.__dict__[ att ][x] for x in sorted( virus.__dict__[ att ] ) )
						else:
							l.append( virus.__dict__[ att ] )
				vals_list.append( l )
				cls_list.append( cls_num )
				gi_list.append( virus.gi )
			print "class %d contains %d elements" %( cls_num, len( viruses_infecting_class ) )
	# ficzery
	'''try:
		#virus = viruses_infecting_class[0]
		viruses_ = viruses_infecting_class[0]
		x = 1
		pdb.set_trace()
		while not viruses_:
			viruses_.extend( viruses_infecting_class[x] )
			x+=1
		virus = viruses_[0]
	except UnboundLocalError:
		virus = viruses[0]'''
	virus = container[0]
	for att in sorted( att_list ):
		if att not in [ 'host_lineage', 'lineage', 'gi', 'host' ]:
			if type( virus.__dict__[ att ] ) == dict:
				feat_list.extend( '%s__%s' %( att, k ) for k in sorted( virus.__dict__[ att ] ) )
			else:
				feat_list.append( att )
	assert len( vals_list ) == len( cls_list ) == len( gi_list )
	return vals_list, cls_list, gi_list, feat_list

def balancedSubsample( value_arrays, class_list, id_list ):
	'''Wybiera klasę o minimalnej liczbie elementów, następnie zwraca wszstkie elementy z tej klasy oraz tą samą ilość losowych elementów z kazdej innej klasy. Zwraca kolejno:
	- value_arrays,
	- class_list,
	- id_list'''
	ret_val_arr, ret_classes, ret_ids = [], [], []
	assert len( value_arrays ) == len( class_list ) == len( id_list )
	indices_dict = { cl:[ i for i in range( len(class_list) ) if class_list[i]==cl ] for cl in set(class_list) }
	min_num = min( len(v) for v in indices_dict.values() )
	for key, val in sorted( indices_dict.iteritems(), key=lambda x:x[0] ):
		random.shuffle( indices_dict[ key ] )
		for index in val[:min_num]:
			ret_val_arr.append( value_arrays[index] )
			ret_classes.append( class_list[index] )
			ret_ids.append( id_list[index] )
	#pdb.set_trace()
	return ret_val_arr, ret_classes, ret_ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='') #todo dodać opis
    parser.add_argument('classifier_type', type=str, help='classifier: SVM, kNN or QDA')
    parser.add_argument('container', action="store", help='path to the container file produced by fetcher')
    parser.add_argument('--outdir', type=str, default=os.path.join(os.path.split(os.path.dirname(__file__))[0], 'files')\
                        , help='output directory')
    parser.add_argument('--scaller', type=str, default='scaller_'+commonFunctions.dateTime()+'.dump',
                        help="Scaller file name")
    parser.add_argument('--classifier', type=str, default='classifier_'+commonFunctions.dateTime()+'.dump',
                        help="Classifier file name")
    args = parser.parse_args()
    print args
    if not (args.classifier_type.lower() == 'svm' or args.classifier_type.lower() == 'knn' or args.classifier_type.lower() == 'qda'):
        raise ValueError("Classifier should be SVM, kNN or QDA")
    out_dir = args.outdir
    commonFunctions.createDirIfNotExists(out_dir)
    scaller_path = os.path.join(out_dir, args.scaller)
    classifier_path = os.path.join(out_dir, args.classifier)
    container = pickle.load(open(os.path.expanduser(args.container)))
    sets = commonFunctions.processSetsOfNotNoneAttrs(commonFunctions.setsOfNotNoneAttrs( container ) )
    sequences = sets[ attribs ]
    attributes, classes, ids, features = commonFunctions.getAttributesClassesIdsFeatures( attribs, sequences, { 0:{ 'Eukaryota':1 }, 1:{ 'Bacteria':1, 'Archaea':1 } } )
    scaller = StandardScaler()
    attributes = scaller.fit_transform(attributes)
    joblib.dump(scaller, scaller_path)
    classifier = classifier_dict[args.classifier]
    classifier.fit(attributes)
    joblib.dump(classifier, classifier_path)
    print 'Scaller and classifier saved in {}'.format(out_dir)
