#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="wojtek"
__date__ ="$2012-09-04 09:26:58$"

import pdb

from lxml import etree

from commonFunctions import constantIfProper
#from HandlerOfParsingExceptions import getAndSaveErr

class EqualityInterface( object ):
	
	def __init__( self ):
		super( EqualityInterface, self ).__init__()

	def __repr__( self ):
		return str( self.__dict__ )
	
	def __eq__(self, other):
		return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
	
	def __ne__(self, other):
		return not self.__eq__(other)

class BaseXML( object ):
	'''Do wypisywania w postaci XML'''
	
	def __init__( self ):
		super( BaseXML, self ).__init__()
	
	def toXML( self ):
		'''Returns XML representation of the object'''
		if 'name' in self.__dict__:
			name = self.name
		else:
			name = type( self ).__name__
		#import pdb
		root = etree.Element( name )
		#pdb.set_trace()
		for key, val in self.__dict__.iteritems():
			if key == 'name':
				continue
			elif key == 'text':
				root.text = val
			elif type( val ) == bool or type( val ) == str or not val:
				child = etree.SubElement( root, key )
				child.text = str( val )
			elif type( val ) == list or type( val ) == tuple:
				child = etree.SubElement( root, key )
				for i in range( len( val ) ):
					element = val[i]
					sub_child = etree.SubElement( child, '%s_%d' % ( key, i ) )
					if key == 'text':
						sub_child.text = element
					if type( element ) == str:
						#pdb.set_trace()
						sub_child.text = element
					#elif type( element ) == tuple or not element:
					elif type( element ) == tuple or element is None:
						sub_child.text = str( element )
					else:
						#pdb.set_trace()
						sub_child.append( element.toXML() )
			elif type( val ) == dict:
				child = etree.SubElement( root, key )
				for k, v in val.iteritems():
					try:
						sub_child = etree.SubElement( child, k )
					except ValueError:
						#gdy k zaczyna sie od cyfry
						sub_child = etree.SubElement( child, '_%s'%k )
					if type( v ) == dict:
						for subk, subv in v.iteritems():
							sub_sub_child = etree.SubElement( sub_child, subk )
							sub_sub_child.text = str( subv )
					elif isinstance(v, (int, long, float, complex)):
						sub_child.text = str( v )
					elif v is None:
						sub_child.text = str( v )
					else:
						pdb.set_trace()
			elif isinstance(val, (int, long, float, complex)) or val is None:
				child = etree.SubElement( root, key )
				child.text = str( val )
			else:
				pdb.set_trace()
				root.append( val.toXML() )
		#print etree.tostring( root, pretty_print=True )
		#pdb.set_trace()
		return root
	
	def __repr__( self ):
		return etree.tostring( self.toXML(), pretty_print=True )

class Base(object):
    #should't be instantialized

    def __init__(self):
        super(Base, self).__init__()

    def __repr__(self):
        ret_str=''
        for key in self.__dict__:
            ret_str+="%s=%s, "%(key, self.__dict__[key])
        return ret_str[:-2]

#hmm a moze po prostu wyrzucać błąd gdy podajemy kiepskie wartości

class AType(Base):
    #should't be instantialized

    def __init__(self, proper):
        super(AType, self).__init__()
        self.__proper=bool(proper)

    def __nonzero__(self):
        return self.__proper

    def __repr__(self):
        ret_str=''
        for key in self.__dict__:
            if not key.endswith('__proper'):
                ret_str+="%s=%s, "%(key, self.__dict__[key])
        return ret_str[:-2]


class MyException( Exception ):
	pass


class UnexpectedValueException(Exception):
    pass


class DictContainsInterface:
	
	def __init__( self ):
		super( DictContainsInterface, self ).__init__()
	
	def __contains__( self, key ):
		return key in self.__dict__

##############################    ID classes  ##################################
class ID(AType):
    "Klasa nadrzędna dla wszystkich typów ID"

    def __init__(self, id):
        super(ID, self).__init__(id)
        try:
            self.__id = int(id)
        except ValueError:
            #gdy nie jest liczbą, np. 'NC_015631'
            self.__id = id

    @constantIfProper
    def ID(self):
        return self.__id

    def __str__(self):
        raise NotImplementedError("You shouldn't instantiate this class")

class TextSeqId(ID):
    #typu NC_010384.1

    def __init__(self, id, version):
        super(TextSeqId, self).__init__(id)
        self.__version = int(version)

    @constantIfProper
    def version(self):
        return self.__version

    @classmethod
    def fromDict(cls, a_dict):
        #a_dict - słownik od Seq-id
        root=a_dict['Seq-id_other']['Textseq-id']
        return cls(root['Textseq-id_accession'], root['Textseq-id_version'])

    def __str__(self):
        return "Text_id=%s.%d"%(self.ID, self.__version)

