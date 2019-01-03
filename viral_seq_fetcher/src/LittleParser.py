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

import os
import pdb
import logging

from lxml import etree

from ParserClasses import processFile

from constants import *
from commonFunctions import *
from SeqEntrySeq import StandaloneSeqEntrySeq, SeqEntrySeqException
from SeqEntrySet import SeqEntrySet
from UnifiedSeq import UnifiedSeq, SeqRepresentation, NoSequenceException

logger = logging.getLogger(os.path.basename(__file__))


class LittleParserException(Exception):
    pass


class LittleParser(object):
    '''Klasa ma znalezc gospodarza i organizm (w postaci Viruses; ssRNA positive-strand viruses, no DNA stage; Picornavirales; Picornaviridae; Enterovirus
    dla odpowiedniego pliku xml, oraz id, nazwe i sekwencje'''

    def __init__(self, **kwargs):
        super(LittleParser, self).__init__()
        for key, value in kwargs.iteritems():
            self.__dict__[key] = value

    @classmethod
    def fromDBRecord(cls, record, keys):
        object_dict = {}
        for nr, key in enumerate(keys, start=0):
            object_dict[key] = record[nr]
        return cls(**object_dict)

    @classmethod
    def fromHandle(cls, handle, fasta_path, taxonomy_dir, debug, verbose):
        '''handle - uchwyt do pliku lub zasobu w sieci'''
        object_dict = {}
        try:
            object_dict['_url'] = handle.geturl()
        except AttributeError:
            object_dict['_name'] = handle.name
        '''self._host_search_url=None
        self._host_fetch_url=[]
        self._organism=None
        self._host_ids=[]
        self._id=None
        self._name=None
        self._seq=None
        self._host_xml=None
        self._wiele_rezultatow_w_taxonomy=False
        self._coding_regions=[]
        self._described_regions=[]'''

        object_dict['_za_ktorym_razem'] = 0
        object_dict['_host'] = []
        # file is empty - throws XMLSyntaxError
        seq = _parse(handle, fasta_path, taxonomy_dir, debug, verbose)
        return seq

    @constantIfProper
    def length(self):
        return self._seq_len

    def hasHost(self):
        if self._host:
            return True
        return False

    def setHost(new_host_id):
        '''jeśli podczas sprawdzania okazało się że skryp nie ustalił gospodarza lub zrobił to niepoprawnie
        to podajemy prawidłowego. Parametry:
        - new_host_id - prawidłowy gospodarz - jego id w bazie taksonomy'''
        pass


def _parse(handle, fasta_path, taxonomy_dir, debug, verbose):
    object_dict = {}
    if verbose:
        print handle.name
    gi = os.path.basename(handle.name)
    int(gi)  # upewniam się, że to zawsze będzie numer
    root = processFile(handle)

    if root.bioseq_set_seq_set__.__dict__.keys() != ['to_evaluate', 'seq_entry_', 'name']:
        raise LittleParserException("root.bioseq_set_seq_set__.__dict__.keys() != ['to_evaluate', 'seq_entry_', 'name']")
    if len(root.bioseq_set_seq_set__.seq_entry_) != 1:
        raise LittleParserException("len(root.bioseq_set_seq_set__.seq_entry_) != 1")

    seq_entry_ = root.bioseq_set_seq_set__.seq_entry_[0]

    if 'seq_entry_seq_' in seq_entry_:
        try:
            seq_entry_seq = StandaloneSeqEntrySeq(seq_entry_.seq_entry_seq_, gi, fasta_path)
        except SeqEntrySeqException, sese:
            logger.debug("While processing %s: %s"(str(sese), gi))
            print sese.message
        uniSeq = UnifiedSeq(seq_entry_seq)
    elif 'seq_entry_set_' in seq_entry_:
        seq_entry_set = SeqEntrySet(seq_entry_.seq_entry_set_, gi, fasta_path)
        uniSeq = UnifiedSeq(seq_entry_set)
    else:
        raise LittleParserException("No seq_entry_seq_ nor seq_entry_set_ in seq_entry_")
    ssseq = SeqRepresentation(uniSeq, taxonomy_dir, debug, verbose)

    return ssseq
