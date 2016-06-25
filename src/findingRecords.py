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
import os
import time
import pdb
import socket
import httplib
import urllib2
import logging
import socket

import cPickle as pickle

from lxml import etree
from Bio import Entrez

from LittleParser import LittleParser
from simple_classes import UnexpectedValueException

CONF = json.load(open("../etc/conf.json"))
logger = logging.getLogger(os.path.basename(__file__))

def findRecords(term, database, debug=False, retmax=0):
	# if retmax==0 - dostajemy wszystkie rekordy
	if debug:
		return ['985485914', '1013949532', '1013949529', '1013949526']
	if not retmax:
		handle = Entrez.esearch(db=database, term=term)
		record = Entrez.read(handle)
		retmax = record['Count']
	handle = Entrez.esearch(db=database, term=term, retmax=retmax)
	#print handle.geturl()
	id_list = Entrez.read(handle)['IdList']
	handle.close()
	print "Found %s ids" % len(id_list)
	return id_list

def createEmptyFile(path):
	"""
	Creates empty file if it doesn't exist
	:param path:
	:return: None
	"""
	#pdb.set_trace()
	if not os.path.exists(path):
		directory = path.rsplit(os.sep, 1)[0]
		if not os.path.exists(directory):
			os.makedirs(directory)
		open(path, 'w').close()

def createDirIfNotExists(path):
	if not os.path.exists(path):
		os.makedirs(path)

def findHost(term, id_list, debug, seq_directory=CONF['seq_dir'], tax_directory=CONF['taxonomy_dir'],\
			 improper_host_path=CONF['improper_host_path'], rettype='xml'):
	'''Argumenty:
	- term - to co dostajemy po termCreation
	- ids - lista identyfikatorow sekwencji z bazy nuccore
	- temp_directory - folder na czesciowe wyniki
	- directory - w którym folderze ma być to zapisywane
	- seq_directory - folder na pliki xml z sekwencjami
	- tex_directory - folder na pliki xml z bazy taxonomy'''
	seqs_with_host=[]
	seqs_without_host=[]
	seqs = []
	createEmptyFile(improper_host_path)
	createDirIfNotExists(tax_directory)
	createDirIfNotExists(seq_directory)
	#if not os.path.exists(seq_directory):
	#    os.mkdir(containers_path)
	# try:
	# 	os.mkdir( '../prints' )
	# except OSError:
	# 	pass
	while id_list:
		print '%s ids left'%len(id_list)
		id_ = id_list[0]
		path = os.path.join(seq_directory, id_)
		while not os.path.exists(path):
			try:
				handle = Entrez.efetch(db="nuccore", id=id_, rettype=rettype, retmode="text")
				print handle.geturl()
				with open(path, 'w') as file_handle:
					file_handle.write(handle.read())
				print "written on disk"
			except (urllib2.URLError, socket.timeout, socket.error), e:
				logger.error(e)
				print e
				time.sleep(1)
			except (KeyboardInterrupt, SystemExit), e:
				#dumping(seqs_with_host, seqs_without_host, id_list, host_fname, no_host_fname, ids_left_fname, temp_directory)
				logger.info(e)
				return
		try:
			with open(path) as handle:
				seq=LittleParser.fromHandle(handle, debug)
				seqs.append( seq )
			id_list.remove(id_)
		except (KeyboardInterrupt, SystemExit), e:
			logger.info(e)
			return
		except RuntimeError, e:
			logger.error(e)
			print e
			time.sleep(1)
		#except (Entrez.Parser.NotXMLError, httplib.IncompleteRead):
		except ( etree.XMLSyntaxError, socket.error, httplib.IncompleteRead, urllib2.URLError, NameError ), e:
			#raise
			print "Parsing error while parsing %s%s"%(seq_directory, id_)
			logger.error(e)
			try:
				os.remove(os.path.join(seq_directory, id_))
			except (IOError, OSError), er:
				logger.info(er)
			#dumping(seqs_with_host, seqs_without_host, id_list, host_fname, no_host_fname, ids_left_fname, temp_directory)
			time.sleep(1)
		except NameError, e:
			logger.debug(e)
			# RuntimeException thrown by BioPython - it's BioPython's bug
			# should be RuntimeError
			time.sleep(1)
		finally:
			handle.close()
			#raise
	#print countProper(), 'proper sequences'

	# part_name=term+'_'+dateTime()
	# host_fname=toFileName(part_name)+'_host.dump'
	# no_host_fname=toFileName(part_name)+'_no_host.dump'
	# ids_left_fname=toFileName(part_name)+'_ids_left.dump'
	#
	# #dumping(seqs_with_host, seqs_without_host, id_list, host_fname, no_host_fname, ids_left_fname, directory)
	# #shutil.rmtree(temp_directory)
	# difflist = [ x for x in os.listdir(seq_directory) if x not in os.listdir( '../prints' ) ]
	# open( '../seqs', 'w' ).write( '\n\n'.join( [str(s) for s in seqs] ) )
	# open( '../prints/diff', 'w' ).write( '\n'.join( difflist ) )
	# container = Container( seqs )
	# container.save()
	return id_list