class SeqId(ID):
    #gi

    def __init__(self, id):
        super(SeqId, self).__init__(id)
    
    def __str__(self):
        return "gi=%d"%self.ID

    @classmethod
    def fromDict(cls, a_dict):
        #a_dict - słownik od Seq-id
        return cls(a_dict['Seq-id_gi'])
        '''try:
        	return cls(a_dict['Seq-id_gi'])
        except KeyError:
        	getAndSaveErr( SeqId('to tylko test') )'''

class DbId(ID):
    #Dbtag

    def __init__(self, id, db):
        #db - database
        super(DbId, self).__init__(id)
        self.__db=db

    @constantIfProper
    def db(self):
        return self.__db

    @classmethod
    def fromDict(cls, a_dict):
        #a_dict - słownik od Seq-id
        root=a_dict['Seq-id_general']['Dbtag']
        return cls(root['Dbtag_tag']['Object-id']['Object-id_id'], root['Dbtag_db'])

    def __str__(self):
        return "database=%s, id=%s"%(self.__db, self.ID)

##############################    Region classes  ##############################

class Bounds (AType):
    '''Ta klasa ma być spójna, nie ma sensu pobierać jednego ze składników jesli nie sa ustawione inne'''

    def __init__(self, from_, to, OK=True):
        if from_>=0 and to>=0 and OK:
            super(Bounds, self).__init__(True)
            self.__from=int(from_)
            self.__to = int(to)
        else:
            super(Bounds, self).__init__(False)

    @constantIfProper
    def FROM(self):
        return self.__from

    @constantIfProper
    def to(self):
        return self.__to

class Region (Bounds):
    '''Ta klasa ma być spójna, nie ma sensu pobierać jednego ze składników jesli nie sa ustawione inne'''

    def __init__(self, from_, to, orientation, OK=True):
        if orientation and OK:
            super(Region, self).__init__(from_, to)
            self.__orientation=orientation
        else:
            super(Region, self).__init__(from_, to, OK=False)


    @classmethod
    def fromBounds(cls, bounds, orientation):
        #alternatywny konstruktor
        #http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
        #use: 
        #r=Region.fromBounds(Bounds(1,100),'+')
        return cls(bounds.FROM, bounds.TO, orientation)
    
    @constantIfProper
    def orientation(self):
        return self.__orientation


class Feature(Region):
    '''Ta klasa nie musi być spójna.
    Mozna pobierać którykolwiek składnik, jeśli dane są składniki klasy nadrzędnej
    W przypadku gdy składnik nie został ustawiony w konstruktorze zwracam pusty string'''

    def __init__(self, from_, to, orientation, frame='', code=-100, Id=ID('0'), comment='', prod_id=0, partial='', except_='', except_text=''):
        super(Feature, self).__init__(from_, to, orientation, OK=True)
        #print "code=", code
        self.__frame=frame
        try:
            self.__code=int(code)
        except ValueError:
            #gdy nie jest intem
            getAndSaveErr( self )
            self.__code=0
        self.__id=Id
        self.__comment=comment
        self.__prod_id=SeqId(prod_id)
        '''try:
            self.__prod_id=SeqId(prod_id)
        except ValueError:
            #gdy nie jest intem
            self.__prod_id=SeqId(0)'''
        if partial=="true":
            self.__partial=True
        elif partial=="false":
            self.__partial=False
        if except_=="true":
            self.__except=True
        elif except_=="false":
            self.__except=False
        self.__except_text=except_text

    @classmethod
    def fromRegion(cls, region, frame='', code=0, Id=ID(0)):
        return cls(region.FROM, region.to, region.orientation, frame, code, Id)

    @classmethod
    def fromBounds(cls, bounds, orientation, frame='', code=0, Id=ID(0)):
        return cls(bounds.FROM, bounds.to, orientation, frame, code, Id)

    @constantIfProper
    def frame(self):
        return self.__frame

    @constantIfProper
    def code(self):
        return self.__code

    @constantIfProper
    def ID(self):
        return self.__id

    @constantIfProper
    def comment(self):
        return self.__comment

    @constantIfProper
    def prod_id(self):
        return self.__prod_id

    def isPartial(self):
        return self.__partial

    def excepted(self):
        return self.__except

    @constantIfProper
    def except_text(self):
        return self.__except_text

################################################################################
class Date(AType):

    def __init__(self, year=0, month=0, day=0):
        proper = year and month and day
        super(Date, self).__init__(proper)
        self.__year = int(year)
        self.__month = int(month)
        self.__day = day

    @constantIfProper
    def day(self):
        return self.__day

    @constantIfProper
    def month(self):
        return self.__day

    @constantIfProper
    def year(self):
        return self.__day


if __name__=='__main__':
    '''a=ID(1)
    #print a
    b=SeqId(2)
    print b
    bo=Bounds(3,4)
    print bo.FROM
    r=Region(5,6,'+')
    print r.orientation
    f=Feature.fromRegion(r)
    print f.FROM'''
