#!/usr/bin/python
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


class BaseEntity(object):
    def __init__(self):
        super(BaseEntity, self).__init__()

    def __repr__(self):
        return repr(self.__dict__)


class Species(BaseEntity):
    '''Opisuje gatunek na podstawie danych z NCBI Taxonomy'''

    def __init__(self, in_dict):
        '''Argumenty: in_dict zawiera klucze tax_id, name, lineage
            - tax_id - id gatunku z bazy NCBI Taxonomy
            - name - nazwa łacińska
            - lineage - lineage w postaci 'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Orthopteroidea; Dictyoptera; Isoptera; Termitidae; Termitinae; Amitermes group; Microcerotermes' '''
        super(Species, self).__init__()
        self.tax_id = in_dict['tax_id']
        self.name = in_dict['name']
        self.lineage = in_dict['lineage']

    @classmethod
    def fromIterable(cls, iterable):
        '''Zakładamy, że wartości w iterable są poukładane w odpowiedniej kolejności'''
        obj_dict = {}
        obj_dict['tax_id'] = iterable[0]
        obj_dict['name'] = iterable[1]
        obj_dict['lineage'] = eval(iterable[2])
        return cls(obj_dict)

    @classmethod
    def fromStrings(cls, tax_id, name, lineage):
        obj_dict = {}
        obj_dict['tax_id'] = tax_id
        obj_dict['name'] = name
        obj_dict['lineage'] = lineage.split('; ')
        return cls(obj_dict)
