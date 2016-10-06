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

import time
import math
import copy
import pdb
import itertools

import numpy

from constants import *
from genetic_codes import *

def dateTime():
    return '_'.join(time.ctime().split(' '))

def toFileName(in_str):
    "zmienia string w dopuszczalna nazwe pliku"
    return in_str.replace(' ', '_').replace('.', '_').replace('/','_').replace('\\','_').replace('?', '_').replace('%', '_').replace('*', '_').replace(':', '_').replace('|', '_').replace('"', '_').replace('<', '_').replace('>', '_')

def getElement(a_dict, key):
    try:
        return a_dict[key]
    except KeyError:
        return ' '

def listAnd(a_list, b_list):
    #zwraca cześć wspólną obu list
    ret_list=[]
    for element in a_list:
        if element in b_list:
            ret_list.append(element)
    return ret_list

def listSub(a_list, b_list):
    #zwraca elementy listy a nie występujące w liście b
    ret_list=[]
    for element in a_list:
        if element not in b_list:
            ret_list.append(element)
    return ret_list

def listXor(a_list, b_list):
    #zwraca elementy listy a nie występujące w liście b
    return list(set(a_list)^set(b_list))

def constant(f):
    #from http://stackoverflow.com/questions/2682745/creating-constant-in-python
    def fset(self, value):
        raise SyntaxError ("You can't change a constant!")
    def fget(self):
        return f(self)
    return property(fget, fset)

def constantIfProper(f):
    #from http://stackoverflow.com/questions/2682745/creating-constant-in-python
    def fset(self, value):
        raise SyntaxError ("You can't change a constant!")
    def fget(self):
        if self:
            return f(self)
        raise AttributeError("Object doesn't contain proper values, so can't return them")
    return property(fget, fset)

def overrides(interface_class):
    #http://stackoverflow.com/questions/1167617/in-python-how-do-i-indicate-im-overriding-a-method
    #like in java
    #ale jednak nie działa
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

def myEval(expression):
    try:
        return eval(expression)
    except (SyntaxError, NameError, TypeError):
        #gdy wyrażenie jest zwykłym ciągiem znaków
        return expression

def createDirIfNotExists( path ):
	'''Tworzy katalog o podanej ścieżce, jeśli wcześniej taki nie istnieje'''
	try:
		os.makedirs( path )
	except OSError:
		pass

def createFileIfNotExists( path ):
	'''Tworzy plik o podanej ścieżce, jeśli wcześniej taki nie istnieje'''
	if not os.path.exists( path ):
		dir_path = path.rsplit( os.sep, 1 )[ 0 ]
		createDirIfNotExists( dir_path )
		open( path, 'w').write( '' )

def reverseComplement(a_string, transcript_dict=transcription_dict):
    a_list=[transcript_dict[s] for s in a_string]
    a_list.reverse()
    return ''.join(a_list)

def arithmeticMean(iterable):
    return sum(iterable)/float(len(iterable))

def std( a_list ):
	return numpy.std( a_list )

def weightedArithmeticMean( in_dict={}, values=[], weights=[] ):
	'''Zwraca średnią ważoną. Można podać słownik, lub osobno listę wartości i listę ich wag.
	Argumenty:
		- in_dict - słownik postaci {liczba:waga}
		- values - lista wartości
		- weights - lista wag'''
	assert bool( in_dict ) != bool( values or weights )
	if in_dict:
		values = in_dict.keys()
		weights = in_dict.values()
	assert len( values ) == len( weights )
	if math.fabs( sum( weights ) - 1 ) < 0.0001:
		# normalizacja wag
		w_sum = sum( weights ) * 1.0 # jest gwarantowany float
		weights = [ w/w_sum for w in weights ]
	return numpy.average( values, weights=weights )

