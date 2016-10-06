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

import os.path
import json

searchURL  = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
fetchURL  = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'

DIR_NAME = os.path.split(os.path.dirname(__file__))[0]
CONF_PATH = os.path.join(DIR_NAME, 'etc', 'conf.json')
CONF = json.load(open(CONF_PATH))

parser_classes_dir = os.path.join(os.path.dirname(__file__), 'parser_classes')
# temp_dir='../temp_fetched_data/'
# res_dir='../fetched_data/'
# seq_dir = os.path.join(DIR_NAME, 'sequences')
# tax_dir = os.path.join(DIR_NAME, 'taxonomy')
# pars_err_dir='../errors'
# bad_hosts_path = '../bad_host'
database_path=os.path.join(DIR_NAME, 'databases')
# containers_path=os.path.join(DIR_NAME, 'containers')

strange_orgname='dziwna budowa orgname w tym pliku'

acid_to_number = {'dna':1.0, 'rna':0.0}
strands_to_number = {'ss':1.0, 'ds':2.0, 'mixed':1.5}

NA_IUPAC = {'A':('A',), 'C':('C',), 'G':('G',), 'T':('T',),
            'R':('A','G'), 'Y':('C','T'), 'M':('A','C'), 'K':('G','T'),
            'S':('C','G'), 'W':('A','T'), 'B':('C','G','T'), 'D':('A','G','T'),
            'H':('A','C','T'), 'V':('A','C','G'), 'N':('A','C','G','T')}

AA_IUPAC = {'A':('A',), 'C':('C',), 'D':('D',), 'E':('E',), 'F':('F',),
            'G':('G',), 'H':('H',), 'I':('I',), 'K':('K',), 'L':('L',),
            'M':('M',), 'N':('N',), 'P':('P',), 'Q':('Q',), 'R':('R',),
            'S':('S',), 'T':('T',), 'V':('V',), 'W':('W',), 'Y':('Y',),
            '_':('_',), 'B':('D','N'), 'Z':('E','Q'),
            'X':('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')}

transcription_dict={'A':'T', 'C':'G', 'G':'C', 'T':'A', 'U':'A', 'R':'Y',
                    'Y':'R', 'N':'N', 'M':'K', 'K':'M', 'S':'W', 'W':'S',
                    'B':'V', 'V':'B', 'D':'H', 'H':'D'}

stop_code = '_'
any_codon_code = 'x'

#zdefiniowane w razie potrzeby dzielenia przez zero - co zwrócić
RSCU_ZERO = 0
CAI_ZERO = 0

if __name__ == '__main__':
	print DIR_NAME
