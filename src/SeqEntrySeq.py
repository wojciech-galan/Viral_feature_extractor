#! /usr/bin/python
#-*- coding: utf-8 -*-

import pdb
import logging
import os

#from ParserClasses import Seq_entry_seq_
from simple_classes import BaseXML, MyException, DictContainsInterface
from simple_classes import UnexpectedValueException

logger = logging.getLogger(os.path.basename(__file__))

class SeqEntrySeq( BaseXML ):
	"Klasa macierzysta do wyciągania potrzebnych wartości z Seq_entry_seq_"
	
	def __init__( self, seq_entry_seq_ ):
		'''Argumenty:
			-	seq_entry_seq_ - w pełni utworzony obiekt klasy Seq_entry_seq_'''
		super( SeqEntrySeq, self ).__init__( )
		self.temp = {} 						# tymczasowe, klasy potomne będą z tego korzystać, potem to kasują
		bioseq = seq_entry_seq_.bioseq
		#pdb.set_trace()
		seq_inst = bioseq.bioseq_inst.seq_inst_
		self.molecule = seq_inst.seq_inst_mol_.value
		self.representation = seq_inst.seq_inst_repr_.value
		if self.representation not in [ 'raw', 'const', 'ref', 'consen', 'delta' ]: #[ 'raw', 'const', 'ref', 'consen', 'delta' ]
			print self.representation
			#pdb.set_trace()
			raise SeqEntrySeqException( 'representation' )
		#pdb.set_trace()
		if 'seq_inst_seq_data__' in seq_inst:
			seq = seq_inst.seq_inst_seq_data__.seq_data_
			self.temp[ 'seq' ] = seq
		else:
			self.temp[ 'seq' ] = None
		try:
			self.strand = seq_inst.seq_inst_strand_.value
		except AttributeError:
			#raise SeqEntrySeqException( 'strand' )
			self.strand = None
		try:
			self.topology = seq_inst.seq_inst_topology_.value
		except AttributeError:
			#raise SeqEntrySeqException( 'topology' )
			self.topology = None
		#inst skończony
		bioseq_ids = bioseq.bioseq_id
		#pdb.set_trace()
		for bioseq_id in bioseq_ids.seq_id_:
			try:
				textseq_id = bioseq_id.seq_id_other_.textseq_id_
				break
			except AttributeError:
				pass
		#pdb.set_trace()
		self.textseq_id = ( textseq_id.textseq_id_accession_.text, textseq_id.textseq_id_version_.text )
		#id też jest
		#pora na hosta
		seq_descr = bioseq.bioseq_descr.seq_descr_
		biosource = None
		molinfo = None
		self.title = None
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
		#pdb.set_trace()
		self.temp[ 'biosource' ] = biosource
		# annot
		self.gene_references = []#wygląda na to, że nie da się powiązać gene_references i cd_regions
		self.cd_regions = []
		self.missing_cd_regions = []
		gene_refs_num = 0
		self.missing_gene_refs = []
		if 'bioseq_annot' in bioseq:
			bioseq_annot = bioseq.bioseq_annot
			for seq_annot in bioseq_annot.seq_annot_:
				seq_annot_data_ = seq_annot.seq_annot_data_
				if 'seq_annot_data_ftable_' in seq_annot_data_:
					seq_annot_data_ftable_ = seq_annot_data_.seq_annot_data_ftable_
					for seq_feat in seq_annot_data_ftable_.seq_feat_:
						seqfeatdata = seq_feat.seq_feat_data_.seqfeatdata
						if 'seqfeatdata_cdregion' in seqfeatdata:
							pass # pdb.set_trace() #zrobić cdregionreference. jak konflikt, to zmienić self.missing_cd_regions
						elif 'seqfeatdata_org' in seqfeatdata:
							pdb.set_trace() #  to się chyba nie zdarza #miałoby chyba być jak orgref z description
						elif 'seqfeatdata_gene' in seqfeatdata:
							try:
								self.gene_references.append( GeneRef( seq_feat ) )
							except GeneRefException:
								pdb.set_trace()
								self.missing_gene_refs.append( str( gene_refs_num ) )
							gene_refs_num += 1

