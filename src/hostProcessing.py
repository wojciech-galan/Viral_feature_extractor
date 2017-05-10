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

import pdb
import os
import httplib
import socket
import urllib2
import re
import time

from Bio import Entrez
import logging
from lxml import etree
from daos import SpeciesDAO
from entities import Species

import timeout
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


def getAllHosts(tax_dir):
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
        except urllib2.URLError, e:
            logger.error(e)
        finally:
            try:
                handle.close()
            except UnboundLocalError:
                pass
    print len(id_list), retmax
    ret_dict = {}
    while id_list:
        host_id = id_list[0]
        res = lineage(host_id, tax_dir)
        id_list.remove(host_id)
        if not res:  # event already logged in function lineage
            continue
        print len(id_list), "ids left", res
        ret_dict[host_id] = res
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


def findHostInNCBITaxonomy(host_name, tax_dir, debug=True):
    '''Szuka organizmu w NCBI Taxonomy'''
    done = False
    while not done:
        try:
            handle = Entrez.esearch(db='taxonomy', term=host_name)
            print "Looking for host in %s" % handle.geturl()
            id_list = Entrez.read(handle)['IdList']
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
            host_data = lineage(id_list[0], tax_dir)
            SpeciesDAO().create(Species.fromStrings(id_list[0], host_data[0], host_data[1]))
            host_data[1] = host_data[1].split('; ')
    else:
        if debug:
            logger.debug('findHostInNCBITaxonomy had problem with %s host name' % host_name)
        return None  # TODO do poprawy
    return host_data[1]  # to lineage


def findHostLineage(host_name, tax_dir, debug=True):
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
            return findHostLineage(name, tax_dir=tax_dir, debug=debug)
    # teraz sprawdzamy, czy nazwa usera nie zaczyna się przypadkiem którąś z nazw z bazy
    elif len(host_name.split()) > 1 and not (host_name.endswith(' sp.') or host_name.endswith(' L.')):
        for name in HOST_NAMES:
            if host_name.startswith(name) and len(name) > 2:
                return hostAlreadyInDb(name)[0].lineage
        if ';' in host_name:
            # pdb.set_trace()
            return findHostLineage(host_name.split(';')[0].strip(), tax_dir=tax_dir, debug=debug)
        else:
            logger.error("EROR while processing host_name %s" % host_name)
    elif len(host_name.split()) > 1 and (host_name.endswith(' sp.') or host_name.endswith(' L.')):
        # pdb.set_trace()
        return findHostLineage(host_name[:-3].strip(), tax_dir=tax_dir, debug=debug)
    else:
        # szukamy hosta w NCBI Taxonomy
        # pdb.set_trace()
        return findHostInNCBITaxonomy(host_name, tax_dir, debug=debug)
        # TODO logowanie, gdy tu coś pójdzie nie tak


def lineage(host_id, tax_directory):
    '''Bierze ID gatunku z bazy NCBi taxonomy.
    Zwraca krotkę ( name, lineage )'''
    # @timeout.timeout(timeout)
    # def timeoutedEntrezRead(db, id_):
    # 	handle = Entrez.efetch(db='taxonomy', id=id_)
    # 	print handle.geturl()
    # 	content = handle.read()
    # 	handle.close()
    # 	return content
    tax_path = os.path.join(tax_directory, host_id)
    try:  # os.path.exists(tax_path):
        with open(tax_path) as handle:
            try:
                content = Entrez.read(handle)
            except (Entrez.Parser.NotXMLError, Entrez.Parser.CorruptedXMLError), e:
                logger.debug(e)
                os.remove(tax_path)
                return lineage(host_id, tax_directory)
    except IOError:  # file doesn't exist
        while True:
            try:
                # content = timeoutedEntrezRead('taxonomy', host_id)
                handle = Entrez.efetch(db='taxonomy', id=host_id)
                print handle.geturl()
                content = handle.read()
                open(tax_path, 'w').write(content)
                handle.close()
            except (etree.XMLSyntaxError, socket.error, httplib.IncompleteRead, urllib2.URLError, socket.timeout), e:
                logger.error(e)
                continue
            handle = open(tax_path)
            try:
                content = Entrez.read(handle)
            except Entrez.Parser.NotXMLError, e:
                logger.error(e)
                os.remove(tax_path)
                continue
            finally:
                handle.close()
            break
    if len(content) == 0:
        logger.info("Didn't found anything in NCBI for host_id %s" % host_id)
        return None
    elif len(content) > 1:
        logger.info("Strange content for host_id %s: %s" % (host_id, str(content)))
        return None
    return [content[0]['ScientificName'], content[0]['Lineage']]


if __name__ == '__main__':
    import socket
    import argparse

    log_filename = os.path.join(os.path.dirname(__file__), CONF['log_file'])
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_filename,
                        filemode='w')
    parser = argparse.ArgumentParser(description='Short sample description')
    parser.add_argument('--email', action="store")
    parser.add_argument('--timeout', action="store", default=5, type=int)
    result = parser.parse_args()
    Entrez.email = result.email
    timeout = result.timeout
    socket.setdefaulttimeout(timeout)
    hosts = getAllHosts(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'files', CONF['taxonomy_dir']))
    putHostsInDb(hosts, True)
