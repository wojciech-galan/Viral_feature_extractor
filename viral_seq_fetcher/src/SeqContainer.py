#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This file is a part of an application named viral_seq_fetcher
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

import copy
import os
import types
import cPickle as pickle
import pdb

from constants import *

from UnifiedSeq import SeqRepresentation
from commonFunctions import dateTime


# ['environmental samples', 'unclassified viruses', 'dsRNA viruses', 'dsDNA viruses, no RNA stage', 'unassigned ssRNA viruses', 'ssRNA negative-strand viruses', 'ssRNA positive-strand viruses, no DNA stage', 'unclassified ssRNA viruses', 'ssDNA viruses', 'unassigned viruses', 'unclassified phages', 'Satellites', 'unclassified archaeal viruses', 'Retro-transcribing viruses', 'unclassified virophages', 'Virus-associated RNAs', 'Deltavirus']
# ['environmental samples', 'unclassified viruses', 'unassigned viruses', 'unclassified phages', 'Satellites', 'unclassified archaeal viruses', 'unclassified virophages', 'Virus-associated RNAs', 'Deltavirus']

class Container(object):
    '''Kontener reprezentacji sekwencji'''

    def __init__(self, seq_representations, created=None):
        '''Argumenty:
            - seq_representations - lista/krotka obiektów typu SeqRepresentation
            - created - kiedy został utworzony'''
        super(Container, self).__init__()
        self.seqs = copy.deepcopy(seq_representations)
        # if created:
        # 	self.created = created
        # else:
        # 	self.created = dateTime()
        self.created = dateTime()

    @classmethod
    def fromFile(cls, path):
        with open(path, 'rb') as f:
            obj = pickle.load(f)
        return obj

    # jak nie podziała - patrz tu: http://stackoverflow.com/questions/19305296/multiple-constructors-in-python-using-inheritance

    def __add__(self, other):
        if type(self) == type(other):
            assert self.created == other.created
            return Container(copy.deepcopy([x for x in self.seqs]) + copy.deepcopy([x for x in other.seqs]),
                             self.created)
        assert all(type(element) == SeqRepresentation for element in other)
        return Container(copy.deepcopy(self.seqs) + other, created=self.created)

    def __radd__(self, other):
        if other == 0:
            return copy.deepcopy(self)
        return self + other

    def __len__(self):
        if type(self.seqs) == types.GeneratorType:
            self.seqs = [x for x in self.seqs]
        return len(self.seqs)

    def __iter__(self):
        return iter(self.seqs)

    def __getitem__(self, a_slice):
        return self.seqs.__getitem__(a_slice)

    def __sub__(self, other):
        assert all(type(element) == SeqRepresentation for element in other)
        ret = []
        other_gis = [seq.gi for seq in other]
        for seq in self.seqs:
            if seq.gi not in other_gis:
                ret.append(copy.deepcopy(seq))
        return Container(ret, self.created)

    # def save( self, name='' ):
    # 	proper_name = False
    # 	f_name = self.created + '_' + name
    # 	while not proper_name:
    # 		if f_name in os.listdir( containers_path ):
    # 			if f_name == self.created:
    # 				f_name = self.created + '_1'
    # 			else:
    # 				v = int( f_name.split('_')[1] )
    # 				f_name = '%s_%d' %( self.created, v+1 )
    # 		else:
    # 			proper_name = True
    # 	with open( os.path.join(containers_path, f_name), 'wb' ) as f:
    # 		pickle.dump( self, f, pickle.HIGHEST_PROTOCOL )

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def getDsRNAViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'dsRNA viruses'], self.created)

    def getDsDNAViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'dsDNA viruses, no RNA stage'], self.created)

    def getSsDNAViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'ssDNA viruses'], self.created)

    def getSsRNAViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'ssRNA viruses'], self.created)

    def getUnassignedSsRNAViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'unassigned ssRNA viruses'], self.created)

    def getSsRNANegativeStrandViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'ssRNA negative-strand viruses'], self.created)

    def getSsRNAPositiveStrandViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'ssRNA positive-strand viruses, no DNA stage'],
                         self.created)

    def getUnclasifiedSsRNAViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'unclassified ssRNA viruses'], self.created)

    def getRetroViruses(self):
        return Container([x for x in self.seqs if x.lineage[1] == 'Retro-transcribing viruses'], self.created)

    def getVirusesInfectingSpeciviedGroup(self, level, group_name):
        '''Pobiera wirusy infekujące określoną grupę organizmów. Argumenty:
            - level - pozycja w host_lineage, na której znajduje się nazwa grupy, liczona od 0
            - group_name - nazwa grupy'''
        return Container([x for x in self.seqs if
                          x.host_lineage and len(x.host_lineage) > level and x.host_lineage[level] == group_name],
                         created=self.created)

    def getVirusesOfLineage(self, level, clad_name):
        '''Pobiera wirusy należące do danego kladu. Argumenty:
            - level - pozycja w lineage, na której znajduje się nazwa kladu, liczona od 0
            - clad_name - nazwa kladu'''
        return Container(
            [x for x in self.seqs if x.lineage and len(x.lineage) > level and x.lineage[level] == clad_name],
            created=self.created)

    def removeIds(self, to_remove):
        self.seqs = [x for x in self.seqs if x.gi not in to_remove]

    def getDependoviruses(self):
        return Container([x for x in self.seqs if len(x.lineage) > 4 and x.lineage[4] == 'Dependoparvovirus'],
                         self.created)

    def getVirusesWithHost(self):
        '''Pobiera tylko wirusy z not None polem Host'''
        return Container([x for x in self.seqs if x.host])

    def getIds(self):
        return [seq.gi for seq in self]


if __name__ == '__main__':
    pass
