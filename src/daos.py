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

# opracowano na podstawie materiałów ze strony
# https://excelicious.wordpress.com/2010/04/23/python-data-access-patterns-part-1/

import apsw
import os

from entities import *
from constants import *

from commonFunctions import createDirIfNotExists

DB_FILE_NAMES = [str(i) for i in range(10)]


def sql_trace(stmt, bindings):
    'Echoes all SQL executed'
    print "SQL:", stmt
    if bindings:
        print "Bindings:", bindings
    return True


class VirtualConnection(object):
    def __init__(self, directory, filenames=DB_FILE_NAMES):
        """

        :param directory: directory, in which database file exist
        :param filenames: names of the db files
        :return:
        """
        super(VirtualConnection, self).__init__()
        self.connections = []
        for s in filenames:
            fname = os.path.join(directory, s)
            if not os.path.exists(fname):
                open(fname, 'w').close()
            self.connections.append(apsw.Connection(fname, statementcachesize=50000))

    def __iter__(self):
        return iter(self.connections)

    def cursor(self):
        return VirtualCursor(self)

    def changes(self):
        return sum([conn.changes() for conn in self.connections])


class VirtualCursor(object):
    def __init__(self, virtual_connection):
        super(VirtualCursor, self).__init__()
        self.cursors = [conn.cursor() for conn in virtual_connection]
        for cur in self.cursors:
            cur.execute("PRAGMA synchronous = OFF")
            cur.execute("PRAGMA journal_mode = MEMORY")

    def setexectrace(self, sql_trace):
        for cur in self.cursors:
            cur.setexectrace(sql_trace)

    def read(self, *args):
        results = []
        for cur in self.cursors:
            cur.execute(*args)
            res = cur.fetchall()
            if res:
                results.extend(res)
        return results

    def execute(self, statements, bindings=None):
        """Only for operations, that modify database and should be performed on all databases"""
        i = 0
        for cur in self.cursors:
            i += 1
            cur.execute(statements, bindings)

    def executemany(self, statements, sequenceofbindings, primary_key='tax_id'):
        """For operations, that should modify database and be performed only on some of the databases"""
        l = [[] for x in range(len(self.cursors))]
        for binding in sequenceofbindings:
            l[int(binding[primary_key][-1])].append(binding)
        for i in range(len(self.cursors)):
            self.cursors[i].executemany(statements, tuple(l[i]))

    def executeone(self, statement, sequenceofbindings, primary_key='tax_id'):
        """For operations, that should modify database and be performed only on one of the databases"""
        cur = self.cursors[int(sequenceofbindings[0][primary_key][-1])]
        cur.execute(statement)


class DataAccessor(object):
    '''
    Class to handle data access using apsw sqlite wrapper
    '''

    def __init__(self, dbpath, echo=False):
        super(DataAccessor, self).__init__()
        try:
            if os.path.exists(dbpath):
                assert os.path.isdir(dbpath)
                self.conn = VirtualConnection(dbpath)
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
                raise NotImplementedError('ORDER BY not implemented yet')
            # stmt += "\nORDER BY "
            # stmt += ', '.join([col[0] + ' ' + col[1] \
            # 	                for col in sort_cols])

            stmt += ';'

            # submit and return results
            args = where_row and (stmt, where_row) or (stmt,)
            results = columns and [dict(zip(columns, row)) \
                                   for row in self.cur.read(*args)] \
                      or [row for row in self.cur.read(*args)]

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

            if len(values) == 1:
                self.cur.execute('BEGIN IMMEDIATE')
            else:
                self.cur.executeone('BEGIN IMMEDIATE', values)
            self.cur.executemany(stmt, values)
            if len(values) == 1:
                self.cur.execute('COMMIT')
            else:
                self.cur.executeone('COMMIT', values)

            return self.conn.changes()

        except apsw.SQLError as sql:
            print 'Error in SQL submitted:', sql
            print 'SQL:', stmt
            if len(values) == 1:
                self.cur.execute('ROLLBACK')
            else:
                self.cur.executeone('ROLLBACK', values)

        except apsw.Error as error:
            print 'APSW Error: ', error
            if len(values) == 1:
                self.cur.execute('ROLLBACK')
            else:
                self.cur.executeone('ROLLBACK', values)

        except Exception as error:
            print 'Error submitting insert:', error
            if len(values) == 1:
                self.cur.execute('ROLLBACK')
            else:
                self.cur.executeone('ROLLBACK', values)


