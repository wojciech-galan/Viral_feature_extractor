#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "wojtek"
__date__ = "$2012-08-21 17:08:34$"

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
	def fromHandle(cls, handle, debug):
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
		seq = _parse(handle, debug)  # object_dict.update(_parse(handle))
		# try:
		# 	seq = _parse(handle)#object_dict.update(_parse(handle))
		# except Exception, e:
		# 	import traceback
		# 	print traceback.format_exc()
		# 	pdb.set_trace()
		return seq  # cls(**object_dict) # do wyjebania

	# if object_dict['_name']=='../sequences/158120308':
	#	open('aaaa', 'w').write(str(object_dict))

	# print 'strands=%s='%object_dict['_seq_strands']
	# if object_dict['_seq_strands'] and object_dict['_seq_strands']!='other':
	#     object_dict['_seq_strands']=strands_to_number[object_dict['_seq_strands']]
	# else:
	#     lineage1=object_dict["_lineage"][1]
	#     #print lineage1
	#     if "ssRNA" in lineage1 or "ssDNA" in lineage1:
	#         object_dict['_seq_strands']=1
	#     elif "dsRNA" in lineage1 or "dsDNA" in lineage1:
	#         object_dict['_seq_strands']=2
	# 	else:
	# 		logger.debug('lineage=%s'%str(lineage1))
	# if not object_dict['_seq_strands']:
	#     del object_dict['_seq_strands']
	# #---------------------observed nuc frequencies--------------------------
	# observed_mono_di_whole_one_strand=nucFrequencies(object_dict['_seq'], 2)
	# object_dict['_GC_content']=observed_mono_di_whole_one_strand['G']+observed_mono_di_whole_one_strand['C']
	# try:
	#     if object_dict['_seq_strands']-1:
	#         for nuc in observed_mono_di_whole_one_strand:
	#             if len(nuc)-1:
	#                 object_dict['_%s_observed_whole'%nuc]=(observed_mono_di_whole_one_strand[nuc]+observed_mono_di_whole_one_strand[reverseComplement(nuc)])/2
	#             else:
	#                 object_dict['_%s_observed_whole'%nuc]=(observed_mono_di_whole_one_strand[nuc]+observed_mono_di_whole_one_strand[transcription_dict[nuc]])/2
	#     else:
	#         for nuc in observed_mono_di_whole_one_strand:
	#             object_dict['_%s_observed_whole'%nuc]=observed_mono_di_whole_one_strand[nuc]
	#     #---------------------relative nuc frequencies----------------------
	#     relative_di_whole=relativeNucFrequencies(observed_mono_di_whole_one_strand, object_dict['_seq_strands'])
	#     for nuc in relative_di_whole:
	#         object_dict['_%s_relative_whole'%nuc]=relative_di_whole[nuc]
	#     #-------------------------------------------------------------------
	# except KeyError:
	#     #gdy nie mam wiadomości o nici
	#     getAndSaveErr( LittleParser() )
	#
	# if object_dict['_host_xml']:
	#     object_dict['_has_xml_host']=True
	# else:
	#     object_dict['_has_xml_host']=False
	# if object_dict['_host']:
	#     object_dict['_has_host']=True
	# else:
	#     object_dict['_has_host']=False
	# #time.sleep(0.333333334)
	# print
	# return cls(**object_dict)
	# print "sparsowane"
	# ----------------------------------------------------
	'''@constant
	def seq(self):'''

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


