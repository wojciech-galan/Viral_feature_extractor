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

import logging
import argparse
import socket

from Bio import Entrez
from findingRecords import *
from SeqContainer import Container
from commonFunctions import createDirIfNotExists

log_filename= os.path.join(os.path.dirname(__file__), CONF['log_file'])
createDirIfNotExists(os.path.dirname(os.path.abspath(log_filename)))

logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
					datefmt='%m-%d %H:%M',
					filename=log_filename,
					filemode='w')

if __name__ == "__main__":
	logger = logging.getLogger(os.path.basename(__file__))
	parser = argparse.ArgumentParser(description='Short sample description')
	parser.add_argument('--email', action="store")
	parser.add_argument('--timeout', action="store", type=int, default=5)
	parser.add_argument('--output', action="store", default=os.path.split(os.path.dirname(__file__))[0])
	parser.add_argument('--container', action="store", default='container.dump')
	# "d" stands for "debug"
	parser.add_argument('-d', action="store_true", default=False)
	result = parser.parse_args()
	#print result
	Entrez.email=result.email
	timeout = result.timeout
	out_dir = os.path.expanduser(result.output)
	debug = result.d
	container_path = os.path.join(out_dir, result.container)
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
			ids=findRecords(term, "nuccore", debug)
			control=0
		except IOError, e:
			logger.error(e)
			print e
	socket.setdefaulttimeout(timeout)
	tax_dir = os.path.join(out_dir, CONF['taxonomy_dir'])
	if os.path.exists(container_path):
		container = Container.fromFile(container_path)
		already_done = container.getIds()
		ids = [id_ for id_ in ids if id_ not in already_done]
		seq_representations = container.seqs
	else:
		seq_representations = []
	seq_representations.extend(findHost(term, ids, out_dir, debug, tax_directory=tax_dir))
	Container(seq_representations).save(container_path)
	# TODO niech loguje ID sekwencji, z którymi się coś nie udało
	# TODO niech (może przy pierwszym wywołaniu programu, na poczśtku) uzupełnia bazę hostów. - doing
	# TODO - sprawdzić, czy potem w miarę szybko jest dostęp do tych danych
	# TODO porównać profilerem, jak to wygląda czasowo dla jednego profilu robionego wcześniej, a drugiego w locie
	# TODO czy działa pod windą?
	# TODO zastanowić się dobrze nad debugiem - kiedy to jest potrzebne
	# może debug konkretnie dla takich plików, gdzie mogło coś nie pójść?
	# TODO ustalić odpowiedzialność leveli - i skorzystać z flagi DEBUG