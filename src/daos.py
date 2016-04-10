#!/usr/bin/python
# -*- coding: utf-8 -*-

# opracowano na podstawie materiałów ze strony
# https://excelicious.wordpress.com/2010/04/23/python-data-access-patterns-part-1/

import apsw
import os

from entities import *
from constants import *

from commonFunctions import createFileIfNotExists
 
def sql_trace(stmt, bindings):
    'Echoes all SQL executed'
    print "SQL:", stmt
    if bindings:
        print "Bindings:", bindings
    return True
 
class DataAccessor(object):
	'''
	Class to handle data access using apsw sqlite wrapper
	'''
	def __init__(self, dbpath, echo=False):
		super( DataAccessor, self ).__init__()
		try:
		    if os.path.exists(dbpath):
		        self.conn = apsw.Connection(dbpath)
		        self.cur = self.conn.cursor()
		        if echo:
		            self.cur.setexectrace(sql_trace)
		    else:
		        raise IOError('Database not found: ' + dbpath)
		except apsw.CantOpenError as detail:
		    print "Unable to open db file: ", dbpath, detail
		    raise

	def read(self, table, columns=None, where_row=None, sort_cols=None):
		'''Executes a SELECT statement against table.

		Arguments:
		table                 -- name of the table to be read
		columns (optional)    -- list of columns to be read
		                      from table
		where_row (optional)  -- dict used to build WHERE
		                      clause
		sort_cols (optional)  -- list of (column, order) pairs
		                      used to specify order of the
		                      rows returned. Needs to be of
		                      the form ('<column>', 'ASC'|'DESC')

		Returns: rows returned from the SELECT statement.
		'''
		try:
			stmt = 'SELECT '
			if columns:
				stmt += ', '.join(columns)
			else:
				stmt += '*'

			# from clause
			stmt += "\nFROM " + table

			# where clause
			if where_row:
				stmt += "\nWHERE "
				stmt += "\n  AND ".join([col + "=:" + col \
					                for col in where_row])

			# order clause
			if sort_cols:
				stmt += "\nORDER BY "
				stmt += ', '.join([col[0] + ' ' + col[1] \
					                for col in sort_cols])

			stmt += ';'

			# submit and return results
			args = where_row and (stmt, where_row) or (stmt,)
			results = columns and [dict(zip(columns, row)) \
				for row in self.cur.execute(*args)] \
				or [row for row in self.cur.execute(*args)]

			return results

		except apsw.SQLError as sql:
			print 'Error in SQL submitted:', sql
			print 'SQL:', stmt
			if where_row:
				print 'Bindings:', where_row

		except apsw.Error as error:
			print 'APSW Error: ', error

		except Exception as error:
			print 'Error reading from database:', error

	def insert(self, table, values):
		'''Executes an INSERT statement against table.

		Arguments:
		table           -- name of the table to be written to
		values          -- list of rows (dicts) to be inserted

		Returns: None
		'''
		try:
			# build list of column names
			cols = values[0].keys()

			# generate insert statement
			stmt = 'INSERT INTO ' + table + ' ('
			stmt += ', '.join(cols)
			stmt += ') VALUES ('
			stmt += ', '.join([":%s" % col for col in cols])
			stmt += ')'
			
			# submit

			self.cur.execute('BEGIN IMMEDIATE')
			self.cur.executemany(stmt, values)
			self.cur.execute('COMMIT')

			return self.conn.changes()

		except apsw.SQLError as sql:
			print 'Error in SQL submitted:', sql
			print 'SQL:', stmt
			self.cur.execute('ROLLBACK')

		except apsw.Error as error:
			print 'APSW Error: ', error
			self.cur.execute('ROLLBACK')

		except Exception as error:
			print 'Error submitting insert:', error
			self.cur.execute('ROLLBACK')


class SpeciesDAO( DataAccessor ):
	'''Klasa dostępu do danych z NCBI Taxonomy'''
	
	def __init__( self, db_path=database_path+'basic.db', echo=False ):
		createFileIfNotExists( db_path )
		super( SpeciesDAO, self ).__init__( db_path, echo=echo )
		self.cur.execute( "CREATE TABLE IF NOT EXISTS Species( tax_id VARCHAR NOT NULL PRIMARY KEY, name VARCHAR NOT NULL, lineage VARCHAR NOT NULL );" )
	
	def create( self, species ):
		'''Wstawia obiekt typu species do bazy'''
		insert_dict = { key: str(val) for key, val in species.__dict__.iteritems() }
		self.createFromListOfDicts( [insert_dict] )
		#super( SpeciesDAO, self ).insert( 'Species', [ insert_dict ] )
	
	def createFromListOfDicts( self, in_list ):
		'''Wstawia dane do bazy, przyjmuje listę słownik typu {'tax_id':'id', name:'n', 'lineage':'l'}'''
		super( SpeciesDAO, self ).insert( 'Species', in_list )
		
	def read( self, where_dict = None, columns=None, sort_cols=None ):
		res = super( SpeciesDAO, self ).read( table='Species', where_row=where_dict, columns=None, sort_cols=None )
		if res:
			return [ Species.fromIterable( r ) for r in res ]
		return []
	
	def clear( self ):
		try:
			self.cur.execute('BEGIN IMMEDIATE' )
			self.cur.execute( 'DELETE FROM Species;' )
			self.cur.execute('COMMIT')

			return self.conn.changes()
		except apsw.Error as error:
			print 'APSW Error: ', error
			self.cur.execute('ROLLBACK')

		except Exception as error:
			print 'Error submitting insert:', error
			self.cur.execute('ROLLBACK')

if __name__ == '__main__':
	s1 = Species.fromStrings( '291867', 'Holocola triangulana', 'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Endopterygota; Amphiesmenoptera; Lepidoptera; Glossata; Neolepidoptera; Heteroneura; Ditrysia; Apoditrysia; Tortricoidea; Tortricidae; Olethreutinae; Eucosmini; Holocola' )
	s2 = Species.fromStrings( '291866', 'Holocola tranquilla', 'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Endopterygota; Amphiesmenoptera; Lepidoptera; Glossata; Neolepidoptera; Heteroneura; Ditrysia; Apoditrysia; Tortricoidea; Tortricidae; Olethreutinae; Eucosmini; Holocola' )
	s3 = Species.fromStrings( '291865', 'Holocola thalassinana', 'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Endopterygota; Amphiesmenoptera; Lepidoptera; Glossata; Neolepidoptera; Heteroneura; Ditrysia; Apoditrysia; Tortricoidea; Tortricidae; Olethreutinae; Eucosmini; Holocola' )
	species_dao = SpeciesDAO()
	print "czyścimy"
	species_dao.clear()
	print "dodajemy"
	species_dao.create( s3 )
	print "czytamy"
	print species_dao.read()
	print "czytamy"
	print species_dao.read(where_dict = {'name':'Holocola thalassinana'})
	print "czyścimy"
	species_dao.clear()