def weightedStandardDeviation( in_dict={}, values=[], weights=[] ):
	'''Zwraca ważone odchylenie standardowe. Implementacja według:
	http://pl.wikipedia.org/wiki/Odchylenie_standardowe#Wa.C5.BCone_odchylenie_standardowe
	Można podać słownik, lub osobno listę wartości i listę ich wag.
	Argumenty:
		- in_dict - słownik postaci {liczba:waga}
		- values - lista wartości
		- weights - lista wag'''
	assert bool( in_dict ) != bool( values or weights )
	if in_dict:
		values = in_dict.keys()
		weights = in_dict.values()
	assert len( values ) == len( weights )
	assert len( values ) >1
	if math.fabs( sum( weights ) - 1 ) > 0.0001:
		# normalizacja wag
		w_sum = sum( weights ) * 1.0 # jest gwarantowany float
		weights = [ w/w_sum for w in weights ]
	# liczenie wariancji
	mean = weightedArithmeticMean( values=values, weights=weights )
	n = len( values )
	variance = sum( weights[i] * ( values[i]-mean )**2 for i in range( n ) )/( n-1.0 )
	return math.sqrt(variance)

def sampleStandardDeviation(iterable):
    l=len(iterable)
    x2=[x**2 for x in iterable]
    return math.sqrt(float(l)/(l-1)*(arithmeticMean(x2)-arithmeticMean(iterable)**2))

def betterCount(sequence, word):
    '''Return the number of overlapping occurrences of substring 'word' in
    string 'sequence' '''
    ret_val=0
    pos=sequence.find(word)
    pos+=1
    while pos:
        pos=sequence.find(word, pos)
        ret_val+=1
        pos+=1
    return ret_val

def combinations (n, inlist, outlist=[]):
    '''Funkcja rekurencyjna ktora tworzy wszystkie mozliwe kombinacje
    danych znakow o okreslonej dlugosci
    - n - dlugosc
    - inlist - lista znakow
    - outlist - wynik'''
    if n==0:
        return outlist
    else:
        if outlist:
            new_outlist=[]
            for element in outlist:
                new_outlist.extend([element+x for x in inlist])
            return combinations(n-1, inlist, new_outlist)
        else:
            return combinations(n-1, inlist, inlist)

def makeCombinations(oligo_nuc, iupac=NA_IUPAC):
    '''Zwraca listę rzeczywistych oligonukleotydów na podstawie
    oligonukleotydu w skład którego wchodzą nuc zdegenerowane'''
    oligo_nuc_list=[]
    for nuc in oligo_nuc:
        for key in iupac.keys():
            if nuc in key:
                nucs=iupac[key]
                break
        if oligo_nuc_list:
            new_oligo_nuc_list=[]
            for element in oligo_nuc_list:
                new_oligo_nuc_list.extend(['%s%s'%(element, x) for x in nucs])
            oligo_nuc_list = new_oligo_nuc_list
        else:
            oligo_nuc_list=nucs
    return set(oligo_nuc_list)

def listSum(list_of_lists):
	'''zwraca listę będącą sumą elementów iterowalnych w argumencie wejściowym. Przykłady:
	>>> listSum([['GAT', 'GAC'], ['AAC', 'AAT']])
	['GAT', 'GAC', 'AAC', 'AAT']
	>>> listSum([['GAT', 'GAC'], ['AAC', 'AAT'], 'ACGTA'])
	['GAT', 'GAC', 'AAC', 'AAT', 'A', 'C', 'G', 'T', 'A']'''
	result=[]
	for sub_list in list_of_lists:
		result.extend(sub_list)
	return result

