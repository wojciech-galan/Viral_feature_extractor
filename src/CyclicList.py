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

from commonFunctions import constant

class CyclicList ( object ):
	'''Coś jak lista, tyle że elementem następnym po ostatnim jest pierwszy. 
	Przy czym ostatni i pierwszy element istnieją, nie jak w zwykłym kole
	Przykłady:
	>>> cl = CyclicList( range(5) )
	>>> cl[2:7]
	CyclicList([2, 3, 4, 0, 1])
	>>> cl[2:12]
	CyclicList([2, 3, 4, 0, 1, 2, 3, 4, 0, 1])
	>>> cl [:-1]
	CyclicList([0, 1, 2, 3])
	>>> cl [2:-1]
	CyclicList([2, 3])
	>>> cl [-1:1]
	CyclicList([4, 0])
	>>> cl[6]=7
	>>> cl
	CyclicList([0, 7, 2, 3, 4])
	>>> cl[2:4]=[11,12]
	>>> cl
	CyclicList([0, 7, 11, 12, 4])
	>>> cl[-4:-2]=[11,12]
	>>> cl
	CyclicList([0, 11, 12, 12, 4])
	>>> cl = CyclicList( range(5) )
	>>> cl[9:11] = [11,12]
	>>> cl
	CyclicList([12, 1, 2, 3, 11])
	'''
	
	def __init__ (self, a_list):
		'''Artumenty:
		- a_list - lista, którą chcemy zapętlić'''
		super( CyclicList, self ).__init__()
		assert ( isinstance( a_list, list ) or isinstance( a_list, CyclicList ) )
		if isinstance( a_list, list ):
			self.__data = a_list[:]
		elif isinstance( a_list, CyclicList ):
			self.__data = a_list.data[:]
	
	def __str__( self ):
		return self.__data.__str__()
	
	def __repr__( self ):
		return 'CyclicList('+self.__data.__repr__()+')'
	
	def __len__( self ):
		return len( self.__data )
	
	def __delitem__( self, index ):
		if isinstance( index, int ):
			del self.__data[ index%len(self.__data) ]
		else:
			start, stop, step = _parseIndex( index, self.__data )
			a_list = []
			for x in xrange( start, stop, step ):
				a_list.append(self[x])
			for element in a_list:
				self.__data.remove( element )
	
	def __setitem__( self, index, data ):
		if isinstance( index, int ):
			self.__data[ index%len(self.__data) ] = data
		else:
			start, stop, step = _parseIndex( index, self.__data )
			i=0
			for x in xrange( start, stop, step ):
				self[x] = data[i]
				i+=1
	
	def __getitem__( self, index ):
		if isinstance( index, int ):
			return self.__data[ index%len(self.__data) ]
		else:
			start, stop, step = _parseIndex( index, self.__data )
			ret_list = [ self[x] for x in xrange( start, stop, step ) ]
			return CyclicList( ret_list )
	
	def append( self, an_object ):
		self.__data.append( an_object )
	
	def count( self, value ):
		return self.__data.count( value )
	
	def index( self, value, start=0, stop=None ):
		if stop==None:
			stop=len(self.__data)
		if stop <= len( self.__data ):
			return self.__data.index( value, start, stop )
		else:
			return self[start:stop].index( value ) + start
	
	def pop( self, index=None ):
		if index==None:
			index = len(self.__data)-1
		return self.__data.pop( index%len(self.__data) )
	
	def remove( self, value ):
		self.__data.remove( value )
	
	def reverse( self ):
		self.__data.reverse()
	
	def sort( self ):
		self.__data.sort()
	
	@constant
	def data( self ):
		return self.__data
	
	def __add__( self, seq_type ):
		if isinstance( seq_type, CyclicList ):
			return CyclicList( self.__data + seq_type.data )  
		return CyclicList( self.__data + seq_type )  
	
	def __radd__( self, seq_type ):
		return CyclicList( seq_type + self.__data )  
	
	def __iadd__( self, seq_type ):
		if isinstance( seq_type, CyclicList ):
			self.__data += seq_type.data
		else:
			self.__data += seq_type
		return CyclicList( self.__data )
	
	def __mul__( self, an_int ):
		return CyclicList( self.__data.__mul__( an_int ) )
	
	def __rmul__( self, an_int ):
		return CyclicList( self.__data.__rmul__( an_int ) )
	
	def __imul__( self, an_int ):
		self.__data *= an_int
		return CyclicList( self.__data )
	
	def __iter__( self ):
		return self.__data.__iter__()
	
	def __eq__( self, other ):
		return ( isinstance(other, self.__class__) ) and ( id(self) == id(other) or self.__dict__ == other.__dict__ )


def _parseIndex( index, a_list ):
	'''funkcja pomocnicza do obróbki slices'''
	try:
		start = int( index.start )
	except TypeError:
		start = 0
	try: 
		step = int( index.step )
	except TypeError:
		step = 1
	try: 
		stop = int( index.stop )
	except TypeError:
		if step<0:
			stop = -1
			start-= 1
		else:
			stop = len( a_list )
	if step > 0:
		while start>stop:
			stop += len( a_list )
	else:
		while start<stop:
			start += len( a_list )
	return (start, stop, step)