class SpeciesDAO(DataAccessor):
    '''Klasa dostępu do danych z NCBI Taxonomy'''

    def __init__(self, db_path=database_path, echo=False):
        createDirIfNotExists(db_path)
        super(SpeciesDAO, self).__init__(db_path, echo=echo)
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Species( tax_id VARCHAR NOT NULL PRIMARY KEY, name VARCHAR NOT NULL, lineage VARCHAR NOT NULL );")

    def create(self, species):
        '''Wstawia obiekt typu species do bazy'''
        insert_dict = {key: str(val) for key, val in species.__dict__.iteritems()}
        self.createFromListOfDicts([insert_dict])

        # super( SpeciesDAO, self ).insert( 'Species', [ insert_dict ] )

    def createFromListOfDicts(self, in_list):
        '''Wstawia dane do bazy, przyjmuje listę słownik typu {'tax_id':'id', name:'n', 'lineage':'l'}'''
        super(SpeciesDAO, self).insert('Species', in_list)

    def read(self, where_dict=None, columns=None, sort_cols=None):
        res = super(SpeciesDAO, self).read(table='Species', where_row=where_dict, columns=None, sort_cols=None)
        if res:
            return [Species.fromIterable(r) for r in res]
        return []

    def clear(self):
        try:
            self.cur.execute('BEGIN IMMEDIATE')
            self.cur.execute('DELETE FROM Species;')
            self.cur.execute('COMMIT')
            return self.conn.changes()
        except apsw.Error as error:
            print 'APSW Error: ', error
            self.cur.execute('ROLLBACK')

        except Exception as error:
            print 'Error submitting insert:', error
            self.cur.execute('ROLLBACK')


if __name__ == '__main__':
    s1 = Species.fromStrings('291867', 'Holocola triangulana',
                             'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Endopterygota; Amphiesmenoptera; Lepidoptera; Glossata; Neolepidoptera; Heteroneura; Ditrysia; Apoditrysia; Tortricoidea; Tortricidae; Olethreutinae; Eucosmini; Holocola')
    s2 = Species.fromStrings('291866', 'Holocola tranquilla',
                             'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Endopterygota; Amphiesmenoptera; Lepidoptera; Glossata; Neolepidoptera; Heteroneura; Ditrysia; Apoditrysia; Tortricoidea; Tortricidae; Olethreutinae; Eucosmini; Holocola')
    s3 = Species.fromStrings('291865', 'Holocola thalassinana',
                             'cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Protostomia; Ecdysozoa; Panarthropoda; Arthropoda; Mandibulata; Pancrustacea; Hexapoda; Insecta; Dicondylia; Pterygota; Neoptera; Endopterygota; Amphiesmenoptera; Lepidoptera; Glossata; Neolepidoptera; Heteroneura; Ditrysia; Apoditrysia; Tortricoidea; Tortricidae; Olethreutinae; Eucosmini; Holocola')
    species_dao = SpeciesDAO()
    print "czyścimy"
    species_dao.clear()
    print "dodajemy"
    species_dao.create(s3)
    species_dao.create(s2)
    species_dao.create(s1)
    print "czytamy"
    print species_dao.read()
    print "czytamy"
    print species_dao.read(where_dict={'name': 'Holocola thalassinana'})
    print "czyścimy"
    species_dao.clear()