def translate(seq, code=gencode_SG1, n_iupac=NA_IUPAC, a_iupac=AA_IUPAC, any_codon = any_codon_code):
	'''wykonuje translację zgodnie z określonym kodem genetycznym.
	W razie, gdyby w sekwencji znalazł się kodon zdegenerowany odpowiadający również kodonom stop, dołączany jest znak "any_codon"'''
	seq.replace('U','T')
	seq=seq.upper()
	if len(seq)%3:
		seq = seq[0:3*(len(seq)//3)]
	try:
		protein=''.join(code[seq[x:x+3]] for x in range(0,len(seq),3))
	except KeyError:
		protein =''
		for x in range(0,len(seq),3):
		    try:
		        protein+=code[seq[x:x+3]]
		    except KeyError:
		        if not all([y in n_iupac.keys() for y in seq[x:x+3]]):
		            raise KeyError('Unproper character in codon %s'%seq[x:x+3])
		        combinations=makeCombinations(seq[x:x+3], n_iupac)
		        #print 'Dodajemy aminokwas "zdegenerowany"'
		        aa=None
		        for ke in sorted(a_iupac.keys(), key=lambda k:len(a_iupac[k])):
		            if combinations.issubset(listSum(revDict(code)[aa] for aa in a_iupac[ke])):
		                aa=ke
		                break
		        protein+=aa or any_codon
		    #print 'Protein =', protein
	return protein 

def product(a_list):
    '''zwraca iloczyn elementow listy'''
    return reduce(lambda x, y: x*y, a_list)

def frequence(sequence, nuc, count=0):
    if len(nuc)==1:
        count = count or sequence.count(nuc)
        return count/float(len(sequence))
    count = count or betterCount(sequence, nuc)
    return count/float(len(sequence)-len(nuc)+1)

'''def frequence(sequence, nuc):
    if len(nuc)==1:
        return seqence.count(nuc)/float(len(sequence))
    return betterCount(sequence, nuc)/float(len(sequence)-len(nuc)+1)'''

def nucList(sequence, length):
    '''Zwraca zakładające się podsekwencje danej sekwencji o żądanej długości'''
    return [sequence[x:x+length] for x in range(len(sequence)-length+1)]

def nucFrequencies(sequence, length, mono=('A', 'C', 'G', 'T')):
    '''zwraca częstości oligonukleotydów o zadanej długości + częstości mononukleotydów
    na danej nici'''
    ret_dict={}
    seq_len=len(sequence)
    mono_count=dict([(nuc, 0) for nuc in mono])
    desired_nucs=combinations(length, mono)

    for nuc in mono:
        count = betterCount(sequence, nuc)
        ret_dict[nuc]=frequence(sequence, nuc, count)
        mono_count[nuc]=count

    for nuc in desired_nucs:
        ret_dict[nuc]=frequence(sequence, nuc)
    
    if seq_len!=sum(mono_count.values()):
        #mamy zdegenerowane
        for nuc in sequence:
            if not nuc in mono:
                for sub_nuc in NA_IUPAC[nuc]:
                    ret_dict[sub_nuc]+=1.0/seq_len/len(NA_IUPAC[nuc])
        if length-1:
            for nuc in nucList(sequence, length):
                if not nuc in desired_nucs:
                    real_nucs=makeCombinations(nuc)
                    for real_nuc in real_nucs:
                        ret_dict[real_nuc]+=1.0/(seq_len-length+1)/len(real_nucs)
    return ret_dict

def zeroDivision(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0

def mergeLists( list_of_tup ):
	'''Przyjmuje listę krotek określających początki i końce list, które moga się nakładać. 
	Dla [ (0,5), (3,8), (10, 20) ] ma zwracać [ (0,8), (10, 20) ]'''
	if len( list_of_tup ) < 2:
		return list_of_tup
	temp_l = []
	for tup in list_of_tup:
		temp_l.extend( range( tup[0], tup[1] ) )
	temp_l = sorted( list( set( temp_l ) ) )
	ret_list = []
	start = min( temp_l )
	for x in range ( 1, len(temp_l) ):
		#print x, temp_l[x-1], temp_l[x]
		if temp_l[x] > 1 + temp_l[x-1]:
			ret_list.append( (start, temp_l[x-1]+1) )
			start = temp_l[x]
	ret_list.append( (start, temp_l[x]+1) )
	return ret_list

def revSubList( seq, list_of_tup_sub ):
	'''Argumenty:
		- seq - sekwencja
		- list_of_tup_sub - lista krotek opisujących początki i końce non-overlapping podsekwencji, które trzeba wykluczyć z danej
		Przykładowo, dla 'abcdefghij', [ (1,5), (7,9) ] zwraca [ (0,1), (5,7), (9,10) ] '''
	if len( list_of_tup_sub ) < 1:
		return [ (0, len(seq)) ]
	temp_s = set( range(0, len(seq)) )
	ret_list = []
	start = min( temp_s )
	for tup_sub in list_of_tup_sub:
		temp_s -= set( range( tup_sub[0], tup_sub[1] ) )
	if temp_s:
		temp_s = list( temp_s )
		temp_s.sort()
		for x in range( 1, len(temp_s) ):
			if temp_s[x] > 1 + temp_s[x-1]:
				ret_list.append( (start, temp_s[x-1]+1) )
				start = temp_s[x]
		ret_list.append( (start, temp_s[x]+1) )
		return ret_list
	else:
		return [ ]

"""def newRelativeNucFrequencies( in_dict, strands, transcript_dict=transcription_dict, na_iupac=NA_IUPAC ):
	'''Przyjmuje wynik działania nucFrequencies. Zwraca słownik z względnymi
	częstościami występowania poszczególnych sekwencji'''
	raise exception( "not finished" )
	assert strands in ( 1, 2 )
	mono_dict=dict([(x, in_dict[x]) for x in in_dict if len(x)==1])
	oligo_dict=dict([(x, in_dict[x]) for x in in_dict if len(x)>1])
	nuc_len = len( oligo_dict.keys()[0] )
	assert all( nuc_len == len(k) for k in oligo_dict )
	if len( mono_dict ) != 4:
		for k in set([ 'A', 'C', 'G', 'T' ]) - set( mono_dict ):
			mono_dict[ k ] = 0.0
	# jeśli oligo_dict jest niekompletny, tzn. dla niektórych oligo nie ma wpisów ( powinny być klucz:0 )
	if len( oligo_dict ) != nuc_len**2:
		for k in [ ''.join(x) for x in itertools.product( mono_dict, repeat=2 ) ]:
			if k not in oligo_dict:
				oligo_dict[ k ] = 0.0
	if not oligo_dict:
		return in_dict
	if strands == 1:
		return { x:float( in_dict[x] ) /( 11 ) } #źle """

def relativeNucFrequencies(in_dict, strands, transcript_dict=transcription_dict):
    '''Przyjmuje wynik działania nucFrequencies. Zwraca słownik z względnymi
    częstościami występowania poszczególnych sekwencji. Przyjmujemy, że częstość występowania opigo zależy tylko od mono, a nie np trinuc od dinuc'''
    #częstotliwość oligonuc na obu niciach liczona według:
    #http://www.pnas.org/content/89/4/1358.full.pdf
    #raise Exception("sprawdzić poprawność liczenia częstości na dwu niciach")
    mono_dict=dict([(x, in_dict[x]) for x in in_dict if len(x)==1])
    oligo_dict=dict([(x, in_dict[x]) for x in in_dict if len(x)>1])
    nuc_len=len(oligo_dict.keys()[0])
    assert all( nuc_len == len(k) for k in oligo_dict )
    if len( mono_dict ) != 4:
    	for k in set([ 'A', 'C', 'G', 'T' ]) - set( mono_dict ):
    		mono_dict[ k ] = 0
    # jeśli oligo_dict jest niekompletny, tzn. dla niektórych oligo nie ma wpisów ( powinny być klucz:0 )
    if len( oligo_dict ) != nuc_len**2:
    	for k in [ ''.join(x) for x in itertools.product( mono_dict, repeat=nuc_len ) ]:
    		if k not in oligo_dict:
    			oligo_dict[ k ] = 0
    #pdb.set_trace()
    if not oligo_dict:
        return in_dict
    if strands-1:
        try:
            return { x:2**(nuc_len-1)*(oligo_dict[x]+oligo_dict[reverseComplement(x)])/product([mono_dict[y]+mono_dict[transcript_dict[y]] for y in x]) for x in oligo_dict}
        except ZeroDivisionError:
            return { x:2**(nuc_len-1)*zeroDivision((oligo_dict[x]+oligo_dict[reverseComplement(x)]),product([mono_dict[y]+mono_dict[transcript_dict[y]] for y in x])) for x in oligo_dict}
    else:
        try:
            return { x:float(oligo_dict[x])/product([mono_dict[y] for y in x]) for x in oligo_dict}
        except ZeroDivisionError:
            return { x:float( zeroDivision(oligo_dict[x],product([mono_dict[y] for y in x])) ) for x in oligo_dict}

def thirdOrderBias( seq, strand, mono=('A', 'C', 'G', 'T'), transcript_dict=transcription_dict ):
	'''Częstotliwości względne nukleotdów w zależności od częstotliwości mono i di
	Patrz: http://www.pnas.org/content/89/4/1358.full.pdf '''
	assert len( seq ) > 2
	assert strand in ( 1, 2 )
	nuc_freqs = nucFrequencies( seq, 2 )
	mono_freqs 	= { k:v for k, v in nuc_freqs.iteritems() if len(k)==1 }
	di_freqs 	= { k:v for k, v in nuc_freqs.iteritems() if len(k)==2 }
	tri_freqs 	= { k:v for k, v in nucFrequencies( seq, 3 ).iteritems() if len(k)==3 }
	ret_dict = {}
	for key in tri_freqs:
		fxyz = tri_freqs[ key ]
		fixyz = tri_freqs[ reverseComplement(key) ]
		if fxyz==0 and ( strand==1 or (strand==2 and fixyz==0) ) :
			ret_dict[ key ] = 0.0
		else:
			fxy  = di_freqs [ key[:2] ]
			fyz  = di_freqs [ key[1:] ]
			fxnz = sum( tri_freqs[ '%s%s%s' %(key[0], n, key[2]) ] for n in mono )
			if strand==1:
				ret_dict[ key ] = float( fxyz ) * mono_freqs[ key[0] ] * mono_freqs[ key[1] ] * mono_freqs[ key[2] ] / ( fxy * fyz * fxnz )
			else:
				fix = mono_freqs[ transcript_dict[ key[0] ] ]
				fiy = mono_freqs[ transcript_dict[ key[1] ] ]
				fiz = mono_freqs[ transcript_dict[ key[2] ] ]
				fixy = di_freqs [ reverseComplement( key[:2] ) ]
				fiyz = di_freqs [ reverseComplement( key[1:] ) ]
				fixnz = sum( tri_freqs[ '%s%s%s' %(transcript_dict[key[2]], n, transcript_dict[key[0]]) ] for n in mono )
				ret_dict[ key ] = float(fxyz + fixyz) * (mono_freqs[key[0]] + fix) * (mono_freqs[key[1]] + fiy) * (mono_freqs[key[2]] + fiz) / ( 2 * (fxy + fixy) * (fyz + fiyz) * (fxnz + fixnz) )
	return ret_dict

def setsOfNotNoneAttrs( list_of_objects ):
	'''Pobiera listę obiektów z tymi samymi atrybutami. Niektóre z tych obiektów mają niektóre ze swoich atrybutów ustawione na None.
	Zwraca słownik { (krotka atrybutów):[ wszystkie z obiektów, w których te atrybuty nie są None ]}, przy czym staramy się zwrócić jak najliczniejsze krotki. Przykładowo, jeśli min ilość atrybutów not-None w obiektach wynosi 2, to nie zwracamy kluczy będących krotkami jednoelementowymi'''
	assert list_of_objects and all( set(an_object.__dict__.keys())==set(list_of_objects[0].__dict__.keys()) for an_object in list_of_objects )
	atts = list( set( tuple( i for i in el.__dict__.keys() if el.__dict__[i]!=None ) for el in list_of_objects ) )
	return { att:[ el for el in list_of_objects if all( el.__dict__[a]!=None for a in att ) ] for att in atts }

def processSetsOfNotNoneAttrs( in_dict ):
	'''Bierze wynik działania setsOfNotNoneAttrs. Funkcja setsOfNotNoneAttrs zwraca słownik, w którym niektóre atrybuty mogą być None. przykładowa para klucz:wartość to ( att1, att2 ):[ Obj1( 1, 2, 3 ), Obj2( 4, 5, None ) ]. Niniejsza funkcja "przytnie" obiekty tak, aby miały tylko wartości not-None, np. ( att1, att2 ):[ Obj1( 1, 2 ), Obj2( 4, 5 ) ]'''
	ret_dict = {}
	for key, val in in_dict.iteritems():
		a_list = []
		for obj in val:
			temp_obj = copy.deepcopy( obj )
			for att in set( temp_obj.__dict__.keys() ) - set( key ):
				del temp_obj.__dict__[att]
			a_list.append( temp_obj )
		#a_list.sort()
		key=list(key)
		key.sort()
		ret_dict[ tuple( key ) ] = a_list
	return ret_dict

def codons (sequence, mono=('A', 'C', 'G', 'T')):
	'''Przyjmuje uprzednio przygotowaną sekwencję KODUJĄCĄ
	Zwraca słownik postaci {'AAA':3, 'AAC':2, ... }'''
	possible_codons = combinations(3, ['A', 'C', 'G', 'T'])
	ret_dict = {}
	for codon in possible_codons:
		ret_dict[codon]=0
	for x in range ( 0, len(sequence), 3):
		nuc = sequence[x:x+3]
		if len( nuc ) != 3:
			# w sytuacji, gdy nie sekwencja jest jakas zjebana, np. za krótka - wtedy ostatni kodon w tej sekwencji może być niepewny
			# zwracamy wszystkie poza nim
			break
		if nuc in possible_codons:
			#nie zdegenerowane
			ret_dict[nuc]+=1 
		else:
			#zdegenerowane
			real_codons=makeCombinations(nuc)
			#print nuc, real_codons
			for real_codon in real_codons:
				ret_dict[real_codon]+=1.0/len(real_codons)
	return ret_dict

def codonFreqs (sequence, mono=('A', 'C', 'G', 'T')):
	'''Liczy częstości kodonów na nici kodującej'''
	codon_dict = codons (sequence, mono)
	ret_dict = {}
	for codon in codon_dict:
		ret_dict[codon]=codon_dict[codon]*3/float( len(sequence) )
	return ret_dict

def revDict(a_dict):
	'''Odwraca słownik - klucze stają się wartościami. W razie, gdyby w a_dict wielu kluczom odpowiadała jedna wartość,
	np. {'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A'}
	w zwracamym słowniku dostajemy 
	'A': ['GCA', 'GCC', 'GCG', 'GCT']'''
	b_dict={}
	for v in a_dict.values():
		b_dict[v]=[k for k in a_dict.keys() if a_dict[k]==v]
	return b_dict

def countSame( population ):
	'''Liczy ilości takich samych osobników w populacji, czyli np.
		population = ( 2, 2, 2, 4, 4 )
		countSame( population )  = [ (2,3), (4,2) ]'''
	try:
		unique = set( population )
	except TypeError:
		# unhashable type
		unique = []
		for el in population:
			if el not in unique:
				unique.append( el )
	return [ ( el, population.count(el) ) for el in unique ]

def setOfCorrelated( data, thresh ):
	'''Zwraca set skorelowanych ze sobą cech. Jeśli cechy a i b są skorelowane, oraz cechy b i c są skorelowane, to a, b i c tworzą grupę.
	Argumenty:
		- data - słownik { set(cecha_a, cecha_b) : wsp_korelacji }
		- threshold - przyjmujemy, że powyżej tej liczby cechy są skorelowane
		'''
	assert all([ isinstance( key, frozenset ) for key in data ])
	l = [ x for x, y in data.iteritems() if y >= thresh ]
	while True:
		num_of_elements = len( l )
		l = compress( l )
		if num_of_elements == len( l ):
			return l

def compress( l ):
	'''Funkcja pomocnicza do setOfCorrelated. "kompresuje" wejściową listę zbiorów, tzn z [ set(a,b), set(b,c), ... ] robi [ set(a,b,c), ... ]'''
	for x in range( len(l)-1 ):
		for y in range( x+1, len(l) ):
			if l[x].intersection( l[y] ):
				l[x] = l[x].union( l[y] )
				del l[y]
				return l
	return l

def setOfCompletellyCorrelated( data, thresh ):
	'''Zwraca set kompletnie skorelowanych ze sobą cech. a, b i c tworzą grupę, tylko jeśli pary (a,b), (b,c), (a,c) są skorelowane.
	Argumenty:
		- data - słownik { (cecha_a, cecha_b) : wsp_korelacji }
		- threshold - przyjmujemy, że powyżej tej liczby cechy są skorelowane'''
	assert all([ isinstance( key, frozenset ) for key in data ])
	l = [ x for x, y in data.iteritems() if y >= thresh ]
	all_feats = []
	for f in data:
		all_feats.extend( f )
	all_feats = list( set( all_feats ) )
	l = completellyCompress( l, all_feats, data, thresh )
	#pdb.set_trace()
	while True:
		num_of_elements = len( l )
		for element1 in l[:]:
			if len( element1 ) == 2:
				for element2 in l[:]:
					if len( element2 ) > 2:
						if element1.issubset( element2 ):
							l.remove( element1 )
							break
		if num_of_elements == len( l ):
			return l

def completellyCompress( l, all_feats, data, thresh ):
	'''Funkcja pomocnicza do setOfCompletellyCorrelated'''
	for x in range( len(l)-1 ):
		for feat1 in all_feats:
			threshs = []
			if feat1 not in l[x]:
				temp = list( l[x] )
				temp.append( feat1 )
				if set( temp ) in l:
					continue
				for feat2 in l[x]:
					try:
						threshs.append( data[ frozenset([ feat1, feat2 ]) ] >= thresh )
					except KeyError: #tzn nie ma w danych czegoś takiego
						threshs.append( False )
			if all( threshs ):
				l[x] = list( l[x] )
				l[x].append( feat1 )
				l[x] = frozenset( l[x] )
	return l

def euclideanDistance( vector1, vector2 ):
	'''Zwraca odległość euklidesową miiędzy dwoma wektorami'''
	assert len( vector1 ) == len( vector2 )
	return math.sqrt( sum([ math.pow( vector1[x]-vector2[x], 2 ) for x in range( len( vector1 ) ) ]) )

if __name__ == "__main__":
	'''a=nucFrequencies(100000*'AGATAN',2)
	print a
	print sum(a.values())'''
	b=nucFrequencies('AGATY',2)
	#print b
	#print sum(b.values())
	#print relativeNucFrequencies(b, 2)
	
	#print reverseComplement("AGATY")
	#print
	#print codons('AGATAAGATAAGATA')
	#print codons('AGATAAGATAAGARA')
	freqs1 = codonFreqs('AGATAAGATAAGARA')
	freqs2 = codonFreqs('AGATAAGATAAGATA')
	#print freqs1, sum(freqs1.values())
	
