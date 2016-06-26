#!/usr/bin/python
# -*- coding: utf-8 -*-

import pdb
import os
import httplib
import socket
import urllib2
import re

from Bio import Entrez
import logging
from lxml import etree
from daos import SpeciesDAO
from entities import Species

from constants import *
from species import species_dict

logger = logging.getLogger(os.path.basename(__file__))


def getHostNames():
	'''Zwraca listę wszystkich nazw hostów'''
	daos = SpeciesDAO()
	return [s.name for s in daos.read()]


###########################################################		uwaga!!!! stała!!!! 	###########################################
HOST_NAMES = tuple(getHostNames())
###########################################################			koniec!!!!		 	###########################################


def getAllHosts():
	'''Pobiera listę wszystkich gatunków z NCBI Taxonomy'''
	done = False
	while not done:
		try:
			handle = Entrez.esearch(db='taxonomy', term='species[rank] AND specified[prop]')
			record = Entrez.read(handle)
			retmax = record['Count']
			handle.close()
			handle = Entrez.esearch(db='taxonomy', term='species[rank] AND specified[prop]', retmax=retmax)
			id_list = Entrez.read(handle)['IdList']
			done = True
		except URLError, e:
			logger.error(e)
		finally:
			handle.close()
	print len(id_list), retmax
	ret_dict = {}
	while id_list:
		host_id = id_list[0]
		res = lineage(host_id)
		if not res:
			id_list.remove(host_id)  # pdb.set_trace()
			continue
		print len(id_list), res
		ret_dict[host_id] = res
		id_list.remove(host_id)
	return ret_dict


def putHostsInDb(hosts_dict, clear=False):
	'''Bierze słownik zwrócony przez getAllHosts.
	próbuje wpisać wszystko do bazy'''
	daos = SpeciesDAO()
	if clear:
		daos.clear()
		species_list = [{'tax_id': k, 'name': v[0], 'lineage': str(v[1].split('; '))} for k, v in
						hosts_dict.iteritems()]
		print "INSERTING DATA"
		daos.createFromListOfDicts(species_list)
	else:
		i = 0
		l = len(hosts_dict)
		for k, v in hosts_dict.iteritems():
			print i, l
			if not daos.read({'tax_id': k}):
				daos.create(Species.fromStrings(k, v[0], v[1]))
				i += 1


def hostAlreadyInDb(host_name):
	'''Odczytuje rekordy w bazie danych pasujące do host_name (powinien być co najwyżej 1).
	Zwraca:
	- listę obiektów typu Species, gdy host_name jest (powinien być jeden)
	- pustą listę, gdy host_name nie ma'''
	ret_val = SpeciesDAO().read({'name': host_name})
	assert len(ret_val) <= 1
	return ret_val


def idInDb(id_):
	return SpeciesDAO().read({'tax_id': id_})


def findHostInNCBITaxonomy(host_name, debug=True):
	'''Szuka organizmu w NCBI Taxonomy'''
	done = False
	while not done:
		try:
			handle = Entrez.esearch(db='taxonomy', term=host_name)
			print "Looking for host in %s" % handle.geturl()
			id_list = Entrez.read(handle)['IdList']
			print "id_list fetched"
			done = True
		except Exception, e:
			logger.error(e)
		finally:
			try:
				handle.close()
			except UnboundLocalError, e:
				logger.error(e)
				# pdb.set_trace()
	if len(id_list) == 1:
		host_already_in_db = hostAlreadyInDb(host_name)
		id_in_db = idInDb(id_list[0])
		if host_already_in_db:
			species = host_already_in_db[0]
			host_data = [species.name, species.lineage]
		elif id_in_db:
			species = id_in_db[0]
			host_data = [species.name, species.lineage]
		else:
			# pdb.set_trace()
			host_data = lineage(id_list[0])
			SpeciesDAO().create(Species.fromStrings(id_list[0], host_data[0], host_data[1]))
			host_data[1] = host_data[1].split('; ')
	else:
		if debug:
			open(bad_hosts_path, 'a').write('%s\n' % host_name)
		return None  # TODO do poprawy
	return host_data[1]  # to lineage


def findHostLineage(host_name, debug=True):
	'''szuka danych organizmu ( lineage ) na podstawie nazwy podanej przez użytkownika'''
	# najpierw sprawdzamy, czy nazwa podana przez usera jest w słowniku
	if host_name.lower() in species_dict:
		host_name = species_dict[host_name.lower()]
	# potem sprawdzamy, czy nazwa jest w bazie
	host_already_in_db = hostAlreadyInDb(host_name)
	if host_already_in_db:
		return host_already_in_db[0].lineage
	elif re.search('\(.+\)', host_name):
		found = re.search('\(.+\)', host_name)
		name = host_name[:found.start()] + host_name[found.end():]
		name = name.strip()
		host_already_in_db = hostAlreadyInDb(name)
		if host_already_in_db:
			return hostAlreadyInDb(name)[0].lineage
		else:
			return findHostLineage(name, debug)
	# teraz sprawdzamy, czy nazwa usera nie zaczyna się przypadkiem którąś z nazw z bazy
	elif len(host_name.split()) > 1 and not (host_name.endswith(' sp.') or host_name.endswith(' L.')):
		for name in HOST_NAMES:
			if host_name.startswith(name) and len(name) > 2:
				return hostAlreadyInDb(name)[0].lineage
		if ';' in host_name:
			# pdb.set_trace()
			return findHostLineage(host_name.split(';')[0].strip(), debug)
	elif len(host_name.split()) > 1 and (host_name.endswith(' sp.') or host_name.endswith(' L.')):
		# pdb.set_trace()
		return findHostLineage(host_name[:-3].strip(), debug)
	else:
		# szukamy hosta w NCBI Taxonomy
		# pdb.set_trace()
		return findHostInNCBITaxonomy(host_name, debug)
    # TODO logowanie, gdy tu coś pójdzie nie tak


def lineage(host_id, tax_directory=tax_dir):
	'''Bierze ID gatunku z bazy NCBi taxonomy.
	Zwraca krotkę ( name, lineage )'''
	# pdb.set_trace()
	if host_id in os.listdir(tax_directory):
		handle = open("%s%s" % (tax_directory, host_id))
		content = Entrez.read(handle)
	else:
		while True:
			try:
				handle = Entrez.efetch(db='taxonomy', id=host_id)
				open("%s%s" % (tax_directory, host_id), 'w').write(handle.read())
				handle.close()
			except (etree.XMLSyntaxError, socket.error, httplib.IncompleteRead, urllib2.URLError), e:
				logger.error(e)
				continue
			except socket.timeout, e:
				logger.error(e)
				print e
			handle = open("%s%s" % (tax_directory, host_id))
			try:
				content = Entrez.read(handle)
			except Entrez.Parser.NotXMLError, e:
				logger.error(e)
				os.remove("%s%s" % (tax_directory, host_id))
				continue
			finally:
				handle.close()
			break
	if len(content) != 1:
		return None  # pdb.set_trace()
	return [content[0]['ScientificName'], content[0]['Lineage']]


if __name__ == '__main__':
	pass