#nie uwzględniam aminokwasowych
class StandaloneSeqEntrySeq( SeqEntrySeq ):
	"Klasa do wyciągania potrzebnych wartości z Seq_entry_seq_"
	
	def __init__( self, seq_entry_seq_, gi ):
		'''Argumenty:
			-	seq_entry_seq_ - w pełni utworzony obiekt klasy Seq_entry_seq_'''
		super( StandaloneSeqEntrySeq, self ).__init__( seq_entry_seq_ )
		self.gi = gi
		seq = self.temp[ 'seq' ]
		try:
			self.seq = seq.seq_data_iupacna_.iupacna.text
		except AttributeError:
			self.seq = None
		if self.molecule not in [ 'rna', 'dna' ]:
			print self.molecule
			pdb.set_trace()
		#pdb.set_trace()
		if not self.strand in [ 'ss', 'ds', 'mixed' ]:
			logger.debug(self.strand)
		
		#inst skończony
		#pora na hosta
		biosource = self.temp[ 'biosource' ]
		org_ref = biosource.biosource_org.org_ref_
		self.taxname = org_ref.org_ref_taxname_.text # nie zawsze
		orgname = org_ref.org_ref_orgname_.orgname
		self.virus_name = orgname.orgname_name.orgname_name_virus.text
		self.gencode = orgname.orgname_gcode.text
		biosource_genome = biosource.biosource_genome
		self.genome = ( biosource_genome.value, biosource_genome.text ) # <BioSource_genome value="genomic">1</BioSource_genome>
																		# w takich przypadkach value to genomic, text to 1
																		# zastosowanie?
		self.subsource_subtype = None									# wybieranie segmentowanych
		if 'biosource_subtype' in biosource:							# nie zawsze jest
			biosource_subtype = biosource.biosource_subtype
			for subsource in biosource_subtype.subsource:
				if subsource.subsource_subtype.value == 'segment':
					self.subsource_subtype = ( subsource.subsource_subtype.value, subsource.subsource_subtype.text, subsource.subsource_name.text )
		self.lineage = orgname.orgname_lineage.text
		self.host = None
		try:
			for orgmod in orgname.orgname_mod.orgmod:
				if orgmod.orgmod_subtype.value == 'nat-host':
					self.host = orgmod.orgmod_subname.text
		except AttributeError:
			pass
		for k, v in self.__dict__.items():
			pass#print k, v
		del self.__dict__[ 'temp' ]
		#print self


class SeqEntrySeqPartOfSet( SeqEntrySeq ):
	"Klasa do wyciągania potrzebnych wartości z Seq_entry_seq_"
	
	def __init__( self, seq_entry_seq_ ):
		'''Argumenty:
			-	seq_entry_seq_ - w pełni utworzony obiekt klasy Seq_entry_seq_'''
		super( SeqEntrySeqPartOfSet, self ).__init__( seq_entry_seq_ )
		seq = self.temp[ 'seq' ]
		if seq and 'seq_data_iupacna_' in seq:
			self.seq = seq.seq_data_iupacna_.iupacna.text
		elif seq and 'seq_data_iupacaa_' in seq:
			self.seq = seq.seq_data_iupacaa_.iupacaa.text
		else:
			self.seq = None
		
		#inst skończony
		'''bioseq_ids = bioseq.bioseq_id
		#pdb.set_trace()
		for bioseq_id in bioseq_ids.seq_id_:
			try:
				textseq_id = bioseq_id.seq_id_other_.textseq_id_
				break
			except AttributeError:
				pass
		#pdb.set_trace()
		self.textseq_id = ( textseq_id.textseq_id_accession_.text, textseq_id.textseq_id_version_.text )'''
		#id też jest
		#pora na hosta
		biosource = self.temp[ 'biosource' ]
		if biosource:
			pdb.set_trace()
			'''org_ref = biosource.biosource_org.org_ref_
			self.taxname = org_ref.org_ref_taxname_.text # nie zawsze
			orgname = org_ref.org_ref_orgname_.orgname
			self.virus_name = orgname.orgname_name.orgname_name_virus.text
			self.gencode = orgname.orgname_gcode.text
			biosource_genome = biosource.biosource_genome
			self.genome = ( biosource_genome.value, biosource_genome.text ) # <BioSource_genome value="genomic">1</BioSource_genome>
																			# w takich przypadkach value to genomic, text to 1
																			# zastosowanie?
			self.subsource_subtype = None									# wybieranie segmentowanych
			if 'biosource_subtype' in biosource:							# nie zawsze jest
				biosource_subtype = biosource.biosource_subtype
				for subsource in biosource_subtype.subsource:
					if subsource.subsource_subtype.value == 'segment':
						self.subsource_subtype = ( subsource.subsource_subtype.value, subsource.subsource_subtype.text )
			self.lineage = orgname.orgname_lineage.text
			try:
				for orgmod in orgname.orgname_mod.orgmod:
					if orgmod.orgmod_subtype.value == 'nat-host':
						self.host = orgmod.orgmod_subname.text
			except AttributeError:
				self.host = None'''
		else:
			self.taxname = None
			self.gencode = None
			self.genome = None
			self.subsource_subtype = None
			self.lineage = None
			self.host = None
			self.virus_name = None
		for k, v in self.__dict__.items():
			pass#print k, v
		del self.__dict__[ 'temp' ]
		

