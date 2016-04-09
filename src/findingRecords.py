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

from Bio import Entrez


def findRecords(term, database, retmax=0):
    # if retmax==0 - dostajemy wszystkie rekordy
    if not retmax:
        handle = Entrez.esearch(db=database, term=term)
        record = Entrez.read(handle)
        retmax = record['Count']
    handle = Entrez.esearch(db=database, term=term, retmax=retmax)
    print handle.geturl()
    id_list = Entrez.read(handle)['IdList']
    handle.close()
    print "Found %s ids" % len(id_list)
    return id_list
