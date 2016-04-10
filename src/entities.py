#!/usr/bin/python
# -*- coding: utf-8 -*-

class BaseEntity( object ):
	
	def __init__( self ):
		super( BaseEntity, self ).__init__()
	
	def __repr__( self ):
		return repr( self.__dict__ )


class Species( BaseEntity ):
	'''Opisuje gatunek na podstawie danych z NCBI Taxonomy'''
	
	def __init__( self, in_dict ):
		'''Argumenty: in_dict zawiera klucze tax_id, name, lineage
			- tax_id - id gatunku z bazy NCBI Taxonomy
			- name - nazwa łacińska
			- lineage - lineage w postaci 'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Orthopteroidea; Dictyoptera; Isoptera; Termitidae; Termitinae; Amitermes group; Microcerotermes' '''
		super( Species, self ).__init__()
		self.tax_id = in_dict[ 'tax_id' ] 
		self.name = in_dict [ 'name' ] 
		self.lineage = in_dict [ 'lineage' ]
	
	@classmethod
	def fromIterable( cls, iterable ):
		'''Zakładamy, że wartości w iterable są poukładane w odpowiedniej kolejności'''
		obj_dict = {}
		obj_dict[ 'tax_id' ] = iterable[0]
		obj_dict [ 'name' ] = iterable[1]
		obj_dict [ 'lineage' ] = eval( iterable[2] )
		return cls( obj_dict )
	
	@classmethod
	def fromStrings( cls, tax_id, name, lineage ):
		obj_dict = {}
		obj_dict[ 'tax_id' ] = tax_id
		obj_dict [ 'name' ] = name
		obj_dict [ 'lineage' ] = lineage.split( '; ' )
		return cls( obj_dict )