class Gene( BaseXML, DictContainsInterface ):
	"Uproszczone gene reference - zawiera nazwę genu"
	
	def __init__( self, root ):
		super( Gene, self ).__init__()
		gene_ref_ = root.gene_ref_
		#<!-- Official gene symbol -->
		try:
			self.locus = gene_ref_.gene_ref_locus_.text
		except AttributeError:
			self.locus = None
		#<!-- systematic gene name (e.g., MI0001, ORF0069) -->
		try:
			self.locus_tag = gene_ref_.gene_ref_locus_tag__.text
		except AttributeError:
			self.locus_tag = None
		try:
			self.gene_ref_desc = gene_ref_.gene_ref_desc_.text
		except AttributeError:
			self.gene_ref_desc = None
		if not any( self.__dict__.values() ):
			pdb.set_trace()
	
	def getName( self ):
		if 'locus' in self and self.locus:
			return self.locus
		elif 'locus_tag' in self and self.locus_tag:
			return self.locus_tag
		return self.gene_ref_desc


class Localisation( BaseXML, DictContainsInterface ):
	"Uproszczone dane o lokalizacji"
	
	def __init__( self, root ):
		super( Localisation, self ).__init__()
		if 'seq_loc_int_' in root:
			interval = root.seq_loc_int_.seq_interval_
			self.FROM, self.TO, self.strand = localisation( interval )
		elif 'seq_loc_mix_' in root:
			self.FROM, self.TO, self.strand = [], [], []
			for seqloc in root.seq_loc_mix_.seq_loc_mix__.seq_loc_:
				if 'seq_loc_int_' in seqloc:
					interval = seqloc.seq_loc_int_.seq_interval_
					FROM, TO, strand = localisation( interval )
					self.FROM.append( FROM )
					self.TO.append( TO )
					self.strand.append( strand )
				elif 'seq_loc_pnt_' in seqloc:
					FROM, TO, strand = parsePnt( seqloc )
					self.FROM.append( FROM )
					self.TO.append( TO )
					self.strand.append( strand )
				elif 'seq_loc_null_' in seqloc:
					pass
				else:
					pdb.set_trace()
			self.FROM, self.TO, self.strand = tuple( self.FROM ), tuple( self.TO ), tuple( self.strand )
		elif 'seq_loc_packed_int__' in root:
			self.FROM, self.TO, self.strand = [], [], []
			#pdb.set_trace()
			for interval in root.seq_loc_packed_int__.packed_seqint_.seq_interval_:
				FROM, TO, strand = localisation( interval )
				self.FROM.append( FROM )
				self.TO.append( TO )
				self.strand.append( strand ) # często jest None
			self.FROM, self.TO, self.strand = tuple( self.FROM ), tuple( self.TO ), tuple( self.strand )
		elif 'seq_loc_pnt_' in root:
			self.FROM, self.TO, self.strand = parsePnt( root )
		else:
			pdb.set_trace()
			raise LocalisationException()


class Database( BaseXML, DictContainsInterface ):
	"Uproszczona Seq-feat_dbxref - szukam tylko gene ID"
	
	def __init__( self, root ):
		super( Database, self ).__init__()
		for dbtag in root.dbtag:
			if dbtag.dbtag_db.text == 'GeneID':
				self.db = dbtag.dbtag_db.text
				self.id = dbtag.dbtag_tag.object_id_.object_id_id_.text
				'''if len( id ) > 1:
					pdb.set_trace()
				self.id = ID[0].dbtag_tag'''
				break
		if not 'db' in self:
			pdb.set_trace()


class GeneRef( BaseXML, DictContainsInterface ):
	"Dane na temat genu - nazwa, lokalizacja, odnośnik do bazy"
	
	def __init__( self, root ):
		super( GeneRef, self ).__init__()
		self.partial = False
		if 'seq_feat_partial_' in root:
			if root.seq_feat_partial_.value == 'true':
				self.partial = True
		self.gene_name = Gene( root.seq_feat_data_.seqfeatdata.seqfeatdata_gene ).getName()
		#id wbazie GeneID
		if 'seq_feat_dbxref_' in root:
			self.id = Database( root.seq_feat_dbxref_ ).id
		else:
			 self.id = None
		if 'seq_feat_product_' in root:
			product = Product( seq_feat.seq_feat_product_ )
		else:
			product = None
		try:
			loc = Localisation( root.seq_feat_location_.seq_loc_ )
		except LocalisationException:
			raise GeneRefException()
		self.FROM 	= loc.FROM
		self.TO   	= loc.TO
		self.strand = loc.strand
		if product:
			self.product_id = product.ID
			self.product_id_type = product.ID_type
		else:
			self.product_id = None
			self.product_id_type = None