def _parse(handle, debug):
	object_dict = {}
	print handle.name
	gi = handle.name.rsplit('/', 1)[1]
	int(gi)  # upewniam się, że to zawsze będzie numer
	root = processFile(handle)

	if root.bioseq_set_seq_set__.__dict__.keys() != ['to_evaluate', 'seq_entry_', 'name']:
		pdb.set_trace()
	if len(root.bioseq_set_seq_set__.seq_entry_) != 1:
		pdb.set_trace()

	seq_entry_ = root.bioseq_set_seq_set__.seq_entry_[0]

	name = handle.name.rsplit('/', 1)[1]
	if 'seq_entry_seq_' in seq_entry_:
		try:
			seq_entry_seq = StandaloneSeqEntrySeq(seq_entry_.seq_entry_seq_, gi)
		except SeqEntrySeqException, sese:
			pdb.set_trace()
			print sese.message
		# open( '../prints/%s' %name, 'w' ).write( str(seq_entry_seq) )
		uniSeq = UnifiedSeq(seq_entry_seq)
	elif 'seq_entry_set_' in seq_entry_:
		seq_entry_set = SeqEntrySet(seq_entry_.seq_entry_set_, gi)
		# open( '../prints/%s' %name, 'w' ).write( str(seq_entry_set) )
		# pdb.set_trace()
		uniSeq = UnifiedSeq(seq_entry_set)
	else:
		pdb.set_trace()
	# ssseq = None
	ssseq = SeqRepresentation(uniSeq, debug)
	# open( '../prints/%s' %name, 'w' ).write( str(ssseq) )

	return ssseq

	# try:
	# 	id_ = BioseqId(bioseq_set['Bioseq_id'])
	# except KeyError:
	# 	getAndSaveErr(LittleParser())
	# print "przed object_dict['_seq_class']=bioseq_set['Bioseq-set_class'].attributes['value'] "
	# try:
	# 	object_dict['_seq_class'] = bioseq_set['Bioseq-set_class'].attributes['value']
	# except KeyError:
	# 	object_dict['_seq_class'] = ''
	# 	getAndSaveErr(LittleParser())
	# try:
	# 	object_dict['_citation'] = bioseq_set['Seq-feat_cit']
	# except KeyError:
	# 	object_dict['_citation'] = ''
	# 	getAndSaveErr(LittleParser())
	# try:
	# 	inst = SeqInst.fromDict(bioseq_set['Bioseq_inst']['Seq-inst'])
	# 	object_dict['_seq'] = inst.seq
	# except:
	# 	getAndSaveErr(LittleParser())
	#
	# print "description"
	# # description
	# try:
	# 	descriptions = bioseq_set["Bioseq-set_descr"]['Seq-descr']
	# 	if len(bioseq_set["Bioseq-set_descr"]) > 1:
	# 		print bioseq_set["Bioseq-set_descr"]
	# 		raise BaseException
	# except KeyError:
	# 	getAndSaveErr(LittleParser())
	# 	descriptions = bioseq_set["Bioseq_descr"]['Seq-descr']
	# 	if len(bioseq_set["Bioseq_descr"]) > 1:
	# 		print bioseq_set["Bioseq_descr"]
	# 		raise BaseException
	# keys = []
	# for description in descriptions:
	# 	if len(description) > 1:
	# 		print descriptions
	# 		getAndSaveErr(LittleParser())
	# 		raise KeyboardInterrupt
	# 	if not description.keys()[0] in ['Seqdesc_source', 'Seqdesc_pub', 'Seqdesc_user', 'Seqdesc_update-date',
	# 									 'Seqdesc_comment', 'Seqdesc_title', 'Seqdesc_molinfo', 'Seqdesc_create-date',
	# 									 'Seqdesc_embl', 'Seqdesc_genbank']:
	# 		# 'Seqdesc_comment' było w ../sequences/375298272
	# 		# 'Seqdesc_title' było w 370882203
	# 		# 'Seqdesc_molinfo' było w 370882203
	# 		# 'Seqdesc_create-date' było w 370882203
	# 		# 'Seqdesc_embl' w 339832375
	# 		# 'Seqdesc_genbank' w 55925641
	# 		print description.keys()
	# 		getAndSaveErr(LittleParser())
	# 		raise KeyboardInterrupt
	# 	keys.append(description.keys()[0])
	#
	# if not all(['Seqdesc_source' in keys, 'Seqdesc_user' in keys]):
	# 	print descriptions
	# 	print keys
	# 	getAndSaveErr(LittleParser())
	# 	raise KeyboardInterrupt
	#
	# # jak do tej pory wykorzystuję tylko 'Seqdesc_source'
	# for description in descriptions:
	# 	if 'Seqdesc_source' in description:
	# 		root = description['Seqdesc_source']['BioSource']
	# 		source = BioSource(root)
	# # wykorzystujemy __source
	# object_dict['_lineage'] = source.lineage
	# host = source.host
	# object_dict['_taxname'] = source.taxname.strip()
	# # print source
	#
	# # seq-set
	# print "seq-set"
	# if 'Bioseq-set_seq-set' in bioseq_set:
	# 	seq_set = bioseq_set['Bioseq-set_seq-set']
	# 	# do dopisania - wszystkie glupie warunki
	# 	# wykorzystuję tylko mały kawałek
	# 	for seq_entry in seq_set:
	# 		molecule = seq_entry["Seq-entry_seq"]['Bioseq']['Bioseq_inst']['Seq-inst']['Seq-inst_mol'].attributes[
	# 			'value']
	# 		if molecule == 'dna' or molecule == 'rna':
	# 			seq_inst = SeqInst.fromDict(seq_entry["Seq-entry_seq"]['Bioseq']['Bioseq_inst']['Seq-inst'])
	# 			id_ = BioseqId(seq_entry["Seq-entry_seq"]['Bioseq']['Bioseq_id'])
	# try:
	# 	object_dict['_gi'] = id_.gi
	# 	object_dict['_dbId'] = id_.dbId
	# 	object_dict['_textSeqId'] = id_.textSeqId
	# except KeyError:
	# 	getAndSaveErr(LittleParser())
	# # annotations
	# print "annots"
	# # Seq-feat_dbxref nie uzywane, dopisać!
	# # 'Seq-feat_xref' podobnie, z ../sequences/372449821
	# # 'Seq-feat_id' w ../sequences/372217834
	# # 'Seq-feat_qual' w ../sequences/358356482
	# # 'Seq-feat_exp-ev' w ../sequences/373231359
	# # 'Seq-feat_cit' w ../sequences/134287154
	# '''object_dict['_annots_with_desc']=[]'''
	# object_dict['_features'] = []
	# try:
	# 	try:
	# 		annots_ = bioseq_set["Bioseq-set_annot"]
	# 	except KeyError:
	# 		annots_ = bioseq_set["Bioseq_annot"]
	# 		getAndSaveErr(LittleParser())
	# 	for annot in annots_:
	# 		if not 'Seq-annot_desc' in annots_:
	# 			# pdb.set_trace()
	# 			object_dict['_features'].extend(Annotation(annot).features)
	# except KeyError:
	# 	getAndSaveErr(LittleParser())
	# '''if object_dict['_annots_with_desc']:
	# 	open('../anndesc/%s'%handle.name.split('/')[-1], 'w').write(open(handle.name).read())'''
	# print object_dict['_features']
	# print "inst"
	# # inst
	# # zrobić to tak żeby były z atrybutów SeqInst atrybuty parsera
	# if 'Bioseq_inst' in bioseq_set:
	# 	try:
	# 		if len(bioseq_set['Bioseq_inst']) != 1:
	# 			raise BaseException
	# 		seq_inst = SeqInst.fromDict(bioseq_set['Bioseq_inst']['Seq-inst'])
	# 	except KeyboardInterrupt:  # KeyError:
	# 		# print bioseq_set['Bioseq_inst']
	# 		raise KeyboardInterrupt
	# 	print "inst:", seq_inst
	#
	# # try:
	# object_dict['_seq'] = seq_inst.seq
	# object_dict['_seq_len'] = seq_inst.len
	# object_dict['_seq_strands'] = seq_inst.strand
	# object_dict['_seq_molecule'] = acid_to_number[seq_inst.mol]
	# object_dict['_seq_repr'] = seq_inst.repr
	# object_dict['_seq_topology'] = seq_inst.topology
	'''except UnboundLocalError:
		pass'''

	'''try:
		seq=et.find('Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_seq-set/Seq-entry/Seq-entry_seq/Bioseq/Bioseq_inst/Seq-inst')
		self._seq_repr = seq.find('Seq-inst_repr').get('value')
		self._seq_mol = seq.find('Seq-inst_mol').get('value')
		self._seq_len = seq.find('Seq-inst_length').text
		self._seq=seq.find('Seq-inst_seq-data/Seq-data/Seq-data_iupacna/IUPACna').text
	except AttributeError:
		pass
	try:
		self._organism=[x.strip() for x in et.find('Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_descr/Seq-descr/Seqdesc/Seqdesc_source/BioSource/BioSource_org/Org-ref/Org-ref_orgname/OrgName/OrgName_lineage').text.split(';')]
	except AttributeError:
		self._organism='Error'
	self._id=findNodeText(et,'Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_seq-set/Seq-entry/Seq-entry_seq/Bioseq/Bioseq_id/Seq-id/Seq-id_other/Textseq-id/Textseq-id_accession')
	self._name=findNodeText(et,'Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_descr/Seq-descr/Seqdesc/Seqdesc_source/BioSource/BioSource_org/Org-ref/Org-ref_taxname')
	'''
	'''#described regions
	try:
		annots=et.find('Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_seq-set/Seq-entry/Seq-entry_seq/Bioseq/Bioseq_annot/Seq-annot/Seq-annot_data/Seq-annot_data_ftable')
		print 'Found described'
		annot_list=annots.getchildren()
		while annot_list:
		    annot=annot_list[0]
		    what=findNodeText(annot, 'Seq-feat_data/SeqFeatData/SeqFeatData_imp/Imp-feat/Imp-feat_key')
		    try:
		        interval=annot.find('Seq-feat_location/Seq-loc/Seq-loc_int/Seq-interval')
		    except AttributeError:
		        continue
		    start=findNodeText(interval,'Seq-interval_from')
		    stop=findNodeText(interval,'Seq-interval_to')
		    orientation=findNodeAttribute(interval,'Seq-interval_strand/Na-strand', 'value')
		    self._described_regions.append({'what':what, 'from':start, 'to': stop, 'orientation':orientation})
		    annot_list.remove(annot)
	except AttributeError:
		pass

	#coding regions
	try:
		annots=et.find('Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_annot/Seq-annot/Seq-annot_data/Seq-annot_data_ftable')
		print 'Found coding'
		annot_list=annots.getchildren()
		while annot_list:
		    annot=annot_list[0]
		    frame=findNodeAttribute(annot,'Seq-feat_data/SeqFeatData/SeqFeatData_cdregion/Cdregion/Cdregion_frame', 'value')
		    code=findNodeText(annot, 'Seq-feat_data/SeqFeatData/SeqFeatData_cdregion/Cdregion/Cdregion_code/Genetic-code/Genetic-code_E/Genetic-code_E_id')
		    try:
		        #interval=annot.find('Seq-feat_location/Seq-loc/Seq-loc_mix/Seq-loc-mix/Seq-loc/Seq-loc_int/Seq-interval')
		        interval=annot.find('Seq-feat_location/Seq-loc/Seq-loc_int/Seq-interval')
		    except AttributeError:
		        continue
		    start=findNodeText(interval,'Seq-interval_from')
		    stop=findNodeText(interval,'Seq-interval_to')
		    orientation=findNodeAttribute(interval,'Seq-interval_strand/Na-strand', 'value')
		    self._coding_regions.append({'frame':frame, 'code':code, 'from':start, 'to': stop, 'orientation':orientation})
		    annot_list.remove(annot)
	except AttributeError:
		pass

	try:
		for orgmod in et.find('Bioseq-set_seq-set/Seq-entry/Seq-entry_set/Bioseq-set/Bioseq-set_descr/Seq-descr/Seqdesc/Seqdesc_source/BioSource/BioSource_org/Org-ref/Org-ref_orgname/OrgName/OrgName_mod').getchildren():
		    if ('value', 'nat-host') in orgmod.find('.//OrgMod_subtype').items():
		        host=orgmod.find('.//OrgMod_subname').text
		        self._host_xml=host
		        break
	except AttributeError:
		#jesli nie znajdzie OrgName_mod
		#print "Nie widze gospodarza"
		pass
	time.sleep(0.333333334)'''
	# print "Gospodarz z pliku xml:%s"%host
	# object_dict['_host_xml'] = host
	# if host and host != strange_orgname:
	# 	# jesli sie pojawi host w rekordzie to szukam jego id nastepujaco:
	# 	# najpierw sprawdzam czy w bazie taxonomy jest nazwa calego hosta, jesli sie pojawi kilka wynikow to wybieram pierwszy z brzegu
	# 	# jesli nic nie znalazl to probuje pierwszych dwu yrazow (zwykle jest to para rodzaj - gatuek)
	# 	# jesli i tu nic nie znalazl to probuje pierwszego
	# 	# jesli nie to zostawiam to co bylo w zmiennej host i potem sprawdzam recznie
	# 	# dobrym przykladem jest wpis "Anatid species" - gdzie nawet pierwszy wyraz w bazie taxonomy nie daje zadnych hitow
	# 	# a to sa kaczkowate
	# 	handle = Entrez.esearch(db='taxonomy', term=host)
	# 	# try:
	# 	print host
	# 	# pdb.set_trace()
	# 	host_ids, object_dict['_wiele_rezultatow_w_taxonomy'] = checkHost(host)
	# 	object_dict['_za_ktorym_razem'] = 1
	# 	if host_ids:
	# 		id_ = host_ids[0]
	# 	else:
	# 		host2 = ' '.join(host.split()[:2])
	# 		host_ids, object_dict['_wiele_rezultatow_w_taxonomy'] = checkHost(host2)
	# 		object_dict['_za_ktorym_razem'] = 2
	# 		if host_ids:
	# 			id_ = host_ids[0]
	# 		else:
	# 			host3 = host.split()[0]
	# 			host_ids, object_dict['_wiele_rezultatow_w_taxonomy'] = checkHost(host3)
	# 			object_dict['_za_ktorym_razem'] = 3
	# 			try:
	# 				id_ = host_ids[0]
	# 			except IndexError:
	# 				object_dict['_host'] = ''
	# 				getAndSaveErr(LittleParser())
	#
	# 	object_dict['_host'] = []
	# 	# tu już efetch
	# 	for host_id in host_ids:
	# 		object_dict['_host'].append(hostLineage(host_id))
	# return object_dict
