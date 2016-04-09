#! /usr/bin/python
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

import json
import argparse

from Bio import Entrez
from findingRecords import *

CONF = json.load(open("../etc/conf.json"))

if __name__ == "__main__":
    #raise Exception('najpierw przekopiować to do "projekt" i uruchomić, potem przerzucić do klasy annotation')
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('email', action="store")
    result = parser.parse_args()
    Entrez.email=result.email
    #term = termCreation('complete', 'title', 'refseq', 'viruses')
    #print term
    # term na podstawie http://www.ncbi.nlm.nih.gov/genomes/GenomesHome.cgi?taxid=10239&hopt=faq#retrieve%20refseq
    term  = CONF['eutils_term']
    # https://www.biostars.org/p/126228/
    # 'srcdb_refseq[prop]' will restrict search to sequences which have been promoted into the redundant NCBI refsequence database
    # 'WGS[Properties]' will restrict search to contigs from WGS genomes
    print term
    control=1
    while control:
        try:
            ids=findRecords(term, "nuccore")
            control=0
        except IOError, e:
            print e
    print ids, len(ids)
    #findHost(term, ids)