class CdRegion( BaseXML, DictContainsInterface ):
	"Uproszczone dane o rejonie kodującym"
	
	def __init__( self, root ):
		super( CdRegion, self ).__init__()
		cdregion = root.seqfeatdata_cdregion.cdregion
		try:
			self.frame = cdregion.cdregion_frame.value	#jeśli nie ma podanej przyjąć 'one'
		except AttributeError:
			self.frame = 'one'
		if 'cdregion_code' in cdregion:
			code = cdregion.cdregion_code.genetic_code_.genetic_code_e_
			if len( code ) != 1:
				pdb.set_trace()
			self.code = code[0].genetic_code_e_id_.text		#id kodu genetycznego. Jeśli go nie będzie, trza go wyłuskać
		else:
			self.code = '1'
		if 'cdregion_orf' in cdregion:
			if cdregion.cdregion_orf.value == 'true':		# This is a signal that nothing is known about the protein
															# product, or even if it is produced. In this case the
															# translated protein sequence will be attached, but there
															# will be no other information associated with it. This flag
															# allows such very speculative coding regions to be easily
															# ignored when scanning the database for genuine protein
															# coding regions.
				self.orf = True
			if cdregion.cdregion_orf.value == 'false':
				self.orf = False
		else:
			self.orf = False
		if 'cdregion_conflict' in cdregion:
			conflict = cdregion.cdregion_conflict.value
			if conflict == 'true':
				self.conflict = True
			if conflict == 'false':
				self.conflict = False
		else:
			self.conflict = False
		if self.conflict:
			raise CdRegionException


class Product( BaseXML, DictContainsInterface ):
	"Uproszczone info o produkcie, konkretnie typ i ID"
	
	def __init__( self, root ):
		super( Product, self ).__init__()
		ID = root.seq_loc_.seq_loc_whole_.seq_id_
		if len( ID.__dict__ ) != 2:
			pdb.set_trace()
		for key, val in ID.__dict__.iteritems():
			if key != 'name':
				self.ID = val.text
				self.ID_type = key.rsplit('_',2)[1]
				break


class CdRegionRef( BaseXML, DictContainsInterface ):
	'''Info o regionie kodującym'''
	
	def __init__( self, root ):
		super( CdRegionRef, self ).__init__()
		#pdb.set_trace()
		self.partial = False
		if 'seq_feat_partial_' in root:
			if root.seq_feat_partial_.value == 'true':
				self.partial = True
		try:
			cdregion = CdRegion( root.seq_feat_data_.seqfeatdata )
		except CdRegionException:
			raise CdRegionRefException()
		loc = Localisation( root.seq_feat_location_.seq_loc_ )
		if 'seq_feat_product_' in root:
			product  = Product( root.seq_feat_product_ )
			self.product_id = product.ID
			self.product_id_type = product.ID_type
		else:
			self.product_id = None
			self.product_id_type = None
		self.frame = cdregion.frame
		self.code  = cdregion.code
		self.orf   = cdregion.orf
		self.FROM 	= loc.FROM
		self.TO   	= loc.TO
		self.strand = loc.strand
		if 'seq_feat_except_text__' in root:
			self.seq_feat_except_text = root.seq_feat_except_text__.text
		else:
			self.seq_feat_except_text = None


class SeqEntrySeqException( MyException ):
	'''Wyjątek rzucany przez SeqEntrySeq, gdy coś pójdzie nie tak
	Użycie:
		raise SeqEntrySeqException
	lub
		raise SeqEntrySeqException( 'wiadomość' )'''
	pass

class LocalisationException( MyException ):
	pass

class GeneRefException( MyException ):
	pass

class CdRegionException( MyException ):
	pass

class CdRegionRefException( MyException ):
	pass

def localisation( interval ):
	#pdb.set_trace()
	FROM = interval.seq_interval_from_.text
	TO   = interval.seq_interval_to_.text
	if 'seq_interval_strand_' in interval:
		strand = interval.seq_interval_strand_.na_strand_.value
	else:
		strand = None
	return ( FROM, TO, strand )

def parsePnt( seqloc ):
	FROM = seqloc.seq_loc_pnt_.seq_point_.seq_point_point_.text
	TO = FROM
	if 'seq_point_strand_' in seqloc.seq_loc_pnt_.seq_point_:
		strand = seqloc.seq_loc_pnt_.seq_point_.seq_point_strand_.na_strand_.value
	else:
		strand = None
	return FROM, TO, strand
