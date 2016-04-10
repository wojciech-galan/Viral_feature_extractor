#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree

from simple_classes import BaseXML, DictContainsInterface

from constants import seq_dir
import pdb

class Pubdesc_seq_raw_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_seq_raw_, self ).__init__()
		self.name = 'Pubdesc_seq-raw'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_consequence_E_loss_of_heterozygosity_reference___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_loss_of_heterozygosity_reference___, self ).__init__()
		self.name = 'Variation-ref_consequence_E_loss-of-heterozygosity_reference'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_xref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_xref_, self ).__init__()
		self.name = 'Medline-entry_xref'
		if root.find('Medline-si') is not None:
			self.medline_si_ = [ Medline_si_(element) for element in root.findall('Medline-si') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Population_data_allele_frequency__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_allele_frequency__, self ).__init__()
		self.name = 'Population-data_allele-frequency'
		self.text = root.text
	
	def __call__( self ):
		pass


class EMBL_block_update_date__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_update_date__, self ).__init__()
		self.name = 'EMBL-block_update-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_name_, self ).__init__()
		self.name = 'Prot-ref_name'
		if root.find('Prot-ref_name_E') is not None:
			self.prot_ref_name_e_ = [ Prot_ref_name_E_(element) for element in root.findall('Prot-ref_name_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_sp( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_sp, self ).__init__()
		self.name = 'Seqdesc_sp'
		self.sp_block_ = SP_block_( root.find('SP-block') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_substance_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_substance_, self ).__init__()
		self.name = 'Medline-entry_substance'
		if root.find('Medline-rn') is not None:
			self.medline_rn_ = [ Medline_rn_(element) for element in root.findall('Medline-rn') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Phenotype_term( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Phenotype_term, self ).__init__()
		self.name = 'Phenotype_term'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_variation( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_variation, self ).__init__()
		self.name = 'SeqFeatData_variation'
		self.variation_ref_ = Variation_ref_( root.find('Variation-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_block_xref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_xref_, self ).__init__()
		self.name = 'EMBL-block_xref'
		if root.find('EMBL-xref') is not None:
			self.embl_xref_ = [ EMBL_xref_(element) for element in root.findall('EMBL-xref') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Author_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Author_name, self ).__init__()
		self.name = 'Author_name'
		self.person_id_ = Person_id_( root.find('Person-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Trna_ext_aa_ncbieaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_aa_ncbieaa_, self ).__init__()
		self.name = 'Trna-ext_aa_ncbieaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_entry_seq_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Seq_entry_seq_, self ).__init__()
		self.name = 'Seq-entry_seq'
		self.bioseq = Bioseq( root.find('Bioseq') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Id_pat_country_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Id_pat_country_, self ).__init__()
		self.name = 'Id-pat_country'
		self.text = root.text
	
	def __call__( self ):
		pass


class Org_ref_mod_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_mod_E_, self ).__init__()
		self.name = 'Org-ref_mod_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Code_break_aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Code_break_aa_, self ).__init__()
		self.name = 'Code-break_aa'
		#jedna z opcji dla ['Code-break_aa_ncbi8aa', 'Code-break_aa_ncbieaa', 'Code-break_aa_ncbistdaa']
		if 'Code-break_aa_ncbi8aa' in [ x.tag for x in root.getchildren() ]:
			self.code_break_aa_ncbi8aa_ = Code_break_aa_ncbi8aa_( root.find('Code-break_aa_ncbi8aa') )
		elif 'Code-break_aa_ncbieaa' in [ x.tag for x in root.getchildren() ]:
			self.code_break_aa_ncbieaa_ = Code_break_aa_ncbieaa_( root.find('Code-break_aa_ncbieaa') )
		else:
			self.code_break_aa_ncbistdaa_ = Code_break_aa_ncbistdaa_( root.find('Code-break_aa_ncbistdaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_chunk_diag__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_chunk_diag__, self ).__init__()
		self.name = 'Spliced-exon-chunk_diag'
		self.text = root.text
	
	def __call__( self ):
		pass


class Clone_ref_unique_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_ref_unique_, self ).__init__()
		self.name = 'Clone-ref_unique'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Variation_ref_synonyms_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_synonyms_, self ).__init__()
		self.name = 'Variation-ref_synonyms'
		if root.find('Variation-ref_synonyms_E') is not None:
			self.variation_ref_synonyms_e_ = [ Variation_ref_synonyms_E_(element) for element in root.findall('Variation-ref_synonyms_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_, self ).__init__()
		self.name = 'Pub-set'
		#jedna z opcji dla ['Pub-set_journal', 'Pub-set_article', 'Pub-set_proc', 'Pub-set_book', 'Pub-set_pub', 'Pub-set_medline', 'Pub-set_patent']
		if 'Pub-set_journal' in [ x.tag for x in root.getchildren() ]:
			self.pub_set_journal_ = Pub_set_journal_( root.find('Pub-set_journal') )
		elif 'Pub-set_article' in [ x.tag for x in root.getchildren() ]:
			self.pub_set_article_ = Pub_set_article_( root.find('Pub-set_article') )
		elif 'Pub-set_proc' in [ x.tag for x in root.getchildren() ]:
			self.pub_set_proc_ = Pub_set_proc_( root.find('Pub-set_proc') )
		elif 'Pub-set_book' in [ x.tag for x in root.getchildren() ]:
			self.pub_set_book_ = Pub_set_book_( root.find('Pub-set_book') )
		elif 'Pub-set_pub' in [ x.tag for x in root.getchildren() ]:
			self.pub_set_pub_ = Pub_set_pub_( root.find('Pub-set_pub') )
		elif 'Pub-set_medline' in [ x.tag for x in root.getchildren() ]:
			self.pub_set_medline_ = Pub_set_medline_( root.find('Pub-set_medline') )
		else:
			self.pub_set_patent_ = Pub_set_patent_( root.find('Pub-set_patent') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seg_dim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_dim_, self ).__init__()
		self.name = 'Packed-seg_dim'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_consequence_E_loss_of_heterozygosity_test___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_loss_of_heterozygosity_test___, self ).__init__()
		self.name = 'Variation-ref_consequence_E_loss-of-heterozygosity_test'
		self.text = root.text
	
	def __call__( self ):
		pass


class Tx_evidence_exp_code__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Tx_evidence_exp_code__, self ).__init__()
		self.name = 'Tx-evidence_exp-code'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'rna-seq', 'rna-size', 'np-map', 'np-size', 'pe-seq', 'cDNA-seq', 'pe-map', 'pe-size', 'pseudo-seq', 'rev-pe-map', 'other']
		self.value = root.get('value')


class Num_real_a_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_real_a_, self ).__init__()
		self.name = 'Num-real_a'
		self.text = root.text
	
	def __call__( self ):
		pass


class Delta_seq_literal_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Delta_seq_literal_, self ).__init__()
		self.name = 'Delta-seq_literal'
		self.seq_literal_ = Seq_literal_( root.find('Seq-literal') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Id_pat_id_app_number__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Id_pat_id_app_number__, self ).__init__()
		self.name = 'Id-pat_id_app-number'
		self.text = root.text
	
	def __call__( self ):
		pass


class PDB_block_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_class_, self ).__init__()
		self.name = 'PDB-block_class'
		self.text = root.text
	
	def __call__( self ):
		pass


class Int_fuzz_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_, self ).__init__()
		self.name = 'Int-fuzz'
		#jedna z opcji dla ['Int-fuzz_lim', 'Int-fuzz_p-m', 'Int-fuzz_range', 'Int-fuzz_alt', 'Int-fuzz_pct']
		if 'Int-fuzz_lim' in [ x.tag for x in root.getchildren() ]:
			self.int_fuzz_lim_ = Int_fuzz_lim_( root.find('Int-fuzz_lim') )
		elif 'Int-fuzz_p-m' in [ x.tag for x in root.getchildren() ]:
			self.int_fuzz_p_m__ = Int_fuzz_p_m__( root.find('Int-fuzz_p-m') )
		elif 'Int-fuzz_range' in [ x.tag for x in root.getchildren() ]:
			self.int_fuzz_range_ = Int_fuzz_range_( root.find('Int-fuzz_range') )
		elif 'Int-fuzz_alt' in [ x.tag for x in root.getchildren() ]:
			self.int_fuzz_alt_ = Int_fuzz_alt_( root.find('Int-fuzz_alt') )
		else:
			self.int_fuzz_pct_ = Int_fuzz_pct_( root.find('Int-fuzz_pct') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_product_strand__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_product_strand__, self ).__init__()
		self.name = 'Spliced-exon_product-strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_cross_reference__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_cross_reference__, self ).__init__()
		self.name = 'PIR-block_cross-reference'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annot_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annot_id_, self ).__init__()
		self.name = 'Annot-id'
		#jedna z opcji dla ['Annot-id_ncbi', 'Annot-id_other', 'Annot-id_local', 'Annot-id_general']
		if 'Annot-id_ncbi' in [ x.tag for x in root.getchildren() ]:
			self.annot_id_ncbi_ = Annot_id_ncbi_( root.find('Annot-id_ncbi') )
		elif 'Annot-id_other' in [ x.tag for x in root.getchildren() ]:
			self.annot_id_other_ = Annot_id_other_( root.find('Annot-id_other') )
		elif 'Annot-id_local' in [ x.tag for x in root.getchildren() ]:
			self.annot_id_local_ = Annot_id_local_( root.find('Annot-id_local') )
		else:
			self.annot_id_general_ = Annot_id_general_( root.find('Annot-id_general') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Feat_id_gibb_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Feat_id_gibb_, self ).__init__()
		self.name = 'Feat-id_gibb'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seg_numseg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_numseg_, self ).__init__()
		self.name = 'Packed-seg_numseg'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_book_coll_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_book_coll_, self ).__init__()
		self.name = 'Cit-book_coll'
		self.title = Title( root.find('Title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_entry_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Seq_entry_, self ).__init__()
		self.name = 'Seq-entry'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		#jedna z opcji dla ['Seq-entry_seq', 'Seq-entry_set']
		if 'Seq-entry_seq' in [ x.tag for x in root.getchildren() ]:
			self.seq_entry_seq_ = Seq_entry_seq_( root.find('Seq-entry_seq') )
		else:
			self.seq_entry_set_ = root.find( 'Seq-entry_set' )
			self.to_evaluate.append( ('Seq-entry_set', '') )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_plasnm_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_plasnm_, self ).__init__()
		self.name = 'SP-block_plasnm'
		if root.find('SP-block_plasnm_E') is not None:
			self.sp_block_plasnm_e_ = [ SP_block_plasnm_E_(element) for element in root.findall('SP-block_plasnm_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_gibbsq_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_gibbsq_, self ).__init__()
		self.name = 'Seq-id_gibbsq'
		self.text = root.text
	
	def __call__( self ):
		pass


class RNA_gen_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_gen_, self ).__init__()
		self.name = 'RNA-gen'
		if root.find('RNA-gen_quals') is not None:
			self.rna_gen_quals_ = RNA_gen_quals_( root.find('RNA-gen_quals') )
		else:
			pass
		if root.find('RNA-gen_product') is not None:
			self.rna_gen_product_ = RNA_gen_product_( root.find('RNA-gen_product') )
		else:
			pass
		if root.find('RNA-gen_class') is not None:
			self.rna_gen_class_ = RNA_gen_class_( root.find('RNA-gen_class') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonBytes_table_bytes_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonBytes_table_bytes_, self ).__init__()
		self.name = 'CommonBytes-table_bytes'
		if root.find('CommonBytes-table_bytes_E') is not None:
			self.commonbytes_table_bytes_e_ = [ CommonBytes_table_bytes_E_(element) for element in root.findall('CommonBytes-table_bytes_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_ext_, self ).__init__()
		self.name = 'Seq-feat_ext'
		self.user_object_ = User_object_( root.find('User-object') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Ref_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Ref_ext_, self ).__init__()
		self.name = 'Ref-ext'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_jta( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_jta, self ).__init__()
		self.name = 'Title_E_jta'
		self.text = root.text
	
	def __call__( self ):
		pass


class Author_affil( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Author_affil, self ).__init__()
		self.name = 'Author_affil'
		self.affil = Affil( root.find('Affil') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_allele_frequency__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_allele_frequency__, self ).__init__()
		self.name = 'Variation-ref_allele-frequency'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cdregion_stops( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_stops, self ).__init__()
		self.name = 'Cdregion_stops'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_data_set_variations_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_data_set_variations_, self ).__init__()
		self.name = 'Variation-ref_data_set_variations'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.variation_ref_ = root.findall( 'Variation-ref' )
		self.to_evaluate.append( ( 'Variation-ref', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_cdregion( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_cdregion, self ).__init__()
		self.name = 'SeqFeatData_cdregion'
		self.cdregion = Cdregion( root.find('Cdregion') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceSupport_protein( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceSupport_protein, self ).__init__()
		self.name = 'ModelEvidenceSupport_protein'
		if root.find('ModelEvidenceItem') is not None:
			self.modelevidenceitem = [ ModelEvidenceItem(element) for element in root.findall('ModelEvidenceItem') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gene_ref_formal_name__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_formal_name__, self ).__init__()
		self.name = 'Gene-ref_formal-name'
		self.gene_nomenclature_ = Gene_nomenclature_( root.find('Gene-nomenclature') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_data_ftable_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_ftable_, self ).__init__()
		self.name = 'Seq-annot_data_ftable'
		if root.find('Seq-feat') is not None:
			self.seq_feat_ = [ Seq_feat_(element) for element in root.findall('Seq-feat') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_partial_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_partial_, self ).__init__()
		self.name = 'Spliced-exon_partial'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Cit_pat_app_date__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_app_date__, self ).__init__()
		self.name = 'Cit-pat_app-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_exon_ext_, self ).__init__()
		self.name = 'Spliced-exon_ext'
		if root.find('User-object') is not None:
			self.user_object_ = [ User_object_(element) for element in root.findall('User-object') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceItem_exon_length_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceItem_exon_length_, self ).__init__()
		self.name = 'ModelEvidenceItem_exon-length'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceItem_supports_all_exon_combo___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceItem_supports_all_exon_combo___, self ).__init__()
		self.name = 'ModelEvidenceItem_supports-all-exon-combo'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Spliced_exon_genomic_end__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_genomic_end__, self ).__init__()
		self.name = 'Spliced-exon_genomic-end'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_seg_master_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Sparse_seg_master_id__, self ).__init__()
		self.name = 'Sparse-seg_master-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_starts_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_starts_, self ).__init__()
		self.name = 'Dense-seg_starts'
		if root.find('Dense-seg_starts_E') is not None:
			self.dense_seg_starts_e_ = [ Dense_seg_starts_E_(element) for element in root.findall('Dense-seg_starts_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PRF_ExtraSrc_part_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_ExtraSrc_part_, self ).__init__()
		self.name = 'PRF-ExtraSrc_part'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_data_unknown_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_data_unknown_, self ).__init__()
		self.name = 'Variation-ref_data_unknown'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_div( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_div, self ).__init__()
		self.name = 'Affil_std_div'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_gibbmt_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_gibbmt_, self ).__init__()
		self.name = 'Seq-id_gibbmt'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_biosrc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_biosrc, self ).__init__()
		self.name = 'SeqFeatData_biosrc'
		self.biosource = BioSource( root.find('BioSource') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PCRPrimerSet( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRPrimerSet, self ).__init__()
		self.name = 'PCRPrimerSet'
		if root.find('PCRPrimer') is not None:
			self.pcrprimer = [ PCRPrimer(element) for element in root.findall('PCRPrimer') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_title_, self ).__init__()
		self.name = 'Seq-feat_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_sub_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_sub_date_, self ).__init__()
		self.name = 'Cit-sub_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_desc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_desc_, self ).__init__()
		self.name = 'Seq-annot_desc'
		self.annot_descr_ = Annot_descr_( root.find('Annot-descr') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_exts_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_exts_, self ).__init__()
		self.name = 'Seq-feat_exts'
		if root.find('User-object') is not None:
			self.user_object_ = [ User_object_(element) for element in root.findall('User-object') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_pub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_pub, self ).__init__()
		self.name = 'Seqdesc_pub'
		self.pubdesc = Pubdesc( root.find('Pubdesc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_block_exp_method__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_exp_method__, self ).__init__()
		self.name = 'PDB-block_exp-method'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_loc_equiv_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_equiv_, self ).__init__()
		self.name = 'Seq-loc_equiv'
		self.seq_loc_equiv__ = Seq_loc_equiv__( root.find('Seq-loc-equiv') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_int__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_int__, self ).__init__()
		self.name = 'SeqTable-multi-data_int'
		if root.find('SeqTable-multi-data_int_E') is not None:
			self.seqtable_multi_data_int_e__ = [ SeqTable_multi_data_int_E__(element) for element in root.findall('SeqTable-multi-data_int_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_rsite( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_rsite, self ).__init__()
		self.name = 'SeqFeatData_rsite'
		self.rsite_ref_ = Rsite_ref_( root.find('Rsite-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_mesh_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_mesh_, self ).__init__()
		self.name = 'Medline-mesh'
		if root.find('Medline-mesh_mp') is not None:
			self.medline_mesh_mp_ = Medline_mesh_mp_( root.find('Medline-mesh_mp') )
		else:
			pass
		self.medline_mesh_term_ = Medline_mesh_term_( root.find('Medline-mesh_term') )
		if root.find('Medline-mesh_qual') is not None:
			self.medline_mesh_qual_ = Medline_mesh_qual_( root.find('Medline-mesh_qual') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class IUPACna( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( IUPACna, self ).__init__()
		self.name = 'IUPACna'
		self.text = root.text
	
	def __call__( self ):
		pass


class Spliced_exon_acceptor_before_exon___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_acceptor_before_exon___, self ).__init__()
		self.name = 'Spliced-exon_acceptor-before-exon'
		self.splice_site_ = Splice_site_( root.find('Splice-site') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Num_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Num_ref_, self ).__init__()
		self.name = 'Num-ref'
		self.num_ref_type_ = Num_ref_type_( root.find('Num-ref_type') )
		if root.find('Num-ref_aligns') is not None:
			self.num_ref_aligns_ = Num_ref_aligns_( root.find('Num-ref_aligns') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_diag_len_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_diag_len_, self ).__init__()
		self.name = 'Dense-diag_len'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annotdesc_comment( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annotdesc_comment, self ).__init__()
		self.name = 'Annotdesc_comment'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_exp_ev__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_exp_ev__, self ).__init__()
		self.name = 'Seq-feat_exp-ev'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['experimental', 'not-experimental']
		self.value = root.get('value')


class PII( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PII, self ).__init__()
		self.name = 'PII'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_object_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_object_class_, self ).__init__()
		self.name = 'User-object_class'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub_man( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_man, self ).__init__()
		self.name = 'Pub_man'
		self.cit_let_ = Cit_let_( root.find('Cit-let') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gene_nomenclature_status_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_nomenclature_status_, self ).__init__()
		self.name = 'Gene-nomenclature_status'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'official', 'interim']
		self.value = root.get('value')


class Real_graph_min_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Real_graph_min_, self ).__init__()
		self.name = 'Real-graph_min'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_phone( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_phone, self ).__init__()
		self.name = 'Affil_std_phone'
		self.text = root.text
	
	def __call__( self ):
		pass


class RNA_qual_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_qual_qual_, self ).__init__()
		self.name = 'RNA-qual_qual'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_std_second_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_second_, self ).__init__()
		self.name = 'Date-std_second'
		self.text = root.text
	
	def __call__( self ):
		pass


class GB_block_keywords_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_keywords_, self ).__init__()
		self.name = 'GB-block_keywords'
		if root.find('GB-block_keywords_E') is not None:
			self.gb_block_keywords_e_ = [ GB_block_keywords_E_(element) for element in root.findall('GB-block_keywords_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_retract( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_retract, self ).__init__()
		self.name = 'Imprint_retract'
		self.citretract = CitRetract( root.find('CitRetract') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_genomic_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_seg_genomic_id__, self ).__init__()
		self.name = 'Spliced-seg_genomic-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_population_data__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_population_data__, self ).__init__()
		self.name = 'Variation-ref_population-data'
		if root.find('Population-data') is not None:
			self.population_data_ = [ Population_data_(element) for element in root.findall('Population-data') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_gen_, self ).__init__()
		self.name = 'Cit-gen'
		if root.find('Cit-gen_cit') is not None:
			self.cit_gen_cit_ = Cit_gen_cit_( root.find('Cit-gen_cit') )
		else:
			pass
		if root.find('Cit-gen_pages') is not None:
			self.cit_gen_pages_ = Cit_gen_pages_( root.find('Cit-gen_pages') )
		else:
			pass
		if root.find('Cit-gen_volume') is not None:
			self.cit_gen_volume_ = Cit_gen_volume_( root.find('Cit-gen_volume') )
		else:
			pass
		if root.find('Cit-gen_authors') is not None:
			self.cit_gen_authors_ = Cit_gen_authors_( root.find('Cit-gen_authors') )
		else:
			pass
		if root.find('Cit-gen_date') is not None:
			self.cit_gen_date_ = Cit_gen_date_( root.find('Cit-gen_date') )
		else:
			pass
		if root.find('Cit-gen_issue') is not None:
			self.cit_gen_issue_ = Cit_gen_issue_( root.find('Cit-gen_issue') )
		else:
			pass
		if root.find('Cit-gen_title') is not None:
			self.cit_gen_title_ = Cit_gen_title_( root.find('Cit-gen_title') )
		else:
			pass
		if root.find('Cit-gen_pmid') is not None:
			self.cit_gen_pmid_ = Cit_gen_pmid_( root.find('Cit-gen_pmid') )
		else:
			pass
		if root.find('Cit-gen_muid') is not None:
			self.cit_gen_muid_ = Cit_gen_muid_( root.find('Cit-gen_muid') )
		else:
			pass
		if root.find('Cit-gen_serial-number') is not None:
			self.cit_gen_serial_number__ = Cit_gen_serial_number__( root.find('Cit-gen_serial-number') )
		else:
			pass
		if root.find('Cit-gen_journal') is not None:
			self.cit_gen_journal_ = Cit_gen_journal_( root.find('Cit-gen_journal') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_block_compound_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_compound_, self ).__init__()
		self.name = 'PDB-block_compound'
		if root.find('PDB-block_compound_E') is not None:
			self.pdb_block_compound_e_ = [ PDB_block_compound_E_(element) for element in root.findall('PDB-block_compound_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_iso_jta_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_iso_jta_, self ).__init__()
		self.name = 'Title_E_iso-jta'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub_set_pub_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_pub_, self ).__init__()
		self.name = 'Pub-set_pub'
		if root.find('Pub') is not None:
			self.pub = [ Pub(element) for element in root.findall('Pub') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Id_pat_doc_type__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Id_pat_doc_type__, self ).__init__()
		self.name = 'Id-pat_doc-type'
		self.text = root.text
	
	def __call__( self ):
		pass


class PDB_seq_id_chain__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_seq_id_chain__, self ).__init__()
		self.name = 'PDB-seq-id_chain'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imp_feat_descr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imp_feat_descr_, self ).__init__()
		self.name = 'Imp-feat_descr'
		self.text = root.text
	
	def __call__( self ):
		pass


class Int_graph_max_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_graph_max_, self ).__init__()
		self.name = 'Int-graph_max'
		self.text = root.text
	
	def __call__( self ):
		pass


class MolInfo_biomol( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MolInfo_biomol, self ).__init__()
		self.name = 'MolInfo_biomol'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'genomic', 'pre-RNA', 'mRNA', 'rRNA', 'tRNA', 'snRNA', 'scRNA', 'peptide', 'other-genetic', 'genomic-mRNA', 'cRNA', 'snoRNA', 'transcribed-RNA', 'ncRNA', 'tmRNA', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seqdesc_method( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_method, self ).__init__()
		self.name = 'Seqdesc_method'
		self.gibb_method_ = GIBB_method_( root.find('GIBB-method') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_authors_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_pat_authors_, self ).__init__()
		self.name = 'Cit-pat_authors'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Feat_id_general_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Feat_id_general_, self ).__init__()
		self.name = 'Feat-id_general'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GB_block_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_date_, self ).__init__()
		self.name = 'GB-block_date'
		self.text = root.text
	
	def __call__( self ):
		pass


class Bioseq_set_seq_set__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Bioseq_set_seq_set__, self ).__init__()
		self.name = 'Bioseq-set_seq-set'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.seq_entry_ = root.findall( 'Seq-entry' )
		self.to_evaluate.append( ( 'Seq-entry', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_source( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_source, self ).__init__()
		self.name = 'Seqdesc_source'
		self.biosource = BioSource( root.find('BioSource') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_rna( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_rna, self ).__init__()
		self.name = 'Txinit_rna'
		if root.find('Txinit_rna_E') is not None:
			self.txinit_rna_e = [ Txinit_rna_E(element) for element in root.findall('Txinit_rna_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_field_data_, self ).__init__()
		self.name = 'User-field_data'
		#jedna z opcji dla ['User-field_data_bool', 'User-field_data_str', 'User-field_data_strs', 'User-field_data_ints', 'User-field_data_int', 'User-field_data_oss', 'User-field_data_fields', 'User-field_data_os', 'User-field_data_objects', 'User-field_data_real', 'User-field_data_reals', 'User-field_data_object']
		if 'User-field_data_bool' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_bool_ = User_field_data_bool_( root.find('User-field_data_bool') )
		elif 'User-field_data_str' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_str_ = User_field_data_str_( root.find('User-field_data_str') )
		elif 'User-field_data_strs' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_strs_ = User_field_data_strs_( root.find('User-field_data_strs') )
		elif 'User-field_data_ints' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_ints_ = User_field_data_ints_( root.find('User-field_data_ints') )
		elif 'User-field_data_int' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_int_ = User_field_data_int_( root.find('User-field_data_int') )
		elif 'User-field_data_oss' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_oss_ = User_field_data_oss_( root.find('User-field_data_oss') )
		elif 'User-field_data_fields' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_fields_ = User_field_data_fields_( root.find('User-field_data_fields') )
		elif 'User-field_data_os' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_os_ = User_field_data_os_( root.find('User-field_data_os') )
		elif 'User-field_data_objects' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_objects_ = User_field_data_objects_( root.find('User-field_data_objects') )
		elif 'User-field_data_real' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_real_ = User_field_data_real_( root.find('User-field_data_real') )
		elif 'User-field_data_reals' in [ x.tag for x in root.getchildren() ]:
			self.user_field_data_reals_ = User_field_data_reals_( root.find('User-field_data_reals') )
		else:
			self.user_field_data_object_ = User_field_data_object_( root.find('User-field_data_object') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Real_graph_values_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Real_graph_values_E_, self ).__init__()
		self.name = 'Real-graph_values_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Numbering( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Numbering, self ).__init__()
		self.name = 'Numbering'
		#jedna z opcji dla ['Numbering_enum', 'Numbering_real', 'Numbering_ref', 'Numbering_cont']
		if 'Numbering_enum' in [ x.tag for x in root.getchildren() ]:
			self.numbering_enum = Numbering_enum( root.find('Numbering_enum') )
		elif 'Numbering_real' in [ x.tag for x in root.getchildren() ]:
			self.numbering_real = Numbering_real( root.find('Numbering_real') )
		elif 'Numbering_ref' in [ x.tag for x in root.getchildren() ]:
			self.numbering_ref = Numbering_ref( root.find('Numbering_ref') )
		else:
			self.numbering_cont = Numbering_cont( root.find('Numbering_cont') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_ext_seg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_ext_seg_, self ).__init__()
		self.name = 'Seq-ext_seg'
		self.seg_ext_ = Seg_ext_( root.find('Seg-ext') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_inittype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_inittype, self ).__init__()
		self.name = 'Txinit_inittype'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'single', 'multiple', 'region']
		self.value = root.get('value')


class Tx_evidence_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Tx_evidence_, self ).__init__()
		self.name = 'Tx-evidence'
		self.tx_evidence_exp_code__ = Tx_evidence_exp_code__( root.find('Tx-evidence_exp-code') )
		if root.find('Tx-evidence_from-homolog') is not None:
			self.tx_evidence_from_homolog__ = Tx_evidence_from_homolog__( root.find('Tx-evidence_from-homolog') )
		else:
			pass
		if root.find('Tx-evidence_low-prec-data') is not None:
			self.tx_evidence_low_prec_data___ = Tx_evidence_low_prec_data___( root.find('Tx-evidence_low-prec-data') )
		else:
			pass
		if root.find('Tx-evidence_expression-system') is not None:
			self.tx_evidence_expression_system__ = Tx_evidence_expression_system__( root.find('Tx-evidence_expression-system') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatSupport_experiment( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatSupport_experiment, self ).__init__()
		self.name = 'SeqFeatSupport_experiment'
		if root.find('ExperimentSupport') is not None:
			self.experimentsupport = [ ExperimentSupport(element) for element in root.findall('ExperimentSupport') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_item_multiplier_fuzz__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Delta_item_multiplier_fuzz__, self ).__init__()
		self.name = 'Delta-item_multiplier-fuzz'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_graph_int_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_graph_int_, self ).__init__()
		self.name = 'Seq-graph_graph_int'
		self.int_graph_ = Int_graph_( root.find('Int-graph') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Patent_priority_country_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_priority_country_, self ).__init__()
		self.name = 'Patent-priority_country'
		self.text = root.text
	
	def __call__( self ):
		pass


class CommonBytes_table_indexes_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonBytes_table_indexes_E_, self ).__init__()
		self.name = 'CommonBytes-table_indexes_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_sub_descr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_sub_descr_, self ).__init__()
		self.name = 'Cit-sub_descr'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_allele_state__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_allele_state__, self ).__init__()
		self.name = 'Variation-ref_allele-state'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'homozygous', 'heterozygous', 'hemizygous', 'nullizygous', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class NCBI8na( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBI8na, self ).__init__()
		self.name = 'NCBI8na'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_table_num_rows__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_table_num_rows__, self ).__init__()
		self.name = 'Seq-table_num-rows'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_synonyms_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_synonyms_E_, self ).__init__()
		self.name = 'Variation-ref_synonyms_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_update_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_update_date_, self ).__init__()
		self.name = 'Seqdesc_update-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_string__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_string__, self ).__init__()
		self.name = 'SeqTable-multi-data_string'
		if root.find('SeqTable-multi-data_string_E') is not None:
			self.seqtable_multi_data_string_e__ = [ SeqTable_multi_data_string_E__(element) for element in root.findall('SeqTable-multi-data_string_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_rn_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_rn_, self ).__init__()
		self.name = 'Medline-rn'
		self.medline_rn_type_ = Medline_rn_type_( root.find('Medline-rn_type') )
		if root.find('Medline-rn_cit') is not None:
			self.medline_rn_cit_ = Medline_rn_cit_( root.find('Medline-rn_cit') )
		else:
			pass
		self.medline_rn_name_ = Medline_rn_name_( root.find('Medline-rn_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_pgcode( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_pgcode, self ).__init__()
		self.name = 'OrgName_pgcode'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_imp( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_imp, self ).__init__()
		self.name = 'SeqFeatData_imp'
		self.imp_feat_ = Imp_feat_( root.find('Imp-feat') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Auth_list_names_std_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_names_std_, self ).__init__()
		self.name = 'Auth-list_names_std'
		if root.find('Author') is not None:
			self.author = [ Author(element) for element in root.findall('Author') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgMod_subtype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgMod_subtype, self ).__init__()
		self.name = 'OrgMod_subtype'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['strain', 'substrain', 'type', 'subtype', 'variety', 'serotype', 'serogroup', 'serovar', 'cultivar', 'pathovar', 'chemovar', 'biovar', 'biotype', 'group', 'subgroup', 'isolate', 'common', 'acronym', 'dosage', 'nat-host', 'sub-species', 'specimen-voucher', 'authority', 'forma', 'forma-specialis', 'ecotype', 'synonym', 'anamorph', 'teleomorph', 'breed', 'gb-acronym', 'gb-anamorph', 'gb-synonym', 'culture-collection', 'bio-material', 'metagenome-source', 'type-material', 'old-lineage', 'old-name', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seq_id_patent_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_patent_, self ).__init__()
		self.name = 'Seq-id_patent'
		self.patent_seq_id__ = Patent_seq_id__( root.find('Patent-seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_equiv__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_equiv__, self ).__init__()
		self.name = 'Seq-loc-equiv'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.seq_loc_ = root.findall( 'Seq-loc' )
		self.to_evaluate.append( ( 'Seq-loc', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PartialOrgName( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PartialOrgName, self ).__init__()
		self.name = 'PartialOrgName'
		if root.find('TaxElement') is not None:
			self.taxelement = [ TaxElement(element) for element in root.findall('TaxElement') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Patent_seq_id_seqid__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_seq_id_seqid__, self ).__init__()
		self.name = 'Patent-seq-id_seqid'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_somatic_origin_E_condition_description__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_somatic_origin_E_condition_description__, self ).__init__()
		self.name = 'Variation-ref_somatic-origin_E_condition_description'
		self.text = root.text
	
	def __call__( self ):
		pass


class PIR_block_host_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_host_, self ).__init__()
		self.name = 'PIR-block_host'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_abstract_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_abstract_, self ).__init__()
		self.name = 'Medline-entry_abstract'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_jour_imp_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_jour_imp_, self ).__init__()
		self.name = 'Cit-jour_imp'
		self.imprint = Imprint( root.find('Imprint') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_seq_raw__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_seq_raw__, self ).__init__()
		self.name = 'PIR-block_seq-raw'
		self.text = root.text
	
	def __call__( self ):
		pass


class Name_std_middle_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_middle_, self ).__init__()
		self.name = 'Name-std_middle'
		self.text = root.text
	
	def __call__( self ):
		pass


class SP_block_keywords_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_keywords_, self ).__init__()
		self.name = 'SP-block_keywords'
		if root.find('SP-block_keywords_E') is not None:
			self.sp_block_keywords_e_ = [ SP_block_keywords_E_(element) for element in root.findall('SP-block_keywords_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Score_value( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Score_value, self ).__init__()
		self.name = 'Score_value'
		#jedna z opcji dla ['Score_value_int', 'Score_value_real']
		if 'Score_value_int' in [ x.tag for x in root.getchildren() ]:
			self.score_value_int = Score_value_int( root.find('Score_value_int') )
		else:
			self.score_value_real = Score_value_real( root.find('Score_value_real') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceSupport_full_length_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceSupport_full_length_, self ).__init__()
		self.name = 'ModelEvidenceSupport_full-length'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Packed_seqpnt_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Packed_seqpnt_, self ).__init__()
		self.name = 'Packed-seqpnt'
		self.packed_seqpnt_id_ = Packed_seqpnt_id_( root.find('Packed-seqpnt_id') )
		if root.find('Packed-seqpnt_fuzz') is not None:
			self.packed_seqpnt_fuzz_ = Packed_seqpnt_fuzz_( root.find('Packed-seqpnt_fuzz') )
		else:
			pass
		if root.find('Packed-seqpnt_strand') is not None:
			self.packed_seqpnt_strand_ = Packed_seqpnt_strand_( root.find('Packed-seqpnt_strand') )
		else:
			pass
		self.packed_seqpnt_points_ = Packed_seqpnt_points_( root.find('Packed-seqpnt_points') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_single_data_int__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_single_data_int__, self ).__init__()
		self.name = 'SeqTable-single-data_int'
		self.text = root.text
	
	def __call__( self ):
		pass


class EMBL_dbname_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_dbname_name_, self ).__init__()
		self.name = 'EMBL-dbname_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Title_E_isbn( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_isbn, self ).__init__()
		self.name = 'Title_E_isbn'
		self.text = root.text
	
	def __call__( self ):
		pass


class PIR_block_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	def __init__( self, root ):
		super( PIR_block_, self ).__init__()
		self.name = 'PIR-block'
		if root.find('PIR-block_had-punct') is not None:
			self.pir_block_had_punct__ = PIR_block_had_punct__( root.find('PIR-block_had-punct') )
		else:
			pass
		if root.find('PIR-block_placement') is not None:
			self.pir_block_placement_ = PIR_block_placement_( root.find('PIR-block_placement') )
		else:
			pass
		if root.find('PIR-block_seqref') is not None:
			self.pir_block_seqref_ = PIR_block_seqref_( root.find('PIR-block_seqref') )
		else:
			pass
		if root.find('PIR-block_includes') is not None:
			self.pir_block_includes_ = PIR_block_includes_( root.find('PIR-block_includes') )
		else:
			pass
		if root.find('PIR-block_summary') is not None:
			self.pir_block_summary_ = PIR_block_summary_( root.find('PIR-block_summary') )
		else:
			pass
		if root.find('PIR-block_date') is not None:
			self.pir_block_date_ = PIR_block_date_( root.find('PIR-block_date') )
		else:
			pass
		if root.find('PIR-block_host') is not None:
			self.pir_block_host_ = PIR_block_host_( root.find('PIR-block_host') )
		else:
			pass
		if root.find('PIR-block_superfamily') is not None:
			self.pir_block_superfamily_ = PIR_block_superfamily_( root.find('PIR-block_superfamily') )
		else:
			pass
		if root.find('PIR-block_cross-reference') is not None:
			self.pir_block_cross_reference__ = PIR_block_cross_reference__( root.find('PIR-block_cross-reference') )
		else:
			pass
		if root.find('PIR-block_seq-raw') is not None:
			self.pir_block_seq_raw__ = PIR_block_seq_raw__( root.find('PIR-block_seq-raw') )
		else:
			pass
		if root.find('PIR-block_genetic') is not None:
			self.pir_block_genetic_ = PIR_block_genetic_( root.find('PIR-block_genetic') )
		else:
			pass
		if root.find('PIR-block_keywords') is not None:
			self.pir_block_keywords_ = PIR_block_keywords_( root.find('PIR-block_keywords') )
		else:
			pass
		if root.find('PIR-block_source') is not None:
			self.pir_block_source_ = PIR_block_source_( root.find('PIR-block_source') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_art_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_art_title_, self ).__init__()
		self.name = 'Cit-art_title'
		self.title = Title( root.find('Title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_desc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_desc_, self ).__init__()
		self.name = 'Prot-ref_desc'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_table_columns_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( Seq_table_columns_, self ).__init__()
		self.name = 'Seq-table_columns'
		if root.find('SeqTable-column') is not None:
			self.seqtable_column_ = [ SeqTable_column_(element) for element in root.findall('SeqTable-column') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_reals_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_reals_E_, self ).__init__()
		self.name = 'User-field_data_reals_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imprint_pages( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_pages, self ).__init__()
		self.name = 'Imprint_pages'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_column_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_column_, self ).__init__()
		self.name = 'SeqTable-column'
		if root.find('SeqTable-column_sparse-other') is not None:
			self.seqtable_column_sparse_other__ = SeqTable_column_sparse_other__( root.find('SeqTable-column_sparse-other') )
		else:
			pass
		self.seqtable_column_header_ = SeqTable_column_header_( root.find('SeqTable-column_header') )
		if root.find('SeqTable-column_sparse') is not None:
			self.seqtable_column_sparse_ = SeqTable_column_sparse_( root.find('SeqTable-column_sparse') )
		else:
			pass
		if root.find('SeqTable-column_data') is not None:
			self.seqtable_column_data_ = SeqTable_column_data_( root.find('SeqTable-column_data') )
		else:
			pass
		if root.find('SeqTable-column_default') is not None:
			self.seqtable_column_default_ = SeqTable_column_default_( root.find('SeqTable-column_default') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_ints_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_ints_E_, self ).__init__()
		self.name = 'User-field_data_ints_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_hist_replaces_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_hist_replaces_, self ).__init__()
		self.name = 'Seq-hist_replaces'
		self.seq_hist_rec__ = Seq_hist_rec__( root.find('Seq-hist-rec') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_modif( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_modif, self ).__init__()
		self.name = 'Seqdesc_modif'
		if root.find('GIBB-mod') is not None:
			self.gibb_mod_ = [ GIBB_mod_(element) for element in root.findall('GIBB-mod') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_keywords_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_keywords_E_, self ).__init__()
		self.name = 'SP-block_keywords_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub, self ).__init__()
		self.name = 'Pub'
		#jedna z opcji dla ['Pub_man', 'Pub_medline', 'Pub_proc', 'Pub_sub', 'Pub_article', 'Pub_gen', 'Pub_pmid', 'Pub_pat-id', 'Pub_book', 'Pub_muid', 'Pub_equiv', 'Pub_patent', 'Pub_journal']
		if 'Pub_man' in [ x.tag for x in root.getchildren() ]:
			self.pub_man = Pub_man( root.find('Pub_man') )
		elif 'Pub_medline' in [ x.tag for x in root.getchildren() ]:
			self.pub_medline = Pub_medline( root.find('Pub_medline') )
		elif 'Pub_proc' in [ x.tag for x in root.getchildren() ]:
			self.pub_proc = Pub_proc( root.find('Pub_proc') )
		elif 'Pub_sub' in [ x.tag for x in root.getchildren() ]:
			self.pub_sub = Pub_sub( root.find('Pub_sub') )
		elif 'Pub_article' in [ x.tag for x in root.getchildren() ]:
			self.pub_article = Pub_article( root.find('Pub_article') )
		elif 'Pub_gen' in [ x.tag for x in root.getchildren() ]:
			self.pub_gen = Pub_gen( root.find('Pub_gen') )
		elif 'Pub_pmid' in [ x.tag for x in root.getchildren() ]:
			self.pub_pmid = Pub_pmid( root.find('Pub_pmid') )
		elif 'Pub_pat-id' in [ x.tag for x in root.getchildren() ]:
			self.pub_pat_id_ = Pub_pat_id_( root.find('Pub_pat-id') )
		elif 'Pub_book' in [ x.tag for x in root.getchildren() ]:
			self.pub_book = Pub_book( root.find('Pub_book') )
		elif 'Pub_muid' in [ x.tag for x in root.getchildren() ]:
			self.pub_muid = Pub_muid( root.find('Pub_muid') )
		elif 'Pub_equiv' in [ x.tag for x in root.getchildren() ]:
			self.pub_equiv = Pub_equiv( root.find('Pub_equiv') )
		elif 'Pub_patent' in [ x.tag for x in root.getchildren() ]:
			self.pub_patent = Pub_patent( root.find('Pub_patent') )
		else:
			self.pub_journal = Pub_journal( root.find('Pub_journal') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_literal_length_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_literal_length_, self ).__init__()
		self.name = 'Seq-literal_length'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_table_feat_type__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_table_feat_type__, self ).__init__()
		self.name = 'Seq-table_feat-type'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_cont_refnum_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_cont_refnum_, self ).__init__()
		self.name = 'Num-cont_refnum'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_align_bounds_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_bounds_, self ).__init__()
		self.name = 'Seq-align_bounds'
		if root.find('Seq-loc') is not None:
			self.seq_loc_ = [ Seq_loc_(element) for element in root.findall('Seq-loc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_mesh_term_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_mesh_term_, self ).__init__()
		self.name = 'Medline-mesh_term'
		self.text = root.text
	
	def __call__( self ):
		pass


class Population_data_population_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_population_, self ).__init__()
		self.name = 'Population-data_population'
		self.text = root.text
	
	def __call__( self ):
		pass


class Name_std_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_, self ).__init__()
		self.name = 'Name-std'
		if root.find('Name-std_title') is not None:
			self.name_std_title_ = Name_std_title_( root.find('Name-std_title') )
		else:
			pass
		if root.find('Name-std_first') is not None:
			self.name_std_first_ = Name_std_first_( root.find('Name-std_first') )
		else:
			pass
		if root.find('Name-std_full') is not None:
			self.name_std_full_ = Name_std_full_( root.find('Name-std_full') )
		else:
			pass
		if root.find('Name-std_middle') is not None:
			self.name_std_middle_ = Name_std_middle_( root.find('Name-std_middle') )
		else:
			pass
		if root.find('Name-std_initials') is not None:
			self.name_std_initials_ = Name_std_initials_( root.find('Name-std_initials') )
		else:
			pass
		if root.find('Name-std_suffix') is not None:
			self.name_std_suffix_ = Name_std_suffix_( root.find('Name-std_suffix') )
		else:
			pass
		self.name_std_last_ = Name_std_last_( root.find('Name-std_last') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Name_std_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_title_, self ).__init__()
		self.name = 'Name-std_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_somatic_origin_E_condition__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_somatic_origin_E_condition__, self ).__init__()
		self.name = 'Variation-ref_somatic-origin_E_condition'
		if root.find('Variation-ref_somatic-origin_E_condition_object-id') is not None:
			self.variation_ref_somatic_origin_e_condition_object_id___ = Variation_ref_somatic_origin_E_condition_object_id___( root.find('Variation-ref_somatic-origin_E_condition_object-id') )
		else:
			pass
		if root.find('Variation-ref_somatic-origin_E_condition_description') is not None:
			self.variation_ref_somatic_origin_e_condition_description__ = Variation_ref_somatic_origin_E_condition_description__( root.find('Variation-ref_somatic-origin_E_condition_description') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_ncbieaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbieaa_, self ).__init__()
		self.name = 'Seq-data_ncbieaa'
		self.ncbieaa = NCBIeaa( root.find('NCBIeaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_pat_, self ).__init__()
		self.name = 'Cit-pat'
		if root.find('Cit-pat_date-issue') is not None:
			self.cit_pat_date_issue__ = Cit_pat_date_issue__( root.find('Cit-pat_date-issue') )
		else:
			pass
		if root.find('Cit-pat_app-date') is not None:
			self.cit_pat_app_date__ = Cit_pat_app_date__( root.find('Cit-pat_app-date') )
		else:
			pass
		if root.find('Cit-pat_priority') is not None:
			self.cit_pat_priority_ = Cit_pat_priority_( root.find('Cit-pat_priority') )
		else:
			pass
		self.cit_pat_doc_type__ = Cit_pat_doc_type__( root.find('Cit-pat_doc-type') )
		if root.find('Cit-pat_applicants') is not None:
			self.cit_pat_applicants_ = Cit_pat_applicants_( root.find('Cit-pat_applicants') )
		else:
			pass
		if root.find('Cit-pat_class') is not None:
			self.cit_pat_class_ = Cit_pat_class_( root.find('Cit-pat_class') )
		else:
			pass
		if root.find('Cit-pat_assignees') is not None:
			self.cit_pat_assignees_ = Cit_pat_assignees_( root.find('Cit-pat_assignees') )
		else:
			pass
		if root.find('Cit-pat_number') is not None:
			self.cit_pat_number_ = Cit_pat_number_( root.find('Cit-pat_number') )
		else:
			pass
		if root.find('Cit-pat_app-number') is not None:
			self.cit_pat_app_number__ = Cit_pat_app_number__( root.find('Cit-pat_app-number') )
		else:
			pass
		self.cit_pat_authors_ = Cit_pat_authors_( root.find('Cit-pat_authors') )
		self.cit_pat_country_ = Cit_pat_country_( root.find('Cit-pat_country') )
		self.cit_pat_title_ = Cit_pat_title_( root.find('Cit-pat_title') )
		if root.find('Cit-pat_abstract') is not None:
			self.cit_pat_abstract_ = Cit_pat_abstract_( root.find('Cit-pat_abstract') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Numbering_ref( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Numbering_ref, self ).__init__()
		self.name = 'Numbering_ref'
		self.num_ref_ = Num_ref_( root.find('Num-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pubdesc_reftype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_reftype, self ).__init__()
		self.name = 'Pubdesc_reftype'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['seq', 'sites', 'feats', 'no-target']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Genetic_code_E_sncbistdaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_sncbistdaa_, self ).__init__()
		self.name = 'Genetic-code_E_sncbistdaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Na_strand_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Na_strand_, self ).__init__()
		self.name = 'Na-strand'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'plus', 'minus', 'both', 'both-rev', 'other']
		self.value = root.get('value')


class RNA_ref_pseudo_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_ref_pseudo_, self ).__init__()
		self.name = 'RNA-ref_pseudo'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class PubStatusDate_pubstatus( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PubStatusDate_pubstatus, self ).__init__()
		self.name = 'PubStatusDate_pubstatus'
		self.pubstatus = PubStatus( root.find('PubStatus') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Giimport_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Giimport_id_, self ).__init__()
		self.name = 'Giimport-id'
		if root.find('Giimport-id_release') is not None:
			self.giimport_id_release_ = Giimport_id_release_( root.find('Giimport-id_release') )
		else:
			pass
		self.giimport_id_id_ = Giimport_id_id_( root.find('Giimport-id_id') )
		if root.find('Giimport-id_db') is not None:
			self.giimport_id_db_ = Giimport_id_db_( root.find('Giimport-id_db') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Affil_std_fax( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_fax, self ).__init__()
		self.name = 'Affil_std_fax'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cdregion( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Cdregion, self ).__init__()
		self.name = 'Cdregion'
		if root.find('Cdregion_orf') is not None:
			self.cdregion_orf = Cdregion_orf( root.find('Cdregion_orf') )
		else:
			pass
		if root.find('Cdregion_frame') is not None:
			self.cdregion_frame = Cdregion_frame( root.find('Cdregion_frame') )
		else:
			pass
		if root.find('Cdregion_conflict') is not None:
			self.cdregion_conflict = Cdregion_conflict( root.find('Cdregion_conflict') )
		else:
			pass
		if root.find('Cdregion_mismatch') is not None:
			self.cdregion_mismatch = Cdregion_mismatch( root.find('Cdregion_mismatch') )
		else:
			pass
		if root.find('Cdregion_code-break') is not None:
			self.cdregion_code_break_ = Cdregion_code_break_( root.find('Cdregion_code-break') )
		else:
			pass
		if root.find('Cdregion_gaps') is not None:
			self.cdregion_gaps = Cdregion_gaps( root.find('Cdregion_gaps') )
		else:
			pass
		if root.find('Cdregion_code') is not None:
			self.cdregion_code = Cdregion_code( root.find('Cdregion_code') )
		else:
			pass
		if root.find('Cdregion_stops') is not None:
			self.cdregion_stops = Cdregion_stops( root.find('Cdregion_stops') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_descr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_descr_, self ).__init__()
		self.name = 'Seq-descr'
		if root.find('Seqdesc') is not None:
			self.seqdesc = [ Seqdesc(element) for element in root.findall('Seqdesc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textseq_id_release_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textseq_id_release_, self ).__init__()
		self.name = 'Textseq-id_release'
		self.text = root.text
	
	def __call__( self ):
		pass


class Linkage_evidence_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Linkage_evidence_type_, self ).__init__()
		self.name = 'Linkage-evidence_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['paired-ends', 'align-genus', 'align-xgenus', 'align-trnscpt', 'within-clone', 'clone-contig', 'map', 'strobe', 'unspecified', 'pcr', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Medline_entry_mesh_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_mesh_, self ).__init__()
		self.name = 'Medline-entry_mesh'
		if root.find('Medline-mesh') is not None:
			self.medline_mesh_ = [ Medline_mesh_(element) for element in root.findall('Medline-mesh') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Auth_list_names_ml_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_names_ml_, self ).__init__()
		self.name = 'Auth-list_names_ml'
		if root.find('Auth-list_names_ml_E') is not None:
			self.auth_list_names_ml_e_ = [ Auth_list_names_ml_E_(element) for element in root.findall('Auth-list_names_ml_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textannot_id_accession_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textannot_id_accession_, self ).__init__()
		self.name = 'Textannot-id_accession'
		self.text = root.text
	
	def __call__( self ):
		pass


class Textseq_id_version_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textseq_id_version_, self ).__init__()
		self.name = 'Textseq-id_version'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_real_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_real_, self ).__init__()
		self.name = 'Num-real'
		if root.find('Num-real_units') is not None:
			self.num_real_units_ = Num_real_units_( root.find('Num-real_units') )
		else:
			pass
		self.num_real_b_ = Num_real_b_( root.find('Num-real_b') )
		self.num_real_a_ = Num_real_a_( root.find('Num-real_a') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Splice_site_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Splice_site_, self ).__init__()
		self.name = 'Splice-site'
		self.splice_site_bases_ = Splice_site_bases_( root.find('Splice-site_bases') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_let_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_let_type_, self ).__init__()
		self.name = 'Cit-let_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['manuscript', 'letter', 'thesis']
		self.value = root.get('value')


class Imprint_history( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_history, self ).__init__()
		self.name = 'Imprint_history'
		self.pubstatusdateset = PubStatusDateSet( root.find('PubStatusDateSet') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_segs_denseg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_denseg_, self ).__init__()
		self.name = 'Seq-align_segs_denseg'
		self.dense_seg_ = Dense_seg_( root.find('Dense-seg') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_table_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( Seq_table_, self ).__init__()
		self.name = 'Seq-table'
		self.seq_table_feat_type__ = Seq_table_feat_type__( root.find('Seq-table_feat-type') )
		if root.find('Seq-table_feat-subtype') is not None:
			self.seq_table_feat_subtype__ = Seq_table_feat_subtype__( root.find('Seq-table_feat-subtype') )
		else:
			pass
		self.seq_table_num_rows__ = Seq_table_num_rows__( root.find('Seq-table_num-rows') )
		self.seq_table_columns_ = Seq_table_columns_( root.find('Seq-table_columns') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Rsite_ref_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Rsite'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Rsite_ref_str_, self ).__init__()
		self.name = 'Rsite-ref_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class VariantProperties_confidence( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_confidence, self ).__init__()
		self.name = 'VariantProperties_confidence'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'likely-artifact', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Variation_ref_ext_locs__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_ext_locs__, self ).__init__()
		self.name = 'Variation-ref_ext-locs'
		if root.find('Ext-loc') is not None:
			self.ext_loc_ = [ Ext_loc_(element) for element in root.findall('Ext-loc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_inst_ext_, self ).__init__()
		self.name = 'Seq-inst_ext'
		self.seq_ext_ = Seq_ext_( root.find('Seq-ext') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_part_supi_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_part_supi_, self ).__init__()
		self.name = 'Imprint_part-supi'
		self.text = root.text
	
	def __call__( self ):
		pass


class Delta_item_seq_this_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Delta_item_seq_this_, self ).__init__()
		self.name = 'Delta-item_seq_this'
		self.text = root.text
	
	def __call__( self ):
		pass


class InferenceSupport_other_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( InferenceSupport_other_type_, self ).__init__()
		self.name = 'InferenceSupport_other-type'
		self.text = root.text
	
	def __call__( self ):
		pass


class PubStatusDate_date( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PubStatusDate_date, self ).__init__()
		self.name = 'PubStatusDate_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_ext_, self ).__init__()
		self.name = 'Variation-ref_ext'
		self.user_object_ = User_object_( root.find('User-object') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_b_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_b_, self ).__init__()
		self.name = 'Seq-graph_b'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_gen_cit_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_cit_, self ).__init__()
		self.name = 'Cit-gen_cit'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_literal_fuzz_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_literal_fuzz_, self ).__init__()
		self.name = 'Seq-literal_fuzz'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PubMedId( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PubMedId, self ).__init__()
		self.name = 'PubMedId'
		self.text = root.text
	
	def __call__( self ):
		pass


class OrgName_name_hybrid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	def __init__( self, root ):
		super( OrgName_name_hybrid, self ).__init__()
		self.name = 'OrgName_name_hybrid'
		self.multiorgname = MultiOrgName( root.find('MultiOrgName') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_point_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_point_id_, self ).__init__()
		self.name = 'Seq-point_id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Linkage_evidence_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Linkage_evidence_, self ).__init__()
		self.name = 'Linkage-evidence'
		self.linkage_evidence_type_ = Linkage_evidence_type_( root.find('Linkage-evidence_type') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_plasnm_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_plasnm_E_, self ).__init__()
		self.name = 'SP-block_plasnm_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Title_E_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_name, self ).__init__()
		self.name = 'Title_E_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_interval_from_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_interval_from_, self ).__init__()
		self.name = 'Seq-interval_from'
		self.text = root.text
	
	def __call__( self ):
		pass


class Numbering_real( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Numbering_real, self ).__init__()
		self.name = 'Numbering_real'
		self.num_real_ = Num_real_( root.find('Num-real') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_seq_id_mol__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_seq_id_mol__, self ).__init__()
		self.name = 'PDB-seq-id_mol'
		self.pdb_mol_id__ = PDB_mol_id__( root.find('PDB-mol-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_single_data_interval__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_single_data_interval__, self ).__init__()
		self.name = 'SeqTable-single-data_interval'
		self.seq_interval_ = Seq_interval_( root.find('Seq-interval') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_seq_confidence_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_seq_confidence_, self ).__init__()
		self.name = 'Clone-seq_confidence'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['multiple', 'na', 'nohit-rep', 'nohitnorep', 'other-chrm', 'unique', 'virtual', 'multiple-rep', 'multiplenorep', 'no-hit', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seq_loc_int_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_int_, self ).__init__()
		self.name = 'Seq-loc_int'
		self.seq_interval_ = Seq_interval_( root.find('Seq-interval') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pubdesc_comment( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_comment, self ).__init__()
		self.name = 'Pubdesc_comment'
		self.text = root.text
	
	def __call__( self ):
		pass


class Int_fuzz_lim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_lim_, self ).__init__()
		self.name = 'Int-fuzz_lim'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unk', 'gt', 'lt', 'tr', 'tl', 'circle', 'other']
		self.value = root.get('value')


class PCRPrimer( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRPrimer, self ).__init__()
		self.name = 'PCRPrimer'
		if root.find('PCRPrimer_seq') is not None:
			self.pcrprimer_seq = PCRPrimer_seq( root.find('PCRPrimer_seq') )
		else:
			pass
		if root.find('PCRPrimer_name') is not None:
			self.pcrprimer_name = PCRPrimer_name( root.find('PCRPrimer_name') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_feat_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_feat_, self ).__init__()
		self.name = 'Seq-loc_feat'
		self.feat_id_ = Feat_id_( root.find('Feat-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imp_feat_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imp_feat_, self ).__init__()
		self.name = 'Imp-feat'
		self.imp_feat_key_ = Imp_feat_key_( root.find('Imp-feat_key') )
		if root.find('Imp-feat_loc') is not None:
			self.imp_feat_loc_ = Imp_feat_loc_( root.find('Imp-feat_loc') )
		else:
			pass
		if root.find('Imp-feat_descr') is not None:
			self.imp_feat_descr_ = Imp_feat_descr_( root.find('Imp-feat_descr') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_column_sparse_other__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_column_sparse_other__, self ).__init__()
		self.name = 'SeqTable-column_sparse-other'
		self.seqtable_single_data__ = SeqTable_single_data__( root.find('SeqTable-single-data') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Delta_ext_, self ).__init__()
		self.name = 'Delta-ext'
		if root.find('Delta-seq') is not None:
			self.delta_seq_ = [ Delta_seq_(element) for element in root.findall('Delta-seq') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_table_feat_subtype__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_table_feat_subtype__, self ).__init__()
		self.name = 'Seq-table_feat-subtype'
		self.text = root.text
	
	def __call__( self ):
		pass


class Clone_ref_clone_seq__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Clone_ref_clone_seq__, self ).__init__()
		self.name = 'Clone-ref_clone-seq'
		self.clone_seq_set__ = Clone_seq_set__( root.find('Clone-seq-set') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_common_string___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_common_string___, self ).__init__()
		self.name = 'SeqTable-multi-data_common-string'
		self.commonstring_table_ = CommonString_table_( root.find('CommonString-table') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_title_, self ).__init__()
		self.name = 'Seq-graph_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class Dense_diag_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Dense_diag_ids_, self ).__init__()
		self.name = 'Dense-diag_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_item_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Delta_item_, self ).__init__()
		self.name = 'Delta-item'
		if root.find('Delta-item_action') is not None:
			self.delta_item_action_ = Delta_item_action_( root.find('Delta-item_action') )
		else:
			pass
		if root.find('Delta-item_multiplier') is not None:
			self.delta_item_multiplier_ = Delta_item_multiplier_( root.find('Delta-item_multiplier') )
		else:
			pass
		if root.find('Delta-item_seq') is not None:
			self.delta_item_seq_ = Delta_item_seq_( root.find('Delta-item_seq') )
		else:
			pass
		if root.find('Delta-item_multiplier-fuzz') is not None:
			self.delta_item_multiplier_fuzz__ = Delta_item_multiplier_fuzz__( root.find('Delta-item_multiplier-fuzz') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_mapping( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_mapping, self ).__init__()
		self.name = 'VariantProperties_mapping'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['has-other-snp', 'has-assembly-conflict', 'is-assembly-specific']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Packed_seqpnt_points_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seqpnt_points_E_, self ).__init__()
		self.name = 'Packed-seqpnt_points_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_, self ).__init__()
		self.name = 'Variation-ref'
		if root.find('Variation-ref_is-ancestral-allele') is not None:
			self.variation_ref_is_ancestral_allele___ = Variation_ref_is_ancestral_allele___( root.find('Variation-ref_is-ancestral-allele') )
		else:
			pass
		if root.find('Variation-ref_allele-origin') is not None:
			self.variation_ref_allele_origin__ = Variation_ref_allele_origin__( root.find('Variation-ref_allele-origin') )
		else:
			pass
		if root.find('Variation-ref_allele-state') is not None:
			self.variation_ref_allele_state__ = Variation_ref_allele_state__( root.find('Variation-ref_allele-state') )
		else:
			pass
		if root.find('Variation-ref_validated') is not None:
			self.variation_ref_validated_ = Variation_ref_validated_( root.find('Variation-ref_validated') )
		else:
			pass
		if root.find('Variation-ref_method') is not None:
			self.variation_ref_method_ = Variation_ref_method_( root.find('Variation-ref_method') )
		else:
			pass
		if root.find('Variation-ref_synonyms') is not None:
			self.variation_ref_synonyms_ = Variation_ref_synonyms_( root.find('Variation-ref_synonyms') )
		else:
			pass
		if root.find('Variation-ref_sample-id') is not None:
			self.variation_ref_sample_id__ = Variation_ref_sample_id__( root.find('Variation-ref_sample-id') )
		else:
			pass
		if root.find('Variation-ref_id') is not None:
			self.variation_ref_id_ = Variation_ref_id_( root.find('Variation-ref_id') )
		else:
			pass
		if root.find('Variation-ref_parent-id') is not None:
			self.variation_ref_parent_id__ = Variation_ref_parent_id__( root.find('Variation-ref_parent-id') )
		else:
			pass
		if root.find('Variation-ref_clinical-test') is not None:
			self.variation_ref_clinical_test__ = Variation_ref_clinical_test__( root.find('Variation-ref_clinical-test') )
		else:
			pass
		if root.find('Variation-ref_allele-frequency') is not None:
			self.variation_ref_allele_frequency__ = Variation_ref_allele_frequency__( root.find('Variation-ref_allele-frequency') )
		else:
			pass
		if root.find('Variation-ref_location') is not None:
			self.variation_ref_location_ = Variation_ref_location_( root.find('Variation-ref_location') )
		else:
			pass
		if root.find('Variation-ref_other-ids') is not None:
			self.variation_ref_other_ids__ = Variation_ref_other_ids__( root.find('Variation-ref_other-ids') )
		else:
			pass
		if root.find('Variation-ref_phenotype') is not None:
			self.variation_ref_phenotype_ = Variation_ref_phenotype_( root.find('Variation-ref_phenotype') )
		else:
			pass
		if root.find('Variation-ref_somatic-origin') is not None:
			self.variation_ref_somatic_origin__ = Variation_ref_somatic_origin__( root.find('Variation-ref_somatic-origin') )
		else:
			pass
		if root.find('Variation-ref_variant-prop') is not None:
			self.variation_ref_variant_prop__ = Variation_ref_variant_prop__( root.find('Variation-ref_variant-prop') )
		else:
			pass
		self.variation_ref_data_ = Variation_ref_data_( root.find('Variation-ref_data') )
		if root.find('Variation-ref_ext') is not None:
			self.variation_ref_ext_ = Variation_ref_ext_( root.find('Variation-ref_ext') )
		else:
			pass
		if root.find('Variation-ref_population-data') is not None:
			self.variation_ref_population_data__ = Variation_ref_population_data__( root.find('Variation-ref_population-data') )
		else:
			pass
		if root.find('Variation-ref_name') is not None:
			self.variation_ref_name_ = Variation_ref_name_( root.find('Variation-ref_name') )
		else:
			pass
		if root.find('Variation-ref_pub') is not None:
			self.variation_ref_pub_ = Variation_ref_pub_( root.find('Variation-ref_pub') )
		else:
			pass
		if root.find('Variation-ref_description') is not None:
			self.variation_ref_description_ = Variation_ref_description_( root.find('Variation-ref_description') )
		else:
			pass
		if root.find('Variation-ref_consequence') is not None:
			self.variation_ref_consequence_ = Variation_ref_consequence_( root.find('Variation-ref_consequence') )
		else:
			pass
		if root.find('Variation-ref_ext-locs') is not None:
			self.variation_ref_ext_locs__ = Variation_ref_ext_locs__( root.find('Variation-ref_ext-locs') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_had_punct__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_had_punct__, self ).__init__()
		self.name = 'PIR-block_had-punct'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Imprint_prepub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_prepub, self ).__init__()
		self.name = 'Imprint_prepub'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['submitted', 'in-press', 'other']
		self.value = root.get('value')


class Seq_bond_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_bond_, self ).__init__()
		self.name = 'Seq-bond'
		if root.find('Seq-bond_b') is not None:
			self.seq_bond_b_ = Seq_bond_b_( root.find('Seq-bond_b') )
		else:
			pass
		self.seq_bond_a_ = Seq_bond_a_( root.find('Seq-bond_a') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_prf( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_prf, self ).__init__()
		self.name = 'Seqdesc_prf'
		self.prf_block_ = PRF_block_( root.find('PRF-block') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Person_id_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Person_id_str_, self ).__init__()
		self.name = 'Person-id_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class VariantProperties_frequency_based_validation__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_frequency_based_validation__, self ).__init__()
		self.name = 'VariantProperties_frequency-based-validation'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['is-mutation', 'above-5pct-all', 'above-5pct-1plus', 'validated', 'above-1pct-all', 'above-1pct-1plus']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seq_data_iupacna_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_iupacna_, self ).__init__()
		self.name = 'Seq-data_iupacna'
		self.iupacna = IUPACna( root.find('IUPACna') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class IUPACaa( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( IUPACaa, self ).__init__()
		self.name = 'IUPACaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_qual_subh_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_qual_subh_, self ).__init__()
		self.name = 'Medline-qual_subh'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub_gen( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_gen, self ).__init__()
		self.name = 'Pub_gen'
		self.cit_gen_ = Cit_gen_( root.find('Cit-gen') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_status_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_status_, self ).__init__()
		self.name = 'Medline-entry_status'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['publisher', 'premedline', 'medline']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Ext_loc_location_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Ext_loc_location_, self ).__init__()
		self.name = 'Ext-loc_location'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_block_creation_date__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_creation_date__, self ).__init__()
		self.name = 'EMBL-block_creation-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_packed_int__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_packed_int__, self ).__init__()
		self.name = 'Seq-loc_packed-int'
		self.packed_seqint_ = Packed_seqint_( root.find('Packed-seqint') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	def __init__( self, root ):
		super( SP_block_, self ).__init__()
		self.name = 'SP-block'
		self.sp_block_class_ = SP_block_class_( root.find('SP-block_class') )
		if root.find('SP-block_imeth') is not None:
			self.sp_block_imeth_ = SP_block_imeth_( root.find('SP-block_imeth') )
		else:
			pass
		if root.find('SP-block_annotupd') is not None:
			self.sp_block_annotupd_ = SP_block_annotupd_( root.find('SP-block_annotupd') )
		else:
			pass
		if root.find('SP-block_keywords') is not None:
			self.sp_block_keywords_ = SP_block_keywords_( root.find('SP-block_keywords') )
		else:
			pass
		if root.find('SP-block_seqref') is not None:
			self.sp_block_seqref_ = SP_block_seqref_( root.find('SP-block_seqref') )
		else:
			pass
		if root.find('SP-block_created') is not None:
			self.sp_block_created_ = SP_block_created_( root.find('SP-block_created') )
		else:
			pass
		if root.find('SP-block_plasnm') is not None:
			self.sp_block_plasnm_ = SP_block_plasnm_( root.find('SP-block_plasnm') )
		else:
			pass
		if root.find('SP-block_extra-acc') is not None:
			self.sp_block_extra_acc__ = SP_block_extra_acc__( root.find('SP-block_extra-acc') )
		else:
			pass
		if root.find('SP-block_dbref') is not None:
			self.sp_block_dbref_ = SP_block_dbref_( root.find('SP-block_dbref') )
		else:
			pass
		if root.find('SP-block_sequpd') is not None:
			self.sp_block_sequpd_ = SP_block_sequpd_( root.find('SP-block_sequpd') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Affil( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil, self ).__init__()
		self.name = 'Affil'
		#jedna z opcji dla ['Affil_std', 'Affil_str']
		if 'Affil_std' in [ x.tag for x in root.getchildren() ]:
			self.affil_std = Affil_std( root.find('Affil_std') )
		else:
			self.affil_str = Affil_str( root.find('Affil_str') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_hist_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_inst_hist_, self ).__init__()
		self.name = 'Seq-inst_hist'
		self.seq_hist_ = Seq_hist_( root.find('Seq-hist') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_protein( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_protein, self ).__init__()
		self.name = 'Txinit_protein'
		if root.find('Prot-ref') is not None:
			self.prot_ref_ = [ Prot_ref_(element) for element in root.findall('Prot-ref') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId_pmcpid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_pmcpid, self ).__init__()
		self.name = 'ArticleId_pmcpid'
		self.pmcpid = PmcPid( root.find('PmcPid') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Trna_ext_aa_ncbistdaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_aa_ncbistdaa_, self ).__init__()
		self.name = 'Trna-ext_aa_ncbistdaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Phenotype_source( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Phenotype_source, self ).__init__()
		self.name = 'Phenotype_source'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_mol_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_mol_type_, self ).__init__()
		self.name = 'Seqdesc_mol-type'
		self.gibb_mol_ = GIBB_mol_( root.find('GIBB-mol') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pubdesc_align_group_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_align_group_, self ).__init__()
		self.name = 'Pubdesc_align-group'
		self.text = root.text
	
	def __call__( self ):
		pass


class Clone_ref_placement_method__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_ref_placement_method__, self ).__init__()
		self.name = 'Clone-ref_placement-method'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['end-seq', 'insert-alignment', 'sts', 'fish', 'fingerprint', 'end-seq-insert-alignment', 'external', 'curated', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Sparse_seg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Sparse_seg_, self ).__init__()
		self.name = 'Sparse-seg'
		if root.find('Sparse-seg_row-scores') is not None:
			self.sparse_seg_row_scores__ = Sparse_seg_row_scores__( root.find('Sparse-seg_row-scores') )
		else:
			pass
		self.sparse_seg_rows_ = Sparse_seg_rows_( root.find('Sparse-seg_rows') )
		if root.find('Sparse-seg_master-id') is not None:
			self.sparse_seg_master_id__ = Sparse_seg_master_id__( root.find('Sparse-seg_master-id') )
		else:
			pass
		if root.find('Sparse-seg_ext') is not None:
			self.sparse_seg_ext_ = Sparse_seg_ext_( root.find('Sparse-seg_ext') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_modifier_stop_codon_found____( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_modifier_stop_codon_found____, self ).__init__()
		self.name = 'Spliced-seg-modifier_stop-codon-found'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Bioseq_set_descr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Bioseq_set_descr_, self ).__init__()
		self.name = 'Bioseq-set_descr'
		self.seq_descr_ = Seq_descr_( root.find('Seq-descr') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_cit_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_cit_, self ).__init__()
		self.name = 'Seq-feat_cit'
		self.pub_set_ = Pub_set_( root.find('Pub-set') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_reals_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_reals_, self ).__init__()
		self.name = 'User-field_data_reals'
		if root.find('User-field_data_reals_E') is not None:
			self.user_field_data_reals_e_ = [ User_field_data_reals_E_(element) for element in root.findall('User-field_data_reals_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_graph_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_graph_, self ).__init__()
		self.name = 'Seq-graph_graph'
		#jedna z opcji dla ['Seq-graph_graph_int', 'Seq-graph_graph_byte', 'Seq-graph_graph_real']
		if 'Seq-graph_graph_int' in [ x.tag for x in root.getchildren() ]:
			self.seq_graph_graph_int_ = Seq_graph_graph_int_( root.find('Seq-graph_graph_int') )
		elif 'Seq-graph_graph_byte' in [ x.tag for x in root.getchildren() ]:
			self.seq_graph_graph_byte_ = Seq_graph_graph_byte_( root.find('Seq-graph_graph_byte') )
		else:
			self.seq_graph_graph_real_ = Seq_graph_graph_real_( root.find('Seq-graph_graph_real') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_single_data__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_single_data__, self ).__init__()
		self.name = 'SeqTable-single-data'
		#jedna z opcji dla ['SeqTable-single-data_bit', 'SeqTable-single-data_id', 'SeqTable-single-data_int', 'SeqTable-single-data_bytes', 'SeqTable-single-data_string', 'SeqTable-single-data_loc', 'SeqTable-single-data_real', 'SeqTable-single-data_interval']
		if 'SeqTable-single-data_bit' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_bit__ = SeqTable_single_data_bit__( root.find('SeqTable-single-data_bit') )
		elif 'SeqTable-single-data_id' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_id__ = SeqTable_single_data_id__( root.find('SeqTable-single-data_id') )
		elif 'SeqTable-single-data_int' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_int__ = SeqTable_single_data_int__( root.find('SeqTable-single-data_int') )
		elif 'SeqTable-single-data_bytes' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_bytes__ = SeqTable_single_data_bytes__( root.find('SeqTable-single-data_bytes') )
		elif 'SeqTable-single-data_string' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_string__ = SeqTable_single_data_string__( root.find('SeqTable-single-data_string') )
		elif 'SeqTable-single-data_loc' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_loc__ = SeqTable_single_data_loc__( root.find('SeqTable-single-data_loc') )
		elif 'SeqTable-single-data_real' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_single_data_real__ = SeqTable_single_data_real__( root.find('SeqTable-single-data_real') )
		else:
			self.seqtable_single_data_interval__ = SeqTable_single_data_interval__( root.find('SeqTable-single-data_interval') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Feat_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Feat_id_, self ).__init__()
		self.name = 'Feat-id'
		#jedna z opcji dla ['Feat-id_general', 'Feat-id_local', 'Feat-id_gibb', 'Feat-id_giim']
		if 'Feat-id_general' in [ x.tag for x in root.getchildren() ]:
			self.feat_id_general_ = Feat_id_general_( root.find('Feat-id_general') )
		elif 'Feat-id_local' in [ x.tag for x in root.getchildren() ]:
			self.feat_id_local_ = Feat_id_local_( root.find('Feat-id_local') )
		elif 'Feat-id_gibb' in [ x.tag for x in root.getchildren() ]:
			self.feat_id_gibb_ = Feat_id_gibb_( root.find('Feat-id_gibb') )
		else:
			self.feat_id_giim_ = Feat_id_giim_( root.find('Feat-id_giim') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_seq_seq_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Clone_seq_seq_, self ).__init__()
		self.name = 'Clone-seq_seq'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_sub_medium_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_sub_medium_, self ).__init__()
		self.name = 'Cit-sub_medium'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['paper', 'tape', 'floppy', 'email', 'other']
		self.value = root.get('value')


class Cit_pat_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_title_, self ).__init__()
		self.name = 'Cit-pat_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class Name_std_last_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_last_, self ).__init__()
		self.name = 'Name-std_last'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_graph_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	def __init__( self, root ):
		super( Seq_graph_loc_, self ).__init__()
		self.name = 'Seq-graph_loc'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_mesh_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_mesh_qual_, self ).__init__()
		self.name = 'Medline-mesh_qual'
		if root.find('Medline-qual') is not None:
			self.medline_qual_ = [ Medline_qual_(element) for element in root.findall('Medline-qual') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_serial_number__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_serial_number__, self ).__init__()
		self.name = 'Cit-gen_serial-number'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pubdesc_fig( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_fig, self ).__init__()
		self.name = 'Pubdesc_fig'
		self.text = root.text
	
	def __call__( self ):
		pass


class SubSource_attrib( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SubSource_attrib, self ).__init__()
		self.name = 'SubSource_attrib'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_art_from_journal_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_art_from_journal_, self ).__init__()
		self.name = 'Cit-art_from_journal'
		self.cit_jour_ = Cit_jour_( root.find('Cit-jour') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Date( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date, self ).__init__()
		self.name = 'Date'
		#jedna z opcji dla ['Date_std', 'Date_str']
		if 'Date_std' in [ x.tag for x in root.getchildren() ]:
			self.date_std = Date_std( root.find('Date_std') )
		else:
			self.date_str = Date_str( root.find('Date_str') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_muid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pub_muid, self ).__init__()
		self.name = 'Pub_muid'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_pat_priority_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_priority_, self ).__init__()
		self.name = 'Cit-pat_priority'
		if root.find('Patent-priority') is not None:
			self.patent_priority_ = [ Patent_priority_(element) for element in root.findall('Patent-priority') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_proc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_proc_, self ).__init__()
		self.name = 'Cit-proc'
		self.cit_proc_meet_ = Cit_proc_meet_( root.find('Cit-proc_meet') )
		self.cit_proc_book_ = Cit_proc_book_( root.find('Cit-proc_book') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_empty_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_empty_, self ).__init__()
		self.name = 'Seq-loc_empty'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_syn_E( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_syn_E, self ).__init__()
		self.name = 'Txinit_syn_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_point_fuzz_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_point_fuzz_, self ).__init__()
		self.name = 'Seq-point_fuzz'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ExperimentSupport_dois( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ExperimentSupport_dois, self ).__init__()
		self.name = 'ExperimentSupport_dois'
		if root.find('DOI') is not None:
			self.doi = [ DOI(element) for element in root.findall('DOI') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_multi_data_id__, self ).__init__()
		self.name = 'SeqTable-multi-data_id'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatSupport_model_evidence_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatSupport_model_evidence_, self ).__init__()
		self.name = 'SeqFeatSupport_model-evidence'
		if root.find('ModelEvidenceSupport') is not None:
			self.modelevidencesupport = [ ModelEvidenceSupport(element) for element in root.findall('ModelEvidenceSupport') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_inst_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_inst_, self ).__init__()
		self.name = 'Variation-inst'
		self.variation_inst_type_ = Variation_inst_type_( root.find('Variation-inst_type') )
		if root.find('Variation-inst_observation') is not None:
			self.variation_inst_observation_ = Variation_inst_observation_( root.find('Variation-inst_observation') )
		else:
			pass
		self.variation_inst_delta_ = Variation_inst_delta_( root.find('Variation-inst_delta') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class RNA_ref_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_ref_type_, self ).__init__()
		self.name = 'RNA-ref_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'premsg', 'mRNA', 'tRNA', 'rRNA', 'snRNA', 'scRNA', 'snoRNA', 'ncRNA', 'tmRNA', 'miscRNA', 'other']
		self.value = root.get('value')


class GB_block_origin_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_origin_, self ).__init__()
		self.name = 'GB-block_origin'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_gap_linkage_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_gap_linkage_, self ).__init__()
		self.name = 'Seq-gap_linkage'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unlinked', 'linked', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Packed_seqpnt_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Packed_seqpnt_id_, self ).__init__()
		self.name = 'Packed-seqpnt_id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonBytes_table_bytes_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonBytes_table_bytes_E_, self ).__init__()
		self.name = 'CommonBytes-table_bytes_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class EvidenceCategory( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EvidenceCategory, self ).__init__()
		self.name = 'EvidenceCategory'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['not-set', 'coordinates', 'description', 'existence']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Trna_ext_codon_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_codon_E_, self ).__init__()
		self.name = 'Trna-ext_codon_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_single_data_loc__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_single_data_loc__, self ).__init__()
		self.name = 'SeqTable-single-data_loc'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_block_extra_acc__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_extra_acc__, self ).__init__()
		self.name = 'EMBL-block_extra-acc'
		if root.find('EMBL-block_extra-acc_E') is not None:
			self.embl_block_extra_acc_e__ = [ EMBL_block_extra_acc_E__(element) for element in root.findall('EMBL-block_extra-acc_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_set_level_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Bioseq_set_level_, self ).__init__()
		self.name = 'Bioseq-set_level'
		self.text = root.text
	
	def __call__( self ):
		pass


class Std_seg_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Std_seg_loc_, self ).__init__()
		self.name = 'Std-seg_loc'
		if root.find('Seq-loc') is not None:
			self.seq_loc_ = [ Seq_loc_(element) for element in root.findall('Seq-loc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_align_type_, self ).__init__()
		self.name = 'Seq-align_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'global', 'diags', 'partial', 'disc', 'other']
		self.value = root.get('value')


class Medline_rn_cit_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_rn_cit_, self ).__init__()
		self.name = 'Medline-rn_cit'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annot_id_general_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annot_id_general_, self ).__init__()
		self.name = 'Annot-id_general'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceItem_id( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceItem_id, self ).__init__()
		self.name = 'ModelEvidenceItem_id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_product_strand__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_product_strand__, self ).__init__()
		self.name = 'Spliced-seg_product-strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class InferenceSupport_pmids( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( InferenceSupport_pmids, self ).__init__()
		self.name = 'InferenceSupport_pmids'
		if root.find('PubMedId') is not None:
			self.pubmedid = [ PubMedId(element) for element in root.findall('PubMedId') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_created_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_created_, self ).__init__()
		self.name = 'SP-block_created'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_pub_type_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_pub_type_E__, self ).__init__()
		self.name = 'Medline-entry_pub-type_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Auth_list_names_str_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_names_str_E_, self ).__init__()
		self.name = 'Auth-list_names_str_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class CitRetract_type( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CitRetract_type, self ).__init__()
		self.name = 'CitRetract_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['retracted', 'notice', 'in-error', 'erratum']
		self.value = root.get('value')


class Seq_align_score_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_align_score_, self ).__init__()
		self.name = 'Seq-align_score'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_mgcode( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_mgcode, self ).__init__()
		self.name = 'OrgName_mgcode'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_data_set_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_data_set_name_, self ).__init__()
		self.name = 'Variation-ref_data_set_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_align_segs_disc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_disc_, self ).__init__()
		self.name = 'Seq-align_segs_disc'
		self.seq_align_set__ = Seq_align_set__( root.find('Seq-align-set') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_seq_data__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_seq_data__, self ).__init__()
		self.name = 'Seq-inst_seq-data'
		self.seq_data_ = Seq_data_( root.find('Seq-data') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class InferenceSupport_type( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( InferenceSupport_type, self ).__init__()
		self.name = 'InferenceSupport_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['not-set', 'similar-to-sequence', 'similar-to-aa', 'similar-to-dna', 'similar-to-rna', 'similar-to-mrna', 'similiar-to-est', 'similar-to-other-rna', 'profile', 'nucleotide-motif', 'protein-motif', 'ab-initio-prediction', 'alignment', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Medline_field_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_field_type_, self ).__init__()
		self.name = 'Medline-field_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['other', 'comment', 'erratum']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class SeqTable_column_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_column_data_, self ).__init__()
		self.name = 'SeqTable-column_data'
		self.seqtable_multi_data__ = SeqTable_multi_data__( root.find('SeqTable-multi-data') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_column_info_title__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_column_info_title__, self ).__init__()
		self.name = 'SeqTable-column-info_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imprint_pubstatus( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_pubstatus, self ).__init__()
		self.name = 'Imprint_pubstatus'
		self.pubstatus = PubStatus( root.find('PubStatus') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CitRetract_exp( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CitRetract_exp, self ).__init__()
		self.name = 'CitRetract_exp'
		self.text = root.text
	
	def __call__( self ):
		pass


class PCRPrimerName( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRPrimerName, self ).__init__()
		self.name = 'PCRPrimerName'
		self.text = root.text
	
	def __call__( self ):
		pass


class PRF_ExtraSrc_host_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_ExtraSrc_host_, self ).__init__()
		self.name = 'PRF-ExtraSrc_host'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_align_first_starts__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_first_starts__, self ).__init__()
		self.name = 'Sparse-align_first-starts'
		if root.find('Sparse-align_first-starts_E') is not None:
			self.sparse_align_first_starts_e__ = [ Sparse_align_first_starts_E__(element) for element in root.findall('Sparse-align_first-starts_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	def __init__( self, root ):
		super( OrgName_name, self ).__init__()
		self.name = 'OrgName_name'
		#jedna z opcji dla ['OrgName_name_partial', 'OrgName_name_virus', 'OrgName_name_binomial', 'OrgName_name_namedhybrid', 'OrgName_name_hybrid']
		if 'OrgName_name_partial' in [ x.tag for x in root.getchildren() ]:
			self.orgname_name_partial = OrgName_name_partial( root.find('OrgName_name_partial') )
		elif 'OrgName_name_virus' in [ x.tag for x in root.getchildren() ]:
			self.orgname_name_virus = OrgName_name_virus( root.find('OrgName_name_virus') )
		elif 'OrgName_name_binomial' in [ x.tag for x in root.getchildren() ]:
			self.orgname_name_binomial = OrgName_name_binomial( root.find('OrgName_name_binomial') )
		elif 'OrgName_name_namedhybrid' in [ x.tag for x in root.getchildren() ]:
			self.orgname_name_namedhybrid = OrgName_name_namedhybrid( root.find('OrgName_name_namedhybrid') )
		else:
			self.orgname_name_hybrid = OrgName_name_hybrid( root.find('OrgName_name_hybrid') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	def __init__( self, root ):
		super( Medline_entry_, self ).__init__()
		self.name = 'Medline-entry'
		if root.find('Medline-entry_status') is not None:
			self.medline_entry_status_ = Medline_entry_status_( root.find('Medline-entry_status') )
		else:
			pass
		self.medline_entry_em_ = Medline_entry_em_( root.find('Medline-entry_em') )
		if root.find('Medline-entry_xref') is not None:
			self.medline_entry_xref_ = Medline_entry_xref_( root.find('Medline-entry_xref') )
		else:
			pass
		if root.find('Medline-entry_substance') is not None:
			self.medline_entry_substance_ = Medline_entry_substance_( root.find('Medline-entry_substance') )
		else:
			pass
		if root.find('Medline-entry_pmid') is not None:
			self.medline_entry_pmid_ = Medline_entry_pmid_( root.find('Medline-entry_pmid') )
		else:
			pass
		if root.find('Medline-entry_pub-type') is not None:
			self.medline_entry_pub_type__ = Medline_entry_pub_type__( root.find('Medline-entry_pub-type') )
		else:
			pass
		if root.find('Medline-entry_abstract') is not None:
			self.medline_entry_abstract_ = Medline_entry_abstract_( root.find('Medline-entry_abstract') )
		else:
			pass
		self.medline_entry_cit_ = Medline_entry_cit_( root.find('Medline-entry_cit') )
		if root.find('Medline-entry_idnum') is not None:
			self.medline_entry_idnum_ = Medline_entry_idnum_( root.find('Medline-entry_idnum') )
		else:
			pass
		if root.find('Medline-entry_uid') is not None:
			self.medline_entry_uid_ = Medline_entry_uid_( root.find('Medline-entry_uid') )
		else:
			pass
		if root.find('Medline-entry_mlfield') is not None:
			self.medline_entry_mlfield_ = Medline_entry_mlfield_( root.find('Medline-entry_mlfield') )
		else:
			pass
		if root.find('Medline-entry_mesh') is not None:
			self.medline_entry_mesh_ = Medline_entry_mesh_( root.find('Medline-entry_mesh') )
		else:
			pass
		if root.find('Medline-entry_gene') is not None:
			self.medline_entry_gene_ = Medline_entry_gene_( root.find('Medline-entry_gene') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_user( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_user, self ).__init__()
		self.name = 'SeqFeatData_user'
		self.user_object_ = User_object_( root.find('User-object') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_diag_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Dense_diag_, self ).__init__()
		self.name = 'Dense-diag'
		self.dense_diag_starts_ = Dense_diag_starts_( root.find('Dense-diag_starts') )
		if root.find('Dense-diag_strands') is not None:
			self.dense_diag_strands_ = Dense_diag_strands_( root.find('Dense-diag_strands') )
		else:
			pass
		if root.find('Dense-diag_scores') is not None:
			self.dense_diag_scores_ = Dense_diag_scores_( root.find('Dense-diag_scores') )
		else:
			pass
		if root.find('Dense-diag_dim') is not None:
			self.dense_diag_dim_ = Dense_diag_dim_( root.find('Dense-diag_dim') )
		else:
			pass
		self.dense_diag_ids_ = Dense_diag_ids_( root.find('Dense-diag_ids') )
		self.dense_diag_len_ = Dense_diag_len_( root.find('Dense-diag_len') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Score_value_int( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Score_value_int, self ).__init__()
		self.name = 'Score_value_int'
		self.text = root.text
	
	def __call__( self ):
		pass


class Clone_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Clone_ref_, self ).__init__()
		self.name = 'Clone-ref'
		if root.find('Clone-ref_unique') is not None:
			self.clone_ref_unique_ = Clone_ref_unique_( root.find('Clone-ref_unique') )
		else:
			pass
		if root.find('Clone-ref_placement-method') is not None:
			self.clone_ref_placement_method__ = Clone_ref_placement_method__( root.find('Clone-ref_placement-method') )
		else:
			pass
		if root.find('Clone-ref_concordant') is not None:
			self.clone_ref_concordant_ = Clone_ref_concordant_( root.find('Clone-ref_concordant') )
		else:
			pass
		if root.find('Clone-ref_library') is not None:
			self.clone_ref_library_ = Clone_ref_library_( root.find('Clone-ref_library') )
		else:
			pass
		if root.find('Clone-ref_clone-seq') is not None:
			self.clone_ref_clone_seq__ = Clone_ref_clone_seq__( root.find('Clone-ref_clone-seq') )
		else:
			pass
		self.clone_ref_name_ = Clone_ref_name_( root.find('Clone-ref_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_language( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_language, self ).__init__()
		self.name = 'Imprint_language'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_gi_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_gi_, self ).__init__()
		self.name = 'Seq-id_gi'
		self.text = root.text
	
	def __call__( self ):
		pass


class Auth_list_names_ml_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_names_ml_E_, self ).__init__()
		self.name = 'Auth-list_names_ml_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pubdesc_maploc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_maploc, self ).__init__()
		self.name = 'Pubdesc_maploc'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cdregion_code( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_code, self ).__init__()
		self.name = 'Cdregion_code'
		self.genetic_code_ = Genetic_code_( root.find('Genetic-code') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Dense_seg_, self ).__init__()
		self.name = 'Dense-seg'
		if root.find('Dense-seg_scores') is not None:
			self.dense_seg_scores_ = Dense_seg_scores_( root.find('Dense-seg_scores') )
		else:
			pass
		self.dense_seg_ids_ = Dense_seg_ids_( root.find('Dense-seg_ids') )
		self.dense_seg_numseg_ = Dense_seg_numseg_( root.find('Dense-seg_numseg') )
		self.dense_seg_lens_ = Dense_seg_lens_( root.find('Dense-seg_lens') )
		if root.find('Dense-seg_strands') is not None:
			self.dense_seg_strands_ = Dense_seg_strands_( root.find('Dense-seg_strands') )
		else:
			pass
		if root.find('Dense-seg_dim') is not None:
			self.dense_seg_dim_ = Dense_seg_dim_( root.find('Dense-seg_dim') )
		else:
			pass
		self.dense_seg_starts_ = Dense_seg_starts_( root.find('Dense-seg_starts') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonString_table_indexes_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonString_table_indexes_E_, self ).__init__()
		self.name = 'CommonString-table_indexes_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceSupport_method( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceSupport_method, self ).__init__()
		self.name = 'ModelEvidenceSupport_method'
		self.text = root.text
	
	def __call__( self ):
		pass


class Map_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Map_ext_, self ).__init__()
		self.name = 'Map-ext'
		if root.find('Seq-feat') is not None:
			self.seq_feat_ = [ Seq_feat_(element) for element in root.findall('Seq-feat') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Org_ref_syn_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_syn_E_, self ).__init__()
		self.name = 'Org-ref_syn_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Meeting_place( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Meeting_place, self ).__init__()
		self.name = 'Meeting_place'
		self.affil = Affil( root.find('Affil') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_product_end__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_product_end__, self ).__init__()
		self.name = 'Spliced-exon_product-end'
		self.product_pos_ = Product_pos_( root.find('Product-pos') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Byte_graph_axis_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Byte_graph_axis_, self ).__init__()
		self.name = 'Byte-graph_axis'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annotdesc_user( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annotdesc_user, self ).__init__()
		self.name = 'Annotdesc_user'
		self.user_object_ = User_object_( root.find('User-object') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class MolInfo( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MolInfo, self ).__init__()
		self.name = 'MolInfo'
		if root.find('MolInfo_tech') is not None:
			self.molinfo_tech = MolInfo_tech( root.find('MolInfo_tech') )
		else:
			pass
		if root.find('MolInfo_completeness') is not None:
			self.molinfo_completeness = MolInfo_completeness( root.find('MolInfo_completeness') )
		else:
			pass
		if root.find('MolInfo_biomol') is not None:
			self.molinfo_biomol = MolInfo_biomol( root.find('MolInfo_biomol') )
		else:
			pass
		if root.find('MolInfo_gbmoltype') is not None:
			self.molinfo_gbmoltype = MolInfo_gbmoltype( root.find('MolInfo_gbmoltype') )
		else:
			pass
		if root.find('MolInfo_techexp') is not None:
			self.molinfo_techexp = MolInfo_techexp( root.find('MolInfo_techexp') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_rec_ids__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_hist_rec_ids__, self ).__init__()
		self.name = 'Seq-hist-rec_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_journal_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_journal_, self ).__init__()
		self.name = 'Pub-set_journal'
		if root.find('Cit-jour') is not None:
			self.cit_jour_ = [ Cit_jour_(element) for element in root.findall('Cit-jour') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_single_data_bytes__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_single_data_bytes__, self ).__init__()
		self.name = 'SeqTable-single-data_bytes'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_gap_linkage_evidence__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_gap_linkage_evidence__, self ).__init__()
		self.name = 'Seq-gap_linkage-evidence'
		if root.find('Linkage-evidence') is not None:
			self.linkage_evidence_ = [ Linkage_evidence_(element) for element in root.findall('Linkage-evidence') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Real_graph_values_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Real_graph_values_, self ).__init__()
		self.name = 'Real-graph_values'
		if root.find('Real-graph_values_E') is not None:
			self.real_graph_values_e_ = [ Real_graph_values_E_(element) for element in root.findall('Real-graph_values_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_num( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_num, self ).__init__()
		self.name = 'SeqFeatData_num'
		self.numbering = Numbering( root.find('Numbering') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_seg_ext__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_seg_ext__, self ).__init__()
		self.name = 'Sparse-seg-ext'
		self.sparse_seg_ext_index__ = Sparse_seg_ext_index__( root.find('Sparse-seg-ext_index') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_allele_origin__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_allele_origin__, self ).__init__()
		self.name = 'Variation-ref_allele-origin'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'germline', 'somatic', 'inherited', 'paternal', 'maternal', 'de-novo', 'biparental', 'uniparental', 'not-tested', 'tested-inconclusive', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Num_real_b_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_real_b_, self ).__init__()
		self.name = 'Num-real_b'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_local_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_local_, self ).__init__()
		self.name = 'Seq-id_local'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId_other( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_other, self ).__init__()
		self.name = 'ArticleId_other'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Feat_id_local_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Feat_id_local_, self ).__init__()
		self.name = 'Feat-id_local'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GB_block_extra_accessions__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_extra_accessions__, self ).__init__()
		self.name = 'GB-block_extra-accessions'
		if root.find('GB-block_extra-accessions_E') is not None:
			self.gb_block_extra_accessions_e__ = [ GB_block_extra_accessions_E__(element) for element in root.findall('GB-block_extra-accessions_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_genbank_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_genbank_, self ).__init__()
		self.name = 'Seq-id_genbank'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_title_x__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_title_x__, self ).__init__()
		self.name = 'Seq-graph_title-x'
		self.text = root.text
	
	def __call__( self ):
		pass


class GB_block_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_, self ).__init__()
		self.name = 'GB-block'
		if root.find('GB-block_taxonomy') is not None:
			self.gb_block_taxonomy_ = GB_block_taxonomy_( root.find('GB-block_taxonomy') )
		else:
			pass
		if root.find('GB-block_div') is not None:
			self.gb_block_div_ = GB_block_div_( root.find('GB-block_div') )
		else:
			pass
		if root.find('GB-block_extra-accessions') is not None:
			self.gb_block_extra_accessions__ = GB_block_extra_accessions__( root.find('GB-block_extra-accessions') )
		else:
			pass
		if root.find('GB-block_date') is not None:
			self.gb_block_date_ = GB_block_date_( root.find('GB-block_date') )
		else:
			pass
		if root.find('GB-block_keywords') is not None:
			self.gb_block_keywords_ = GB_block_keywords_( root.find('GB-block_keywords') )
		else:
			pass
		if root.find('GB-block_entry-date') is not None:
			self.gb_block_entry_date__ = GB_block_entry_date__( root.find('GB-block_entry-date') )
		else:
			pass
		if root.find('GB-block_origin') is not None:
			self.gb_block_origin_ = GB_block_origin_( root.find('GB-block_origin') )
		else:
			pass
		if root.find('GB-block_source') is not None:
			self.gb_block_source_ = GB_block_source_( root.find('GB-block_source') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_extra_acc_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_extra_acc_E__, self ).__init__()
		self.name = 'SP-block_extra-acc_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Org_ref_taxname_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_taxname_, self ).__init__()
		self.name = 'Org-ref_taxname'
		self.text = root.text
	
	def __call__( self ):
		pass


class TaxElement_fixed_level_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( TaxElement_fixed_level_, self ).__init__()
		self.name = 'TaxElement_fixed-level'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['other', 'family', 'order', 'class']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Cit_pat_applicants_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_pat_applicants_, self ).__init__()
		self.name = 'Cit-pat_applicants'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BioSource_pcr_primers_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	def __init__( self, root ):
		super( BioSource_pcr_primers_, self ).__init__()
		self.name = 'BioSource_pcr-primers'
		self.pcrreactionset = PCRReactionSet( root.find('PCRReactionSet') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_seg_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_seg_ext_, self ).__init__()
		self.name = 'Sparse-seg_ext'
		if root.find('Sparse-seg-ext') is not None:
			self.sparse_seg_ext__ = [ Sparse_seg_ext__(element) for element in root.findall('Sparse-seg-ext') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_pub_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_pub_, self ).__init__()
		self.name = 'Variation-ref_pub'
		self.pub = Pub( root.find('Pub') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_seq_id_rel__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_seq_id_rel__, self ).__init__()
		self.name = 'PDB-seq-id_rel'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_ncbistdaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbistdaa_, self ).__init__()
		self.name = 'Seq-data_ncbistdaa'
		self.ncbistdaa = NCBIstdaa( root.find('NCBIstdaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_, self ).__init__()
		self.name = 'Seq-annot_data'
		#jedna z opcji dla ['Seq-annot_data_ids', 'Seq-annot_data_seq-table', 'Seq-annot_data_align', 'Seq-annot_data_locs', 'Seq-annot_data_ftable', 'Seq-annot_data_graph']
		if 'Seq-annot_data_ids' in [ x.tag for x in root.getchildren() ]:
			self.seq_annot_data_ids_ = Seq_annot_data_ids_( root.find('Seq-annot_data_ids') )
		elif 'Seq-annot_data_seq-table' in [ x.tag for x in root.getchildren() ]:
			self.seq_annot_data_seq_table__ = Seq_annot_data_seq_table__( root.find('Seq-annot_data_seq-table') )
		elif 'Seq-annot_data_align' in [ x.tag for x in root.getchildren() ]:
			self.seq_annot_data_align_ = Seq_annot_data_align_( root.find('Seq-annot_data_align') )
		elif 'Seq-annot_data_locs' in [ x.tag for x in root.getchildren() ]:
			self.seq_annot_data_locs_ = Seq_annot_data_locs_( root.find('Seq-annot_data_locs') )
		elif 'Seq-annot_data_ftable' in [ x.tag for x in root.getchildren() ]:
			self.seq_annot_data_ftable_ = Seq_annot_data_ftable_( root.find('Seq-annot_data_ftable') )
		else:
			self.seq_annot_data_graph_ = Seq_annot_data_graph_( root.find('Seq-annot_data_graph') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Population_data_genotype_frequency__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_genotype_frequency__, self ).__init__()
		self.name = 'Population-data_genotype-frequency'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annot_id_other_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annot_id_other_, self ).__init__()
		self.name = 'Annot-id_other'
		self.textannot_id_ = Textannot_id_( root.find('Textannot-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_name_virus( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_name_virus, self ).__init__()
		self.name = 'OrgName_name_virus'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_seg_ext_index__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_seg_ext_index__, self ).__init__()
		self.name = 'Sparse-seg-ext_index'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_multi_data_real_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_real_E__, self ).__init__()
		self.name = 'SeqTable-multi-data_real_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_multi_data_loc__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_multi_data_loc__, self ).__init__()
		self.name = 'SeqTable-multi-data_loc'
		if root.find('Seq-loc') is not None:
			self.seq_loc_ = [ Seq_loc_(element) for element in root.findall('Seq-loc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_gap_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_gap_, self ).__init__()
		self.name = 'Seq-gap'
		self.seq_gap_type_ = Seq_gap_type_( root.find('Seq-gap_type') )
		if root.find('Seq-gap_linkage') is not None:
			self.seq_gap_linkage_ = Seq_gap_linkage_( root.find('Seq-gap_linkage') )
		else:
			pass
		if root.find('Seq-gap_linkage-evidence') is not None:
			self.seq_gap_linkage_evidence__ = Seq_gap_linkage_evidence__( root.find('Seq-gap_linkage-evidence') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_block_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	def __init__( self, root ):
		super( PDB_block_, self ).__init__()
		self.name = 'PDB-block'
		self.pdb_block_class_ = PDB_block_class_( root.find('PDB-block_class') )
		if root.find('PDB-block_replace') is not None:
			self.pdb_block_replace_ = PDB_block_replace_( root.find('PDB-block_replace') )
		else:
			pass
		if root.find('PDB-block_exp-method') is not None:
			self.pdb_block_exp_method__ = PDB_block_exp_method__( root.find('PDB-block_exp-method') )
		else:
			pass
		self.pdb_block_source_ = PDB_block_source_( root.find('PDB-block_source') )
		self.pdb_block_compound_ = PDB_block_compound_( root.find('PDB-block_compound') )
		self.pdb_block_deposition_ = PDB_block_deposition_( root.find('PDB-block_deposition') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_interval__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_multi_data_interval__, self ).__init__()
		self.name = 'SeqTable-multi-data_interval'
		if root.find('Seq-interval') is not None:
			self.seq_interval_ = [ Seq_interval_(element) for element in root.findall('Seq-interval') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_psec_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_psec_str_, self ).__init__()
		self.name = 'SeqFeatData_psec-str'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['helix', 'sheet', 'turn']
		self.value = root.get('value')


class Dense_diag_strands_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_diag_strands_, self ).__init__()
		self.name = 'Dense-diag_strands'
		if root.find('Na-strand') is not None:
			self.na_strand_ = [ Na_strand_(element) for element in root.findall('Na-strand') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Object_id_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Object_id_id_, self ).__init__()
		self.name = 'Object-id_id'
		self.text = root.text
	
	def __call__( self ):
		pass


class Genetic_code_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_, self ).__init__()
		self.name = 'Genetic-code'
		if root.find('Genetic-code_E') is not None:
			self.genetic_code_e_ = [ Genetic_code_E_(element) for element in root.findall('Genetic-code_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PRF_block_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_block_, self ).__init__()
		self.name = 'PRF-block'
		if root.find('PRF-block_extra-src') is not None:
			self.prf_block_extra_src__ = PRF_block_extra_src__( root.find('PRF-block_extra-src') )
		else:
			pass
		if root.find('PRF-block_keywords') is not None:
			self.prf_block_keywords_ = PRF_block_keywords_( root.find('PRF-block_keywords') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Trna_ext_aa_iupacaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_aa_iupacaa_, self ).__init__()
		self.name = 'Trna-ext_aa_iupacaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class DocRef_type( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( DocRef_type, self ).__init__()
		self.name = 'DocRef_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['medline', 'pubmed', 'ncbigi']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Spliced_seg_modifier_start_codon_found____( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_modifier_start_codon_found____, self ).__init__()
		self.name = 'Spliced-seg-modifier_start-codon-found'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Sparse_align_second_starts__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_second_starts__, self ).__init__()
		self.name = 'Sparse-align_second-starts'
		if root.find('Sparse-align_second-starts_E') is not None:
			self.sparse_align_second_starts_e__ = [ Sparse_align_second_starts_E__(element) for element in root.findall('Sparse-align_second-starts_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_replace_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_replace_ids_, self ).__init__()
		self.name = 'PDB-replace_ids'
		if root.find('PDB-replace_ids_E') is not None:
			self.pdb_replace_ids_e_ = [ PDB_replace_ids_E_(element) for element in root.findall('PDB-replace_ids_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_abr( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_abr, self ).__init__()
		self.name = 'Title_E_abr'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_ref_db_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_db_, self ).__init__()
		self.name = 'Gene-ref_db'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Real_graph_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Real_graph_, self ).__init__()
		self.name = 'Real-graph'
		self.real_graph_values_ = Real_graph_values_( root.find('Real-graph_values') )
		self.real_graph_axis_ = Real_graph_axis_( root.find('Real-graph_axis') )
		self.real_graph_min_ = Real_graph_min_( root.find('Real-graph_min') )
		self.real_graph_max_ = Real_graph_max_( root.find('Real-graph_max') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_modelev( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_modelev, self ).__init__()
		self.name = 'Seqdesc_modelev'
		self.modelevidencesupport = ModelEvidenceSupport( root.find('ModelEvidenceSupport') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_seqref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	def __init__( self, root ):
		super( SP_block_seqref_, self ).__init__()
		self.name = 'SP-block_seqref'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_mix_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_mix_, self ).__init__()
		self.name = 'Seq-loc_mix'
		self.seq_loc_mix__ = Seq_loc_mix__( root.find('Seq-loc-mix') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgMod_attrib( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgMod_attrib, self ).__init__()
		self.name = 'OrgMod_attrib'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_si_cit_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_si_cit_, self ).__init__()
		self.name = 'Medline-si_cit'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_data_ncbi8na_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbi8na_, self ).__init__()
		self.name = 'Seq-data_ncbi8na'
		self.ncbi8na = NCBI8na( root.find('NCBI8na') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_fuzz_alt_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_alt_E_, self ).__init__()
		self.name = 'Int-fuzz_alt_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Spliced_exon_chunk_match__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_chunk_match__, self ).__init__()
		self.name = 'Spliced-exon-chunk_match'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_rna( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_rna, self ).__init__()
		self.name = 'SeqFeatData_rna'
		self.rna_ref_ = RNA_ref_( root.find('RNA-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_sparse_index__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_sparse_index__, self ).__init__()
		self.name = 'SeqTable-sparse-index'
		#jedna z opcji dla ['SeqTable-sparse-index_bit-set', 'SeqTable-sparse-index_indexes']
		if 'SeqTable-sparse-index_bit-set' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_sparse_index_bit_set___ = SeqTable_sparse_index_bit_set___( root.find('SeqTable-sparse-index_bit-set') )
		else:
			self.seqtable_sparse_index_indexes__ = SeqTable_sparse_index_indexes__( root.find('SeqTable-sparse-index_indexes') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_set_annot_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Bioseq_set_annot_, self ).__init__()
		self.name = 'Bioseq-set_annot'
		if root.find('Seq-annot') is not None:
			self.seq_annot_ = [ Seq_annot_(element) for element in root.findall('Seq-annot') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_sequpd_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_sequpd_, self ).__init__()
		self.name = 'SP-block_sequpd'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_proc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_proc_, self ).__init__()
		self.name = 'Pub-set_proc'
		if root.find('Cit-proc') is not None:
			self.cit_proc_ = [ Cit_proc_(element) for element in root.findall('Cit-proc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gb_qual_val_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gb_qual_val_, self ).__init__()
		self.name = 'Gb-qual_val'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_field_data_strs_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_strs_E_, self ).__init__()
		self.name = 'User-field_data_strs_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Splice_site_bases_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Splice_site_bases_, self ).__init__()
		self.name = 'Splice-site_bases'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_gen_pmid_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_pmid_, self ).__init__()
		self.name = 'Cit-gen_pmid'
		self.pubmedid = PubMedId( root.find('PubMedId') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Bioseq, self ).__init__()
		self.name = 'Bioseq'
		self.bioseq_id = Bioseq_id( root.find('Bioseq_id') )
		if root.find('Bioseq_descr') is not None:
			self.bioseq_descr = Bioseq_descr( root.find('Bioseq_descr') )
		else:
			pass
		if root.find('Bioseq_annot') is not None:
			self.bioseq_annot = Bioseq_annot( root.find('Bioseq_annot') )
		else:
			pass
		self.bioseq_inst = Bioseq_inst( root.find('Bioseq_inst') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class TaxElement( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( TaxElement, self ).__init__()
		self.name = 'TaxElement'
		self.taxelement_fixed_level_ = TaxElement_fixed_level_( root.find('TaxElement_fixed-level') )
		if root.find('TaxElement_level') is not None:
			self.taxelement_level = TaxElement_level( root.find('TaxElement_level') )
		else:
			pass
		self.taxelement_name = TaxElement_name( root.find('TaxElement_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_data_align_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_align_, self ).__init__()
		self.name = 'Seq-annot_data_align'
		if root.find('Seq-align') is not None:
			self.seq_align_ = [ Seq_align_(element) for element in root.findall('Seq-align') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_pub_type__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_pub_type__, self ).__init__()
		self.name = 'Medline-entry_pub-type'
		if root.find('Medline-entry_pub-type_E') is not None:
			self.medline_entry_pub_type_e__ = [ Medline_entry_pub_type_E__(element) for element in root.findall('Medline-entry_pub-type_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class RNA_ref_ext_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_ref_ext_name_, self ).__init__()
		self.name = 'RNA-ref_ext_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_seq( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_seq, self ).__init__()
		self.name = 'SeqFeatData_seq'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Name_std_suffix_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_suffix_, self ).__init__()
		self.name = 'Name-std_suffix'
		self.text = root.text
	
	def __call__( self ):
		pass


class EMBL_block_div_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_div_, self ).__init__()
		self.name = 'EMBL-block_div'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['fun', 'inv', 'mam', 'org', 'phg', 'pln', 'pri', 'pro', 'rod', 'syn', 'una', 'vrl', 'vrt', 'pat', 'est', 'sts', 'other']
		self.value = root.get('value')


class Spliced_exon_chunk_mismatch__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_chunk_mismatch__, self ).__init__()
		self.name = 'Spliced-exon-chunk_mismatch'
		self.text = root.text
	
	def __call__( self ):
		pass


class Patent_seq_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_seq_id__, self ).__init__()
		self.name = 'Patent-seq-id'
		self.patent_seq_id_cit__ = Patent_seq_id_cit__( root.find('Patent-seq-id_cit') )
		self.patent_seq_id_seqid__ = Patent_seq_id_seqid__( root.find('Patent-seq-id_seqid') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Genetic_code_E_ncbieaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_ncbieaa_, self ).__init__()
		self.name = 'Genetic-code_E_ncbieaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_object_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_object_type_, self ).__init__()
		self.name = 'User-object_type'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_sub_authors_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_sub_authors_, self ).__init__()
		self.name = 'Cit-sub_authors'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_single_data_real__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_single_data_real__, self ).__init__()
		self.name = 'SeqTable-single-data_real'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_pat_class_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_class_E_, self ).__init__()
		self.name = 'Cit-pat_class_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Dbtag( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dbtag, self ).__init__()
		self.name = 'Dbtag'
		self.dbtag_db = Dbtag_db( root.find('Dbtag_db') )
		self.dbtag_tag = Dbtag_tag( root.find('Dbtag_tag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_strand_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_strand_, self ).__init__()
		self.name = 'Seq-inst_strand'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'ss', 'ds', 'mixed', 'other']
		self.value = root.get('value')


class Seqdesc_embl( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_embl, self ).__init__()
		self.name = 'Seqdesc_embl'
		self.embl_block_ = EMBL_block_( root.find('EMBL-block') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PRF_ExtraSrc_strain_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_ExtraSrc_strain_, self ).__init__()
		self.name = 'PRF-ExtraSrc_strain'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_field_data_strs_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_strs_, self ).__init__()
		self.name = 'User-field_data_strs'
		if root.find('User-field_data_strs_E') is not None:
			self.user_field_data_strs_e_ = [ User_field_data_strs_E_(element) for element in root.findall('User-field_data_strs_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textseq_id_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textseq_id_name_, self ).__init__()
		self.name = 'Textseq-id_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class NCBIstdaa( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBIstdaa, self ).__init__()
		self.name = 'NCBIstdaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Genetic_code_E_ncbistdaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_ncbistdaa_, self ).__init__()
		self.name = 'Genetic-code_E_ncbistdaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_bond( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_bond, self ).__init__()
		self.name = 'SeqFeatData_bond'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['disulfide', 'thiolester', 'xlink', 'thioether', 'other']
		self.value = root.get('value')


class SP_block_annotupd_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_annotupd_, self ).__init__()
		self.name = 'SP-block_annotupd'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_gap_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_gap_type_, self ).__init__()
		self.name = 'Seq-gap_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'fragment', 'clone', 'short-arm', 'heterochromatin', 'centromere', 'telomere', 'repeat', 'contig', 'scaffold', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seq_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_id_, self ).__init__()
		self.name = 'Seq-id'
		#jedna z opcji dla ['Seq-id_gpipe', 'Seq-id_local', 'Seq-id_gibbmt', 'Seq-id_ddbj', 'Seq-id_tpg', 'Seq-id_tpd', 'Seq-id_embl', 'Seq-id_named-annot-track', 'Seq-id_tpe', 'Seq-id_prf', 'Seq-id_pir', 'Seq-id_general', 'Seq-id_swissprot', 'Seq-id_giim', 'Seq-id_other', 'Seq-id_pdb', 'Seq-id_gibbsq', 'Seq-id_gi', 'Seq-id_genbank', 'Seq-id_patent']
		if 'Seq-id_gpipe' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_gpipe_ = Seq_id_gpipe_( root.find('Seq-id_gpipe') )
		elif 'Seq-id_local' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_local_ = Seq_id_local_( root.find('Seq-id_local') )
		elif 'Seq-id_gibbmt' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_gibbmt_ = Seq_id_gibbmt_( root.find('Seq-id_gibbmt') )
		elif 'Seq-id_ddbj' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_ddbj_ = Seq_id_ddbj_( root.find('Seq-id_ddbj') )
		elif 'Seq-id_tpg' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_tpg_ = Seq_id_tpg_( root.find('Seq-id_tpg') )
		elif 'Seq-id_tpd' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_tpd_ = Seq_id_tpd_( root.find('Seq-id_tpd') )
		elif 'Seq-id_embl' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_embl_ = Seq_id_embl_( root.find('Seq-id_embl') )
		elif 'Seq-id_named-annot-track' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_named_annot_track___ = Seq_id_named_annot_track___( root.find('Seq-id_named-annot-track') )
		elif 'Seq-id_tpe' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_tpe_ = Seq_id_tpe_( root.find('Seq-id_tpe') )
		elif 'Seq-id_prf' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_prf_ = Seq_id_prf_( root.find('Seq-id_prf') )
		elif 'Seq-id_pir' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_pir_ = Seq_id_pir_( root.find('Seq-id_pir') )
		elif 'Seq-id_general' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_general_ = Seq_id_general_( root.find('Seq-id_general') )
		elif 'Seq-id_swissprot' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_swissprot_ = Seq_id_swissprot_( root.find('Seq-id_swissprot') )
		elif 'Seq-id_giim' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_giim_ = Seq_id_giim_( root.find('Seq-id_giim') )
		elif 'Seq-id_other' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_other_ = Seq_id_other_( root.find('Seq-id_other') )
		elif 'Seq-id_pdb' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_pdb_ = Seq_id_pdb_( root.find('Seq-id_pdb') )
		elif 'Seq-id_gibbsq' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_gibbsq_ = Seq_id_gibbsq_( root.find('Seq-id_gibbsq') )
		elif 'Seq-id_gi' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_gi_ = Seq_id_gi_( root.find('Seq-id_gi') )
		elif 'Seq-id_genbank' in [ x.tag for x in root.getchildren() ]:
			self.seq_id_genbank_ = Seq_id_genbank_( root.find('Seq-id_genbank') )
		else:
			self.seq_id_patent_ = Seq_id_patent_( root.find('Seq-id_patent') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_block_source_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_source_, self ).__init__()
		self.name = 'PDB-block_source'
		if root.find('PDB-block_source_E') is not None:
			self.pdb_block_source_e_ = [ PDB_block_source_E_(element) for element in root.findall('PDB-block_source_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_name_, self ).__init__()
		self.name = 'Variation-ref_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_enum_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_enum_, self ).__init__()
		self.name = 'Num-enum'
		self.num_enum_num_ = Num_enum_num_( root.find('Num-enum_num') )
		self.num_enum_names_ = Num_enum_names_( root.find('Num-enum_names') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Id_pat_id_number_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Id_pat_id_number_, self ).__init__()
		self.name = 'Id-pat_id_number'
		self.text = root.text
	
	def __call__( self ):
		pass


class PIR_block_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_date_, self ).__init__()
		self.name = 'PIR-block_date'
		self.text = root.text
	
	def __call__( self ):
		pass


class EMBL_dbname_code_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_dbname_code_, self ).__init__()
		self.name = 'EMBL-dbname_code'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['embl', 'genbank', 'ddbj', 'geninfo', 'medline', 'swissprot', 'pir', 'pdb', 'epd', 'ecd', 'tfd', 'flybase', 'prosite', 'enzyme', 'mim', 'ecoseq', 'hiv', 'other']
		self.value = root.get('value')


class Num_cont_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_cont_, self ).__init__()
		self.name = 'Num-cont'
		if root.find('Num-cont_ascending') is not None:
			self.num_cont_ascending_ = Num_cont_ascending_( root.find('Num-cont_ascending') )
		else:
			pass
		if root.find('Num-cont_has-zero') is not None:
			self.num_cont_has_zero__ = Num_cont_has_zero__( root.find('Num-cont_has-zero') )
		else:
			pass
		if root.find('Num-cont_refnum') is not None:
			self.num_cont_refnum_ = Num_cont_refnum_( root.find('Num-cont_refnum') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_somatic_origin__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_somatic_origin__, self ).__init__()
		self.name = 'Variation-ref_somatic-origin'
		if root.find('Variation-ref_somatic-origin_E') is not None:
			self.variation_ref_somatic_origin_e__ = [ Variation_ref_somatic_origin_E__(element) for element in root.findall('Variation-ref_somatic-origin_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class RNA_gen_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_gen_class_, self ).__init__()
		self.name = 'RNA-gen_class'
		self.text = root.text
	
	def __call__( self ):
		pass


class Clone_seq_location_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Clone_seq_location_, self ).__init__()
		self.name = 'Clone-seq_location'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_ncbi4na_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbi4na_, self ).__init__()
		self.name = 'Seq-data_ncbi4na'
		self.ncbi4na = NCBI4na( root.find('NCBI4na') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_replace_ids_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_replace_ids_E_, self ).__init__()
		self.name = 'PDB-replace_ids_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_country( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_country, self ).__init__()
		self.name = 'Affil_std_country'
		self.text = root.text
	
	def __call__( self ):
		pass


class Spliced_seg_product_length__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_product_length__, self ).__init__()
		self.name = 'Spliced-seg_product-length'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imp_feat_key_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imp_feat_key_, self ).__init__()
		self.name = 'Imp-feat_key'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_book_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_book_, self ).__init__()
		self.name = 'Cit-book'
		self.cit_book_authors_ = Cit_book_authors_( root.find('Cit-book_authors') )
		if root.find('Cit-book_coll') is not None:
			self.cit_book_coll_ = Cit_book_coll_( root.find('Cit-book_coll') )
		else:
			pass
		self.cit_book_imp_ = Cit_book_imp_( root.find('Cit-book_imp') )
		self.cit_book_title_ = Cit_book_title_( root.find('Cit-book_title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_mol_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_mol_id__, self ).__init__()
		self.name = 'PDB-mol-id'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_idnum_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_idnum_, self ).__init__()
		self.name = 'Medline-entry_idnum'
		if root.find('Medline-entry_idnum_E') is not None:
			self.medline_entry_idnum_e_ = [ Medline_entry_idnum_E_(element) for element in root.findall('Medline-entry_idnum_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_except_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_except_, self ).__init__()
		self.name = 'Seq-feat_except'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Pub_proc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_proc, self ).__init__()
		self.name = 'Pub_proc'
		self.cit_proc_ = Cit_proc_( root.find('Cit-proc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_proc_meet_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_proc_meet_, self ).__init__()
		self.name = 'Cit-proc_meet'
		self.meeting = Meeting( root.find('Meeting') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Score_set_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Score_set_, self ).__init__()
		self.name = 'Score-set'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Giimport_id_release_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Giimport_id_release_, self ).__init__()
		self.name = 'Giimport-id_release'
		self.text = root.text
	
	def __call__( self ):
		pass


class Rsite_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Rsite'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Rsite_ref_, self ).__init__()
		self.name = 'Rsite-ref'
		#jedna z opcji dla ['Rsite-ref_db', 'Rsite-ref_str']
		if 'Rsite-ref_db' in [ x.tag for x in root.getchildren() ]:
			self.rsite_ref_db_ = Rsite_ref_db_( root.find('Rsite-ref_db') )
		else:
			self.rsite_ref_str_ = Rsite_ref_str_( root.find('Rsite-ref_str') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_is_ancestral_allele___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_is_ancestral_allele___, self ).__init__()
		self.name = 'Variation-ref_is-ancestral-allele'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Person_id_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Person_id_name_, self ).__init__()
		self.name = 'Person-id_name'
		self.name_std_ = Name_std_( root.find('Name-std') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_issn( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_issn, self ).__init__()
		self.name = 'Title_E_issn'
		self.text = root.text
	
	def __call__( self ):
		pass


class OrgName_lineage( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_lineage, self ).__init__()
		self.name = 'OrgName_lineage'
		self.text = root.text
	
	def __call__( self ):
		pass


class Dense_seg_lens_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_lens_E_, self ).__init__()
		self.name = 'Dense-seg_lens_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_interval_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_interval_, self ).__init__()
		self.name = 'Seq-interval'
		if root.find('Seq-interval_fuzz-to') is not None:
			self.seq_interval_fuzz_to__ = Seq_interval_fuzz_to__( root.find('Seq-interval_fuzz-to') )
		else:
			pass
		self.seq_interval_to_ = Seq_interval_to_( root.find('Seq-interval_to') )
		self.seq_interval_from_ = Seq_interval_from_( root.find('Seq-interval_from') )
		if root.find('Seq-interval_fuzz-from') is not None:
			self.seq_interval_fuzz_from__ = Seq_interval_fuzz_from__( root.find('Seq-interval_fuzz-from') )
		else:
			pass
		if root.find('Seq-interval_strand') is not None:
			self.seq_interval_strand_ = Seq_interval_strand_( root.find('Seq-interval_strand') )
		else:
			pass
		self.seq_interval_id_ = Seq_interval_id_( root.find('Seq-interval_id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annot_descr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annot_descr_, self ).__init__()
		self.name = 'Annot-descr'
		if root.find('Annotdesc') is not None:
			self.annotdesc = [ Annotdesc(element) for element in root.findall('Annotdesc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annot_id_ncbi_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annot_id_ncbi_, self ).__init__()
		self.name = 'Annot-id_ncbi'
		self.text = root.text
	
	def __call__( self ):
		pass


class ExperimentSupport( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ExperimentSupport, self ).__init__()
		self.name = 'ExperimentSupport'
		self.experimentsupport_explanation = ExperimentSupport_explanation( root.find('ExperimentSupport_explanation') )
		if root.find('ExperimentSupport_dois') is not None:
			self.experimentsupport_dois = ExperimentSupport_dois( root.find('ExperimentSupport_dois') )
		else:
			pass
		if root.find('ExperimentSupport_pmids') is not None:
			self.experimentsupport_pmids = ExperimentSupport_pmids( root.find('ExperimentSupport_pmids') )
		else:
			pass
		if root.find('ExperimentSupport_category') is not None:
			self.experimentsupport_category = ExperimentSupport_category( root.find('ExperimentSupport_category') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_mix__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_mix__, self ).__init__()
		self.name = 'Seq-loc-mix'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.seq_loc_ = root.findall( 'Seq-loc' )
		self.to_evaluate.append( ( 'Seq-loc', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_expression( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_expression, self ).__init__()
		self.name = 'Txinit_expression'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_loc_pnt_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_pnt_, self ).__init__()
		self.name = 'Seq-loc_pnt'
		self.seq_point_ = Seq_point_( root.find('Seq-point') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_patent( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_patent, self ).__init__()
		self.name = 'Pub_patent'
		self.cit_pat_ = Cit_pat_( root.find('Cit-pat') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_name, self ).__init__()
		self.name = 'Seqdesc_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class InferenceSupport_basis( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( InferenceSupport_basis, self ).__init__()
		self.name = 'InferenceSupport_basis'
		self.evidencebasis = EvidenceBasis( root.find('EvidenceBasis') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_other_validation_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_other_validation_, self ).__init__()
		self.name = 'VariantProperties_other-validation'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Cit_sub_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_sub_, self ).__init__()
		self.name = 'Cit-sub'
		if root.find('Cit-sub_medium') is not None:
			self.cit_sub_medium_ = Cit_sub_medium_( root.find('Cit-sub_medium') )
		else:
			pass
		if root.find('Cit-sub_date') is not None:
			self.cit_sub_date_ = Cit_sub_date_( root.find('Cit-sub_date') )
		else:
			pass
		self.cit_sub_authors_ = Cit_sub_authors_( root.find('Cit-sub_authors') )
		if root.find('Cit-sub_descr') is not None:
			self.cit_sub_descr_ = Cit_sub_descr_( root.find('Cit-sub_descr') )
		else:
			pass
		if root.find('Cit-sub_imp') is not None:
			self.cit_sub_imp_ = Cit_sub_imp_( root.find('Cit-sub_imp') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PRF_ExtraSrc_state_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_ExtraSrc_state_, self ).__init__()
		self.name = 'PRF-ExtraSrc_state'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annotdesc_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annotdesc_name, self ).__init__()
		self.name = 'Annotdesc_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_interval_fuzz_to__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_interval_fuzz_to__, self ).__init__()
		self.name = 'Seq-interval_fuzz-to'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PCRReaction_forward( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRReaction_forward, self ).__init__()
		self.name = 'PCRReaction_forward'
		self.pcrprimerset = PCRPrimerSet( root.find('PCRPrimerSet') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Affil_std( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std, self ).__init__()
		self.name = 'Affil_std'
		if root.find('Affil_std_affil') is not None:
			self.affil_std_affil = Affil_std_affil( root.find('Affil_std_affil') )
		else:
			pass
		if root.find('Affil_std_phone') is not None:
			self.affil_std_phone = Affil_std_phone( root.find('Affil_std_phone') )
		else:
			pass
		if root.find('Affil_std_div') is not None:
			self.affil_std_div = Affil_std_div( root.find('Affil_std_div') )
		else:
			pass
		if root.find('Affil_std_sub') is not None:
			self.affil_std_sub = Affil_std_sub( root.find('Affil_std_sub') )
		else:
			pass
		if root.find('Affil_std_fax') is not None:
			self.affil_std_fax = Affil_std_fax( root.find('Affil_std_fax') )
		else:
			pass
		if root.find('Affil_std_email') is not None:
			self.affil_std_email = Affil_std_email( root.find('Affil_std_email') )
		else:
			pass
		if root.find('Affil_std_city') is not None:
			self.affil_std_city = Affil_std_city( root.find('Affil_std_city') )
		else:
			pass
		if root.find('Affil_std_postal-code') is not None:
			self.affil_std_postal_code_ = Affil_std_postal_code_( root.find('Affil_std_postal-code') )
		else:
			pass
		if root.find('Affil_std_country') is not None:
			self.affil_std_country = Affil_std_country( root.find('Affil_std_country') )
		else:
			pass
		if root.find('Affil_std_street') is not None:
			self.affil_std_street = Affil_std_street( root.find('Affil_std_street') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Id_pat_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Id_pat_id_, self ).__init__()
		self.name = 'Id-pat_id'
		#jedna z opcji dla ['Id-pat_id_app-number', 'Id-pat_id_number']
		if 'Id-pat_id_app-number' in [ x.tag for x in root.getchildren() ]:
			self.id_pat_id_app_number__ = Id_pat_id_app_number__( root.find('Id-pat_id_app-number') )
		else:
			self.id_pat_id_number_ = Id_pat_id_number_( root.find('Id-pat_id_number') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_oss_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_oss_, self ).__init__()
		self.name = 'User-field_data_oss'
		if root.find('User-field_data_oss_E') is not None:
			self.user_field_data_oss_e_ = [ User_field_data_oss_E_(element) for element in root.findall('User-field_data_oss_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Date_std_day_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_day_, self ).__init__()
		self.name = 'Date-std_day'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_num( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_num, self ).__init__()
		self.name = 'Seqdesc_num'
		self.numbering = Numbering( root.find('Numbering') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_sample_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_sample_id__, self ).__init__()
		self.name = 'Variation-ref_sample-id'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_embl_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_embl_, self ).__init__()
		self.name = 'Seq-id_embl'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_product_type__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_product_type__, self ).__init__()
		self.name = 'Spliced-seg_product-type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['transcript', 'protein']
		self.value = root.get('value')


class Seq_graph_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	def __init__( self, root ):
		super( Seq_graph_, self ).__init__()
		self.name = 'Seq-graph'
		self.seq_graph_graph_ = Seq_graph_graph_( root.find('Seq-graph_graph') )
		if root.find('Seq-graph_comp') is not None:
			self.seq_graph_comp_ = Seq_graph_comp_( root.find('Seq-graph_comp') )
		else:
			pass
		if root.find('Seq-graph_title') is not None:
			self.seq_graph_title_ = Seq_graph_title_( root.find('Seq-graph_title') )
		else:
			pass
		if root.find('Seq-graph_comment') is not None:
			self.seq_graph_comment_ = Seq_graph_comment_( root.find('Seq-graph_comment') )
		else:
			pass
		self.seq_graph_numval_ = Seq_graph_numval_( root.find('Seq-graph_numval') )
		if root.find('Seq-graph_title-y') is not None:
			self.seq_graph_title_y__ = Seq_graph_title_y__( root.find('Seq-graph_title-y') )
		else:
			pass
		if root.find('Seq-graph_a') is not None:
			self.seq_graph_a_ = Seq_graph_a_( root.find('Seq-graph_a') )
		else:
			pass
		self.seq_graph_loc_ = Seq_graph_loc_( root.find('Seq-graph_loc') )
		if root.find('Seq-graph_b') is not None:
			self.seq_graph_b_ = Seq_graph_b_( root.find('Seq-graph_b') )
		else:
			pass
		if root.find('Seq-graph_title-x') is not None:
			self.seq_graph_title_x__ = Seq_graph_title_x__( root.find('Seq-graph_title-x') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_genotype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_genotype, self ).__init__()
		self.name = 'VariantProperties_genotype'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['in-haplotype-set', 'has-genotypes']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class RNA_ref_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	def __init__( self, root ):
		super( RNA_ref_ext_, self ).__init__()
		self.name = 'RNA-ref_ext'
		#jedna z opcji dla ['RNA-ref_ext_gen', 'RNA-ref_ext_tRNA', 'RNA-ref_ext_name']
		if 'RNA-ref_ext_gen' in [ x.tag for x in root.getchildren() ]:
			self.rna_ref_ext_gen_ = RNA_ref_ext_gen_( root.find('RNA-ref_ext_gen') )
		elif 'RNA-ref_ext_tRNA' in [ x.tag for x in root.getchildren() ]:
			self.rna_ref_ext_trna_ = RNA_ref_ext_tRNA_( root.find('RNA-ref_ext_tRNA') )
		else:
			self.rna_ref_ext_name_ = RNA_ref_ext_name_( root.find('RNA-ref_ext_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class NCBIeaa( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBIeaa, self ).__init__()
		self.name = 'NCBIeaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_field_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_field_ids_, self ).__init__()
		self.name = 'Medline-field_ids'
		if root.find('DocRef') is not None:
			self.docref = [ DocRef(element) for element in root.findall('DocRef') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Object_id_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Object_id_str_, self ).__init__()
		self.name = 'Object-id_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_annot_data_locs_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_locs_, self ).__init__()
		self.name = 'Seq-annot_data_locs'
		if root.find('Seq-loc') is not None:
			self.seq_loc_ = [ Seq_loc_(element) for element in root.findall('Seq-loc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_set_coll_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Bioseq_set_coll_, self ).__init__()
		self.name = 'Bioseq-set_coll'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_volume_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_volume_, self ).__init__()
		self.name = 'Cit-gen_volume'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_consequence_E_frameshift_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_frameshift_, self ).__init__()
		self.name = 'Variation-ref_consequence_E_frameshift'
		if root.find('Variation-ref_consequence_E_frameshift_phase') is not None:
			self.variation_ref_consequence_e_frameshift_phase_ = Variation_ref_consequence_E_frameshift_phase_( root.find('Variation-ref_consequence_E_frameshift_phase') )
		else:
			pass
		if root.find('Variation-ref_consequence_E_frameshift_x-length') is not None:
			self.variation_ref_consequence_e_frameshift_x_length__ = Variation_ref_consequence_E_frameshift_x_length__( root.find('Variation-ref_consequence_E_frameshift_x-length') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_location_accurate_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_location_accurate_, self ).__init__()
		self.name = 'Txinit_location-accurate'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Population_data_sample_ids__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_sample_ids__, self ).__init__()
		self.name = 'Population-data_sample-ids'
		if root.find('Object-id') is not None:
			self.object_id_ = [ Object_id_(element) for element in root.findall('Object-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_pub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_pub, self ).__init__()
		self.name = 'SeqFeatData_pub'
		self.pubdesc = Pubdesc( root.find('Pubdesc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_location_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_location_, self ).__init__()
		self.name = 'Seq-feat_location'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_topology_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_topology_, self ).__init__()
		self.name = 'Seq-inst_topology'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'linear', 'circular', 'tandem', 'other']
		self.value = root.get('value')


class Cit_art_from_book_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_art_from_book_, self ).__init__()
		self.name = 'Cit-art_from_book'
		self.cit_book_ = Cit_book_( root.find('Cit-book') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class MedlineUID( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MedlineUID, self ).__init__()
		self.name = 'MedlineUID'
		self.text = root.text
	
	def __call__( self ):
		pass


class Person_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Person_id_, self ).__init__()
		self.name = 'Person-id'
		#jedna z opcji dla ['Person-id_ml', 'Person-id_dbtag', 'Person-id_consortium', 'Person-id_str', 'Person-id_name']
		if 'Person-id_ml' in [ x.tag for x in root.getchildren() ]:
			self.person_id_ml_ = Person_id_ml_( root.find('Person-id_ml') )
		elif 'Person-id_dbtag' in [ x.tag for x in root.getchildren() ]:
			self.person_id_dbtag_ = Person_id_dbtag_( root.find('Person-id_dbtag') )
		elif 'Person-id_consortium' in [ x.tag for x in root.getchildren() ]:
			self.person_id_consortium_ = Person_id_consortium_( root.find('Person-id_consortium') )
		elif 'Person-id_str' in [ x.tag for x in root.getchildren() ]:
			self.person_id_str_ = Person_id_str_( root.find('Person-id_str') )
		else:
			self.person_id_name_ = Person_id_name_( root.find('Person-id_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Org_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	def __init__( self, root ):
		super( Org_ref_, self ).__init__()
		self.name = 'Org-ref'
		if root.find('Org-ref_syn') is not None:
			self.org_ref_syn_ = Org_ref_syn_( root.find('Org-ref_syn') )
		else:
			pass
		if root.find('Org-ref_mod') is not None:
			self.org_ref_mod_ = Org_ref_mod_( root.find('Org-ref_mod') )
		else:
			pass
		if root.find('Org-ref_taxname') is not None:
			self.org_ref_taxname_ = Org_ref_taxname_( root.find('Org-ref_taxname') )
		else:
			pass
		if root.find('Org-ref_common') is not None:
			self.org_ref_common_ = Org_ref_common_( root.find('Org-ref_common') )
		else:
			pass
		if root.find('Org-ref_db') is not None:
			self.org_ref_db_ = Org_ref_db_( root.find('Org-ref_db') )
		else:
			pass
		if root.find('Org-ref_orgname') is not None:
			self.org_ref_orgname_ = Org_ref_orgname_( root.find('Org-ref_orgname') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_genomic_strand__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_genomic_strand__, self ).__init__()
		self.name = 'Spliced-exon_genomic-strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_pdb( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_pdb, self ).__init__()
		self.name = 'Seqdesc_pdb'
		self.pdb_block_ = PDB_block_( root.find('PDB-block') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class MolInfo_tech( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MolInfo_tech, self ).__init__()
		self.name = 'MolInfo_tech'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'standard', 'est', 'sts', 'survey', 'genemap', 'physmap', 'derived', 'concept-trans', 'seq-pept', 'both', 'seq-pept-overlap', 'seq-pept-homol', 'concept-trans-a', 'htgs-1', 'htgs-2', 'htgs-3', 'fli-cdna', 'htgs-0', 'htc', 'wgs', 'barcode', 'composite-wgs-htgs', 'tsa', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Program_id_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Program_id_name_, self ).__init__()
		self.name = 'Program-id_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_gen_muid_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_muid_, self ).__init__()
		self.name = 'Cit-gen_muid'
		self.text = root.text
	
	def __call__( self ):
		pass


class Meeting_date( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Meeting_date, self ).__init__()
		self.name = 'Meeting_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_item_seq_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Delta_item_seq_, self ).__init__()
		self.name = 'Delta-item_seq'
		#jedna z opcji dla ['Delta-item_seq_literal', 'Delta-item_seq_this', 'Delta-item_seq_loc']
		if 'Delta-item_seq_literal' in [ x.tag for x in root.getchildren() ]:
			self.delta_item_seq_literal_ = Delta_item_seq_literal_( root.find('Delta-item_seq_literal') )
		elif 'Delta-item_seq_this' in [ x.tag for x in root.getchildren() ]:
			self.delta_item_seq_this_ = Delta_item_seq_this_( root.find('Delta-item_seq_this') )
		else:
			self.delta_item_seq_loc_ = Delta_item_seq_loc_( root.find('Delta-item_seq_loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_book( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_book, self ).__init__()
		self.name = 'Pub_book'
		self.cit_book_ = Cit_book_( root.find('Cit-book') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_div( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_div, self ).__init__()
		self.name = 'OrgName_div'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_align_segs_std_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_std_, self ).__init__()
		self.name = 'Seq-align_segs_std'
		if root.find('Std-seg') is not None:
			self.std_seg_ = [ Std_seg_(element) for element in root.findall('Std-seg') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_user( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_user, self ).__init__()
		self.name = 'Seqdesc_user'
		self.user_object_ = User_object_( root.find('User-object') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Org_ref_syn_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_syn_, self ).__init__()
		self.name = 'Org-ref_syn'
		if root.find('Org-ref_syn_E') is not None:
			self.org_ref_syn_e_ = [ Org_ref_syn_E_(element) for element in root.findall('Org-ref_syn_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonString_table_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonString_table_, self ).__init__()
		self.name = 'CommonString-table'
		self.commonstring_table_indexes_ = CommonString_table_indexes_( root.find('CommonString-table_indexes') )
		self.commonstring_table_strings_ = CommonString_table_strings_( root.find('CommonString-table_strings') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textannot_id_version_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textannot_id_version_, self ).__init__()
		self.name = 'Textannot-id_version'
		self.text = root.text
	
	def __call__( self ):
		pass


class ArticleId_pmpid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_pmpid, self ).__init__()
		self.name = 'ArticleId_pmpid'
		self.pmpid = PmPid( root.find('PmPid') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dbtag_tag( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dbtag_tag, self ).__init__()
		self.name = 'Dbtag_tag'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_let_man_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_let_man_id__, self ).__init__()
		self.name = 'Cit-let_man-id'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_std_year_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_year_, self ).__init__()
		self.name = 'Date-std_year'
		self.text = root.text
	
	def __call__( self ):
		pass


class Rsite_ref_db_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Rsite'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Rsite_ref_db_, self ).__init__()
		self.name = 'Rsite-ref_db'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_ec_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_ec_E_, self ).__init__()
		self.name = 'Prot-ref_ec_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imprint_volume( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_volume, self ).__init__()
		self.name = 'Imprint_volume'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_annot_db_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_annot_db_, self ).__init__()
		self.name = 'Seq-annot_db'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['genbank', 'embl', 'ddbj', 'pir', 'sp', 'bbone', 'pdb', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Variation_ref_consequence_E_frameshift_x_length__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_frameshift_x_length__, self ).__init__()
		self.name = 'Variation-ref_consequence_E_frameshift_x-length'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cdregion_conflict( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_conflict, self ).__init__()
		self.name = 'Cdregion_conflict'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Pub_sub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_sub, self ).__init__()
		self.name = 'Pub_sub'
		self.cit_sub_ = Cit_sub_( root.find('Cit-sub') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_product_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_exon_product_id__, self ).__init__()
		self.name = 'Spliced-exon_product-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_int_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_int_, self ).__init__()
		self.name = 'User-field_data_int'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_multi_data_bytes__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_bytes__, self ).__init__()
		self.name = 'SeqTable-multi-data_bytes'
		if root.find('SeqTable-multi-data_bytes_E') is not None:
			self.seqtable_multi_data_bytes_e__ = [ SeqTable_multi_data_bytes_E__(element) for element in root.findall('SeqTable-multi-data_bytes_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Heterogen( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Heterogen, self ).__init__()
		self.name = 'Heterogen'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_multi_data_string_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_string_E__, self ).__init__()
		self.name = 'SeqTable-multi-data_string_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatXref( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatXref, self ).__init__()
		self.name = 'SeqFeatXref'
		if root.find('SeqFeatXref_id') is not None:
			self.seqfeatxref_id = SeqFeatXref_id( root.find('SeqFeatXref_id') )
		else:
			pass
		if root.find('SeqFeatXref_data') is not None:
			self.seqfeatxref_data = SeqFeatXref_data( root.find('SeqFeatXref_data') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_dim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_dim_, self ).__init__()
		self.name = 'Dense-seg_dim'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_enum_names_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_enum_names_E_, self ).__init__()
		self.name = 'Num-enum_names_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_nomenclature_source_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_nomenclature_source_, self ).__init__()
		self.name = 'Gene-nomenclature_source'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_activity_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_activity_E_, self ).__init__()
		self.name = 'Prot-ref_activity_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seg_scores_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_scores_, self ).__init__()
		self.name = 'Packed-seg_scores'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_dbxref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_dbxref_, self ).__init__()
		self.name = 'Seq-feat_dbxref'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Auth_list_names_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_names_str_, self ).__init__()
		self.name = 'Auth-list_names_str'
		if root.find('Auth-list_names_str_E') is not None:
			self.auth_list_names_str_e_ = [ Auth_list_names_str_E_(element) for element in root.findall('Auth-list_names_str_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_txinit( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_txinit, self ).__init__()
		self.name = 'SeqFeatData_txinit'
		self.txinit = Txinit( root.find('Txinit') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_single_data_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_single_data_id__, self ).__init__()
		self.name = 'SeqTable-single-data_id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_real__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_real__, self ).__init__()
		self.name = 'SeqTable-multi-data_real'
		if root.find('SeqTable-multi-data_real_E') is not None:
			self.seqtable_multi_data_real_e__ = [ SeqTable_multi_data_real_E__(element) for element in root.findall('SeqTable-multi-data_real_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_title( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_title, self ).__init__()
		self.name = 'Seqdesc_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_sub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_sub, self ).__init__()
		self.name = 'Affil_std_sub'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_art_from_proc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_art_from_proc_, self ).__init__()
		self.name = 'Cit-art_from_proc'
		self.cit_proc_ = Cit_proc_( root.find('Cit-proc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_ncbipaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbipaa_, self ).__init__()
		self.name = 'Seq-data_ncbipaa'
		self.ncbipaa = NCBIpaa( root.find('NCBIpaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Code_break_aa_ncbieaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Code_break_aa_ncbieaa_, self ).__init__()
		self.name = 'Code-break_aa_ncbieaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class PubStatusDate( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PubStatusDate, self ).__init__()
		self.name = 'PubStatusDate'
		self.pubstatusdate_pubstatus = PubStatusDate_pubstatus( root.find('PubStatusDate_pubstatus') )
		self.pubstatusdate_date = PubStatusDate_date( root.find('PubStatusDate_date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Trna_ext_aa_ncbi8aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_aa_ncbi8aa_, self ).__init__()
		self.name = 'Trna-ext_aa_ncbi8aa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_let_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_let_, self ).__init__()
		self.name = 'Cit-let'
		if root.find('Cit-let_type') is not None:
			self.cit_let_type_ = Cit_let_type_( root.find('Cit-let_type') )
		else:
			pass
		self.cit_let_cit_ = Cit_let_cit_( root.find('Cit-let_cit') )
		if root.find('Cit-let_man-id') is not None:
			self.cit_let_man_id__ = Cit_let_man_id__( root.find('Cit-let_man-id') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_journal_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_journal_, self ).__init__()
		self.name = 'Cit-gen_journal'
		self.title = Title( root.find('Title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_abstract_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_abstract_, self ).__init__()
		self.name = 'Cit-pat_abstract'
		self.text = root.text
	
	def __call__( self ):
		pass


class Txinit_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_name, self ).__init__()
		self.name = 'Txinit_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_ref_syn_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_syn_E_, self ).__init__()
		self.name = 'Gene-ref_syn_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seg_strands_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_strands_, self ).__init__()
		self.name = 'Packed-seg_strands'
		if root.find('Na-strand') is not None:
			self.na_strand_ = [ Na_strand_(element) for element in root.findall('Na-strand') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_location_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_location_, self ).__init__()
		self.name = 'Variation-ref_location'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_bond_b_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_bond_b_, self ).__init__()
		self.name = 'Seq-bond_b'
		self.seq_point_ = Seq_point_( root.find('Seq-point') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_issue( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_issue, self ).__init__()
		self.name = 'Imprint_issue'
		self.text = root.text
	
	def __call__( self ):
		pass


class Spliced_exon_scores_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_scores_, self ).__init__()
		self.name = 'Spliced-exon_scores'
		self.score_set_ = Score_set_( root.find('Score-set') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_fuzz_range_max_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_range_max_, self ).__init__()
		self.name = 'Int-fuzz_range_max'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_literal_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_literal_, self ).__init__()
		self.name = 'Seq-literal'
		if root.find('Seq-literal_seq-data') is not None:
			self.seq_literal_seq_data__ = Seq_literal_seq_data__( root.find('Seq-literal_seq-data') )
		else:
			pass
		self.seq_literal_length_ = Seq_literal_length_( root.find('Seq-literal_length') )
		if root.find('Seq-literal_fuzz') is not None:
			self.seq_literal_fuzz_ = Seq_literal_fuzz_( root.find('Seq-literal_fuzz') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_modifier__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_modifier__, self ).__init__()
		self.name = 'Spliced-seg-modifier'
		#jedna z opcji dla ['Spliced-seg-modifier_start-codon-found', 'Spliced-seg-modifier_stop-codon-found']
		if 'Spliced-seg-modifier_start-codon-found' in [ x.tag for x in root.getchildren() ]:
			self.spliced_seg_modifier_start_codon_found____ = Spliced_seg_modifier_start_codon_found____( root.find('Spliced-seg-modifier_start-codon-found') )
		else:
			self.spliced_seg_modifier_stop_codon_found____ = Spliced_seg_modifier_stop_codon_found____( root.find('Spliced-seg-modifier_stop-codon-found') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Byte_graph_max_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Byte_graph_max_, self ).__init__()
		self.name = 'Byte-graph_max'
		self.text = root.text
	
	def __call__( self ):
		pass


class Real_graph_axis_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Real_graph_axis_, self ).__init__()
		self.name = 'Real-graph_axis'
		self.text = root.text
	
	def __call__( self ):
		pass


class GIBB_mol_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GIBB_mol_, self ).__init__()
		self.name = 'GIBB-mol'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'genomic', 'pre-mRNA', 'mRNA', 'rRNA', 'tRNA', 'snRNA', 'scRNA', 'peptide', 'other-genetic', 'genomic-mRNA', 'other']
		self.value = root.get('value')


class User_field_data_real_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_real_, self ).__init__()
		self.name = 'User-field_data_real'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_ref_maploc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_maploc_, self ).__init__()
		self.name = 'Gene-ref_maploc'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_hist_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_hist_, self ).__init__()
		self.name = 'Seq-hist'
		if root.find('Seq-hist_assembly') is not None:
			self.seq_hist_assembly_ = Seq_hist_assembly_( root.find('Seq-hist_assembly') )
		else:
			pass
		if root.find('Seq-hist_deleted') is not None:
			self.seq_hist_deleted_ = Seq_hist_deleted_( root.find('Seq-hist_deleted') )
		else:
			pass
		if root.find('Seq-hist_replaced-by') is not None:
			self.seq_hist_replaced_by__ = Seq_hist_replaced_by__( root.find('Seq-hist_replaced-by') )
		else:
			pass
		if root.find('Seq-hist_replaces') is not None:
			self.seq_hist_replaces_ = Seq_hist_replaces_( root.find('Seq-hist_replaces') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pubdesc_poly_a_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_poly_a_, self ).__init__()
		self.name = 'Pubdesc_poly-a'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Spliced_exon_parts_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_parts_, self ).__init__()
		self.name = 'Spliced-exon_parts'
		if root.find('Spliced-exon-chunk') is not None:
			self.spliced_exon_chunk__ = [ Spliced_exon_chunk__(element) for element in root.findall('Spliced-exon-chunk') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Score_id( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Score_id, self ).__init__()
		self.name = 'Score_id'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_deleted_bool_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_hist_deleted_bool_, self ).__init__()
		self.name = 'Seq-hist_deleted_bool'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Ext_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Ext_loc_, self ).__init__()
		self.name = 'Ext-loc'
		self.ext_loc_location_ = Ext_loc_location_( root.find('Ext-loc_location') )
		self.ext_loc_id_ = Ext_loc_id_( root.find('Ext-loc_id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_pdb_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_pdb_, self ).__init__()
		self.name = 'Seq-id_pdb'
		self.pdb_seq_id__ = PDB_seq_id__( root.find('PDB-seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_align_id_, self ).__init__()
		self.name = 'Seq-align_id'
		if root.find('Object-id') is not None:
			self.object_id_ = [ Object_id_(element) for element in root.findall('Object-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_ext_map_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_ext_map_, self ).__init__()
		self.name = 'Seq-ext_map'
		self.map_ext_ = Map_ext_( root.find('Map-ext') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_ncbi2na_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbi2na_, self ).__init__()
		self.name = 'Seq-data_ncbi2na'
		self.ncbi2na = NCBI2na( root.find('NCBI2na') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_somatic_origin_E_source__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_somatic_origin_E_source__, self ).__init__()
		self.name = 'Variation-ref_somatic-origin_E_source'
		self.subsource = SubSource( root.find('SubSource') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_allele_origin_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_allele_origin_, self ).__init__()
		self.name = 'VariantProperties_allele-origin'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'germline', 'somatic', 'inherited', 'paternal', 'maternal', 'de-novo', 'biparental', 'uniparental', 'not-tested', 'tested-inconclusive', 'not-reported', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Person_id_consortium_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Person_id_consortium_, self ).__init__()
		self.name = 'Person-id_consortium'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceItem_exon_count_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceItem_exon_count_, self ).__init__()
		self.name = 'ModelEvidenceItem_exon-count'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_ddbj_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_ddbj_, self ).__init__()
		self.name = 'Seq-id_ddbj'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Auth_list_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Auth_list_, self ).__init__()
		self.name = 'Auth-list'
		self.auth_list_names_ = Auth_list_names_( root.find('Auth-list_names') )
		if root.find('Auth-list_affil') is not None:
			self.auth_list_affil_ = Auth_list_affil_( root.find('Auth-list_affil') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_patent_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_patent_, self ).__init__()
		self.name = 'Pub-set_patent'
		if root.find('Cit-pat') is not None:
			self.cit_pat_ = [ Cit_pat_(element) for element in root.findall('Cit-pat') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Genetic_code_E_ncbi8aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_ncbi8aa_, self ).__init__()
		self.name = 'Genetic-code_E_ncbi8aa'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_comment( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_comment, self ).__init__()
		self.name = 'SeqFeatData_comment'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_annot_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_, self ).__init__()
		self.name = 'Seq-annot'
		if root.find('Seq-annot_db') is not None:
			self.seq_annot_db_ = Seq_annot_db_( root.find('Seq-annot_db') )
		else:
			pass
		if root.find('Seq-annot_desc') is not None:
			self.seq_annot_desc_ = Seq_annot_desc_( root.find('Seq-annot_desc') )
		else:
			pass
		self.seq_annot_data_ = Seq_annot_data_( root.find('Seq-annot_data') )
		if root.find('Seq-annot_name') is not None:
			self.seq_annot_name_ = Seq_annot_name_( root.find('Seq-annot_name') )
		else:
			pass
		if root.find('Seq-annot_id') is not None:
			self.seq_annot_id_ = Seq_annot_id_( root.find('Seq-annot_id') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_project_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_project_data_, self ).__init__()
		self.name = 'VariantProperties_project-data'
		if root.find('VariantProperties_project-data_E') is not None:
			self.variantproperties_project_data_e_ = [ VariantProperties_project_data_E_(element) for element in root.findall('VariantProperties_project-data_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_data_instance_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_data_instance_, self ).__init__()
		self.name = 'Variation-ref_data_instance'
		self.variation_inst_ = Variation_inst_( root.find('Variation-inst') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_txsystem( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_txsystem, self ).__init__()
		self.name = 'Txinit_txsystem'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'pol1', 'pol2', 'pol3', 'bacterial', 'viral', 'rna', 'organelle', 'other']
		self.value = root.get('value')


class MolInfo_techexp( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MolInfo_techexp, self ).__init__()
		self.name = 'MolInfo_techexp'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_data_, self ).__init__()
		self.name = 'Seq-feat_data'
		self.seqfeatdata = SeqFeatData( root.find('SeqFeatData') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Ext_loc_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Ext_loc_id_, self ).__init__()
		self.name = 'Ext-loc_id'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_includes_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_includes_, self ).__init__()
		self.name = 'PIR-block_includes'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_align_lens_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_lens_E_, self ).__init__()
		self.name = 'Sparse-align_lens_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Spliced_seg_genomic_strand__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_genomic_strand__, self ).__init__()
		self.name = 'Spliced-seg_genomic-strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annotdesc_align( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annotdesc_align, self ).__init__()
		self.name = 'Annotdesc_align'
		self.align_def_ = Align_def_( root.find('Align-def') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_name_namedhybrid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_name_namedhybrid, self ).__init__()
		self.name = 'OrgName_name_namedhybrid'
		self.binomialorgname = BinomialOrgName( root.find('BinomialOrgName') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_authors_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_gen_authors_, self ).__init__()
		self.name = 'Cit-gen_authors'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_pub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_pub, self ).__init__()
		self.name = 'Imprint_pub'
		self.affil = Affil( root.find('Affil') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textannot_id_release_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textannot_id_release_, self ).__init__()
		self.name = 'Textannot-id_release'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_email( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_email, self ).__init__()
		self.name = 'Affil_std_email'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_consequence_E_loss_of_heterozygosity___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_loss_of_heterozygosity___, self ).__init__()
		self.name = 'Variation-ref_consequence_E_loss-of-heterozygosity'
		if root.find('Variation-ref_consequence_E_loss-of-heterozygosity_reference') is not None:
			self.variation_ref_consequence_e_loss_of_heterozygosity_reference___ = Variation_ref_consequence_E_loss_of_heterozygosity_reference___( root.find('Variation-ref_consequence_E_loss-of-heterozygosity_reference') )
		else:
			pass
		if root.find('Variation-ref_consequence_E_loss-of-heterozygosity_test') is not None:
			self.variation_ref_consequence_e_loss_of_heterozygosity_test___ = Variation_ref_consequence_E_loss_of_heterozygosity_test___( root.find('Variation-ref_consequence_E_loss-of-heterozygosity_test') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_coden( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_coden, self ).__init__()
		self.name = 'Title_E_coden'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Packed_seg_, self ).__init__()
		self.name = 'Packed-seg'
		self.packed_seg_numseg_ = Packed_seg_numseg_( root.find('Packed-seg_numseg') )
		if root.find('Packed-seg_scores') is not None:
			self.packed_seg_scores_ = Packed_seg_scores_( root.find('Packed-seg_scores') )
		else:
			pass
		self.packed_seg_starts_ = Packed_seg_starts_( root.find('Packed-seg_starts') )
		if root.find('Packed-seg_strands') is not None:
			self.packed_seg_strands_ = Packed_seg_strands_( root.find('Packed-seg_strands') )
		else:
			pass
		if root.find('Packed-seg_dim') is not None:
			self.packed_seg_dim_ = Packed_seg_dim_( root.find('Packed-seg_dim') )
		else:
			pass
		self.packed_seg_present_ = Packed_seg_present_( root.find('Packed-seg_present') )
		self.packed_seg_ids_ = Packed_seg_ids_( root.find('Packed-seg_ids') )
		self.packed_seg_lens_ = Packed_seg_lens_( root.find('Packed-seg_lens') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_label_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_label_, self ).__init__()
		self.name = 'User-field_label'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_dim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_align_dim_, self ).__init__()
		self.name = 'Seq-align_dim'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_ext_, self ).__init__()
		self.name = 'Seq-ext'
		#jedna z opcji dla ['Seq-ext_seg', 'Seq-ext_map', 'Seq-ext_delta', 'Seq-ext_ref']
		if 'Seq-ext_seg' in [ x.tag for x in root.getchildren() ]:
			self.seq_ext_seg_ = Seq_ext_seg_( root.find('Seq-ext_seg') )
		elif 'Seq-ext_map' in [ x.tag for x in root.getchildren() ]:
			self.seq_ext_map_ = Seq_ext_map_( root.find('Seq-ext_map') )
		elif 'Seq-ext_delta' in [ x.tag for x in root.getchildren() ]:
			self.seq_ext_delta_ = Seq_ext_delta_( root.find('Seq-ext_delta') )
		else:
			self.seq_ext_ref_ = Seq_ext_ref_( root.find('Seq-ext_ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class NCBI2na( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBI2na, self ).__init__()
		self.name = 'NCBI2na'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_ids_, self ).__init__()
		self.name = 'Seq-feat_ids'
		if root.find('Feat-id') is not None:
			self.feat_id_ = [ Feat_id_(element) for element in root.findall('Feat-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Author_level( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Author_level, self ).__init__()
		self.name = 'Author_level'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['primary', 'secondary']
		self.value = root.get('value')


class Seq_align_segs_sparse_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_sparse_, self ).__init__()
		self.name = 'Seq-align_segs_sparse'
		self.sparse_seg_ = Sparse_seg_( root.find('Sparse-seg') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_summary_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_summary_, self ).__init__()
		self.name = 'PIR-block_summary'
		self.text = root.text
	
	def __call__( self ):
		pass


class Person_id_ml_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Person_id_ml_, self ).__init__()
		self.name = 'Person-id_ml'
		self.text = root.text
	
	def __call__( self ):
		pass


class Prot_ref_processed_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_processed_, self ).__init__()
		self.name = 'Prot-ref_processed'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'preprotein', 'mature', 'signal-peptide', 'transit-peptide']
		self.value = root.get('value')


class Object_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Object_id_, self ).__init__()
		self.name = 'Object-id'
		#jedna z opcji dla ['Object-id_str', 'Object-id_id']
		if 'Object-id_str' in [ x.tag for x in root.getchildren() ]:
			self.object_id_str_ = Object_id_str_( root.find('Object-id_str') )
		else:
			self.object_id_id_ = Object_id_id_( root.find('Object-id_id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gene_ref_locus_tag__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_locus_tag__, self ).__init__()
		self.name = 'Gene-ref_locus-tag'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_column_sparse_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_column_sparse_, self ).__init__()
		self.name = 'SeqTable-column_sparse'
		self.seqtable_sparse_index__ = SeqTable_sparse_index__( root.find('SeqTable-sparse-index') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Std_seg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Std_seg_, self ).__init__()
		self.name = 'Std-seg'
		self.std_seg_loc_ = Std_seg_loc_( root.find('Std-seg_loc') )
		if root.find('Std-seg_ids') is not None:
			self.std_seg_ids_ = Std_seg_ids_( root.find('Std-seg_ids') )
		else:
			pass
		if root.find('Std-seg_dim') is not None:
			self.std_seg_dim_ = Std_seg_dim_( root.find('Std-seg_dim') )
		else:
			pass
		if root.find('Std-seg_scores') is not None:
			self.std_seg_scores_ = Std_seg_scores_( root.find('Std-seg_scores') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_article_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_article_, self ).__init__()
		self.name = 'Pub-set_article'
		if root.find('Cit-art') is not None:
			self.cit_art_ = [ Cit_art_(element) for element in root.findall('Cit-art') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_partial_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_partial_, self ).__init__()
		self.name = 'Seq-feat_partial'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class EMBL_block_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	def __init__( self, root ):
		super( EMBL_block_, self ).__init__()
		self.name = 'EMBL-block'
		if root.find('EMBL-block_class') is not None:
			self.embl_block_class_ = EMBL_block_class_( root.find('EMBL-block_class') )
		else:
			pass
		if root.find('EMBL-block_div') is not None:
			self.embl_block_div_ = EMBL_block_div_( root.find('EMBL-block_div') )
		else:
			pass
		if root.find('EMBL-block_xref') is not None:
			self.embl_block_xref_ = EMBL_block_xref_( root.find('EMBL-block_xref') )
		else:
			pass
		self.embl_block_creation_date__ = EMBL_block_creation_date__( root.find('EMBL-block_creation-date') )
		if root.find('EMBL-block_extra-acc') is not None:
			self.embl_block_extra_acc__ = EMBL_block_extra_acc__( root.find('EMBL-block_extra-acc') )
		else:
			pass
		self.embl_block_update_date__ = EMBL_block_update_date__( root.find('EMBL-block_update-date') )
		if root.find('EMBL-block_keywords') is not None:
			self.embl_block_keywords_ = EMBL_block_keywords_( root.find('EMBL-block_keywords') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_tsub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_tsub, self ).__init__()
		self.name = 'Title_E_tsub'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_ref_syn_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_syn_, self ).__init__()
		self.name = 'Gene-ref_syn'
		if root.find('Gene-ref_syn_E') is not None:
			self.gene_ref_syn_e_ = [ Gene_ref_syn_E_(element) for element in root.findall('Gene-ref_syn_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_seq_support_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_seq_support_, self ).__init__()
		self.name = 'Clone-seq_support'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['prototype', 'supporting', 'supports-other', 'non-supporting']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Spliced_exon_chunk_product_ins___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_chunk_product_ins___, self ).__init__()
		self.name = 'Spliced-exon-chunk_product-ins'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_idnum_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_idnum_E_, self ).__init__()
		self.name = 'Medline-entry_idnum_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_field_data_bool_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_bool_, self ).__init__()
		self.name = 'User-field_data_bool'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Seq_data_ncbi8aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbi8aa_, self ).__init__()
		self.name = 'Seq-data_ncbi8aa'
		self.ncbi8aa = NCBI8aa( root.find('NCBI8aa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_xref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_xref_, self ).__init__()
		self.name = 'Seq-feat_xref'
		if root.find('SeqFeatXref') is not None:
			self.seqfeatxref = [ SeqFeatXref(element) for element in root.findall('SeqFeatXref') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_ec_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_ec_, self ).__init__()
		self.name = 'Prot-ref_ec'
		if root.find('Prot-ref_ec_E') is not None:
			self.prot_ref_ec_e_ = [ Prot_ref_ec_E_(element) for element in root.findall('Prot-ref_ec_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textseq_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textseq_id_, self ).__init__()
		self.name = 'Textseq-id'
		if root.find('Textseq-id_accession') is not None:
			self.textseq_id_accession_ = Textseq_id_accession_( root.find('Textseq-id_accession') )
		else:
			pass
		if root.find('Textseq-id_release') is not None:
			self.textseq_id_release_ = Textseq_id_release_( root.find('Textseq-id_release') )
		else:
			pass
		if root.find('Textseq-id_name') is not None:
			self.textseq_id_name_ = Textseq_id_name_( root.find('Textseq-id_name') )
		else:
			pass
		if root.find('Textseq-id_version') is not None:
			self.textseq_id_version_ = Textseq_id_version_( root.find('Textseq-id_version') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_data_set_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_data_set_, self ).__init__()
		self.name = 'Variation-ref_data_set'
		self.variation_ref_data_set_type_ = Variation_ref_data_set_type_( root.find('Variation-ref_data_set_type') )
		if root.find('Variation-ref_data_set_name') is not None:
			self.variation_ref_data_set_name_ = Variation_ref_data_set_name_( root.find('Variation-ref_data_set_name') )
		else:
			pass
		self.variation_ref_data_set_variations_ = Variation_ref_data_set_variations_( root.find('Variation-ref_data_set_variations') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_clinical_test__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_clinical_test__, self ).__init__()
		self.name = 'Variation-ref_clinical-test'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_set_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqset'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Bioseq_set_class_, self ).__init__()
		self.name = 'Bioseq-set_class'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'nuc-prot', 'segset', 'conset', 'parts', 'gibb', 'gi', 'genbank', 'pir', 'pub-set', 'equiv', 'swissprot', 'pdb-entry', 'mut-set', 'pop-set', 'phy-set', 'eco-set', 'gen-prod-set', 'wgs-set', 'named-annot', 'named-annot-prod', 'read-set', 'paired-end-reads', 'small-genome-set', 'other']
		self.value = root.get('value')


class BioSource_origin( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BioSource_origin, self ).__init__()
		self.name = 'BioSource_origin'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'natural', 'natmut', 'mut', 'artificial', 'synthetic', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Pubdesc_num( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Pubdesc_num, self ).__init__()
		self.name = 'Pubdesc_num'
		self.numbering = Numbering( root.find('Numbering') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_jour_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_jour_, self ).__init__()
		self.name = 'Cit-jour'
		self.cit_jour_imp_ = Cit_jour_imp_( root.find('Cit-jour_imp') )
		self.cit_jour_title_ = Cit_jour_title_( root.find('Cit-jour_title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_ints_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_ints_, self ).__init__()
		self.name = 'User-field_data_ints'
		if root.find('User-field_data_ints_E') is not None:
			self.user_field_data_ints_e_ = [ User_field_data_ints_E_(element) for element in root.findall('User-field_data_ints_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Byte_graph_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Byte_graph_, self ).__init__()
		self.name = 'Byte-graph'
		self.byte_graph_axis_ = Byte_graph_axis_( root.find('Byte-graph_axis') )
		self.byte_graph_max_ = Byte_graph_max_( root.find('Byte-graph_max') )
		self.byte_graph_min_ = Byte_graph_min_( root.find('Byte-graph_min') )
		self.byte_graph_values_ = Byte_graph_values_( root.find('Byte-graph_values') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_data_, self ).__init__()
		self.name = 'Variation-ref_data'
		#jedna z opcji dla ['Variation-ref_data_uniparental-disomy', 'Variation-ref_data_instance', 'Variation-ref_data_complex', 'Variation-ref_data_note', 'Variation-ref_data_unknown', 'Variation-ref_data_set']
		if 'Variation-ref_data_uniparental-disomy' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_data_uniparental_disomy__ = Variation_ref_data_uniparental_disomy__( root.find('Variation-ref_data_uniparental-disomy') )
		elif 'Variation-ref_data_instance' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_data_instance_ = Variation_ref_data_instance_( root.find('Variation-ref_data_instance') )
		elif 'Variation-ref_data_complex' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_data_complex_ = Variation_ref_data_complex_( root.find('Variation-ref_data_complex') )
		elif 'Variation-ref_data_note' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_data_note_ = Variation_ref_data_note_( root.find('Variation-ref_data_note') )
		elif 'Variation-ref_data_unknown' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_data_unknown_ = Variation_ref_data_unknown_( root.find('Variation-ref_data_unknown') )
		else:
			self.variation_ref_data_set_ = Variation_ref_data_set_( root.find('Variation-ref_data_set') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_diag_dim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_diag_dim_, self ).__init__()
		self.name = 'Dense-diag_dim'
		self.text = root.text
	
	def __call__( self ):
		pass


class Numbering_enum( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Numbering_enum, self ).__init__()
		self.name = 'Numbering_enum'
		self.num_enum_ = Num_enum_( root.find('Num-enum') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonString_table_strings_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonString_table_strings_, self ).__init__()
		self.name = 'CommonString-table_strings'
		if root.find('CommonString-table_strings_E') is not None:
			self.commonstring_table_strings_e_ = [ CommonString_table_strings_E_(element) for element in root.findall('CommonString-table_strings_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_align_second_strands__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_second_strands__, self ).__init__()
		self.name = 'Sparse-align_second-strands'
		if root.find('Na-strand') is not None:
			self.na_strand_ = [ Na_strand_(element) for element in root.findall('Na-strand') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_exons_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_seg_exons_, self ).__init__()
		self.name = 'Spliced-seg_exons'
		if root.find('Spliced-exon') is not None:
			self.spliced_exon_ = [ Spliced_exon_(element) for element in root.findall('Spliced-exon') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_lens_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_lens_, self ).__init__()
		self.name = 'Dense-seg_lens'
		if root.find('Dense-seg_lens_E') is not None:
			self.dense_seg_lens_e_ = [ Dense_seg_lens_E_(element) for element in root.findall('Dense-seg_lens_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_seqref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	def __init__( self, root ):
		super( PIR_block_seqref_, self ).__init__()
		self.name = 'PIR-block_seqref'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_inst_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_inst_type_, self ).__init__()
		self.name = 'Variation-inst_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'identity', 'inv', 'snv', 'mnp', 'delins', 'del', 'ins', 'microsatellite', 'transposon', 'cnv', 'direct-copy', 'rev-direct-copy', 'inverted-copy', 'everted-copy', 'translocation', 'prot-missense', 'prot-nonsense', 'prot-neutral', 'prot-silent', 'prot-other', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Std_seg_scores_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Std_seg_scores_, self ).__init__()
		self.name = 'Std-seg_scores'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Align_def_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Align_def_, self ).__init__()
		self.name = 'Align-def'
		self.align_def_align_type__ = Align_def_align_type__( root.find('Align-def_align-type') )
		if root.find('Align-def_ids') is not None:
			self.align_def_ids_ = Align_def_ids_( root.find('Align-def_ids') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Author( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Author, self ).__init__()
		self.name = 'Author'
		if root.find('Author_is-corr') is not None:
			self.author_is_corr_ = Author_is_corr_( root.find('Author_is-corr') )
		else:
			pass
		if root.find('Author_level') is not None:
			self.author_level = Author_level( root.find('Author_level') )
		else:
			pass
		if root.find('Author_role') is not None:
			self.author_role = Author_role( root.find('Author_role') )
		else:
			pass
		if root.find('Author_affil') is not None:
			self.author_affil = Author_affil( root.find('Author_affil') )
		else:
			pass
		self.author_name = Author_name( root.find('Author_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seg_lens_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_lens_, self ).__init__()
		self.name = 'Packed-seg_lens'
		if root.find('Packed-seg_lens_E') is not None:
			self.packed_seg_lens_e_ = [ Packed_seg_lens_E_(element) for element in root.findall('Packed-seg_lens_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleIdSet( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleIdSet, self ).__init__()
		self.name = 'ArticleIdSet'
		if root.find('ArticleId') is not None:
			self.articleid = [ ArticleId(element) for element in root.findall('ArticleId') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textannot_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textannot_id_, self ).__init__()
		self.name = 'Textannot-id'
		if root.find('Textannot-id_accession') is not None:
			self.textannot_id_accession_ = Textannot_id_accession_( root.find('Textannot-id_accession') )
		else:
			pass
		if root.find('Textannot-id_version') is not None:
			self.textannot_id_version_ = Textannot_id_version_( root.find('Textannot-id_version') )
		else:
			pass
		if root.find('Textannot-id_release') is not None:
			self.textannot_id_release_ = Textannot_id_release_( root.find('Textannot-id_release') )
		else:
			pass
		if root.find('Textannot-id_name') is not None:
			self.textannot_id_name_ = Textannot_id_name_( root.find('Textannot-id_name') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_set_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Bioseq_set_id_, self ).__init__()
		self.name = 'Bioseq-set_id'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cdregion_code_break_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Cdregion_code_break_, self ).__init__()
		self.name = 'Cdregion_code-break'
		if root.find('Code-break') is not None:
			self.code_break_ = [ Code_break_(element) for element in root.findall('Code-break') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_iupacaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_iupacaa_, self ).__init__()
		self.name = 'Seq-data_iupacaa'
		self.iupacaa = IUPACaa( root.find('IUPACaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_placement_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_placement_, self ).__init__()
		self.name = 'PIR-block_placement'
		self.text = root.text
	
	def __call__( self ):
		pass


class Phenotype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Phenotype, self ).__init__()
		self.name = 'Phenotype'
		if root.find('Phenotype_clinical-significance') is not None:
			self.phenotype_clinical_significance_ = Phenotype_clinical_significance_( root.find('Phenotype_clinical-significance') )
		else:
			pass
		if root.find('Phenotype_source') is not None:
			self.phenotype_source = Phenotype_source( root.find('Phenotype_source') )
		else:
			pass
		if root.find('Phenotype_xref') is not None:
			self.phenotype_xref = Phenotype_xref( root.find('Phenotype_xref') )
		else:
			pass
		if root.find('Phenotype_term') is not None:
			self.phenotype_term = Phenotype_term( root.find('Phenotype_term') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BioSource_subtype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BioSource_subtype, self ).__init__()
		self.name = 'BioSource_subtype'
		if root.find('SubSource') is not None:
			self.subsource = [ SubSource(element) for element in root.findall('SubSource') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GIBB_mod_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GIBB_mod_, self ).__init__()
		self.name = 'GIBB-mod'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['dna', 'rna', 'extrachrom', 'plasmid', 'mitochondrial', 'chloroplast', 'kinetoplast', 'cyanelle', 'synthetic', 'recombinant', 'partial', 'complete', 'mutagen', 'natmut', 'transposon', 'insertion-seq', 'no-left', 'no-right', 'macronuclear', 'proviral', 'est', 'sts', 'survey', 'chromoplast', 'genemap', 'restmap', 'physmap', 'other']
		self.value = root.get('value')


class Medline_rn_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_rn_name_, self ).__init__()
		self.name = 'Medline-rn_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_multi_data_bit__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_bit__, self ).__init__()
		self.name = 'SeqTable-multi-data_bit'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub_journal( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_journal, self ).__init__()
		self.name = 'Pub_journal'
		self.cit_jour_ = Cit_jour_( root.find('Cit-jour') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	def __init__( self, root ):
		super( OrgName, self ).__init__()
		self.name = 'OrgName'
		if root.find('OrgName_name') is not None:
			self.orgname_name = OrgName_name( root.find('OrgName_name') )
		else:
			pass
		if root.find('OrgName_gcode') is not None:
			self.orgname_gcode = OrgName_gcode( root.find('OrgName_gcode') )
		else:
			pass
		if root.find('OrgName_pgcode') is not None:
			self.orgname_pgcode = OrgName_pgcode( root.find('OrgName_pgcode') )
		else:
			pass
		if root.find('OrgName_mgcode') is not None:
			self.orgname_mgcode = OrgName_mgcode( root.find('OrgName_mgcode') )
		else:
			pass
		if root.find('OrgName_div') is not None:
			self.orgname_div = OrgName_div( root.find('OrgName_div') )
		else:
			pass
		if root.find('OrgName_mod') is not None:
			self.orgname_mod = OrgName_mod( root.find('OrgName_mod') )
		else:
			pass
		if root.find('OrgName_attrib') is not None:
			self.orgname_attrib = OrgName_attrib( root.find('OrgName_attrib') )
		else:
			pass
		if root.find('OrgName_lineage') is not None:
			self.orgname_lineage = OrgName_lineage( root.find('OrgName_lineage') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_molinfo( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_molinfo, self ).__init__()
		self.name = 'Seqdesc_molinfo'
		self.molinfo = MolInfo( root.find('MolInfo') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_xref_dbname_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_xref_dbname_, self ).__init__()
		self.name = 'EMBL-xref_dbname'
		self.embl_dbname_ = EMBL_dbname_( root.find('EMBL-dbname') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_data_complex_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_data_complex_, self ).__init__()
		self.name = 'Variation-ref_data_complex'
		self.text = root.text
	
	def __call__( self ):
		pass


class InferenceSupport_category( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( InferenceSupport_category, self ).__init__()
		self.name = 'InferenceSupport_category'
		self.evidencecategory = EvidenceCategory( root.find('EvidenceCategory') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_het( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_het, self ).__init__()
		self.name = 'Seqdesc_het'
		self.heterogen = Heterogen( root.find('Heterogen') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_numval_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_numval_, self ).__init__()
		self.name = 'Seq-graph_numval'
		self.text = root.text
	
	def __call__( self ):
		pass


class Align_def_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Align_def_ids_, self ).__init__()
		self.name = 'Align-def_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_db_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_db_, self ).__init__()
		self.name = 'Prot-ref_db'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_consequence_E_splicing_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_splicing_, self ).__init__()
		self.name = 'Variation-ref_consequence_E_splicing'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annotdesc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annotdesc, self ).__init__()
		self.name = 'Annotdesc'
		#jedna z opcji dla ['Annotdesc_pub', 'Annotdesc_user', 'Annotdesc_name', 'Annotdesc_src', 'Annotdesc_title', 'Annotdesc_comment', 'Annotdesc_update-date', 'Annotdesc_create-date', 'Annotdesc_region', 'Annotdesc_align']
		if 'Annotdesc_pub' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_pub = Annotdesc_pub( root.find('Annotdesc_pub') )
		elif 'Annotdesc_user' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_user = Annotdesc_user( root.find('Annotdesc_user') )
		elif 'Annotdesc_name' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_name = Annotdesc_name( root.find('Annotdesc_name') )
		elif 'Annotdesc_src' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_src = Annotdesc_src( root.find('Annotdesc_src') )
		elif 'Annotdesc_title' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_title = Annotdesc_title( root.find('Annotdesc_title') )
		elif 'Annotdesc_comment' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_comment = Annotdesc_comment( root.find('Annotdesc_comment') )
		elif 'Annotdesc_update-date' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_update_date_ = Annotdesc_update_date_( root.find('Annotdesc_update-date') )
		elif 'Annotdesc_create-date' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_create_date_ = Annotdesc_create_date_( root.find('Annotdesc_create-date') )
		elif 'Annotdesc_region' in [ x.tag for x in root.getchildren() ]:
			self.annotdesc_region = Annotdesc_region( root.find('Annotdesc_region') )
		else:
			self.annotdesc_align = Annotdesc_align( root.find('Annotdesc_align') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_object_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_field_data_object_, self ).__init__()
		self.name = 'User-field_data_object'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.user_object_ = root.find( 'User-object' )
		self.to_evaluate.append( ( 'User-object', '' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_fuzz_p_m__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_p_m__, self ).__init__()
		self.name = 'Int-fuzz_p-m'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seqpnt_points_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seqpnt_points_, self ).__init__()
		self.name = 'Packed-seqpnt_points'
		if root.find('Packed-seqpnt_points_E') is not None:
			self.packed_seqpnt_points_e_ = [ Packed_seqpnt_points_E_(element) for element in root.findall('Packed-seqpnt_points_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_het( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_het, self ).__init__()
		self.name = 'SeqFeatData_het'
		self.heterogen = Heterogen( root.find('Heterogen') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BioSource_org( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	def __init__( self, root ):
		super( BioSource_org, self ).__init__()
		self.name = 'BioSource_org'
		self.org_ref_ = Org_ref_( root.find('Org-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EvidenceBasis( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( EvidenceBasis, self ).__init__()
		self.name = 'EvidenceBasis'
		if root.find('EvidenceBasis_programs') is not None:
			self.evidencebasis_programs = EvidenceBasis_programs( root.find('EvidenceBasis_programs') )
		else:
			pass
		if root.find('EvidenceBasis_accessions') is not None:
			self.evidencebasis_accessions = EvidenceBasis_accessions( root.find('EvidenceBasis_accessions') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Phenotype_xref( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Phenotype_xref, self ).__init__()
		self.name = 'Phenotype_xref'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Org_ref_db_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_db_, self ).__init__()
		self.name = 'Org-ref_db'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_pages_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_pages_, self ).__init__()
		self.name = 'Cit-gen_pages'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_real_units_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_real_units_, self ).__init__()
		self.name = 'Num-real_units'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_org( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_org, self ).__init__()
		self.name = 'Seqdesc_org'
		self.org_ref_ = Org_ref_( root.find('Org-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_item_action_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Delta_item_action_, self ).__init__()
		self.name = 'Delta-item_action'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['morph', 'offset', 'del-at', 'ins-before']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seq_loc_bond_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_bond_, self ).__init__()
		self.name = 'Seq-loc_bond'
		self.seq_bond_ = Seq_bond_( root.find('Seq-bond') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_jour_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_jour_title_, self ).__init__()
		self.name = 'Cit-jour_title'
		self.title = Title( root.find('Title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Score_value_real( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Score_value_real, self ).__init__()
		self.name = 'Score_value_real'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pubdesc_pub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Pubdesc_pub, self ).__init__()
		self.name = 'Pubdesc_pub'
		self.pub_equiv_ = Pub_equiv_( root.find('Pub-equiv') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_int_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_int_E__, self ).__init__()
		self.name = 'SeqTable-multi-data_int_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Title_E( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E, self ).__init__()
		self.name = 'Title_E'
		#jedna z opcji dla ['Title_E_issn', 'Title_E_iso-jta', 'Title_E_tsub', 'Title_E_jta', 'Title_E_trans', 'Title_E_coden', 'Title_E_ml-jta', 'Title_E_abr', 'Title_E_name', 'Title_E_isbn']
		if 'Title_E_issn' in [ x.tag for x in root.getchildren() ]:
			self.title_e_issn = Title_E_issn( root.find('Title_E_issn') )
		elif 'Title_E_iso-jta' in [ x.tag for x in root.getchildren() ]:
			self.title_e_iso_jta_ = Title_E_iso_jta_( root.find('Title_E_iso-jta') )
		elif 'Title_E_tsub' in [ x.tag for x in root.getchildren() ]:
			self.title_e_tsub = Title_E_tsub( root.find('Title_E_tsub') )
		elif 'Title_E_jta' in [ x.tag for x in root.getchildren() ]:
			self.title_e_jta = Title_E_jta( root.find('Title_E_jta') )
		elif 'Title_E_trans' in [ x.tag for x in root.getchildren() ]:
			self.title_e_trans = Title_E_trans( root.find('Title_E_trans') )
		elif 'Title_E_coden' in [ x.tag for x in root.getchildren() ]:
			self.title_e_coden = Title_E_coden( root.find('Title_E_coden') )
		elif 'Title_E_ml-jta' in [ x.tag for x in root.getchildren() ]:
			self.title_e_ml_jta_ = Title_E_ml_jta_( root.find('Title_E_ml-jta') )
		elif 'Title_E_abr' in [ x.tag for x in root.getchildren() ]:
			self.title_e_abr = Title_E_abr( root.find('Title_E_abr') )
		elif 'Title_E_name' in [ x.tag for x in root.getchildren() ]:
			self.title_e_name = Title_E_name( root.find('Title_E_name') )
		else:
			self.title_e_isbn = Title_E_isbn( root.find('Title_E_isbn') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_seq_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Delta_seq_loc_, self ).__init__()
		self.name = 'Delta-seq_loc'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_tpe_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_tpe_, self ).__init__()
		self.name = 'Seq-id_tpe'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatXref_id( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatXref_id, self ).__init__()
		self.name = 'SeqFeatXref_id'
		self.feat_id_ = Feat_id_( root.find('Feat-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_interval_to_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_interval_to_, self ).__init__()
		self.name = 'Seq-interval_to'
		self.text = root.text
	
	def __call__( self ):
		pass


class Dense_diag_starts_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_diag_starts_, self ).__init__()
		self.name = 'Dense-diag_starts'
		if root.find('Dense-diag_starts_E') is not None:
			self.dense_diag_starts_e_ = [ Dense_diag_starts_E_(element) for element in root.findall('Dense-diag_starts_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_gap_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_gap_, self ).__init__()
		self.name = 'Seq-data_gap'
		self.seq_gap_ = Seq_gap_( root.find('Seq-gap') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_number_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_number_, self ).__init__()
		self.name = 'Cit-pat_number'
		self.text = root.text
	
	def __call__( self ):
		pass


class Txinit( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	def __init__( self, root ):
		super( Txinit, self ).__init__()
		self.name = 'Txinit'
		if root.find('Txinit_location-accurate') is not None:
			self.txinit_location_accurate_ = Txinit_location_accurate_( root.find('Txinit_location-accurate') )
		else:
			pass
		if root.find('Txinit_mapping-precise') is not None:
			self.txinit_mapping_precise_ = Txinit_mapping_precise_( root.find('Txinit_mapping-precise') )
		else:
			pass
		if root.find('Txinit_inittype') is not None:
			self.txinit_inittype = Txinit_inittype( root.find('Txinit_inittype') )
		else:
			pass
		self.txinit_txsystem = Txinit_txsystem( root.find('Txinit_txsystem') )
		if root.find('Txinit_txorg') is not None:
			self.txinit_txorg = Txinit_txorg( root.find('Txinit_txorg') )
		else:
			pass
		if root.find('Txinit_rna') is not None:
			self.txinit_rna = Txinit_rna( root.find('Txinit_rna') )
		else:
			pass
		if root.find('Txinit_evidence') is not None:
			self.txinit_evidence = Txinit_evidence( root.find('Txinit_evidence') )
		else:
			pass
		if root.find('Txinit_expression') is not None:
			self.txinit_expression = Txinit_expression( root.find('Txinit_expression') )
		else:
			pass
		if root.find('Txinit_gene') is not None:
			self.txinit_gene = Txinit_gene( root.find('Txinit_gene') )
		else:
			pass
		self.txinit_name = Txinit_name( root.find('Txinit_name') )
		if root.find('Txinit_protein') is not None:
			self.txinit_protein = Txinit_protein( root.find('Txinit_protein') )
		else:
			pass
		if root.find('Txinit_txdescr') is not None:
			self.txinit_txdescr = Txinit_txdescr( root.find('Txinit_txdescr') )
		else:
			pass
		if root.find('Txinit_syn') is not None:
			self.txinit_syn = Txinit_syn( root.find('Txinit_syn') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_name_binomial( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_name_binomial, self ).__init__()
		self.name = 'OrgName_name_binomial'
		self.binomialorgname = BinomialOrgName( root.find('BinomialOrgName') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_section( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_section, self ).__init__()
		self.name = 'Imprint_section'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_align_segs_packed_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_packed_, self ).__init__()
		self.name = 'Seq-align_segs_packed'
		self.packed_seg_ = Packed_seg_( root.find('Packed-seg') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_medline_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_medline_, self ).__init__()
		self.name = 'Pub-set_medline'
		if root.find('Medline-entry') is not None:
			self.medline_entry_ = [ Medline_entry_(element) for element in root.findall('Medline-entry') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SubSource_subtype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SubSource_subtype, self ).__init__()
		self.name = 'SubSource_subtype'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['chromosome', 'map', 'clone', 'subclone', 'haplotype', 'genotype', 'sex', 'cell-line', 'cell-type', 'tissue-type', 'clone-lib', 'dev-stage', 'frequency', 'germline', 'rearranged', 'lab-host', 'pop-variant', 'tissue-lib', 'plasmid-name', 'transposon-name', 'insertion-seq-name', 'plastid-name', 'country', 'segment', 'endogenous-virus-name', 'transgenic', 'environmental-sample', 'isolation-source', 'lat-lon', 'collection-date', 'collected-by', 'identified-by', 'fwd-primer-seq', 'rev-primer-seq', 'fwd-primer-name', 'rev-primer-name', 'metagenomic', 'mating-type', 'linkage-group', 'haplogroup', 'whole-replicon', 'phenotype', 'altitude', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Variation_ref_consequence_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_consequence_, self ).__init__()
		self.name = 'Variation-ref_consequence'
		if root.find('Variation-ref_consequence_E') is not None:
			self.variation_ref_consequence_e_ = [ Variation_ref_consequence_E_(element) for element in root.findall('Variation-ref_consequence_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_deleted_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_hist_deleted_date_, self ).__init__()
		self.name = 'Seq-hist_deleted_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class NCBIpaa( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBIpaa, self ).__init__()
		self.name = 'NCBIpaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_std_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_, self ).__init__()
		self.name = 'Date-std'
		if root.find('Date-std_month') is not None:
			self.date_std_month_ = Date_std_month_( root.find('Date-std_month') )
		else:
			pass
		if root.find('Date-std_hour') is not None:
			self.date_std_hour_ = Date_std_hour_( root.find('Date-std_hour') )
		else:
			pass
		self.date_std_year_ = Date_std_year_( root.find('Date-std_year') )
		if root.find('Date-std_season') is not None:
			self.date_std_season_ = Date_std_season_( root.find('Date-std_season') )
		else:
			pass
		if root.find('Date-std_minute') is not None:
			self.date_std_minute_ = Date_std_minute_( root.find('Date-std_minute') )
		else:
			pass
		if root.find('Date-std_second') is not None:
			self.date_std_second_ = Date_std_second_( root.find('Date-std_second') )
		else:
			pass
		if root.find('Date-std_day') is not None:
			self.date_std_day_ = Date_std_day_( root.find('Date-std_day') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_assembly_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_hist_assembly_, self ).__init__()
		self.name = 'Seq-hist_assembly'
		if root.find('Seq-align') is not None:
			self.seq_align_ = [ Seq_align_(element) for element in root.findall('Seq-align') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId, self ).__init__()
		self.name = 'ArticleId'
		#jedna z opcji dla ['ArticleId_other', 'ArticleId_pmpid', 'ArticleId_medline', 'ArticleId_doi', 'ArticleId_pii', 'ArticleId_pmcpid', 'ArticleId_pmcid', 'ArticleId_pubmed']
		if 'ArticleId_other' in [ x.tag for x in root.getchildren() ]:
			self.articleid_other = ArticleId_other( root.find('ArticleId_other') )
		elif 'ArticleId_pmpid' in [ x.tag for x in root.getchildren() ]:
			self.articleid_pmpid = ArticleId_pmpid( root.find('ArticleId_pmpid') )
		elif 'ArticleId_medline' in [ x.tag for x in root.getchildren() ]:
			self.articleid_medline = ArticleId_medline( root.find('ArticleId_medline') )
		elif 'ArticleId_doi' in [ x.tag for x in root.getchildren() ]:
			self.articleid_doi = ArticleId_doi( root.find('ArticleId_doi') )
		elif 'ArticleId_pii' in [ x.tag for x in root.getchildren() ]:
			self.articleid_pii = ArticleId_pii( root.find('ArticleId_pii') )
		elif 'ArticleId_pmcpid' in [ x.tag for x in root.getchildren() ]:
			self.articleid_pmcpid = ArticleId_pmcpid( root.find('ArticleId_pmcpid') )
		elif 'ArticleId_pmcid' in [ x.tag for x in root.getchildren() ]:
			self.articleid_pmcid = ArticleId_pmcid( root.find('ArticleId_pmcid') )
		else:
			self.articleid_pubmed = ArticleId_pubmed( root.find('ArticleId_pubmed') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SubSource_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SubSource_name, self ).__init__()
		self.name = 'SubSource_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Trna_ext_codon_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_codon_, self ).__init__()
		self.name = 'Trna-ext_codon'
		if root.find('Trna-ext_codon_E') is not None:
			self.trna_ext_codon_e_ = [ Trna_ext_codon_E_(element) for element in root.findall('Trna-ext_codon_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Num_enum_num_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_enum_num_, self ).__init__()
		self.name = 'Num-enum_num'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_validated_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_validated_, self ).__init__()
		self.name = 'Variation-ref_validated'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class ArticleId_pubmed( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_pubmed, self ).__init__()
		self.name = 'ArticleId_pubmed'
		self.pubmedid = PubMedId( root.find('PubMedId') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annotdesc_pub( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annotdesc_pub, self ).__init__()
		self.name = 'Annotdesc_pub'
		self.pubdesc = Pubdesc( root.find('Pubdesc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_rec__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_hist_rec__, self ).__init__()
		self.name = 'Seq-hist-rec'
		self.seq_hist_rec_ids__ = Seq_hist_rec_ids__( root.find('Seq-hist-rec_ids') )
		if root.find('Seq-hist-rec_date') is not None:
			self.seq_hist_rec_date__ = Seq_hist_rec_date__( root.find('Seq-hist-rec_date') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_data_graph_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_graph_, self ).__init__()
		self.name = 'Seq-annot_data_graph'
		if root.find('Seq-graph') is not None:
			self.seq_graph_ = [ Seq_graph_(element) for element in root.findall('Seq-graph') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_bond_a_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_bond_a_, self ).__init__()
		self.name = 'Seq-bond_a'
		self.seq_point_ = Seq_point_( root.find('Seq-point') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_class_, self ).__init__()
		self.name = 'Cit-pat_class'
		if root.find('Cit-pat_class_E') is not None:
			self.cit_pat_class_e_ = [ Cit_pat_class_E_(element) for element in root.findall('Cit-pat_class_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_ext_delta_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_ext_delta_, self ).__init__()
		self.name = 'Seq-ext_delta'
		self.delta_ext_ = Delta_ext_( root.find('Delta-ext') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Patent_priority_number_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_priority_number_, self ).__init__()
		self.name = 'Patent-priority_number'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_street( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_street, self ).__init__()
		self.name = 'Affil_std_street'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_align_first_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Sparse_align_first_id__, self ).__init__()
		self.name = 'Sparse-align_first-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_gene( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_gene, self ).__init__()
		self.name = 'SeqFeatData_gene'
		self.gene_ref_ = Gene_ref_( root.find('Gene-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonString_table_strings_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonString_table_strings_E_, self ).__init__()
		self.name = 'CommonString-table_strings_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_ext_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_ext_ref_, self ).__init__()
		self.name = 'Seq-ext_ref'
		self.ref_ext_ = Ref_ext_( root.find('Ref-ext') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_diag_starts_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_diag_starts_E_, self ).__init__()
		self.name = 'Dense-diag_starts_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceSupport_dbxref( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceSupport_dbxref, self ).__init__()
		self.name = 'ModelEvidenceSupport_dbxref'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_general_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_general_, self ).__init__()
		self.name = 'Seq-id_general'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc, self ).__init__()
		self.name = 'Seqdesc'
		#jedna z opcji dla ['Seqdesc_prf', 'Seqdesc_pir', 'Seqdesc_molinfo', 'Seqdesc_sp', 'Seqdesc_update-date', 'Seqdesc_modif', 'Seqdesc_org', 'Seqdesc_dbxref', 'Seqdesc_maploc', 'Seqdesc_mol-type', 'Seqdesc_pdb', 'Seqdesc_num', 'Seqdesc_embl', 'Seqdesc_user', 'Seqdesc_create-date', 'Seqdesc_pub', 'Seqdesc_source', 'Seqdesc_title', 'Seqdesc_region', 'Seqdesc_het', 'Seqdesc_genbank', 'Seqdesc_modelev', 'Seqdesc_comment', 'Seqdesc_name', 'Seqdesc_method']
		if 'Seqdesc_prf' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_prf = Seqdesc_prf( root.find('Seqdesc_prf') )
		elif 'Seqdesc_pir' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_pir = Seqdesc_pir( root.find('Seqdesc_pir') )
		elif 'Seqdesc_molinfo' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_molinfo = Seqdesc_molinfo( root.find('Seqdesc_molinfo') )
		elif 'Seqdesc_sp' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_sp = Seqdesc_sp( root.find('Seqdesc_sp') )
		elif 'Seqdesc_update-date' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_update_date_ = Seqdesc_update_date_( root.find('Seqdesc_update-date') )
		elif 'Seqdesc_modif' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_modif = Seqdesc_modif( root.find('Seqdesc_modif') )
		elif 'Seqdesc_org' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_org = Seqdesc_org( root.find('Seqdesc_org') )
		elif 'Seqdesc_dbxref' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_dbxref = Seqdesc_dbxref( root.find('Seqdesc_dbxref') )
		elif 'Seqdesc_maploc' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_maploc = Seqdesc_maploc( root.find('Seqdesc_maploc') )
		elif 'Seqdesc_mol-type' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_mol_type_ = Seqdesc_mol_type_( root.find('Seqdesc_mol-type') )
		elif 'Seqdesc_pdb' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_pdb = Seqdesc_pdb( root.find('Seqdesc_pdb') )
		elif 'Seqdesc_num' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_num = Seqdesc_num( root.find('Seqdesc_num') )
		elif 'Seqdesc_embl' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_embl = Seqdesc_embl( root.find('Seqdesc_embl') )
		elif 'Seqdesc_user' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_user = Seqdesc_user( root.find('Seqdesc_user') )
		elif 'Seqdesc_create-date' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_create_date_ = Seqdesc_create_date_( root.find('Seqdesc_create-date') )
		elif 'Seqdesc_pub' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_pub = Seqdesc_pub( root.find('Seqdesc_pub') )
		elif 'Seqdesc_source' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_source = Seqdesc_source( root.find('Seqdesc_source') )
		elif 'Seqdesc_title' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_title = Seqdesc_title( root.find('Seqdesc_title') )
		elif 'Seqdesc_region' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_region = Seqdesc_region( root.find('Seqdesc_region') )
		elif 'Seqdesc_het' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_het = Seqdesc_het( root.find('Seqdesc_het') )
		elif 'Seqdesc_genbank' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_genbank = Seqdesc_genbank( root.find('Seqdesc_genbank') )
		elif 'Seqdesc_modelev' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_modelev = Seqdesc_modelev( root.find('Seqdesc_modelev') )
		elif 'Seqdesc_comment' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_comment = Seqdesc_comment( root.find('Seqdesc_comment') )
		elif 'Seqdesc_name' in [ x.tag for x in root.getchildren() ]:
			self.seqdesc_name = Seqdesc_name( root.find('Seqdesc_name') )
		else:
			self.seqdesc_method = Seqdesc_method( root.find('Seqdesc_method') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_swissprot_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_swissprot_, self ).__init__()
		self.name = 'Seq-id_swissprot'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_rna_E( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_rna_E, self ).__init__()
		self.name = 'Txinit_rna_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_graph_a_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_a_, self ).__init__()
		self.name = 'Seq-graph_a'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_inst_mol_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_mol_, self ).__init__()
		self.name = 'Seq-inst_mol'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'dna', 'rna', 'aa', 'na', 'other']
		self.value = root.get('value')


class Cit_pat_doc_type__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_doc_type__, self ).__init__()
		self.name = 'Cit-pat_doc-type'
		self.text = root.text
	
	def __call__( self ):
		pass


class Patent_priority_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_priority_date_, self ).__init__()
		self.name = 'Patent-priority_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_sub_imp_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_sub_imp_, self ).__init__()
		self.name = 'Cit-sub_imp'
		self.imprint = Imprint( root.find('Imprint') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_strands_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_strands_, self ).__init__()
		self.name = 'Dense-seg_strands'
		if root.find('Na-strand') is not None:
			self.na_strand_ = [ Na_strand_(element) for element in root.findall('Na-strand') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_starts_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_starts_E_, self ).__init__()
		self.name = 'Dense-seg_starts_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class PmcID( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PmcID, self ).__init__()
		self.name = 'PmcID'
		self.text = root.text
	
	def __call__( self ):
		pass


class Product_pos_protpos_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Product_pos_protpos_, self ).__init__()
		self.name = 'Product-pos_protpos'
		self.prot_pos_ = Prot_pos_( root.find('Prot-pos') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CitRetract( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CitRetract, self ).__init__()
		self.name = 'CitRetract'
		self.citretract_type = CitRetract_type( root.find('CitRetract_type') )
		if root.find('CitRetract_exp') is not None:
			self.citretract_exp = CitRetract_exp( root.find('CitRetract_exp') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pubdesc_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_name, self ).__init__()
		self.name = 'Pubdesc_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class ExperimentSupport_category( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ExperimentSupport_category, self ).__init__()
		self.name = 'ExperimentSupport_category'
		self.evidencecategory = EvidenceCategory( root.find('EvidenceCategory') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class DOI( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( DOI, self ).__init__()
		self.name = 'DOI'
		self.text = root.text
	
	def __call__( self ):
		pass


class Genetic_code_E_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_name_, self ).__init__()
		self.name = 'Genetic-code_E_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_inst_delta_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_inst_delta_, self ).__init__()
		self.name = 'Variation-inst_delta'
		if root.find('Delta-item') is not None:
			self.delta_item_ = [ Delta_item_(element) for element in root.findall('Delta-item') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_attrib( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_attrib, self ).__init__()
		self.name = 'OrgName_attrib'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gb_qual_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gb_qual_qual_, self ).__init__()
		self.name = 'Gb-qual_qual'
		self.text = root.text
	
	def __call__( self ):
		pass


class BinomialOrgName_species( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BinomialOrgName_species, self ).__init__()
		self.name = 'BinomialOrgName_species'
		self.text = root.text
	
	def __call__( self ):
		pass


class PDB_block_compound_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_compound_E_, self ).__init__()
		self.name = 'PDB-block_compound_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class GB_block_keywords_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_keywords_E_, self ).__init__()
		self.name = 'GB-block_keywords_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cdregion_mismatch( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_mismatch, self ).__init__()
		self.name = 'Cdregion_mismatch'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pubdesc_numexc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pubdesc_numexc, self ).__init__()
		self.name = 'Pubdesc_numexc'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Person_id_dbtag_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Person_id_dbtag_, self ).__init__()
		self.name = 'Person-id_dbtag'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_evidence( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_evidence, self ).__init__()
		self.name = 'Txinit_evidence'
		if root.find('Tx-evidence') is not None:
			self.tx_evidence_ = [ Tx_evidence_(element) for element in root.findall('Tx-evidence') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class TaxElement_level( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( TaxElement_level, self ).__init__()
		self.name = 'TaxElement_level'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_field_data_oss_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_oss_E_, self ).__init__()
		self.name = 'User-field_data_oss_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_tpg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_tpg_, self ).__init__()
		self.name = 'Seq-id_tpg'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Std_seg_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Std_seg_ids_, self ).__init__()
		self.name = 'Std-seg_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceItem_full_length_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceItem_full_length_, self ).__init__()
		self.name = 'ModelEvidenceItem_full-length'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Name_std_initials_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_initials_, self ).__init__()
		self.name = 'Name-std_initials'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_book_authors_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_book_authors_, self ).__init__()
		self.name = 'Cit-book_authors'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Meeting( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Meeting, self ).__init__()
		self.name = 'Meeting'
		if root.find('Meeting_place') is not None:
			self.meeting_place = Meeting_place( root.find('Meeting_place') )
		else:
			pass
		self.meeting_number = Meeting_number( root.find('Meeting_number') )
		self.meeting_date = Meeting_date( root.find('Meeting_date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_graph_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_graph_, self ).__init__()
		self.name = 'Int-graph'
		self.int_graph_max_ = Int_graph_max_( root.find('Int-graph_max') )
		self.int_graph_axis_ = Int_graph_axis_( root.find('Int-graph_axis') )
		self.int_graph_min_ = Int_graph_min_( root.find('Int-graph_min') )
		self.int_graph_values_ = Int_graph_values_( root.find('Int-graph_values') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_inst( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Bioseq_inst, self ).__init__()
		self.name = 'Bioseq_inst'
		self.seq_inst_ = Seq_inst_( root.find('Seq-inst') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seg_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Packed_seg_ids_, self ).__init__()
		self.name = 'Packed-seg_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonString_table_indexes_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonString_table_indexes_, self ).__init__()
		self.name = 'CommonString-table_indexes'
		if root.find('CommonString-table_indexes_E') is not None:
			self.commonstring_table_indexes_e_ = [ CommonString_table_indexes_E_(element) for element in root.findall('CommonString-table_indexes_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_superfamily_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_superfamily_, self ).__init__()
		self.name = 'PIR-block_superfamily'
		self.text = root.text
	
	def __call__( self ):
		pass


class RNA_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_qual_, self ).__init__()
		self.name = 'RNA-qual'
		self.rna_qual_qual_ = RNA_qual_qual_( root.find('RNA-qual_qual') )
		self.rna_qual_val_ = RNA_qual_val_( root.find('RNA-qual_val') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_graph_values_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_graph_values_, self ).__init__()
		self.name = 'Int-graph_values'
		if root.find('Int-graph_values_E') is not None:
			self.int_graph_values_e_ = [ Int_graph_values_E_(element) for element in root.findall('Int-graph_values_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatSupport( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatSupport, self ).__init__()
		self.name = 'SeqFeatSupport'
		if root.find('SeqFeatSupport_inference') is not None:
			self.seqfeatsupport_inference = SeqFeatSupport_inference( root.find('SeqFeatSupport_inference') )
		else:
			pass
		if root.find('SeqFeatSupport_experiment') is not None:
			self.seqfeatsupport_experiment = SeqFeatSupport_experiment( root.find('SeqFeatSupport_experiment') )
		else:
			pass
		if root.find('SeqFeatSupport_model-evidence') is not None:
			self.seqfeatsupport_model_evidence_ = SeqFeatSupport_model_evidence_( root.find('SeqFeatSupport_model-evidence') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_description_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_description_, self ).__init__()
		self.name = 'Variation-ref_description'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_region( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_region, self ).__init__()
		self.name = 'Seqdesc_region'
		self.text = root.text
	
	def __call__( self ):
		pass


class InferenceSupport_same_species_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( InferenceSupport_same_species_, self ).__init__()
		self.name = 'InferenceSupport_same-species'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Genetic_code_E_sncbi8aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_sncbi8aa_, self ).__init__()
		self.name = 'Genetic-code_E_sncbi8aa'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_field_data_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_str_, self ).__init__()
		self.name = 'User-field_data_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_region( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_region, self ).__init__()
		self.name = 'SeqFeatData_region'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_inst_fuzz_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_fuzz_, self ).__init__()
		self.name = 'Seq-inst_fuzz'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_variant_prop__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_variant_prop__, self ).__init__()
		self.name = 'Variation-ref_variant-prop'
		self.variantproperties = VariantProperties( root.find('VariantProperties') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EvidenceBasis_accessions( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( EvidenceBasis_accessions, self ).__init__()
		self.name = 'EvidenceBasis_accessions'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Real_graph_max_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Real_graph_max_, self ).__init__()
		self.name = 'Real-graph_max'
		self.text = root.text
	
	def __call__( self ):
		pass


class VariantProperties_quality_check_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_quality_check_, self ).__init__()
		self.name = 'VariantProperties_quality-check'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['contig-allele-missing', 'withdrawn-by-submitter', 'non-overlapping-alleles', 'strain-specific', 'genotype-conflict']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Sparse_align_seg_scores__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_seg_scores__, self ).__init__()
		self.name = 'Sparse-align_seg-scores'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_xref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_xref_, self ).__init__()
		self.name = 'EMBL-xref'
		self.embl_xref_dbname_ = EMBL_xref_dbname_( root.find('EMBL-xref_dbname') )
		self.embl_xref_id_ = EMBL_xref_id_( root.find('EMBL-xref_id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_numseg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_numseg_, self ).__init__()
		self.name = 'Dense-seg_numseg'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_pseudo_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_pseudo_, self ).__init__()
		self.name = 'Seq-feat_pseudo'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Prot_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_, self ).__init__()
		self.name = 'Prot-ref'
		if root.find('Prot-ref_processed') is not None:
			self.prot_ref_processed_ = Prot_ref_processed_( root.find('Prot-ref_processed') )
		else:
			pass
		if root.find('Prot-ref_name') is not None:
			self.prot_ref_name_ = Prot_ref_name_( root.find('Prot-ref_name') )
		else:
			pass
		if root.find('Prot-ref_desc') is not None:
			self.prot_ref_desc_ = Prot_ref_desc_( root.find('Prot-ref_desc') )
		else:
			pass
		if root.find('Prot-ref_activity') is not None:
			self.prot_ref_activity_ = Prot_ref_activity_( root.find('Prot-ref_activity') )
		else:
			pass
		if root.find('Prot-ref_ec') is not None:
			self.prot_ref_ec_ = Prot_ref_ec_( root.find('Prot-ref_ec') )
		else:
			pass
		if root.find('Prot-ref_db') is not None:
			self.prot_ref_db_ = Prot_ref_db_( root.find('Prot-ref_db') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PCRPrimer_seq( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRPrimer_seq, self ).__init__()
		self.name = 'PCRPrimer_seq'
		self.pcrprimerseq = PCRPrimerSeq( root.find('PCRPrimerSeq') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class NCBIpna( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBIpna, self ).__init__()
		self.name = 'NCBIpna'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seg_present_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_present_, self ).__init__()
		self.name = 'Packed-seg_present'
		self.text = root.text
	
	def __call__( self ):
		pass


class Affil_std_city( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_city, self ).__init__()
		self.name = 'Affil_std_city'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_uid_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_uid_, self ).__init__()
		self.name = 'Medline-entry_uid'
		self.text = root.text
	
	def __call__( self ):
		pass


class Int_graph_values_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_graph_values_E_, self ).__init__()
		self.name = 'Int-graph_values_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Bioseq_set_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Bioseq_set_, self ).__init__()
		self.name = 'Bioseq-set'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		if root.find('Bioseq-set_class') is not None:
			self.bioseq_set_class_ = Bioseq_set_class_( root.find('Bioseq-set_class') )
		else:
			pass
		if root.find('Bioseq-set_id') is not None:
			self.bioseq_set_id_ = Bioseq_set_id_( root.find('Bioseq-set_id') )
		else:
			pass
		if root.find('Bioseq-set_coll') is not None:
			self.bioseq_set_coll_ = Bioseq_set_coll_( root.find('Bioseq-set_coll') )
		else:
			pass
		if root.find('Bioseq-set_level') is not None:
			self.bioseq_set_level_ = Bioseq_set_level_( root.find('Bioseq-set_level') )
		else:
			pass
		if root.find('Bioseq-set_release') is not None:
			self.bioseq_set_release_ = Bioseq_set_release_( root.find('Bioseq-set_release') )
		else:
			pass
		if root.find('Bioseq-set_date') is not None:
			self.bioseq_set_date_ = Bioseq_set_date_( root.find('Bioseq-set_date') )
		else:
			pass
		if root.find('Bioseq-set_descr') is not None:
			self.bioseq_set_descr_ = Bioseq_set_descr_( root.find('Bioseq-set_descr') )
		else:
			pass
		if root.find('Bioseq-set_annot') is not None:
			self.bioseq_set_annot_ = Bioseq_set_annot_( root.find('Bioseq-set_annot') )
		else:
			pass
		self.bioseq_set_seq_set__ = root.find( 'Bioseq-set_seq-set' )
		self.to_evaluate.append( ( 'Bioseq-set_seq-set', '' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_pmid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pub_pmid, self ).__init__()
		self.name = 'Pub_pmid'
		self.pubmedid = PubMedId( root.find('PubMedId') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_let_cit_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_let_cit_, self ).__init__()
		self.name = 'Cit-let_cit'
		self.cit_book_ = Cit_book_( root.find('Cit-book') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_title_, self ).__init__()
		self.name = 'Cit-gen_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_single_data_string__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_single_data_string__, self ).__init__()
		self.name = 'SeqTable-single-data_string'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_interval_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_interval_id_, self ).__init__()
		self.name = 'Seq-interval_id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_pmid_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_pmid_, self ).__init__()
		self.name = 'Medline-entry_pmid'
		self.pubmedid = PubMedId( root.find('PubMedId') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_data_os_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_data_os_, self ).__init__()
		self.name = 'User-field_data_os'
		self.text = root.text
	
	def __call__( self ):
		pass


class SP_block_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_class_, self ).__init__()
		self.name = 'SP-block_class'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'standard', 'prelim', 'other']
		self.value = root.get('value')


class EMBL_block_keywords_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_keywords_E_, self ).__init__()
		self.name = 'EMBL-block_keywords_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class OrgName_name_partial( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_name_partial, self ).__init__()
		self.name = 'OrgName_name_partial'
		self.partialorgname = PartialOrgName( root.find('PartialOrgName') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_donor_after_exon___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_donor_after_exon___, self ).__init__()
		self.name = 'Spliced-exon_donor-after-exon'
		self.splice_site_ = Splice_site_( root.find('Splice-site') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonBytes_table_indexes_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonBytes_table_indexes_, self ).__init__()
		self.name = 'CommonBytes-table_indexes'
		if root.find('CommonBytes-table_indexes_E') is not None:
			self.commonbytes_table_indexes_e_ = [ CommonBytes_table_indexes_E_(element) for element in root.findall('CommonBytes-table_indexes_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_equiv_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_equiv_, self ).__init__()
		self.name = 'Pub-equiv'
		if root.find('Pub') is not None:
			self.pub = [ Pub(element) for element in root.findall('Pub') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_null_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_loc_null_, self ).__init__()
		self.name = 'Seq-loc_null'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_sparse_index_bit_set___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_sparse_index_bit_set___, self ).__init__()
		self.name = 'SeqTable-sparse-index_bit-set'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_tpd_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_tpd_, self ).__init__()
		self.name = 'Seq-id_tpd'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_effect( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_effect, self ).__init__()
		self.name = 'VariantProperties_effect'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['no-change', 'synonymous', 'nonsense', 'missense', 'frameshift', 'up-regulator', 'down-regulator', 'methylation', 'stop-gain', 'stop-loss']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class SeqTable_sparse_index_indexes_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_sparse_index_indexes_E__, self ).__init__()
		self.name = 'SeqTable-sparse-index_indexes_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceSupport_exon_length_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceSupport_exon_length_, self ).__init__()
		self.name = 'ModelEvidenceSupport_exon-length'
		self.text = root.text
	
	def __call__( self ):
		pass


class Author_role( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Author_role, self ).__init__()
		self.name = 'Author_role'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['compiler', 'editor', 'patent-assignee', 'translator']
		self.value = root.get('value')


class RNA_qual_set__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_qual_set__, self ).__init__()
		self.name = 'RNA-qual-set'
		if root.find('RNA-qual') is not None:
			self.rna_qual_ = [ RNA_qual_(element) for element in root.findall('RNA-qual') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_column_info_field_name___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_column_info_field_name___, self ).__init__()
		self.name = 'SeqTable-column-info_field-name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Delta_item_seq_literal_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Delta_item_seq_literal_, self ).__init__()
		self.name = 'Delta-item_seq_literal'
		self.seq_literal_ = Seq_literal_( root.find('Seq-literal') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatSupport_inference( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatSupport_inference, self ).__init__()
		self.name = 'SeqFeatSupport_inference'
		if root.find('InferenceSupport') is not None:
			self.inferencesupport = [ InferenceSupport(element) for element in root.findall('InferenceSupport') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Bioseq_set_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Bioseq_set_date_, self ).__init__()
		self.name = 'Bioseq-set_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_, self ).__init__()
		self.name = 'Seq-loc'
		#jedna z opcji dla ['Seq-loc_null', 'Seq-loc_bond', 'Seq-loc_mix', 'Seq-loc_equiv', 'Seq-loc_pnt', 'Seq-loc_packed-int', 'Seq-loc_int', 'Seq-loc_packed-pnt', 'Seq-loc_whole', 'Seq-loc_feat', 'Seq-loc_empty']
		if 'Seq-loc_null' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_null_ = Seq_loc_null_( root.find('Seq-loc_null') )
		elif 'Seq-loc_bond' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_bond_ = Seq_loc_bond_( root.find('Seq-loc_bond') )
		elif 'Seq-loc_mix' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_mix_ = Seq_loc_mix_( root.find('Seq-loc_mix') )
		elif 'Seq-loc_equiv' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_equiv_ = Seq_loc_equiv_( root.find('Seq-loc_equiv') )
		elif 'Seq-loc_pnt' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_pnt_ = Seq_loc_pnt_( root.find('Seq-loc_pnt') )
		elif 'Seq-loc_packed-int' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_packed_int__ = Seq_loc_packed_int__( root.find('Seq-loc_packed-int') )
		elif 'Seq-loc_int' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_int_ = Seq_loc_int_( root.find('Seq-loc_int') )
		elif 'Seq-loc_packed-pnt' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_packed_pnt__ = Seq_loc_packed_pnt__( root.find('Seq-loc_packed-pnt') )
		elif 'Seq-loc_whole' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_whole_ = Seq_loc_whole_( root.find('Seq-loc_whole') )
		elif 'Seq-loc_feat' in [ x.tag for x in root.getchildren() ]:
			self.seq_loc_feat_ = Seq_loc_feat_( root.find('Seq-loc_feat') )
		else:
			self.seq_loc_empty_ = Seq_loc_empty_( root.find('Seq-loc_empty') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_segs_dendiag_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_dendiag_, self ).__init__()
		self.name = 'Seq-align_segs_dendiag'
		if root.find('Dense-diag') is not None:
			self.dense_diag_ = [ Dense_diag_(element) for element in root.findall('Dense-diag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_gene_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_gene_E_, self ).__init__()
		self.name = 'Medline-entry_gene_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class RNA_ref_ext_tRNA_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	def __init__( self, root ):
		super( RNA_ref_ext_tRNA_, self ).__init__()
		self.name = 'RNA-ref_ext_tRNA'
		self.trna_ext_ = Trna_ext_( root.find('Trna-ext') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_source_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_source_, self ).__init__()
		self.name = 'PIR-block_source'
		self.text = root.text
	
	def __call__( self ):
		pass


class PIR_block_keywords_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_keywords_, self ).__init__()
		self.name = 'PIR-block_keywords'
		if root.find('PIR-block_keywords_E') is not None:
			self.pir_block_keywords_e_ = [ PIR_block_keywords_E_(element) for element in root.findall('PIR-block_keywords_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Product_pos_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Product_pos_, self ).__init__()
		self.name = 'Product-pos'
		#jedna z opcji dla ['Product-pos_nucpos', 'Product-pos_protpos']
		if 'Product-pos_nucpos' in [ x.tag for x in root.getchildren() ]:
			self.product_pos_nucpos_ = Product_pos_nucpos_( root.find('Product-pos_nucpos') )
		else:
			self.product_pos_protpos_ = Product_pos_protpos_( root.find('Product-pos_protpos') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_block_extra_acc_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_extra_acc_E__, self ).__init__()
		self.name = 'EMBL-block_extra-acc_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_std_hour_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_hour_, self ).__init__()
		self.name = 'Date-std_hour'
		self.text = root.text
	
	def __call__( self ):
		pass


class PDB_block_deposition_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_deposition_, self ).__init__()
		self.name = 'PDB-block_deposition'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Tx_evidence_expression_system__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Tx_evidence_expression_system__, self ).__init__()
		self.name = 'Tx-evidence_expression-system'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['unknown', 'physiological', 'in-vitro', 'oocyte', 'transfection', 'transgenic', 'other']
		self.value = root.get('value')


class SubSource( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SubSource, self ).__init__()
		self.name = 'SubSource'
		self.subsource_subtype = SubSource_subtype( root.find('SubSource_subtype') )
		if root.find('SubSource_attrib') is not None:
			self.subsource_attrib = SubSource_attrib( root.find('SubSource_attrib') )
		else:
			pass
		self.subsource_name = SubSource_name( root.find('SubSource_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_block_keywords_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_keywords_, self ).__init__()
		self.name = 'EMBL-block_keywords'
		if root.find('EMBL-block_keywords_E') is not None:
			self.embl_block_keywords_e_ = [ EMBL_block_keywords_E_(element) for element in root.findall('EMBL-block_keywords_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Giimport_id_db_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Giimport_id_db_, self ).__init__()
		self.name = 'Giimport-id_db'
		self.text = root.text
	
	def __call__( self ):
		pass


class Prot_pos_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_pos_, self ).__init__()
		self.name = 'Prot-pos'
		if root.find('Prot-pos_frame') is not None:
			self.prot_pos_frame_ = Prot_pos_frame_( root.find('Prot-pos_frame') )
		else:
			pass
		self.prot_pos_amin_ = Prot_pos_amin_( root.find('Prot-pos_amin') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GB_block_div_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_div_, self ).__init__()
		self.name = 'GB-block_div'
		self.text = root.text
	
	def __call__( self ):
		pass


class Auth_list_names_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_names_, self ).__init__()
		self.name = 'Auth-list_names'
		#jedna z opcji dla ['Auth-list_names_ml', 'Auth-list_names_str', 'Auth-list_names_std']
		if 'Auth-list_names_ml' in [ x.tag for x in root.getchildren() ]:
			self.auth_list_names_ml_ = Auth_list_names_ml_( root.find('Auth-list_names_ml') )
		elif 'Auth-list_names_str' in [ x.tag for x in root.getchildren() ]:
			self.auth_list_names_str_ = Auth_list_names_str_( root.find('Auth-list_names_str') )
		else:
			self.auth_list_names_std_ = Auth_list_names_std_( root.find('Auth-list_names_std') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_art_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_art_, self ).__init__()
		self.name = 'Cit-art'
		self.cit_art_from_ = Cit_art_from_( root.find('Cit-art_from') )
		if root.find('Cit-art_title') is not None:
			self.cit_art_title_ = Cit_art_title_( root.find('Cit-art_title') )
		else:
			pass
		if root.find('Cit-art_authors') is not None:
			self.cit_art_authors_ = Cit_art_authors_( root.find('Cit-art_authors') )
		else:
			pass
		if root.find('Cit-art_ids') is not None:
			self.cit_art_ids_ = Cit_art_ids_( root.find('Cit-art_ids') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_scores_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_seg_scores_, self ).__init__()
		self.name = 'Dense-seg_scores'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_ref_concordant_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_ref_concordant_, self ).__init__()
		self.name = 'Clone-ref_concordant'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Medline_si_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_si_, self ).__init__()
		self.name = 'Medline-si'
		self.medline_si_type_ = Medline_si_type_( root.find('Medline-si_type') )
		if root.find('Medline-si_cit') is not None:
			self.medline_si_cit_ = Medline_si_cit_( root.find('Medline-si_cit') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GIBB_method_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GIBB_method_, self ).__init__()
		self.name = 'GIBB-method'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['concept-trans', 'seq-pept', 'both', 'seq-pept-overlap', 'seq-pept-homol', 'concept-trans-a', 'other']
		self.value = root.get('value')


class Cit_pat_country_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_country_, self ).__init__()
		self.name = 'Cit-pat_country'
		self.text = root.text
	
	def __call__( self ):
		pass


class MolInfo_gbmoltype( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MolInfo_gbmoltype, self ).__init__()
		self.name = 'MolInfo_gbmoltype'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_align_second_starts_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_second_starts_E__, self ).__init__()
		self.name = 'Sparse-align_second-starts_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_si_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_si_type_, self ).__init__()
		self.name = 'Medline-si_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['ddbj', 'carbbank', 'embl', 'hdb', 'genbank', 'hgml', 'mim', 'msd', 'pdb', 'pir', 'prfseqdb', 'psd', 'swissprot', 'gdb']
		self.value = root.get('value')


class EMBL_xref_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_xref_id_, self ).__init__()
		self.name = 'EMBL-xref_id'
		if root.find('Object-id') is not None:
			self.object_id_ = [ Object_id_(element) for element in root.findall('Object-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PRF_ExtraSrc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_ExtraSrc_, self ).__init__()
		self.name = 'PRF-ExtraSrc'
		if root.find('PRF-ExtraSrc_strain') is not None:
			self.prf_extrasrc_strain_ = PRF_ExtraSrc_strain_( root.find('PRF-ExtraSrc_strain') )
		else:
			pass
		if root.find('PRF-ExtraSrc_state') is not None:
			self.prf_extrasrc_state_ = PRF_ExtraSrc_state_( root.find('PRF-ExtraSrc_state') )
		else:
			pass
		if root.find('PRF-ExtraSrc_taxon') is not None:
			self.prf_extrasrc_taxon_ = PRF_ExtraSrc_taxon_( root.find('PRF-ExtraSrc_taxon') )
		else:
			pass
		if root.find('PRF-ExtraSrc_part') is not None:
			self.prf_extrasrc_part_ = PRF_ExtraSrc_part_( root.find('PRF-ExtraSrc_part') )
		else:
			pass
		if root.find('PRF-ExtraSrc_host') is not None:
			self.prf_extrasrc_host_ = PRF_ExtraSrc_host_( root.find('PRF-ExtraSrc_host') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_comment( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_comment, self ).__init__()
		self.name = 'Seqdesc_comment'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_id_, self ).__init__()
		self.name = 'Variation-ref_id'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_is_ancestral_allele__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_is_ancestral_allele__, self ).__init__()
		self.name = 'VariantProperties_is-ancestral-allele'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Seq_id_named_annot_track___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_named_annot_track___, self ).__init__()
		self.name = 'Seq-id_named-annot-track'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_genbank( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_genbank, self ).__init__()
		self.name = 'Seqdesc_genbank'
		self.gb_block_ = GB_block_( root.find('GB-block') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BinomialOrgName_genus( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BinomialOrgName_genus, self ).__init__()
		self.name = 'BinomialOrgName_genus'
		self.text = root.text
	
	def __call__( self ):
		pass


class Dense_diag_scores_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dense_diag_scores_, self ).__init__()
		self.name = 'Dense-diag_scores'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_poly_a__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_poly_a__, self ).__init__()
		self.name = 'Spliced-seg_poly-a'
		self.text = root.text
	
	def __call__( self ):
		pass


class PRF_ExtraSrc_taxon_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_ExtraSrc_taxon_, self ).__init__()
		self.name = 'PRF-ExtraSrc_taxon'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_align_lens_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_lens_, self ).__init__()
		self.name = 'Sparse-align_lens'
		if root.find('Sparse-align_lens_E') is not None:
			self.sparse_align_lens_e_ = [ Sparse_align_lens_E_(element) for element in root.findall('Sparse-align_lens_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GB_block_taxonomy_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_taxonomy_, self ).__init__()
		self.name = 'GB-block_taxonomy'
		self.text = root.text
	
	def __call__( self ):
		pass


class Population_data_flags_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_flags_, self ).__init__()
		self.name = 'Population-data_flags'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['is-default-population', 'is-minor-allele', 'is-rare-allele']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class ModelEvidenceSupport_est( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceSupport_est, self ).__init__()
		self.name = 'ModelEvidenceSupport_est'
		if root.find('ModelEvidenceItem') is not None:
			self.modelevidenceitem = [ ModelEvidenceItem(element) for element in root.findall('ModelEvidenceItem') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gene_nomenclature_symbol_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_nomenclature_symbol_, self ).__init__()
		self.name = 'Gene-nomenclature_symbol'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_art_authors_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_art_authors_, self ).__init__()
		self.name = 'Cit-art_authors'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_extra_acc__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_extra_acc__, self ).__init__()
		self.name = 'SP-block_extra-acc'
		if root.find('SP-block_extra-acc_E') is not None:
			self.sp_block_extra_acc_e__ = [ SP_block_extra_acc_E__(element) for element in root.findall('SP-block_extra-acc_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_loc_packed_pnt__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_packed_pnt__, self ).__init__()
		self.name = 'Seq-loc_packed-pnt'
		self.packed_seqpnt_ = Packed_seqpnt_( root.find('Packed-seqpnt') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annotdesc_src( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annotdesc_src, self ).__init__()
		self.name = 'Annotdesc_src'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gene_nomenclature_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_nomenclature_name_, self ).__init__()
		self.name = 'Gene-nomenclature_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_em_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_em_, self ).__init__()
		self.name = 'Medline-entry_em'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties, self ).__init__()
		self.name = 'VariantProperties'
		if root.find('VariantProperties_genotype') is not None:
			self.variantproperties_genotype = VariantProperties_genotype( root.find('VariantProperties_genotype') )
		else:
			pass
		if root.find('VariantProperties_other-validation') is not None:
			self.variantproperties_other_validation_ = VariantProperties_other_validation_( root.find('VariantProperties_other-validation') )
		else:
			pass
		if root.find('VariantProperties_resource-link') is not None:
			self.variantproperties_resource_link_ = VariantProperties_resource_link_( root.find('VariantProperties_resource-link') )
		else:
			pass
		if root.find('VariantProperties_confidence') is not None:
			self.variantproperties_confidence = VariantProperties_confidence( root.find('VariantProperties_confidence') )
		else:
			pass
		if root.find('VariantProperties_mapping') is not None:
			self.variantproperties_mapping = VariantProperties_mapping( root.find('VariantProperties_mapping') )
		else:
			pass
		if root.find('VariantProperties_gene-location') is not None:
			self.variantproperties_gene_location_ = VariantProperties_gene_location_( root.find('VariantProperties_gene-location') )
		else:
			pass
		if root.find('VariantProperties_map-weight') is not None:
			self.variantproperties_map_weight_ = VariantProperties_map_weight_( root.find('VariantProperties_map-weight') )
		else:
			pass
		if root.find('VariantProperties_allele-state') is not None:
			self.variantproperties_allele_state_ = VariantProperties_allele_state_( root.find('VariantProperties_allele-state') )
		else:
			pass
		if root.find('VariantProperties_effect') is not None:
			self.variantproperties_effect = VariantProperties_effect( root.find('VariantProperties_effect') )
		else:
			pass
		if root.find('VariantProperties_quality-check') is not None:
			self.variantproperties_quality_check_ = VariantProperties_quality_check_( root.find('VariantProperties_quality-check') )
		else:
			pass
		if root.find('VariantProperties_allele-origin') is not None:
			self.variantproperties_allele_origin_ = VariantProperties_allele_origin_( root.find('VariantProperties_allele-origin') )
		else:
			pass
		if root.find('VariantProperties_frequency-based-validation') is not None:
			self.variantproperties_frequency_based_validation__ = VariantProperties_frequency_based_validation__( root.find('VariantProperties_frequency-based-validation') )
		else:
			pass
		if root.find('VariantProperties_is-ancestral-allele') is not None:
			self.variantproperties_is_ancestral_allele__ = VariantProperties_is_ancestral_allele__( root.find('VariantProperties_is-ancestral-allele') )
		else:
			pass
		self.variantproperties_version = VariantProperties_version( root.find('VariantProperties_version') )
		if root.find('VariantProperties_project-data') is not None:
			self.variantproperties_project_data_ = VariantProperties_project_data_( root.find('VariantProperties_project-data') )
		else:
			pass
		if root.find('VariantProperties_allele-frequency') is not None:
			self.variantproperties_allele_frequency_ = VariantProperties_allele_frequency_( root.find('VariantProperties_allele-frequency') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_pos_frame_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_pos_frame_, self ).__init__()
		self.name = 'Prot-pos_frame'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_data_uniparental_disomy__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_data_uniparental_disomy__, self ).__init__()
		self.name = 'Variation-ref_data_uniparental-disomy'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_align_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_, self ).__init__()
		self.name = 'Seq-align'
		self.seq_align_type_ = Seq_align_type_( root.find('Seq-align_type') )
		if root.find('Seq-align_ext') is not None:
			self.seq_align_ext_ = Seq_align_ext_( root.find('Seq-align_ext') )
		else:
			pass
		if root.find('Seq-align_score') is not None:
			self.seq_align_score_ = Seq_align_score_( root.find('Seq-align_score') )
		else:
			pass
		if root.find('Seq-align_id') is not None:
			self.seq_align_id_ = Seq_align_id_( root.find('Seq-align_id') )
		else:
			pass
		if root.find('Seq-align_dim') is not None:
			self.seq_align_dim_ = Seq_align_dim_( root.find('Seq-align_dim') )
		else:
			pass
		self.seq_align_segs_ = Seq_align_segs_( root.find('Seq-align_segs') )
		if root.find('Seq-align_bounds') is not None:
			self.seq_align_bounds_ = Seq_align_bounds_( root.find('Seq-align_bounds') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_graph_byte_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_graph_byte_, self ).__init__()
		self.name = 'Seq-graph_graph_byte'
		self.byte_graph_ = Byte_graph_( root.find('Byte-graph') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annotdesc_region( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Annotdesc_region, self ).__init__()
		self.name = 'Annotdesc_region'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_mapping_precise_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_mapping_precise_, self ).__init__()
		self.name = 'Txinit_mapping-precise'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Seq_align_segs_spliced_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_spliced_, self ).__init__()
		self.name = 'Seq-align_segs_spliced'
		self.spliced_seg_ = Spliced_seg_( root.find('Spliced-seg') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_clone( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_clone, self ).__init__()
		self.name = 'SeqFeatData_clone'
		self.clone_ref_ = Clone_ref_( root.find('Clone-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_seg_rows_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Sparse_seg_rows_, self ).__init__()
		self.name = 'Sparse-seg_rows'
		if root.find('Sparse-align') is not None:
			self.sparse_align_ = [ Sparse_align_(element) for element in root.findall('Sparse-align') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BinomialOrgName( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BinomialOrgName, self ).__init__()
		self.name = 'BinomialOrgName'
		self.binomialorgname_genus = BinomialOrgName_genus( root.find('BinomialOrgName_genus') )
		if root.find('BinomialOrgName_species') is not None:
			self.binomialorgname_species = BinomialOrgName_species( root.find('BinomialOrgName_species') )
		else:
			pass
		if root.find('BinomialOrgName_subspecies') is not None:
			self.binomialorgname_subspecies = BinomialOrgName_subspecies( root.find('BinomialOrgName_subspecies') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class NCBI4na( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBI4na, self ).__init__()
		self.name = 'NCBI4na'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_non_std_residue__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_non_std_residue__, self ).__init__()
		self.name = 'SeqFeatData_non-std-residue'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_create_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_create_date_, self ).__init__()
		self.name = 'Seqdesc_create-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_deleted_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_hist_deleted_, self ).__init__()
		self.name = 'Seq-hist_deleted'
		#jedna z opcji dla ['Seq-hist_deleted_date', 'Seq-hist_deleted_bool']
		if 'Seq-hist_deleted_date' in [ x.tag for x in root.getchildren() ]:
			self.seq_hist_deleted_date_ = Seq_hist_deleted_date_( root.find('Seq-hist_deleted_date') )
		else:
			self.seq_hist_deleted_bool_ = Seq_hist_deleted_bool_( root.find('Seq-hist_deleted_bool') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_txorg( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	def __init__( self, root ):
		super( Txinit_txorg, self ).__init__()
		self.name = 'Txinit_txorg'
		self.org_ref_ = Org_ref_( root.find('Org-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_other_ids__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_other_ids__, self ).__init__()
		self.name = 'Variation-ref_other-ids'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Feat_id_giim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Feat_id_giim_, self ).__init__()
		self.name = 'Feat-id_giim'
		self.giimport_id_ = Giimport_id_( root.find('Giimport-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_comment_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_comment_, self ).__init__()
		self.name = 'Seq-feat_comment'
		self.text = root.text
	
	def __call__( self ):
		pass


class Product_pos_nucpos_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Product_pos_nucpos_, self ).__init__()
		self.name = 'Product-pos_nucpos'
		self.text = root.text
	
	def __call__( self ):
		pass


class Org_ref_mod_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_mod_, self ).__init__()
		self.name = 'Org-ref_mod'
		if root.find('Org-ref_mod_E') is not None:
			self.org_ref_mod_e_ = [ Org_ref_mod_E_(element) for element in root.findall('Org-ref_mod_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_set__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_set__, self ).__init__()
		self.name = 'Seq-align-set'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.seq_align_ = root.findall( 'Seq-align' )
		self.to_evaluate.append( ( 'Seq-align', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class RNA_gen_quals_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_gen_quals_, self ).__init__()
		self.name = 'RNA-gen_quals'
		self.rna_qual_set__ = RNA_qual_set__( root.find('RNA-qual-set') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seg_starts_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_starts_, self ).__init__()
		self.name = 'Packed-seg_starts'
		if root.find('Packed-seg_starts_E') is not None:
			self.packed_seg_starts_e_ = [ Packed_seg_starts_E_(element) for element in root.findall('Packed-seg_starts_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Genetic_code_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_, self ).__init__()
		self.name = 'Genetic-code_E'
		#jedna z opcji dla ['Genetic-code_E_ncbi8aa', 'Genetic-code_E_ncbieaa', 'Genetic-code_E_id', 'Genetic-code_E_sncbistdaa', 'Genetic-code_E_name', 'Genetic-code_E_sncbi8aa', 'Genetic-code_E_sncbieaa', 'Genetic-code_E_ncbistdaa']
		if 'Genetic-code_E_ncbi8aa' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_ncbi8aa_ = Genetic_code_E_ncbi8aa_( root.find('Genetic-code_E_ncbi8aa') )
		elif 'Genetic-code_E_ncbieaa' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_ncbieaa_ = Genetic_code_E_ncbieaa_( root.find('Genetic-code_E_ncbieaa') )
		elif 'Genetic-code_E_id' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_id_ = Genetic_code_E_id_( root.find('Genetic-code_E_id') )
		elif 'Genetic-code_E_sncbistdaa' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_sncbistdaa_ = Genetic_code_E_sncbistdaa_( root.find('Genetic-code_E_sncbistdaa') )
		elif 'Genetic-code_E_name' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_name_ = Genetic_code_E_name_( root.find('Genetic-code_E_name') )
		elif 'Genetic-code_E_sncbi8aa' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_sncbi8aa_ = Genetic_code_E_sncbi8aa_( root.find('Genetic-code_E_sncbi8aa') )
		elif 'Genetic-code_E_sncbieaa' in [ x.tag for x in root.getchildren() ]:
			self.genetic_code_e_sncbieaa_ = Genetic_code_E_sncbieaa_( root.find('Genetic-code_E_sncbieaa') )
		else:
			self.genetic_code_e_ncbistdaa_ = Genetic_code_E_ncbistdaa_( root.find('Genetic-code_E_ncbistdaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data_common_bytes___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_common_bytes___, self ).__init__()
		self.name = 'SeqTable-multi-data_common-bytes'
		self.commonbytes_table_ = CommonBytes_table_( root.find('CommonBytes-table') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Txinit_txdescr( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_txdescr, self ).__init__()
		self.name = 'Txinit_txdescr'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_cit_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	def __init__( self, root ):
		super( Medline_entry_cit_, self ).__init__()
		self.name = 'Medline-entry_cit'
		self.cit_art_ = Cit_art_( root.find('Cit-art') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_ml_jta_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_ml_jta_, self ).__init__()
		self.name = 'Title_E_ml-jta'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_giim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_giim_, self ).__init__()
		self.name = 'Seq-id_giim'
		self.giimport_id_ = Giimport_id_( root.find('Giimport-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_comp_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_comp_, self ).__init__()
		self.name = 'Seq-graph_comp'
		self.text = root.text
	
	def __call__( self ):
		pass


class VariantProperties_allele_state_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_allele_state_, self ).__init__()
		self.name = 'VariantProperties_allele-state'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'homozygous', 'heterozygous', 'hemizygous', 'nullizygous', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Pub_pat_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Pub_pat_id_, self ).__init__()
		self.name = 'Pub_pat-id'
		self.id_pat_ = Id_pat_( root.find('Id-pat') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_id_pir_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_pir_, self ).__init__()
		self.name = 'Seq-id_pir'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_rn_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_rn_type_, self ).__init__()
		self.name = 'Medline-rn_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['nameonly', 'cas', 'ec']
		self.value = root.get('value')


class PIR_block_keywords_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_keywords_E_, self ).__init__()
		self.name = 'PIR-block_keywords_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_str( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_str, self ).__init__()
		self.name = 'Date_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub_article( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_article, self ).__init__()
		self.name = 'Pub_article'
		self.cit_art_ = Cit_art_( root.find('Cit-art') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seg_lens_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_lens_E_, self ).__init__()
		self.name = 'Packed-seg_lens_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Genetic_code_E_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_id_, self ).__init__()
		self.name = 'Genetic-code_E_id'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_interval_strand_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_interval_strand_, self ).__init__()
		self.name = 'Seq-interval_strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_id_, self ).__init__()
		self.name = 'Seq-feat_id'
		self.feat_id_ = Feat_id_( root.find('Feat-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_seq_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Delta_seq_, self ).__init__()
		self.name = 'Delta-seq'
		#jedna z opcji dla ['Delta-seq_loc', 'Delta-seq_literal']
		if 'Delta-seq_loc' in [ x.tag for x in root.getchildren() ]:
			self.delta_seq_loc_ = Delta_seq_loc_( root.find('Delta-seq_loc') )
		else:
			self.delta_seq_literal_ = Delta_seq_literal_( root.find('Delta-seq_literal') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId_pii( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_pii, self ).__init__()
		self.name = 'ArticleId_pii'
		self.pii = PII( root.find('PII') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Name_std_first_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_first_, self ).__init__()
		self.name = 'Name-std_first'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_hist_replaced_by__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_hist_replaced_by__, self ).__init__()
		self.name = 'Seq-hist_replaced-by'
		self.seq_hist_rec__ = Seq_hist_rec__( root.find('Seq-hist-rec') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class TaxElement_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( TaxElement_name, self ).__init__()
		self.name = 'TaxElement_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_ref_desc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_desc_, self ).__init__()
		self.name = 'Gene-ref_desc'
		self.text = root.text
	
	def __call__( self ):
		pass


class PDB_block_source_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_source_E_, self ).__init__()
		self.name = 'PDB-block_source_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_field_str_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_field_str_, self ).__init__()
		self.name = 'Medline-field_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_column_info__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_column_info__, self ).__init__()
		self.name = 'SeqTable-column-info'
		if root.find('SeqTable-column-info_field-id') is not None:
			self.seqtable_column_info_field_id___ = SeqTable_column_info_field_id___( root.find('SeqTable-column-info_field-id') )
		else:
			pass
		if root.find('SeqTable-column-info_title') is not None:
			self.seqtable_column_info_title__ = SeqTable_column_info_title__( root.find('SeqTable-column-info_title') )
		else:
			pass
		if root.find('SeqTable-column-info_field-name') is not None:
			self.seqtable_column_info_field_name___ = SeqTable_column_info_field_name___( root.find('SeqTable-column-info_field-name') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Meeting_number( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Meeting_number, self ).__init__()
		self.name = 'Meeting_number'
		self.text = root.text
	
	def __call__( self ):
		pass


class Delta_item_seq_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Delta_item_seq_loc_, self ).__init__()
		self.name = 'Delta-item_seq_loc'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Org_ref_common_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Org_ref_common_, self ).__init__()
		self.name = 'Org-ref_common'
		self.text = root.text
	
	def __call__( self ):
		pass


class VariantProperties_version( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_version, self ).__init__()
		self.name = 'VariantProperties_version'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cdregion_orf( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_orf, self ).__init__()
		self.name = 'Cdregion_orf'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Tx_evidence_low_prec_data___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Tx_evidence_low_prec_data___, self ).__init__()
		self.name = 'Tx-evidence_low-prec-data'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Imprint_part_sup_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_part_sup_, self ).__init__()
		self.name = 'Imprint_part-sup'
		self.text = root.text
	
	def __call__( self ):
		pass


class Spliced_seg_modifiers_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_seg_modifiers_, self ).__init__()
		self.name = 'Spliced-seg_modifiers'
		if root.find('Spliced-seg-modifier') is not None:
			self.spliced_seg_modifier__ = [ Spliced_seg_modifier__(element) for element in root.findall('Spliced-seg-modifier') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Id_pat_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Id_pat_, self ).__init__()
		self.name = 'Id-pat'
		self.id_pat_country_ = Id_pat_country_( root.find('Id-pat_country') )
		self.id_pat_id_ = Id_pat_id_( root.find('Id-pat_id') )
		if root.find('Id-pat_doc-type') is not None:
			self.id_pat_doc_type__ = Id_pat_doc_type__( root.find('Id-pat_doc-type') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_inst_observation_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_inst_observation_, self ).__init__()
		self.name = 'Variation-inst_observation'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['asserted', 'reference', 'variant']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class User_field_data_objects_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_field_data_objects_, self ).__init__()
		self.name = 'User-field_data_objects'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.user_object_ = root.findall( 'User-object' )
		self.to_evaluate.append( ( 'User-object', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Patent_seq_id_cit__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_seq_id_cit__, self ).__init__()
		self.name = 'Patent-seq-id_cit'
		self.id_pat_ = Id_pat_( root.find('Id-pat') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_inst_, self ).__init__()
		self.name = 'Seq-inst'
		if root.find('Seq-inst_topology') is not None:
			self.seq_inst_topology_ = Seq_inst_topology_( root.find('Seq-inst_topology') )
		else:
			pass
		self.seq_inst_repr_ = Seq_inst_repr_( root.find('Seq-inst_repr') )
		if root.find('Seq-inst_strand') is not None:
			self.seq_inst_strand_ = Seq_inst_strand_( root.find('Seq-inst_strand') )
		else:
			pass
		self.seq_inst_mol_ = Seq_inst_mol_( root.find('Seq-inst_mol') )
		if root.find('Seq-inst_ext') is not None:
			self.seq_inst_ext_ = Seq_inst_ext_( root.find('Seq-inst_ext') )
		else:
			pass
		if root.find('Seq-inst_fuzz') is not None:
			self.seq_inst_fuzz_ = Seq_inst_fuzz_( root.find('Seq-inst_fuzz') )
		else:
			pass
		if root.find('Seq-inst_seq-data') is not None:
			self.seq_inst_seq_data__ = Seq_inst_seq_data__( root.find('Seq-inst_seq-data') )
		else:
			pass
		if root.find('Seq-inst_hist') is not None:
			self.seq_inst_hist_ = Seq_inst_hist_( root.find('Seq-inst_hist') )
		else:
			pass
		if root.find('Seq-inst_length') is not None:
			self.seq_inst_length_ = Seq_inst_length_( root.find('Seq-inst_length') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceSupport( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceSupport, self ).__init__()
		self.name = 'ModelEvidenceSupport'
		if root.find('ModelEvidenceSupport_full-length') is not None:
			self.modelevidencesupport_full_length_ = ModelEvidenceSupport_full_length_( root.find('ModelEvidenceSupport_full-length') )
		else:
			pass
		if root.find('ModelEvidenceSupport_supports-all-exon-combo') is not None:
			self.modelevidencesupport_supports_all_exon_combo___ = ModelEvidenceSupport_supports_all_exon_combo___( root.find('ModelEvidenceSupport_supports-all-exon-combo') )
		else:
			pass
		if root.find('ModelEvidenceSupport_dbxref') is not None:
			self.modelevidencesupport_dbxref = ModelEvidenceSupport_dbxref( root.find('ModelEvidenceSupport_dbxref') )
		else:
			pass
		if root.find('ModelEvidenceSupport_protein') is not None:
			self.modelevidencesupport_protein = ModelEvidenceSupport_protein( root.find('ModelEvidenceSupport_protein') )
		else:
			pass
		if root.find('ModelEvidenceSupport_exon-count') is not None:
			self.modelevidencesupport_exon_count_ = ModelEvidenceSupport_exon_count_( root.find('ModelEvidenceSupport_exon-count') )
		else:
			pass
		if root.find('ModelEvidenceSupport_method') is not None:
			self.modelevidencesupport_method = ModelEvidenceSupport_method( root.find('ModelEvidenceSupport_method') )
		else:
			pass
		if root.find('ModelEvidenceSupport_identification') is not None:
			self.modelevidencesupport_identification = ModelEvidenceSupport_identification( root.find('ModelEvidenceSupport_identification') )
		else:
			pass
		if root.find('ModelEvidenceSupport_mrna') is not None:
			self.modelevidencesupport_mrna = ModelEvidenceSupport_mrna( root.find('ModelEvidenceSupport_mrna') )
		else:
			pass
		if root.find('ModelEvidenceSupport_exon-length') is not None:
			self.modelevidencesupport_exon_length_ = ModelEvidenceSupport_exon_length_( root.find('ModelEvidenceSupport_exon-length') )
		else:
			pass
		if root.find('ModelEvidenceSupport_est') is not None:
			self.modelevidencesupport_est = ModelEvidenceSupport_est( root.find('ModelEvidenceSupport_est') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_fuzz_alt_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_alt_, self ).__init__()
		self.name = 'Int-fuzz_alt'
		if root.find('Int-fuzz_alt_E') is not None:
			self.int_fuzz_alt_e_ = [ Int_fuzz_alt_E_(element) for element in root.findall('Int-fuzz_alt_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PCRReactionSet( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	def __init__( self, root ):
		super( PCRReactionSet, self ).__init__()
		self.name = 'PCRReactionSet'
		if root.find('PCRReaction') is not None:
			self.pcrreaction = [ PCRReaction(element) for element in root.findall('PCRReaction') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_chunk_genomic_ins___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_chunk_genomic_ins___, self ).__init__()
		self.name = 'Spliced-exon-chunk_genomic-ins'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceSupport_supports_all_exon_combo___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceSupport_supports_all_exon_combo___, self ).__init__()
		self.name = 'ModelEvidenceSupport_supports-all-exon-combo'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class PRF_block_keywords_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_block_keywords_, self ).__init__()
		self.name = 'PRF-block_keywords'
		if root.find('PRF-block_keywords_E') is not None:
			self.prf_block_keywords_e_ = [ PRF_block_keywords_E_(element) for element in root.findall('PRF-block_keywords_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_gcode( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_gcode, self ).__init__()
		self.name = 'OrgName_gcode'
		self.text = root.text
	
	def __call__( self ):
		pass


class Patent_priority_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Patent_priority_, self ).__init__()
		self.name = 'Patent-priority'
		self.patent_priority_number_ = Patent_priority_number_( root.find('Patent-priority_number') )
		self.patent_priority_date_ = Patent_priority_date_( root.find('Patent-priority_date') )
		self.patent_priority_country_ = Patent_priority_country_( root.find('Patent-priority_country') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PubStatusDateSet( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PubStatusDateSet, self ).__init__()
		self.name = 'PubStatusDateSet'
		if root.find('PubStatusDate') is not None:
			self.pubstatusdate = [ PubStatusDate(element) for element in root.findall('PubStatusDate') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Byte_graph_min_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Byte_graph_min_, self ).__init__()
		self.name = 'Byte-graph_min'
		self.text = root.text
	
	def __call__( self ):
		pass


class Auth_list_affil_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Auth_list_affil_, self ).__init__()
		self.name = 'Auth-list_affil'
		self.affil = Affil( root.find('Affil') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_exon_, self ).__init__()
		self.name = 'Spliced-exon'
		if root.find('Spliced-exon_partial') is not None:
			self.spliced_exon_partial_ = Spliced_exon_partial_( root.find('Spliced-exon_partial') )
		else:
			pass
		if root.find('Spliced-exon_genomic-strand') is not None:
			self.spliced_exon_genomic_strand__ = Spliced_exon_genomic_strand__( root.find('Spliced-exon_genomic-strand') )
		else:
			pass
		if root.find('Spliced-exon_product-strand') is not None:
			self.spliced_exon_product_strand__ = Spliced_exon_product_strand__( root.find('Spliced-exon_product-strand') )
		else:
			pass
		if root.find('Spliced-exon_product-id') is not None:
			self.spliced_exon_product_id__ = Spliced_exon_product_id__( root.find('Spliced-exon_product-id') )
		else:
			pass
		self.spliced_exon_genomic_start__ = Spliced_exon_genomic_start__( root.find('Spliced-exon_genomic-start') )
		if root.find('Spliced-exon_scores') is not None:
			self.spliced_exon_scores_ = Spliced_exon_scores_( root.find('Spliced-exon_scores') )
		else:
			pass
		if root.find('Spliced-exon_donor-after-exon') is not None:
			self.spliced_exon_donor_after_exon___ = Spliced_exon_donor_after_exon___( root.find('Spliced-exon_donor-after-exon') )
		else:
			pass
		self.spliced_exon_genomic_end__ = Spliced_exon_genomic_end__( root.find('Spliced-exon_genomic-end') )
		if root.find('Spliced-exon_parts') is not None:
			self.spliced_exon_parts_ = Spliced_exon_parts_( root.find('Spliced-exon_parts') )
		else:
			pass
		if root.find('Spliced-exon_genomic-id') is not None:
			self.spliced_exon_genomic_id__ = Spliced_exon_genomic_id__( root.find('Spliced-exon_genomic-id') )
		else:
			pass
		self.spliced_exon_product_start__ = Spliced_exon_product_start__( root.find('Spliced-exon_product-start') )
		self.spliced_exon_product_end__ = Spliced_exon_product_end__( root.find('Spliced-exon_product-end') )
		if root.find('Spliced-exon_acceptor-before-exon') is not None:
			self.spliced_exon_acceptor_before_exon___ = Spliced_exon_acceptor_before_exon___( root.find('Spliced-exon_acceptor-before-exon') )
		else:
			pass
		if root.find('Spliced-exon_ext') is not None:
			self.spliced_exon_ext_ = Spliced_exon_ext_( root.find('Spliced-exon_ext') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PmPid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PmPid, self ).__init__()
		self.name = 'PmPid'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceSupport_mrna( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceSupport_mrna, self ).__init__()
		self.name = 'ModelEvidenceSupport_mrna'
		if root.find('ModelEvidenceItem') is not None:
			self.modelevidenceitem = [ ModelEvidenceItem(element) for element in root.findall('ModelEvidenceItem') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PCRPrimer_name( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRPrimer_name, self ).__init__()
		self.name = 'PCRPrimer_name'
		self.pcrprimername = PCRPrimerName( root.find('PCRPrimerName') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgName_mod( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgName_mod, self ).__init__()
		self.name = 'OrgName_mod'
		if root.find('OrgMod') is not None:
			self.orgmod = [ OrgMod(element) for element in root.findall('OrgMod') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BioSource_genome( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BioSource_genome, self ).__init__()
		self.name = 'BioSource_genome'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'genomic', 'chloroplast', 'chromoplast', 'kinetoplast', 'mitochondrion', 'plastid', 'macronuclear', 'extrachrom', 'plasmid', 'transposon', 'insertion-seq', 'cyanelle', 'proviral', 'virion', 'nucleomorph', 'apicoplast', 'leucoplast', 'proplastid', 'endogenous-virus', 'hydrogenosome', 'chromosome', 'chromatophore']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Clone_ref_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_ref_name_, self ).__init__()
		self.name = 'Clone-ref_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Bioseq_id( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Bioseq_id, self ).__init__()
		self.name = 'Bioseq_id'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dense_seg_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Dense_seg_ids_, self ).__init__()
		self.name = 'Dense-seg_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId_pmcid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_pmcid, self ).__init__()
		self.name = 'ArticleId_pmcid'
		self.pmcid = PmcID( root.find('PmcID') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Imprint_date( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_date, self ).__init__()
		self.name = 'Imprint_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData, self ).__init__()
		self.name = 'SeqFeatData'
		#jedna z opcji dla ['SeqFeatData_het', 'SeqFeatData_clone', 'SeqFeatData_cdregion', 'SeqFeatData_org', 'SeqFeatData_rsite', 'SeqFeatData_bond', 'SeqFeatData_prot', 'SeqFeatData_psec-str', 'SeqFeatData_gene', 'SeqFeatData_pub', 'SeqFeatData_seq', 'SeqFeatData_biosrc', 'SeqFeatData_txinit', 'SeqFeatData_num', 'SeqFeatData_comment', 'SeqFeatData_non-std-residue', 'SeqFeatData_imp', 'SeqFeatData_user', 'SeqFeatData_variation', 'SeqFeatData_site', 'SeqFeatData_region', 'SeqFeatData_rna']
		if 'SeqFeatData_het' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_het = SeqFeatData_het( root.find('SeqFeatData_het') )
		elif 'SeqFeatData_clone' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_clone = SeqFeatData_clone( root.find('SeqFeatData_clone') )
		elif 'SeqFeatData_cdregion' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_cdregion = SeqFeatData_cdregion( root.find('SeqFeatData_cdregion') )
		elif 'SeqFeatData_org' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_org = SeqFeatData_org( root.find('SeqFeatData_org') )
		elif 'SeqFeatData_rsite' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_rsite = SeqFeatData_rsite( root.find('SeqFeatData_rsite') )
		elif 'SeqFeatData_bond' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_bond = SeqFeatData_bond( root.find('SeqFeatData_bond') )
		elif 'SeqFeatData_prot' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_prot = SeqFeatData_prot( root.find('SeqFeatData_prot') )
		elif 'SeqFeatData_psec-str' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_psec_str_ = SeqFeatData_psec_str_( root.find('SeqFeatData_psec-str') )
		elif 'SeqFeatData_gene' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_gene = SeqFeatData_gene( root.find('SeqFeatData_gene') )
		elif 'SeqFeatData_pub' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_pub = SeqFeatData_pub( root.find('SeqFeatData_pub') )
		elif 'SeqFeatData_seq' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_seq = SeqFeatData_seq( root.find('SeqFeatData_seq') )
		elif 'SeqFeatData_biosrc' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_biosrc = SeqFeatData_biosrc( root.find('SeqFeatData_biosrc') )
		elif 'SeqFeatData_txinit' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_txinit = SeqFeatData_txinit( root.find('SeqFeatData_txinit') )
		elif 'SeqFeatData_num' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_num = SeqFeatData_num( root.find('SeqFeatData_num') )
		elif 'SeqFeatData_comment' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_comment = SeqFeatData_comment( root.find('SeqFeatData_comment') )
		elif 'SeqFeatData_non-std-residue' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_non_std_residue__ = SeqFeatData_non_std_residue__( root.find('SeqFeatData_non-std-residue') )
		elif 'SeqFeatData_imp' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_imp = SeqFeatData_imp( root.find('SeqFeatData_imp') )
		elif 'SeqFeatData_user' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_user = SeqFeatData_user( root.find('SeqFeatData_user') )
		elif 'SeqFeatData_variation' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_variation = SeqFeatData_variation( root.find('SeqFeatData_variation') )
		elif 'SeqFeatData_site' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_site = SeqFeatData_site( root.find('SeqFeatData_site') )
		elif 'SeqFeatData_region' in [ x.tag for x in root.getchildren() ]:
			self.seqfeatdata_region = SeqFeatData_region( root.find('SeqFeatData_region') )
		else:
			self.seqfeatdata_rna = SeqFeatData_rna( root.find('SeqFeatData_rna') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class InferenceSupport_dois( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( InferenceSupport_dois, self ).__init__()
		self.name = 'InferenceSupport_dois'
		if root.find('DOI') is not None:
			self.doi = [ DOI(element) for element in root.findall('DOI') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_resource_link_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_resource_link_, self ).__init__()
		self.name = 'VariantProperties_resource-link'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['preserved', 'provisional', 'has3D', 'submitterLinkout', 'clinical', 'genotypeKit']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Bioseq_annot( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Bioseq_annot, self ).__init__()
		self.name = 'Bioseq_annot'
		if root.find('Seq-annot') is not None:
			self.seq_annot_ = [ Seq_annot_(element) for element in root.findall('Seq-annot') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_multi_data__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_multi_data__, self ).__init__()
		self.name = 'SeqTable-multi-data'
		#jedna z opcji dla ['SeqTable-multi-data_interval', 'SeqTable-multi-data_real', 'SeqTable-multi-data_string', 'SeqTable-multi-data_int', 'SeqTable-multi-data_id', 'SeqTable-multi-data_loc', 'SeqTable-multi-data_common-bytes', 'SeqTable-multi-data_common-string', 'SeqTable-multi-data_bytes', 'SeqTable-multi-data_bit']
		if 'SeqTable-multi-data_interval' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_interval__ = SeqTable_multi_data_interval__( root.find('SeqTable-multi-data_interval') )
		elif 'SeqTable-multi-data_real' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_real__ = SeqTable_multi_data_real__( root.find('SeqTable-multi-data_real') )
		elif 'SeqTable-multi-data_string' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_string__ = SeqTable_multi_data_string__( root.find('SeqTable-multi-data_string') )
		elif 'SeqTable-multi-data_int' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_int__ = SeqTable_multi_data_int__( root.find('SeqTable-multi-data_int') )
		elif 'SeqTable-multi-data_id' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_id__ = SeqTable_multi_data_id__( root.find('SeqTable-multi-data_id') )
		elif 'SeqTable-multi-data_loc' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_loc__ = SeqTable_multi_data_loc__( root.find('SeqTable-multi-data_loc') )
		elif 'SeqTable-multi-data_common-bytes' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_common_bytes___ = SeqTable_multi_data_common_bytes___( root.find('SeqTable-multi-data_common-bytes') )
		elif 'SeqTable-multi-data_common-string' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_common_string___ = SeqTable_multi_data_common_string___( root.find('SeqTable-multi-data_common-string') )
		elif 'SeqTable-multi-data_bytes' in [ x.tag for x in root.getchildren() ]:
			self.seqtable_multi_data_bytes__ = SeqTable_multi_data_bytes__( root.find('SeqTable-multi-data_bytes') )
		else:
			self.seqtable_multi_data_bit__ = SeqTable_multi_data_bit__( root.find('SeqTable-multi-data_bit') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_seq_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_seq_id__, self ).__init__()
		self.name = 'PDB-seq-id'
		self.pdb_seq_id_mol__ = PDB_seq_id_mol__( root.find('PDB-seq-id_mol') )
		if root.find('PDB-seq-id_rel') is not None:
			self.pdb_seq_id_rel__ = PDB_seq_id_rel__( root.find('PDB-seq-id_rel') )
		else:
			pass
		if root.find('PDB-seq-id_chain') is not None:
			self.pdb_seq_id_chain__ = PDB_seq_id_chain__( root.find('PDB-seq-id_chain') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId_medline( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_medline, self ).__init__()
		self.name = 'ArticleId_medline'
		self.medlineuid = MedlineUID( root.find('MedlineUID') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class InferenceSupport( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( InferenceSupport, self ).__init__()
		self.name = 'InferenceSupport'
		if root.find('InferenceSupport_type') is not None:
			self.inferencesupport_type = InferenceSupport_type( root.find('InferenceSupport_type') )
		else:
			pass
		if root.find('InferenceSupport_same-species') is not None:
			self.inferencesupport_same_species_ = InferenceSupport_same_species_( root.find('InferenceSupport_same-species') )
		else:
			pass
		if root.find('InferenceSupport_pmids') is not None:
			self.inferencesupport_pmids = InferenceSupport_pmids( root.find('InferenceSupport_pmids') )
		else:
			pass
		self.inferencesupport_basis = InferenceSupport_basis( root.find('InferenceSupport_basis') )
		if root.find('InferenceSupport_other-type') is not None:
			self.inferencesupport_other_type_ = InferenceSupport_other_type_( root.find('InferenceSupport_other-type') )
		else:
			pass
		if root.find('InferenceSupport_category') is not None:
			self.inferencesupport_category = InferenceSupport_category( root.find('InferenceSupport_category') )
		else:
			pass
		if root.find('InferenceSupport_dois') is not None:
			self.inferencesupport_dois = InferenceSupport_dois( root.find('InferenceSupport_dois') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title, self ).__init__()
		self.name = 'Title'
		if root.find('Title_E') is not None:
			self.title_e = [ Title_E(element) for element in root.findall('Title_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Trna_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	def __init__( self, root ):
		super( Trna_ext_, self ).__init__()
		self.name = 'Trna-ext'
		if root.find('Trna-ext_anticodon') is not None:
			self.trna_ext_anticodon_ = Trna_ext_anticodon_( root.find('Trna-ext_anticodon') )
		else:
			pass
		if root.find('Trna-ext_aa') is not None:
			self.trna_ext_aa_ = Trna_ext_aa_( root.find('Trna-ext_aa') )
		else:
			pass
		if root.find('Trna-ext_codon') is not None:
			self.trna_ext_codon_ = Trna_ext_codon_( root.find('Trna-ext_codon') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_product_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_seg_product_id__, self ).__init__()
		self.name = 'Spliced-seg_product-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Num_cont_has_zero__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_cont_has_zero__, self ).__init__()
		self.name = 'Num-cont_has-zero'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Clone_seq_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Clone_seq_, self ).__init__()
		self.name = 'Clone-seq'
		self.clone_seq_type_ = Clone_seq_type_( root.find('Clone-seq_type') )
		if root.find('Clone-seq_confidence') is not None:
			self.clone_seq_confidence_ = Clone_seq_confidence_( root.find('Clone-seq_confidence') )
		else:
			pass
		if root.find('Clone-seq_support') is not None:
			self.clone_seq_support_ = Clone_seq_support_( root.find('Clone-seq_support') )
		else:
			pass
		if root.find('Clone-seq_align-id') is not None:
			self.clone_seq_align_id__ = Clone_seq_align_id__( root.find('Clone-seq_align-id') )
		else:
			pass
		if root.find('Clone-seq_seq') is not None:
			self.clone_seq_seq_ = Clone_seq_seq_( root.find('Clone-seq_seq') )
		else:
			pass
		self.clone_seq_location_ = Clone_seq_location_( root.find('Clone-seq_location') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_product_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_product_, self ).__init__()
		self.name = 'Seq-feat_product'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_consequence_E_frameshift_phase_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_frameshift_phase_, self ).__init__()
		self.name = 'Variation-ref_consequence_E_frameshift_phase'
		self.text = root.text
	
	def __call__( self ):
		pass


class NCBI8aa( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( NCBI8aa, self ).__init__()
		self.name = 'NCBI8aa'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_object_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_object_data_, self ).__init__()
		self.name = 'User-object_data'
		if root.find('User-field') is not None:
			self.user_field_ = [ User_field_(element) for element in root.findall('User-field') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_ref_library_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_ref_library_, self ).__init__()
		self.name = 'Clone-ref_library'
		self.text = root.text
	
	def __call__( self ):
		pass


class Trna_ext_anticodon_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	def __init__( self, root ):
		super( Trna_ext_anticodon_, self ).__init__()
		self.name = 'Trna-ext_anticodon'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PmcPid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PmcPid, self ).__init__()
		self.name = 'PmcPid'
		self.text = root.text
	
	def __call__( self ):
		pass


class PDB_replace_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_replace_date_, self ).__init__()
		self.name = 'PDB-replace_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Program_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Program_id_, self ).__init__()
		self.name = 'Program-id'
		if root.find('Program-id_version') is not None:
			self.program_id_version_ = Program_id_version_( root.find('Program-id_version') )
		else:
			pass
		self.program_id_name_ = Program_id_name_( root.find('Program-id_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_block_replace_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_block_replace_, self ).__init__()
		self.name = 'PDB-block_replace'
		self.pdb_replace_ = PDB_replace_( root.find('PDB-replace') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_column_info_field_id___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_column_info_field_id___, self ).__init__()
		self.name = 'SeqTable-column-info_field-id'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['location', 'location-id', 'location-gi', 'location-from', 'location-to', 'location-strand', 'location-fuzz-from-lim', 'location-fuzz-to-lim', 'product', 'product-id', 'product-gi', 'product-from', 'product-to', 'product-strand', 'product-fuzz-from-lim', 'product-fuzz-to-lim', 'id-local', 'xref-id-local', 'partial', 'comment', 'title', 'ext', 'qual', 'dbxref', 'data-imp-key', 'data-region', 'data-cdregion-frame', 'ext-type', 'qual-qual', 'qual-val', 'dbxref-db', 'dbxref-tag']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Org_ref_orgname_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	def __init__( self, root ):
		super( Org_ref_orgname_, self ).__init__()
		self.name = 'Org-ref_orgname'
		self.orgname = OrgName( root.find('OrgName') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_hist_rec_date__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_hist_rec_date__, self ).__init__()
		self.name = 'Seq-hist-rec_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ExperimentSupport_explanation( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ExperimentSupport_explanation, self ).__init__()
		self.name = 'ExperimentSupport_explanation'
		self.text = root.text
	
	def __call__( self ):
		pass


class Std_seg_dim_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Std_seg_dim_, self ).__init__()
		self.name = 'Std-seg_dim'
		self.text = root.text
	
	def __call__( self ):
		pass


class Int_fuzz_range_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_range_, self ).__init__()
		self.name = 'Int-fuzz_range'
		self.int_fuzz_range_max_ = Int_fuzz_range_max_( root.find('Int-fuzz_range_max') )
		self.int_fuzz_range_min_ = Int_fuzz_range_min_( root.find('Int-fuzz_range_min') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_name_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_name_E_, self ).__init__()
		self.name = 'Prot-ref_name_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_, self ).__init__()
		self.name = 'Seq-data'
		#jedna z opcji dla ['Seq-data_iupacaa', 'Seq-data_ncbi2na', 'Seq-data_ncbistdaa', 'Seq-data_ncbieaa', 'Seq-data_iupacna', 'Seq-data_ncbi8na', 'Seq-data_ncbi4na', 'Seq-data_gap', 'Seq-data_ncbipna', 'Seq-data_ncbipaa', 'Seq-data_ncbi8aa']
		if 'Seq-data_iupacaa' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_iupacaa_ = Seq_data_iupacaa_( root.find('Seq-data_iupacaa') )
		elif 'Seq-data_ncbi2na' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbi2na_ = Seq_data_ncbi2na_( root.find('Seq-data_ncbi2na') )
		elif 'Seq-data_ncbistdaa' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbistdaa_ = Seq_data_ncbistdaa_( root.find('Seq-data_ncbistdaa') )
		elif 'Seq-data_ncbieaa' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbieaa_ = Seq_data_ncbieaa_( root.find('Seq-data_ncbieaa') )
		elif 'Seq-data_iupacna' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_iupacna_ = Seq_data_iupacna_( root.find('Seq-data_iupacna') )
		elif 'Seq-data_ncbi8na' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbi8na_ = Seq_data_ncbi8na_( root.find('Seq-data_ncbi8na') )
		elif 'Seq-data_ncbi4na' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbi4na_ = Seq_data_ncbi4na_( root.find('Seq-data_ncbi4na') )
		elif 'Seq-data_gap' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_gap_ = Seq_data_gap_( root.find('Seq-data_gap') )
		elif 'Seq-data_ncbipna' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbipna_ = Seq_data_ncbipna_( root.find('Seq-data_ncbipna') )
		elif 'Seq-data_ncbipaa' in [ x.tag for x in root.getchildren() ]:
			self.seq_data_ncbipaa_ = Seq_data_ncbipaa_( root.find('Seq-data_ncbipaa') )
		else:
			self.seq_data_ncbi8aa_ = Seq_data_ncbi8aa_( root.find('Seq-data_ncbi8aa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_equiv( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_equiv, self ).__init__()
		self.name = 'Pub_equiv'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.pub_equiv_ = root.find( 'Pub-equiv' )
		self.to_evaluate.append( ( 'Pub-equiv', '' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ArticleId_doi( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ArticleId_doi, self ).__init__()
		self.name = 'ArticleId_doi'
		self.doi = DOI( root.find('DOI') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_qual_mp_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_qual_mp_, self ).__init__()
		self.name = 'Medline-qual_mp'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Gene_ref_locus_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_locus_, self ).__init__()
		self.name = 'Gene-ref_locus'
		self.text = root.text
	
	def __call__( self ):
		pass


class Sparse_seg_row_scores__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_seg_row_scores__, self ).__init__()
		self.name = 'Sparse-seg_row-scores'
		if root.find('Score') is not None:
			self.score = [ Score(element) for element in root.findall('Score') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_annot_name_, self ).__init__()
		self.name = 'Seq-annot_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annotdesc_title( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annotdesc_title, self ).__init__()
		self.name = 'Annotdesc_title'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_single_data_bit__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_single_data_bit__, self ).__init__()
		self.name = 'SeqTable-single-data_bit'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Variation_ref_consequence_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_consequence_E_, self ).__init__()
		self.name = 'Variation-ref_consequence_E'
		#jedna z opcji dla ['Variation-ref_consequence_E_splicing', 'Variation-ref_consequence_E_frameshift', 'Variation-ref_consequence_E_loss-of-heterozygosity', 'Variation-ref_consequence_E_variation', 'Variation-ref_consequence_E_note', 'Variation-ref_consequence_E_unknown']
		if 'Variation-ref_consequence_E_splicing' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_consequence_e_splicing_ = Variation_ref_consequence_E_splicing_( root.find('Variation-ref_consequence_E_splicing') )
		elif 'Variation-ref_consequence_E_frameshift' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_consequence_e_frameshift_ = Variation_ref_consequence_E_frameshift_( root.find('Variation-ref_consequence_E_frameshift') )
		elif 'Variation-ref_consequence_E_loss-of-heterozygosity' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_consequence_e_loss_of_heterozygosity___ = Variation_ref_consequence_E_loss_of_heterozygosity___( root.find('Variation-ref_consequence_E_loss-of-heterozygosity') )
		elif 'Variation-ref_consequence_E_variation' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_consequence_e_variation_ = Variation_ref_consequence_E_variation_( root.find('Variation-ref_consequence_E_variation') )
		elif 'Variation-ref_consequence_E_note' in [ x.tag for x in root.getchildren() ]:
			self.variation_ref_consequence_e_note_ = Variation_ref_consequence_E_note_( root.find('Variation-ref_consequence_E_note') )
		else:
			self.variation_ref_consequence_e_unknown_ = Variation_ref_consequence_E_unknown_( root.find('Variation-ref_consequence_E_unknown') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_dbref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_dbref_, self ).__init__()
		self.name = 'SP-block_dbref'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Numbering_cont( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Numbering_cont, self ).__init__()
		self.name = 'Numbering_cont'
		self.num_cont_ = Num_cont_( root.find('Num-cont') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Prot_ref_activity_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Protein'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_ref_activity_, self ).__init__()
		self.name = 'Prot-ref_activity'
		if root.find('Prot-ref_activity_E') is not None:
			self.prot_ref_activity_e_ = [ Prot_ref_activity_E_(element) for element in root.findall('Prot-ref_activity_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_id_, self ).__init__()
		self.name = 'Seq-annot_id'
		if root.find('Annot-id') is not None:
			self.annot_id_ = [ Annot_id_(element) for element in root.findall('Annot-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceSupport_exon_count_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ModelEvidenceSupport_exon_count_, self ).__init__()
		self.name = 'ModelEvidenceSupport_exon-count'
		self.text = root.text
	
	def __call__( self ):
		pass


class GB_block_entry_date__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_entry_date__, self ).__init__()
		self.name = 'GB-block_entry-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Affil_std_affil( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_affil, self ).__init__()
		self.name = 'Affil_std_affil'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_column_header_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_column_header_, self ).__init__()
		self.name = 'SeqTable-column_header'
		self.seqtable_column_info__ = SeqTable_column_info__( root.find('SeqTable-column-info') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_align_second_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Sparse_align_second_id__, self ).__init__()
		self.name = 'Sparse-align_second-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_graph_title_y__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_title_y__, self ).__init__()
		self.name = 'Seq-graph_title-y'
		self.text = root.text
	
	def __call__( self ):
		pass


class Bioseq_set_release_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Bioseq_set_release_, self ).__init__()
		self.name = 'Bioseq-set_release'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_gpipe_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_gpipe_, self ).__init__()
		self.name = 'Seq-id_gpipe'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_data_ncbipna_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_data_ncbipna_, self ).__init__()
		self.name = 'Seq-data_ncbipna'
		self.ncbipna = NCBIpna( root.find('NCBIpna') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_field_, self ).__init__()
		self.name = 'User-field'
		if root.find('User-field_num') is not None:
			self.user_field_num_ = User_field_num_( root.find('User-field_num') )
		else:
			pass
		self.user_field_label_ = User_field_label_( root.find('User-field_label') )
		self.user_field_data_ = User_field_data_( root.find('User-field_data') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seqdesc_pir( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seqdesc_pir, self ).__init__()
		self.name = 'Seqdesc_pir'
		self.pir_block_ = PIR_block_( root.find('PIR-block') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_length_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_length_, self ).__init__()
		self.name = 'Seq-inst_length'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_ref_aligns_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Num_ref_aligns_, self ).__init__()
		self.name = 'Num-ref_aligns'
		self.seq_align_ = Seq_align_( root.find('Seq-align') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Align_def_align_type__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Align_def_align_type__, self ).__init__()
		self.name = 'Align-def_align-type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['ref', 'alt', 'blocks', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class RNA_gen_product_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_gen_product_, self ).__init__()
		self.name = 'RNA-gen_product'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_pat_assignees_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_pat_assignees_, self ).__init__()
		self.name = 'Cit-pat_assignees'
		self.auth_list_ = Auth_list_( root.find('Auth-list') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_align_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Sparse_align_, self ).__init__()
		self.name = 'Sparse-align'
		self.sparse_align_second_starts__ = Sparse_align_second_starts__( root.find('Sparse-align_second-starts') )
		self.sparse_align_first_starts__ = Sparse_align_first_starts__( root.find('Sparse-align_first-starts') )
		self.sparse_align_lens_ = Sparse_align_lens_( root.find('Sparse-align_lens') )
		self.sparse_align_numseg_ = Sparse_align_numseg_( root.find('Sparse-align_numseg') )
		self.sparse_align_second_id__ = Sparse_align_second_id__( root.find('Sparse-align_second-id') )
		if root.find('Sparse-align_seg-scores') is not None:
			self.sparse_align_seg_scores__ = Sparse_align_seg_scores__( root.find('Sparse-align_seg-scores') )
		else:
			pass
		self.sparse_align_first_id__ = Sparse_align_first_id__( root.find('Sparse-align_first-id') )
		if root.find('Sparse-align_second-strands') is not None:
			self.sparse_align_second_strands__ = Sparse_align_second_strands__( root.find('Sparse-align_second-strands') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PIR_block_genetic_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PIR-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PIR_block_genetic_, self ).__init__()
		self.name = 'PIR-block_genetic'
		self.text = root.text
	
	def __call__( self ):
		pass


class Code_break_aa_ncbi8aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Code_break_aa_ncbi8aa_, self ).__init__()
		self.name = 'Code-break_aa_ncbi8aa'
		self.text = root.text
	
	def __call__( self ):
		pass


class RNA_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	def __init__( self, root ):
		super( RNA_ref_, self ).__init__()
		self.name = 'RNA-ref'
		if root.find('RNA-ref_pseudo') is not None:
			self.rna_ref_pseudo_ = RNA_ref_pseudo_( root.find('RNA-ref_pseudo') )
		else:
			pass
		self.rna_ref_type_ = RNA_ref_type_( root.find('RNA-ref_type') )
		if root.find('RNA-ref_ext') is not None:
			self.rna_ref_ext_ = RNA_ref_ext_( root.find('RNA-ref_ext') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_point_strand_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_point_strand_, self ).__init__()
		self.name = 'Seq-point_strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_book_imp_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_book_imp_, self ).__init__()
		self.name = 'Cit-book_imp'
		self.imprint = Imprint( root.find('Imprint') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Score( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Score, self ).__init__()
		self.name = 'Score'
		self.score_value = Score_value( root.find('Score_value') )
		if root.find('Score_id') is not None:
			self.score_id = Score_id( root.find('Score_id') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Gene_nomenclature_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_nomenclature_, self ).__init__()
		self.name = 'Gene-nomenclature'
		self.gene_nomenclature_status_ = Gene_nomenclature_status_( root.find('Gene-nomenclature_status') )
		if root.find('Gene-nomenclature_symbol') is not None:
			self.gene_nomenclature_symbol_ = Gene_nomenclature_symbol_( root.find('Gene-nomenclature_symbol') )
		else:
			pass
		if root.find('Gene-nomenclature_name') is not None:
			self.gene_nomenclature_name_ = Gene_nomenclature_name_( root.find('Gene-nomenclature_name') )
		else:
			pass
		if root.find('Gene-nomenclature_source') is not None:
			self.gene_nomenclature_source_ = Gene_nomenclature_source_( root.find('Gene-nomenclature_source') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_align_first_starts_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_first_starts_E__, self ).__init__()
		self.name = 'Sparse-align_first-starts_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class User_object_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_object_, self ).__init__()
		self.name = 'User-object'
		self.user_object_data_ = User_object_data_( root.find('User-object_data') )
		if root.find('User-object_class') is not None:
			self.user_object_class_ = User_object_class_( root.find('User-object_class') )
		else:
			pass
		self.user_object_type_ = User_object_type_( root.find('User-object_type') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BioSource_is_focus_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BioSource_is_focus_, self ).__init__()
		self.name = 'BioSource_is-focus'
		self.text = root.text
	
	def __call__( self ):
		pass


class Code_break_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Code_break_loc_, self ).__init__()
		self.name = 'Code-break_loc'
		self.seq_loc_ = Seq_loc_( root.find('Seq-loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Pub_set_book_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_set_book_, self ).__init__()
		self.name = 'Pub-set_book'
		if root.find('Cit-book') is not None:
			self.cit_book_ = [ Cit_book_(element) for element in root.findall('Cit-book') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Genetic_code_E_sncbieaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Genetic_code_E_sncbieaa_, self ).__init__()
		self.name = 'Genetic-code_E_sncbieaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class ModelEvidenceSupport_identification( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceSupport_identification, self ).__init__()
		self.name = 'ModelEvidenceSupport_identification'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_entry_mlfield_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_mlfield_, self ).__init__()
		self.name = 'Medline-entry_mlfield'
		if root.find('Medline-field') is not None:
			self.medline_field_ = [ Medline_field_(element) for element in root.findall('Medline-field') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PCRReaction_reverse( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRReaction_reverse, self ).__init__()
		self.name = 'PCRReaction_reverse'
		self.pcrprimerset = PCRPrimerSet( root.find('PCRPrimerSet') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_data_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_ids_, self ).__init__()
		self.name = 'Seq-annot_data_ids'
		if root.find('Seq-id') is not None:
			self.seq_id_ = [ Seq_id_(element) for element in root.findall('Seq-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_org( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatData_org, self ).__init__()
		self.name = 'SeqFeatData_org'
		self.org_ref_ = Org_ref_( root.find('Org-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class CommonBytes_table_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( CommonBytes_table_, self ).__init__()
		self.name = 'CommonBytes-table'
		self.commonbytes_table_indexes_ = CommonBytes_table_indexes_( root.find('CommonBytes-table_indexes') )
		self.commonbytes_table_bytes_ = CommonBytes_table_bytes_( root.find('CommonBytes-table_bytes') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_fuzz_pct_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_pct_, self ).__init__()
		self.name = 'Int-fuzz_pct'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_other_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_other_, self ).__init__()
		self.name = 'Seq-id_other'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annotdesc_create_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annotdesc_create_date_, self ).__init__()
		self.name = 'Annotdesc_create-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class OrgMod( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgMod, self ).__init__()
		self.name = 'OrgMod'
		self.orgmod_subtype = OrgMod_subtype( root.find('OrgMod_subtype') )
		self.orgmod_subname = OrgMod_subname( root.find('OrgMod_subname') )
		if root.find('OrgMod_attrib') is not None:
			self.orgmod_attrib = OrgMod_attrib( root.find('OrgMod_attrib') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_dbname_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_dbname_, self ).__init__()
		self.name = 'EMBL-dbname'
		#jedna z opcji dla ['EMBL-dbname_code', 'EMBL-dbname_name']
		if 'EMBL-dbname_code' in [ x.tag for x in root.getchildren() ]:
			self.embl_dbname_code_ = EMBL_dbname_code_( root.find('EMBL-dbname_code') )
		else:
			self.embl_dbname_name_ = EMBL_dbname_name_( root.find('EMBL-dbname_name') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class RNA_qual_val_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_qual_val_, self ).__init__()
		self.name = 'RNA-qual_val'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_dbxref( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_dbxref, self ).__init__()
		self.name = 'Seqdesc_dbxref'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_align_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_ext_, self ).__init__()
		self.name = 'Seq-align_ext'
		if root.find('User-object') is not None:
			self.user_object_ = [ User_object_(element) for element in root.findall('User-object') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cdregion_frame( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_frame, self ).__init__()
		self.name = 'Cdregion_frame'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'one', 'two', 'three']
		self.value = root.get('value')


class Cit_book_title_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_book_title_, self ).__init__()
		self.name = 'Cit-book_title'
		self.title = Title( root.find('Title') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_graph_min_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_graph_min_, self ).__init__()
		self.name = 'Int-graph_min'
		self.text = root.text
	
	def __call__( self ):
		pass


class Int_fuzz_range_min_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_fuzz_range_min_, self ).__init__()
		self.name = 'Int-fuzz_range_min'
		self.text = root.text
	
	def __call__( self ):
		pass


class Giimport_id_id_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Giimport_id_id_, self ).__init__()
		self.name = 'Giimport-id_id'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_method_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_method_E_, self ).__init__()
		self.name = 'Variation-ref_method_E'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'bac-acgh', 'computational', 'curated', 'digital-array', 'expression-array', 'fish', 'flanking-sequence', 'maph', 'mcd-analysis', 'mlpa', 'oea-assembly', 'oligo-acgh', 'paired-end', 'pcr', 'qpcr', 'read-depth', 'roma', 'rt-pcr', 'sage', 'sequence-alignment', 'sequencing', 'snp-array', 'snp-genoytyping', 'southern', 'western', 'optical-mapping', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Seq_graph_graph_real_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_graph_real_, self ).__init__()
		self.name = 'Seq-graph_graph_real'
		self.real_graph_ = Real_graph_( root.find('Real-graph') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class MultiOrgName( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	def __init__( self, root ):
		super( MultiOrgName, self ).__init__()
		self.name = 'MultiOrgName'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.orgname = root.findall( 'OrgName' )
		self.to_evaluate.append( ( 'OrgName', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Title_E_trans( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Title_E_trans, self ).__init__()
		self.name = 'Title_E_trans'
		self.text = root.text
	
	def __call__( self ):
		pass


class Prot_pos_amin_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Prot_pos_amin_, self ).__init__()
		self.name = 'Prot-pos_amin'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_qual_, self ).__init__()
		self.name = 'Seq-feat_qual'
		if root.find('Gb-qual') is not None:
			self.gb_qual_ = [ Gb_qual_(element) for element in root.findall('Gb-qual') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SP_block_imeth_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: SP-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SP_block_imeth_, self ).__init__()
		self.name = 'SP-block_imeth'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class RNA_ref_ext_gen_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( RNA_ref_ext_gen_, self ).__init__()
		self.name = 'RNA-ref_ext_gen'
		self.rna_gen_ = RNA_gen_( root.find('RNA-gen') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class GB_block_source_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_source_, self ).__init__()
		self.name = 'GB-block_source'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_id_prf_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_id_prf_, self ).__init__()
		self.name = 'Seq-id_prf'
		self.textseq_id_ = Textseq_id_( root.find('Textseq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_allele_frequency_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_allele_frequency_, self ).__init__()
		self.name = 'VariantProperties_allele-frequency'
		self.text = root.text
	
	def __call__( self ):
		pass


class Txinit_syn( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Txinit_syn, self ).__init__()
		self.name = 'Txinit_syn'
		if root.find('Txinit_syn_E') is not None:
			self.txinit_syn_e = [ Txinit_syn_E(element) for element in root.findall('Txinit_syn_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Code_break_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Code_break_, self ).__init__()
		self.name = 'Code-break'
		self.code_break_aa_ = Code_break_aa_( root.find('Code-break_aa') )
		self.code_break_loc_ = Code_break_loc_( root.find('Code-break_loc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_seq_set__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Clone_seq_set__, self ).__init__()
		self.name = 'Clone-seq-set'
		if root.find('Clone-seq') is not None:
			self.clone_seq_ = [ Clone_seq_(element) for element in root.findall('Clone-seq') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_proc_book_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_proc_book_, self ).__init__()
		self.name = 'Cit-proc_book'
		self.cit_book_ = Cit_book_( root.find('Cit-book') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_literal_seq_data__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_literal_seq_data__, self ).__init__()
		self.name = 'Seq-literal_seq-data'
		self.seq_data_ = Seq_data_( root.find('Seq-data') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seg_ext_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seg_ext_, self ).__init__()
		self.name = 'Seg-ext'
		if root.find('Seq-loc') is not None:
			self.seq_loc_ = [ Seq_loc_(element) for element in root.findall('Seq-loc') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Date_std_season_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_season_, self ).__init__()
		self.name = 'Date-std_season'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_gen_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_date_, self ).__init__()
		self.name = 'Cit-gen_date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Dbtag_db( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Dbtag_db, self ).__init__()
		self.name = 'Dbtag_db'
		self.text = root.text
	
	def __call__( self ):
		pass


class EvidenceBasis_programs( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EvidenceBasis_programs, self ).__init__()
		self.name = 'EvidenceBasis_programs'
		if root.find('Program-id') is not None:
			self.program_id_ = [ Program_id_(element) for element in root.findall('Program-id') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_interval_fuzz_from__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_interval_fuzz_from__, self ).__init__()
		self.name = 'Seq-interval_fuzz-from'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Date_std( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std, self ).__init__()
		self.name = 'Date_std'
		self.date_std_ = Date_std_( root.find('Date-std') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BioSource( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	def __init__( self, root ):
		super( BioSource, self ).__init__()
		self.name = 'BioSource'
		if root.find('BioSource_origin') is not None:
			self.biosource_origin = BioSource_origin( root.find('BioSource_origin') )
		else:
			pass
		if root.find('BioSource_genome') is not None:
			self.biosource_genome = BioSource_genome( root.find('BioSource_genome') )
		else:
			pass
		if root.find('BioSource_subtype') is not None:
			self.biosource_subtype = BioSource_subtype( root.find('BioSource_subtype') )
		else:
			pass
		self.biosource_org = BioSource_org( root.find('BioSource_org') )
		if root.find('BioSource_pcr-primers') is not None:
			self.biosource_pcr_primers_ = BioSource_pcr_primers_( root.find('BioSource_pcr-primers') )
		else:
			pass
		if root.find('BioSource_is-focus') is not None:
			self.biosource_is_focus_ = BioSource_is_focus_( root.find('BioSource_is-focus') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Name_std_full_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Name_std_full_, self ).__init__()
		self.name = 'Name-std_full'
		self.text = root.text
	
	def __call__( self ):
		pass


class VariantProperties_map_weight_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_map_weight_, self ).__init__()
		self.name = 'VariantProperties_map-weight'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['is-uniquely-placed', 'placed-twice-on-same-chrom', 'placed-twice-on-diff-chrom', 'many-placements']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Code_break_aa_ncbistdaa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Code_break_aa_ncbistdaa_, self ).__init__()
		self.name = 'Code-break_aa_ncbistdaa'
		self.text = root.text
	
	def __call__( self ):
		pass


class Bioseq_descr( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Bioseq_descr, self ).__init__()
		self.name = 'Bioseq_descr'
		self.seq_descr_ = Seq_descr_( root.find('Seq-descr') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_method_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_method_, self ).__init__()
		self.name = 'Variation-ref_method'
		if root.find('Variation-ref_method_E') is not None:
			self.variation_ref_method_e_ = [ Variation_ref_method_E_(element) for element in root.findall('Variation-ref_method_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class BinomialOrgName_subspecies( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( BinomialOrgName_subspecies, self ).__init__()
		self.name = 'BinomialOrgName_subspecies'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imp_feat_loc_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imp_feat_loc_, self ).__init__()
		self.name = 'Imp-feat_loc'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_field_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_field_, self ).__init__()
		self.name = 'Medline-field'
		self.medline_field_type_ = Medline_field_type_( root.find('Medline-field_type') )
		self.medline_field_str_ = Medline_field_str_( root.find('Medline-field_str') )
		if root.find('Medline-field_ids') is not None:
			self.medline_field_ids_ = Medline_field_ids_( root.find('Medline-field_ids') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Clone_seq_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_seq_type_, self ).__init__()
		self.name = 'Clone-seq_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['insert', 'end', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Tx_evidence_from_homolog__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-TxInit'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Tx_evidence_from_homolog__, self ).__init__()
		self.name = 'Tx-evidence_from-homolog'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class User_field_data_fields_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	def __init__( self, root ):
		super( User_field_data_fields_, self ).__init__()
		self.name = 'User-field_data_fields'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.user_field_ = root.findall( 'User-field' )
		self.to_evaluate.append( ( 'User-field', '*' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_consequence_E_unknown_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_unknown_, self ).__init__()
		self.name = 'Variation-ref_consequence_E_unknown'
		self.text = root.text
	
	def __call__( self ):
		pass


class OrgMod_subname( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Organism'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( OrgMod_subname, self ).__init__()
		self.name = 'OrgMod_subname'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_std_minute_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_minute_, self ).__init__()
		self.name = 'Date-std_minute'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_point_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_point_, self ).__init__()
		self.name = 'Seq-point'
		if root.find('Seq-point_strand') is not None:
			self.seq_point_strand_ = Seq_point_strand_( root.find('Seq-point_strand') )
		else:
			pass
		self.seq_point_id_ = Seq_point_id_( root.find('Seq-point_id') )
		self.seq_point_point_ = Seq_point_point_( root.find('Seq-point_point') )
		if root.find('Seq-point_fuzz') is not None:
			self.seq_point_fuzz_ = Seq_point_fuzz_( root.find('Seq-point_fuzz') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Sparse_align_numseg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Sparse_align_numseg_, self ).__init__()
		self.name = 'Sparse-align_numseg'
		self.text = root.text
	
	def __call__( self ):
		pass


class Annotdesc_update_date_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annotdesc_update_date_, self ).__init__()
		self.name = 'Annotdesc_update-date'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_column_default_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	def __init__( self, root ):
		super( SeqTable_column_default_, self ).__init__()
		self.name = 'SeqTable-column_default'
		self.seqtable_single_data__ = SeqTable_single_data__( root.find('SeqTable-single-data') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_genomic_start__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_genomic_start__, self ).__init__()
		self.name = 'Spliced-exon_genomic-start'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_except_text__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_feat_except_text__, self ).__init__()
		self.name = 'Seq-feat_except-text'
		self.text = root.text
	
	def __call__( self ):
		pass


class Txinit_gene( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-TxInit'''
	
	def __init__( self, root ):
		super( Txinit_gene, self ).__init__()
		self.name = 'Txinit_gene'
		if root.find('Gene-ref') is not None:
			self.gene_ref_ = [ Gene_ref_(element) for element in root.findall('Gene-ref') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Textseq_id_accession_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textseq_id_accession_, self ).__init__()
		self.name = 'Textseq-id_accession'
		self.text = root.text
	
	def __call__( self ):
		pass


class Pub_medline( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Pub'''
	
	def __init__( self, root ):
		super( Pub_medline, self ).__init__()
		self.name = 'Pub_medline'
		self.medline_entry_ = Medline_entry_( root.find('Medline-entry') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_inst_repr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_inst_repr_, self ).__init__()
		self.name = 'Seq-inst_repr'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'virtual', 'raw', 'seg', 'const', 'ref', 'consen', 'map', 'delta', 'other']
		self.value = root.get('value')


class Gene_ref_allele_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_allele_, self ).__init__()
		self.name = 'Gene-ref_allele'
		self.text = root.text
	
	def __call__( self ):
		pass


class Imprint_cprt( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Imprint_cprt, self ).__init__()
		self.name = 'Imprint_cprt'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ExperimentSupport_pmids( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( ExperimentSupport_pmids, self ).__init__()
		self.name = 'ExperimentSupport_pmids'
		if root.find('PubMedId') is not None:
			self.pubmedid = [ PubMedId(element) for element in root.findall('PubMedId') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_product_start__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_product_start__, self ).__init__()
		self.name = 'Spliced-exon_product-start'
		self.product_pos_ = Product_pos_( root.find('Product-pos') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seqpnt_fuzz_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seqpnt_fuzz_, self ).__init__()
		self.name = 'Packed-seqpnt_fuzz'
		self.int_fuzz_ = Int_fuzz_( root.find('Int-fuzz') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_feat_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_, self ).__init__()
		self.name = 'Seq-feat'
		if root.find('Seq-feat_pseudo') is not None:
			self.seq_feat_pseudo_ = Seq_feat_pseudo_( root.find('Seq-feat_pseudo') )
		else:
			pass
		if root.find('Seq-feat_partial') is not None:
			self.seq_feat_partial_ = Seq_feat_partial_( root.find('Seq-feat_partial') )
		else:
			pass
		if root.find('Seq-feat_except') is not None:
			self.seq_feat_except_ = Seq_feat_except_( root.find('Seq-feat_except') )
		else:
			pass
		if root.find('Seq-feat_exp-ev') is not None:
			self.seq_feat_exp_ev__ = Seq_feat_exp_ev__( root.find('Seq-feat_exp-ev') )
		else:
			pass
		if root.find('Seq-feat_title') is not None:
			self.seq_feat_title_ = Seq_feat_title_( root.find('Seq-feat_title') )
		else:
			pass
		if root.find('Seq-feat_except-text') is not None:
			self.seq_feat_except_text__ = Seq_feat_except_text__( root.find('Seq-feat_except-text') )
		else:
			pass
		if root.find('Seq-feat_exts') is not None:
			self.seq_feat_exts_ = Seq_feat_exts_( root.find('Seq-feat_exts') )
		else:
			pass
		if root.find('Seq-feat_qual') is not None:
			self.seq_feat_qual_ = Seq_feat_qual_( root.find('Seq-feat_qual') )
		else:
			pass
		if root.find('Seq-feat_product') is not None:
			self.seq_feat_product_ = Seq_feat_product_( root.find('Seq-feat_product') )
		else:
			pass
		if root.find('Seq-feat_xref') is not None:
			self.seq_feat_xref_ = Seq_feat_xref_( root.find('Seq-feat_xref') )
		else:
			pass
		if root.find('Seq-feat_support') is not None:
			self.seq_feat_support_ = Seq_feat_support_( root.find('Seq-feat_support') )
		else:
			pass
		self.seq_feat_data_ = Seq_feat_data_( root.find('Seq-feat_data') )
		if root.find('Seq-feat_ids') is not None:
			self.seq_feat_ids_ = Seq_feat_ids_( root.find('Seq-feat_ids') )
		else:
			pass
		if root.find('Seq-feat_ext') is not None:
			self.seq_feat_ext_ = Seq_feat_ext_( root.find('Seq-feat_ext') )
		else:
			pass
		if root.find('Seq-feat_comment') is not None:
			self.seq_feat_comment_ = Seq_feat_comment_( root.find('Seq-feat_comment') )
		else:
			pass
		self.seq_feat_location_ = Seq_feat_location_( root.find('Seq-feat_location') )
		if root.find('Seq-feat_dbxref') is not None:
			self.seq_feat_dbxref_ = Seq_feat_dbxref_( root.find('Seq-feat_dbxref') )
		else:
			pass
		if root.find('Seq-feat_id') is not None:
			self.seq_feat_id_ = Seq_feat_id_( root.find('Seq-feat_id') )
		else:
			pass
		if root.find('Seq-feat_cit') is not None:
			self.seq_feat_cit_ = Seq_feat_cit_( root.find('Seq-feat_cit') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class User_field_num_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( User_field_num_, self ).__init__()
		self.name = 'User-field_num'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatXref_data( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( SeqFeatXref_data, self ).__init__()
		self.name = 'SeqFeatXref_data'
		self.seqfeatdata = SeqFeatData( root.find('SeqFeatData') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Byte_graph_values_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Byte_graph_values_, self ).__init__()
		self.name = 'Byte-graph_values'
		self.text = root.text
	
	def __call__( self ):
		pass


class Author_is_corr_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Author_is_corr_, self ).__init__()
		self.name = 'Author_is-corr'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['true', 'false']
		self.value = root.get('value')


class Variation_ref_data_note_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_data_note_, self ).__init__()
		self.name = 'Variation-ref_data_note'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seqdesc_maploc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seqdesc_maploc, self ).__init__()
		self.name = 'Seqdesc_maploc'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_parent_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_parent_id__, self ).__init__()
		self.name = 'Variation-ref_parent-id'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_chunk__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Spliced_exon_chunk__, self ).__init__()
		self.name = 'Spliced-exon-chunk'
		#jedna z opcji dla ['Spliced-exon-chunk_product-ins', 'Spliced-exon-chunk_mismatch', 'Spliced-exon-chunk_genomic-ins', 'Spliced-exon-chunk_diag', 'Spliced-exon-chunk_match']
		if 'Spliced-exon-chunk_product-ins' in [ x.tag for x in root.getchildren() ]:
			self.spliced_exon_chunk_product_ins___ = Spliced_exon_chunk_product_ins___( root.find('Spliced-exon-chunk_product-ins') )
		elif 'Spliced-exon-chunk_mismatch' in [ x.tag for x in root.getchildren() ]:
			self.spliced_exon_chunk_mismatch__ = Spliced_exon_chunk_mismatch__( root.find('Spliced-exon-chunk_mismatch') )
		elif 'Spliced-exon-chunk_genomic-ins' in [ x.tag for x in root.getchildren() ]:
			self.spliced_exon_chunk_genomic_ins___ = Spliced_exon_chunk_genomic_ins___( root.find('Spliced-exon-chunk_genomic-ins') )
		elif 'Spliced-exon-chunk_diag' in [ x.tag for x in root.getchildren() ]:
			self.spliced_exon_chunk_diag__ = Spliced_exon_chunk_diag__( root.find('Spliced-exon-chunk_diag') )
		else:
			self.spliced_exon_chunk_match__ = Spliced_exon_chunk_match__( root.find('Spliced-exon-chunk_match') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class DocRef_uid( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( DocRef_uid, self ).__init__()
		self.name = 'DocRef_uid'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_loc_whole_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Seq_loc_whole_, self ).__init__()
		self.name = 'Seq-loc_whole'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Medline_mesh_mp_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_mesh_mp_, self ).__init__()
		self.name = 'Medline-mesh_mp'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Medline_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_qual_, self ).__init__()
		self.name = 'Medline-qual'
		if root.find('Medline-qual_mp') is not None:
			self.medline_qual_mp_ = Medline_qual_mp_( root.find('Medline-qual_mp') )
		else:
			pass
		self.medline_qual_subh_ = Medline_qual_subh_( root.find('Medline-qual_subh') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PRF_block_extra_src__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_block_extra_src__, self ).__init__()
		self.name = 'PRF-block_extra-src'
		self.prf_extrasrc_ = PRF_ExtraSrc_( root.find('PRF-ExtraSrc') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_consequence_E_variation_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	def __init__( self, root ):
		super( Variation_ref_consequence_E_variation_, self ).__init__()
		self.name = 'Variation-ref_consequence_E_variation'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.variation_ref_ = root.find( 'Variation-ref' )
		self.to_evaluate.append( ( 'Variation-ref', '' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PubStatus( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PubStatus, self ).__init__()
		self.name = 'PubStatus'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['received', 'accepted', 'epublish', 'ppublish', 'revised', 'pmc', 'pmcr', 'pubmed', 'pubmedr', 'aheadofprint', 'premedline', 'medline', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Imprint( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Imprint, self ).__init__()
		self.name = 'Imprint'
		if root.find('Imprint_prepub') is not None:
			self.imprint_prepub = Imprint_prepub( root.find('Imprint_prepub') )
		else:
			pass
		if root.find('Imprint_section') is not None:
			self.imprint_section = Imprint_section( root.find('Imprint_section') )
		else:
			pass
		if root.find('Imprint_part-supi') is not None:
			self.imprint_part_supi_ = Imprint_part_supi_( root.find('Imprint_part-supi') )
		else:
			pass
		if root.find('Imprint_pubstatus') is not None:
			self.imprint_pubstatus = Imprint_pubstatus( root.find('Imprint_pubstatus') )
		else:
			pass
		if root.find('Imprint_cprt') is not None:
			self.imprint_cprt = Imprint_cprt( root.find('Imprint_cprt') )
		else:
			pass
		if root.find('Imprint_retract') is not None:
			self.imprint_retract = Imprint_retract( root.find('Imprint_retract') )
		else:
			pass
		if root.find('Imprint_pub') is not None:
			self.imprint_pub = Imprint_pub( root.find('Imprint_pub') )
		else:
			pass
		if root.find('Imprint_part-sup') is not None:
			self.imprint_part_sup_ = Imprint_part_sup_( root.find('Imprint_part-sup') )
		else:
			pass
		if root.find('Imprint_issue') is not None:
			self.imprint_issue = Imprint_issue( root.find('Imprint_issue') )
		else:
			pass
		if root.find('Imprint_pages') is not None:
			self.imprint_pages = Imprint_pages( root.find('Imprint_pages') )
		else:
			pass
		if root.find('Imprint_volume') is not None:
			self.imprint_volume = Imprint_volume( root.find('Imprint_volume') )
		else:
			pass
		if root.find('Imprint_history') is not None:
			self.imprint_history = Imprint_history( root.find('Imprint_history') )
		else:
			pass
		if root.find('Imprint_language') is not None:
			self.imprint_language = Imprint_language( root.find('Imprint_language') )
		else:
			pass
		self.imprint_date = Imprint_date( root.find('Imprint_date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class MolInfo_completeness( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( MolInfo_completeness, self ).__init__()
		self.name = 'MolInfo_completeness'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'complete', 'partial', 'no-left', 'no-right', 'no-ends', 'has-left', 'has-right', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Cit_art_ids_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_art_ids_, self ).__init__()
		self.name = 'Cit-art_ids'
		self.articleidset = ArticleIdSet( root.find('ArticleIdSet') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_seg_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_seg_, self ).__init__()
		self.name = 'Spliced-seg'
		self.spliced_seg_product_type__ = Spliced_seg_product_type__( root.find('Spliced-seg_product-type') )
		self.spliced_seg_exons_ = Spliced_seg_exons_( root.find('Spliced-seg_exons') )
		if root.find('Spliced-seg_product-id') is not None:
			self.spliced_seg_product_id__ = Spliced_seg_product_id__( root.find('Spliced-seg_product-id') )
		else:
			pass
		if root.find('Spliced-seg_genomic-id') is not None:
			self.spliced_seg_genomic_id__ = Spliced_seg_genomic_id__( root.find('Spliced-seg_genomic-id') )
		else:
			pass
		if root.find('Spliced-seg_genomic-strand') is not None:
			self.spliced_seg_genomic_strand__ = Spliced_seg_genomic_strand__( root.find('Spliced-seg_genomic-strand') )
		else:
			pass
		if root.find('Spliced-seg_product-strand') is not None:
			self.spliced_seg_product_strand__ = Spliced_seg_product_strand__( root.find('Spliced-seg_product-strand') )
		else:
			pass
		if root.find('Spliced-seg_product-length') is not None:
			self.spliced_seg_product_length__ = Spliced_seg_product_length__( root.find('Spliced-seg_product-length') )
		else:
			pass
		if root.find('Spliced-seg_modifiers') is not None:
			self.spliced_seg_modifiers_ = Spliced_seg_modifiers_( root.find('Spliced-seg_modifiers') )
		else:
			pass
		if root.find('Spliced-seg_poly-a') is not None:
			self.spliced_seg_poly_a__ = Spliced_seg_poly_a__( root.find('Spliced-seg_poly-a') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_gen_issue_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_gen_issue_, self ).__init__()
		self.name = 'Cit-gen_issue'
		self.text = root.text
	
	def __call__( self ):
		pass


class PRF_block_keywords_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PRF-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PRF_block_keywords_E_, self ).__init__()
		self.name = 'PRF-block_keywords_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Packed_seqpnt_strand_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seqpnt_strand_, self ).__init__()
		self.name = 'Packed-seqpnt_strand'
		self.na_strand_ = Na_strand_( root.find('Na-strand') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Packed_seqint_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	def __init__( self, root ):
		super( Packed_seqint_, self ).__init__()
		self.name = 'Packed-seqint'
		if root.find('Seq-interval') is not None:
			self.seq_interval_ = [ Seq_interval_(element) for element in root.findall('Seq-interval') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Phenotype_clinical_significance_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Phenotype_clinical_significance_, self ).__init__()
		self.name = 'Phenotype_clinical-significance'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'untested', 'non-pathogenic', 'probable-non-pathogenic', 'probable-pathogenic', 'pathogenic', 'drug-response', 'histocompatibility', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Textannot_id_name_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Textannot_id_name_, self ).__init__()
		self.name = 'Textannot-id_name'
		self.text = root.text
	
	def __call__( self ):
		pass


class PCRPrimerSeq( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PCRPrimerSeq, self ).__init__()
		self.name = 'PCRPrimerSeq'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_enum_names_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_enum_names_, self ).__init__()
		self.name = 'Num-enum_names'
		if root.find('Num-enum_names_E') is not None:
			self.num_enum_names_e_ = [ Num_enum_names_E_(element) for element in root.findall('Num-enum_names_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Num_cont_ascending_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_cont_ascending_, self ).__init__()
		self.name = 'Num-cont_ascending'
		#attribute-value: "true"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Seq_align_segs_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Seq_align_segs_, self ).__init__()
		self.name = 'Seq-align_segs'
		#jedna z opcji dla ['Seq-align_segs_dendiag', 'Seq-align_segs_std', 'Seq-align_segs_packed', 'Seq-align_segs_disc', 'Seq-align_segs_denseg', 'Seq-align_segs_spliced', 'Seq-align_segs_sparse']
		if 'Seq-align_segs_dendiag' in [ x.tag for x in root.getchildren() ]:
			self.seq_align_segs_dendiag_ = Seq_align_segs_dendiag_( root.find('Seq-align_segs_dendiag') )
		elif 'Seq-align_segs_std' in [ x.tag for x in root.getchildren() ]:
			self.seq_align_segs_std_ = Seq_align_segs_std_( root.find('Seq-align_segs_std') )
		elif 'Seq-align_segs_packed' in [ x.tag for x in root.getchildren() ]:
			self.seq_align_segs_packed_ = Seq_align_segs_packed_( root.find('Seq-align_segs_packed') )
		elif 'Seq-align_segs_disc' in [ x.tag for x in root.getchildren() ]:
			self.seq_align_segs_disc_ = Seq_align_segs_disc_( root.find('Seq-align_segs_disc') )
		elif 'Seq-align_segs_denseg' in [ x.tag for x in root.getchildren() ]:
			self.seq_align_segs_denseg_ = Seq_align_segs_denseg_( root.find('Seq-align_segs_denseg') )
		elif 'Seq-align_segs_spliced' in [ x.tag for x in root.getchildren() ]:
			self.seq_align_segs_spliced_ = Seq_align_segs_spliced_( root.find('Seq-align_segs_spliced') )
		else:
			self.seq_align_segs_sparse_ = Seq_align_segs_sparse_( root.find('Seq-align_segs_sparse') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Delta_item_multiplier_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Delta_item_multiplier_, self ).__init__()
		self.name = 'Delta-item_multiplier'
		self.text = root.text
	
	def __call__( self ):
		pass


class Medline_entry_gene_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Medline_entry_gene_, self ).__init__()
		self.name = 'Medline-entry_gene'
		if root.find('Medline-entry_gene_E') is not None:
			self.medline_entry_gene_e_ = [ Medline_entry_gene_E_(element) for element in root.findall('Medline-entry_gene_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_somatic_origin_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_somatic_origin_E__, self ).__init__()
		self.name = 'Variation-ref_somatic-origin_E'
		if root.find('Variation-ref_somatic-origin_E_condition') is not None:
			self.variation_ref_somatic_origin_e_condition__ = Variation_ref_somatic_origin_E_condition__( root.find('Variation-ref_somatic-origin_E_condition') )
		else:
			pass
		if root.find('Variation-ref_somatic-origin_E_source') is not None:
			self.variation_ref_somatic_origin_e_source__ = Variation_ref_somatic_origin_E_source__( root.find('Variation-ref_somatic-origin_E_source') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cdregion_gaps( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cdregion_gaps, self ).__init__()
		self.name = 'Cdregion_gaps'
		self.text = root.text
	
	def __call__( self ):
		pass


class Clone_seq_align_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Clone_seq_align_id__, self ).__init__()
		self.name = 'Clone-seq_align-id'
		self.dbtag = Dbtag( root.find('Dbtag') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_date_issue__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_date_issue__, self ).__init__()
		self.name = 'Cit-pat_date-issue'
		self.date = Date( root.find('Date') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_gene_location_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_gene_location_, self ).__init__()
		self.name = 'VariantProperties_gene-location'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['in-gene', 'near-gene-5', 'near-gene-3', 'intron', 'donor', 'acceptor', 'utr-5', 'utr-3', 'in-start-codon', 'in-stop-codon', 'intergenic', 'conserved-noncoding']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class Affil_std_postal_code_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_std_postal_code_, self ).__init__()
		self.name = 'Affil_std_postal-code'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqFeatData_site( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_site, self ).__init__()
		self.name = 'SeqFeatData_site'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['active', 'binding', 'cleavage', 'inhibit', 'modified', 'glycosylation', 'myristoylation', 'mutagenized', 'metal-binding', 'phosphorylation', 'acetylation', 'amidation', 'methylation', 'hydroxylation', 'sulfatation', 'oxidative-deamination', 'pyrrolidone-carboxylic-acid', 'gamma-carboxyglutamic-acid', 'blocked', 'lipid-binding', 'np-binding', 'dna-binding', 'signal-peptide', 'transit-peptide', 'transmembrane-region', 'nitrosylation', 'other']
		self.value = root.get('value')


class Seq_graph_comment_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_graph_comment_, self ).__init__()
		self.name = 'Seq-graph_comment'
		self.text = root.text
	
	def __call__( self ):
		pass


class Variation_ref_somatic_origin_E_condition_object_id___( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_somatic_origin_E_condition_object_id___, self ).__init__()
		self.name = 'Variation-ref_somatic-origin_E_condition_object-id'
		if root.find('Dbtag') is not None:
			self.dbtag = [ Dbtag(element) for element in root.findall('Dbtag') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class DocRef( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Medline'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( DocRef, self ).__init__()
		self.name = 'DocRef'
		self.docref_type = DocRef_type( root.find('DocRef_type') )
		self.docref_uid = DocRef_uid( root.find('DocRef_uid') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Spliced_exon_genomic_id__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	def __init__( self, root ):
		super( Spliced_exon_genomic_id__, self ).__init__()
		self.name = 'Spliced-exon_genomic-id'
		self.seq_id_ = Seq_id_( root.find('Seq-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqFeatData_prot( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqFeatData_prot, self ).__init__()
		self.name = 'SeqFeatData_prot'
		self.prot_ref_ = Prot_ref_( root.find('Prot-ref') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Affil_str( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Affil_str, self ).__init__()
		self.name = 'Affil_str'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_entry_set_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqset'''
	
	def __init__( self, root ):
		super( Seq_entry_set_, self ).__init__()
		self.name = 'Seq-entry_set'
		self.to_evaluate = []#to, co nie jest jeszcze do końca utworzone
		self.bioseq_set_ = root.find( 'Bioseq-set' )
		self.to_evaluate.append( ( 'Bioseq-set', '' ) )
	
	def __call__( self ):
		for element in self.to_evaluate[:]:
			if element[1] in ['*', '+']:
				self.__dict__[ toNameString(element[0]).lower() ] = [ eval( toNameString(element[0]) )( x ) for x in ( self.__dict__[ toNameString(element[0]).lower() ] ) ]
				[ x() for x in self.__dict__[ toNameString(element[0]).lower() ] ]
			else:
				self.__dict__[ toNameString(element[0]).lower() ] = eval( toNameString(element[0]) )( self.__dict__[ toNameString(element[0]).lower()  ] )
				self.__dict__[ toNameString(element[0]).lower() ]()
			self.to_evaluate.remove( element )
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class ModelEvidenceItem( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( ModelEvidenceItem, self ).__init__()
		self.name = 'ModelEvidenceItem'
		if root.find('ModelEvidenceItem_supports-all-exon-combo') is not None:
			self.modelevidenceitem_supports_all_exon_combo___ = ModelEvidenceItem_supports_all_exon_combo___( root.find('ModelEvidenceItem_supports-all-exon-combo') )
		else:
			pass
		if root.find('ModelEvidenceItem_full-length') is not None:
			self.modelevidenceitem_full_length_ = ModelEvidenceItem_full_length_( root.find('ModelEvidenceItem_full-length') )
		else:
			pass
		if root.find('ModelEvidenceItem_exon-count') is not None:
			self.modelevidenceitem_exon_count_ = ModelEvidenceItem_exon_count_( root.find('ModelEvidenceItem_exon-count') )
		else:
			pass
		if root.find('ModelEvidenceItem_exon-length') is not None:
			self.modelevidenceitem_exon_length_ = ModelEvidenceItem_exon_length_( root.find('ModelEvidenceItem_exon-length') )
		else:
			pass
		self.modelevidenceitem_id = ModelEvidenceItem_id( root.find('ModelEvidenceItem_id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class VariantProperties_project_data_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( VariantProperties_project_data_E_, self ).__init__()
		self.name = 'VariantProperties_project-data_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class SeqTable_multi_data_bytes_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_multi_data_bytes_E__, self ).__init__()
		self.name = 'SeqTable-multi-data_bytes_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gb_qual_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gb_qual_, self ).__init__()
		self.name = 'Gb-qual'
		self.gb_qual_qual_ = Gb_qual_qual_( root.find('Gb-qual_qual') )
		self.gb_qual_val_ = Gb_qual_val_( root.find('Gb-qual_val') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Population_data_chromosomes_tested__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_chromosomes_tested__, self ).__init__()
		self.name = 'Population-data_chromosomes-tested'
		self.text = root.text
	
	def __call__( self ):
		pass


class Cit_art_from_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	def __init__( self, root ):
		super( Cit_art_from_, self ).__init__()
		self.name = 'Cit-art_from'
		#jedna z opcji dla ['Cit-art_from_book', 'Cit-art_from_proc', 'Cit-art_from_journal']
		if 'Cit-art_from_book' in [ x.tag for x in root.getchildren() ]:
			self.cit_art_from_book_ = Cit_art_from_book_( root.find('Cit-art_from_book') )
		elif 'Cit-art_from_proc' in [ x.tag for x in root.getchildren() ]:
			self.cit_art_from_proc_ = Cit_art_from_proc_( root.find('Cit-art_from_proc') )
		else:
			self.cit_art_from_journal_ = Cit_art_from_journal_( root.find('Cit-art_from_journal') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class PDB_replace_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: PDB-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( PDB_replace_, self ).__init__()
		self.name = 'PDB-replace'
		self.pdb_replace_date_ = PDB_replace_date_( root.find('PDB-replace_date') )
		self.pdb_replace_ids_ = PDB_replace_ids_( root.find('PDB-replace_ids') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_phenotype_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_phenotype_, self ).__init__()
		self.name = 'Variation-ref_phenotype'
		if root.find('Phenotype') is not None:
			self.phenotype = [ Phenotype(element) for element in root.findall('Phenotype') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Int_graph_axis_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqres'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Int_graph_axis_, self ).__init__()
		self.name = 'Int-graph_axis'
		self.text = root.text
	
	def __call__( self ):
		pass


class PCRReaction( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-BioSource'''
	
	def __init__( self, root ):
		super( PCRReaction, self ).__init__()
		self.name = 'PCRReaction'
		if root.find('PCRReaction_forward') is not None:
			self.pcrreaction_forward = PCRReaction_forward( root.find('PCRReaction_forward') )
		else:
			pass
		if root.find('PCRReaction_reverse') is not None:
			self.pcrreaction_reverse = PCRReaction_reverse( root.find('PCRReaction_reverse') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class SeqTable_sparse_index_indexes__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-SeqTable'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( SeqTable_sparse_index_indexes__, self ).__init__()
		self.name = 'SeqTable-sparse-index_indexes'
		if root.find('SeqTable-sparse-index_indexes_E') is not None:
			self.seqtable_sparse_index_indexes_e__ = [ SeqTable_sparse_index_indexes_E__(element) for element in root.findall('SeqTable-sparse-index_indexes_E') ]
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_point_point_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqloc'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Seq_point_point_, self ).__init__()
		self.name = 'Seq-point_point'
		self.text = root.text
	
	def __call__( self ):
		pass


class Date_std_month_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Date_std_month_, self ).__init__()
		self.name = 'Date-std_month'
		self.text = root.text
	
	def __call__( self ):
		pass


class Trna_ext_aa_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-RNA'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Trna_ext_aa_, self ).__init__()
		self.name = 'Trna-ext_aa'
		#jedna z opcji dla ['Trna-ext_aa_ncbi8aa', 'Trna-ext_aa_ncbieaa', 'Trna-ext_aa_iupacaa', 'Trna-ext_aa_ncbistdaa']
		if 'Trna-ext_aa_ncbi8aa' in [ x.tag for x in root.getchildren() ]:
			self.trna_ext_aa_ncbi8aa_ = Trna_ext_aa_ncbi8aa_( root.find('Trna-ext_aa_ncbi8aa') )
		elif 'Trna-ext_aa_ncbieaa' in [ x.tag for x in root.getchildren() ]:
			self.trna_ext_aa_ncbieaa_ = Trna_ext_aa_ncbieaa_( root.find('Trna-ext_aa_ncbieaa') )
		elif 'Trna-ext_aa_iupacaa' in [ x.tag for x in root.getchildren() ]:
			self.trna_ext_aa_iupacaa_ = Trna_ext_aa_iupacaa_( root.find('Trna-ext_aa_iupacaa') )
		else:
			self.trna_ext_aa_ncbistdaa_ = Trna_ext_aa_ncbistdaa_( root.find('Trna-ext_aa_ncbistdaa') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Program_id_version_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Program_id_version_, self ).__init__()
		self.name = 'Program-id_version'
		self.text = root.text
	
	def __call__( self ):
		pass


class Num_ref_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Num_ref_type_, self ).__init__()
		self.name = 'Num-ref_type'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'sources', 'aligns']
		self.value = root.get('value')


class Pubdesc( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Pubdesc, self ).__init__()
		self.name = 'Pubdesc'
		if root.find('Pubdesc_poly-a') is not None:
			self.pubdesc_poly_a_ = Pubdesc_poly_a_( root.find('Pubdesc_poly-a') )
		else:
			pass
		if root.find('Pubdesc_numexc') is not None:
			self.pubdesc_numexc = Pubdesc_numexc( root.find('Pubdesc_numexc') )
		else:
			pass
		if root.find('Pubdesc_reftype') is not None:
			self.pubdesc_reftype = Pubdesc_reftype( root.find('Pubdesc_reftype') )
		else:
			pass
		if root.find('Pubdesc_maploc') is not None:
			self.pubdesc_maploc = Pubdesc_maploc( root.find('Pubdesc_maploc') )
		else:
			pass
		if root.find('Pubdesc_align-group') is not None:
			self.pubdesc_align_group_ = Pubdesc_align_group_( root.find('Pubdesc_align-group') )
		else:
			pass
		if root.find('Pubdesc_seq-raw') is not None:
			self.pubdesc_seq_raw_ = Pubdesc_seq_raw_( root.find('Pubdesc_seq-raw') )
		else:
			pass
		if root.find('Pubdesc_name') is not None:
			self.pubdesc_name = Pubdesc_name( root.find('Pubdesc_name') )
		else:
			pass
		if root.find('Pubdesc_num') is not None:
			self.pubdesc_num = Pubdesc_num( root.find('Pubdesc_num') )
		else:
			pass
		if root.find('Pubdesc_fig') is not None:
			self.pubdesc_fig = Pubdesc_fig( root.find('Pubdesc_fig') )
		else:
			pass
		self.pubdesc_pub = Pubdesc_pub( root.find('Pubdesc_pub') )
		if root.find('Pubdesc_comment') is not None:
			self.pubdesc_comment = Pubdesc_comment( root.find('Pubdesc_comment') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Seq_annot_data_seq_table__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	def __init__( self, root ):
		super( Seq_annot_data_seq_table__, self ).__init__()
		self.name = 'Seq-annot_data_seq-table'
		self.seq_table_ = Seq_table_( root.find('Seq-table') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_data_set_type_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_data_set_type_, self ).__init__()
		self.name = 'Variation-ref_data_set_type'
		#attribute-value: #IMPLIED
		assert root.get('value') in ['unknown', 'compound', 'products', 'haplotype', 'genotype', 'mosaic', 'individual', 'population', 'alleles', 'package', 'other']
		if root.get('value') is not None:
			self.value = root.get('value')
		self.text = root.text

class GB_block_extra_accessions_E__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: GenBank-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( GB_block_extra_accessions_E__, self ).__init__()
		self.name = 'GB-block_extra-accessions_E'
		self.text = root.text
	
	def __call__( self ):
		pass


class Gene_ref_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Gene'''
	
	def __init__( self, root ):
		super( Gene_ref_, self ).__init__()
		self.name = 'Gene-ref'
		if root.find('Gene-ref_pseudo') is not None:
			self.gene_ref_pseudo_ = Gene_ref_pseudo_( root.find('Gene-ref_pseudo') )
		else:
			pass
		if root.find('Gene-ref_locus') is not None:
			self.gene_ref_locus_ = Gene_ref_locus_( root.find('Gene-ref_locus') )
		else:
			pass
		if root.find('Gene-ref_desc') is not None:
			self.gene_ref_desc_ = Gene_ref_desc_( root.find('Gene-ref_desc') )
		else:
			pass
		if root.find('Gene-ref_syn') is not None:
			self.gene_ref_syn_ = Gene_ref_syn_( root.find('Gene-ref_syn') )
		else:
			pass
		if root.find('Gene-ref_allele') is not None:
			self.gene_ref_allele_ = Gene_ref_allele_( root.find('Gene-ref_allele') )
		else:
			pass
		if root.find('Gene-ref_maploc') is not None:
			self.gene_ref_maploc_ = Gene_ref_maploc_( root.find('Gene-ref_maploc') )
		else:
			pass
		if root.find('Gene-ref_locus-tag') is not None:
			self.gene_ref_locus_tag__ = Gene_ref_locus_tag__( root.find('Gene-ref_locus-tag') )
		else:
			pass
		if root.find('Gene-ref_formal-name') is not None:
			self.gene_ref_formal_name__ = Gene_ref_formal_name__( root.find('Gene-ref_formal-name') )
		else:
			pass
		if root.find('Gene-ref_db') is not None:
			self.gene_ref_db_ = Gene_ref_db_( root.find('Gene-ref_db') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Annot_id_local_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Sequence'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Annot_id_local_, self ).__init__()
		self.name = 'Annot-id_local'
		self.object_id_ = Object_id_( root.find('Object-id') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Variation_ref_consequence_E_note_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Variation_ref_consequence_E_note_, self ).__init__()
		self.name = 'Variation-ref_consequence_E_note'
		self.text = root.text
	
	def __call__( self ):
		pass


class Population_data_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Variation'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Population_data_, self ).__init__()
		self.name = 'Population-data'
		if root.find('Population-data_flags') is not None:
			self.population_data_flags_ = Population_data_flags_( root.find('Population-data_flags') )
		else:
			pass
		if root.find('Population-data_sample-ids') is not None:
			self.population_data_sample_ids__ = Population_data_sample_ids__( root.find('Population-data_sample-ids') )
		else:
			pass
		if root.find('Population-data_genotype-frequency') is not None:
			self.population_data_genotype_frequency__ = Population_data_genotype_frequency__( root.find('Population-data_genotype-frequency') )
		else:
			pass
		if root.find('Population-data_chromosomes-tested') is not None:
			self.population_data_chromosomes_tested__ = Population_data_chromosomes_tested__( root.find('Population-data_chromosomes-tested') )
		else:
			pass
		self.population_data_population_ = Population_data_population_( root.find('Population-data_population') )
		if root.find('Population-data_allele-frequency') is not None:
			self.population_data_allele_frequency__ = Population_data_allele_frequency__( root.find('Population-data_allele-frequency') )
		else:
			pass
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class Cit_pat_app_number__( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Biblio'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Cit_pat_app_number__, self ).__init__()
		self.name = 'Cit-pat_app-number'
		self.text = root.text
	
	def __call__( self ):
		pass


class Seq_feat_support_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqfeat'''
	
	def __init__( self, root ):
		super( Seq_feat_support_, self ).__init__()
		self.name = 'Seq-feat_support'
		self.seqfeatsupport = SeqFeatSupport( root.find('SeqFeatSupport') )
	
	def __call__( self ):
		for element in self.__dict__:
			if isinstance( self.__dict__[element], BaseXML ):
				try:
					self.__dict__[element]()
				except TypeError: #not callable
					pass
			elif type( self.__dict__[element] ) == list and element!='to_evaluate':
				for x in range( len( self.__dict__[ element ] ) ):
					sub_element = self.__dict__[ element ][x]
					if type( sub_element ) == etree._Element:
						pdb.set_trace()
						self.__dict__[ element ][x] = eval( toNameString(sub_element.tag) )
						self.__dict__[ element ][x]()
					if isinstance( sub_element, BaseXML ):
						sub_element()


class EMBL_block_class_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: EMBL-General'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( EMBL_block_class_, self ).__init__()
		self.name = 'EMBL-block_class'
		#attribute-value: #REQUIRED
		assert root.get('value') in ['not-set', 'standard', 'unannotated', 'other']
		self.value = root.get('value')


class Gene_ref_pseudo_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Attribute
	pochodzi z modułu: NCBI-Gene'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Gene_ref_pseudo_, self ).__init__()
		self.name = 'Gene-ref_pseudo'
		#attribute-value: "false"
		pdb.set_trace()#jeszcze się z tym nie spotkałem i nie wiem, jak to ma wyglądać
		assert root.get('value') in ['true', 'false']
class Packed_seg_starts_E_( BaseXML, DictContainsInterface ):
	'''Klasa wygenerowana automatycznie
	typ: Element
	pochodzi z modułu: NCBI-Seqalign'''
	
	#jest gałęzią końcową
	def __init__( self, root ):
		super( Packed_seg_starts_E_, self ).__init__()
		self.name = 'Packed-seg_starts_E'
		self.text = root.text
	
	def __call__( self ):
		pass


def toNameString( in_string ):
	'''Pobiera stringa. Zwraca stringa, w którym wszystkie wystąpienia '-' zamieniono na '_'. 
	Na końcu tego stringa dopisujemy tyle '_', ile wykonano podmian'''	
	how_much = in_string.count( '-' )
	out_string = in_string.replace( '-', '_' )
	out_string += '_'*how_much
	return out_string

def processFile( f_path ):
	'''Uruchamia obróbkę danego pliku. Zwraca sparsowany plik'''
	tree = etree.parse( f_path )
	root = Bioseq_set_( tree.getroot() )
	root()
	return root

if __name__ == '__main__':
	import os
	for f_name in os.listdir( seq_dir ):
		print f_name
		processFile( seq_dir + f_name )
