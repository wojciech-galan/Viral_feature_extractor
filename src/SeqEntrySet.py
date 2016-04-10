#! /usr/bin/python
# -*- coding: utf-8 -*-

import pdb

from simple_classes import BaseXML
from simple_classes import MyException
from SeqEntrySeq import SeqEntrySeqPartOfSet #, SeqEntrySeqException, BiosourceNotPresent, NotDnaNorRna
from SeqEntrySeq import Product
from SeqEntrySeq import GeneRef, GeneRefException
from SeqEntrySeq import CdRegion, CdRegionException
from SeqEntrySeq import CdRegionRef, CdRegionRefException

class SeqEntrySet( BaseXML ):
	"Klasa do wyciągania potrzebnych wartości z Seq_entry_set_"
	
	def __init__( self, root, gi ):
		'''Argumenty:
			-	seq_entry_set_ - w pełni utworzony obiekt klasy Seq_entry_seq_'''
		super( SeqEntrySet, self ).__init__( ) 
		bioseq_set = root.bioseq_set_
		self.gi = gi
		if 'bioseq_set_level_' in bioseq_set and  int( bioseq_set.bioseq_set_level_.text ) > 1:
			pdb.set_trace()
		if bioseq_set.bioseq_set_class_.value != 'nuc-prot':
			pdb.set_trace()
		if 'bioseq_set_id_' in bioseq_set:
			self.set_id = bioseq_set.bioseq_set_id_.object_id_.object_id_id_.text
		else:
			self.set_id = None
		if 'bioseq_set_coll_' in bioseq_set:
			pdb.set_trace()
		# descr
		#pdb.set_trace()
		seq_descr = bioseq_set.bioseq_set_descr_.seq_descr_ 
		biosource = None
		molinfo = None
		self.title = None
		#pdb.set_trace()
		for seqdesc in seq_descr.seqdesc:
			try:
				self.title = seqdesc.seqdesc_title.text
			except AttributeError:
				pass
			try:
				biosource = seqdesc.seqdesc_source.biosource	# biosource jest zawsze obecny w Seqdesc_source 
			except AttributeError:
				pass
			try:
				molinfo = seqdesc.seqdesc_molinfo.molinfo
				#pdb.set_trace()
			except AttributeError:
				pass
			if self.title and biosource and molinfo:
				break
		self.biomol = None
		self.completeness = None
		if molinfo:
			try:
				self.biomol = ( molinfo.molinfo_biomol.value, molinfo.molinfo_biomol.text )
			except AttributeError:
				pass
			try:
				self.completeness = ( molinfo.molinfo_completeness.value, molinfo.molinfo_completeness.text )
			except AttributeError:
				pass
		org_ref = biosource.biosource_org.org_ref_
		self.taxname = org_ref.org_ref_taxname_.text # nie zawsze
		orgname = org_ref.org_ref_orgname_.orgname
		if 'orgname_name_virus' in orgname.orgname_name:
			self.virus_name = orgname.orgname_name.orgname_name_virus.text
		else:
			self.virus_name = None
		self.gencode = orgname.orgname_gcode.text
		try:
			biosource_genome = biosource.biosource_genome
			self.genome = ( biosource_genome.value, biosource_genome.text ) # <BioSource_genome value="genomic">1</BioSource_genome>
																		# w takich przypadkach value to genomic, text to 1
																		# zastosowanie?
																		# wybieranie segmentowanych
		except:
			self.genome = None
		self.subsource_subtype = None									
		if 'biosource_subtype' in biosource:							# nie zawsze jest
			biosource_subtype = biosource.biosource_subtype
			for subsource in biosource_subtype.subsource:
				if subsource.subsource_subtype.value == 'segment':
					self.subsource_subtype = ( subsource.subsource_subtype.value, subsource.subsource_subtype.text )
		self.lineage = orgname.orgname_lineage.text
		self.host = None
		try:
			for orgmod in orgname.orgname_mod.orgmod:
				if orgmod.orgmod_subtype.value == 'nat-host':
					self.host = orgmod.orgmod_subname.text
		except AttributeError:
			pass
		#annot
		self.gene_references = []#wygląda na to, że nie da się powiązać gene_references i cd_regions
		self.cd_regions = []
		cdr_num = 0
		self.missing_cd_regions = []
		gene_refs_num = 0
		self.missing_gene_refs = []
		if 'bioseq_set_annot_' in bioseq_set:
			bioseq_annot = bioseq_set.bioseq_set_annot_
			for seq_annot in bioseq_annot.seq_annot_:
				seq_annot_data_ = seq_annot.seq_annot_data_
				if 'seq_annot_data_ftable_' in seq_annot_data_:
					seq_annot_data_ftable_ = seq_annot_data_.seq_annot_data_ftable_
					for seq_feat in seq_annot_data_ftable_.seq_feat_:
						seqfeatdata = seq_feat.seq_feat_data_.seqfeatdata
						if 'seqfeatdata_cdregion' in seqfeatdata:
							if 'seqfeatdata_gene' in seqfeatdata:
								pdb.set_trace()
							try:
								self.cd_regions.append( CdRegionRef( seq_feat ) )
							except CdRegionRefException:
								self.missing_cd_regions.append( str( cdr_num ) )
							cdr_num += 1
						elif 'seqfeatdata_org' in seqfeatdata:
							pdb.set_trace() #  to się chyba nie zdarza #miałoby chyba być jak orgref z description
						elif 'seqfeatdata_gene' in seqfeatdata:
							try:
								self.gene_references.append( GeneRef( seq_feat ) )
							except GeneRefException:
								self.missing_gene_refs.append( str( gene_refs_num ) )
							gene_refs_num += 1
		
		#sprawdzam sekwencje należące do setu
		seqs = bioseq_set.bioseq_set_seq_set__.seq_entry_
		self.sequences = []
		self.missing_seqs = []
		for n in range( len(seqs) ):
			seq = seqs[n]
			try:
				self.sequences.append( SeqEntrySeqPartOfSet( seq.seq_entry_seq_ ) )
			except Exception as e:
				print type( e ).__name__, e
				pdb.set_trace()
			except SeqEntrySeqException:
				#pdb.set_trace()
				self.missing_seqs.append[ str(n) ]
		#print self

class SeqEntrySetException( MyException ):
	pass
