#! /usr/bin/python
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

import copy

from commonFunctions import codons, revDict, arithmeticMean
from genetic_codes import *
from constants import *
from CyclicList import CyclicList

#przydałby się code cleanup

#miary codon usage bias - wzory z http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1003&context=bioscigenetics
def rscu ( codon_usage_dict, gencode=gencode_SG1, zero=RSCU_ZERO ):
	'''Oblicza RSCU (Relative synonymous codon usage)
	- codon_usage_dict - słownik postaci {kodon:ilość_jego_wystąpień_w_sekwencji}
	- gencode - słownik z kodem genetycznym'''
	ret_dict = {}
	rev_dict = revDict( gencode )
	for aa in rev_dict:
		n = len( rev_dict[aa] )
		suma = sum( [codon_usage_dict[key] for key in rev_dict[aa]] )
		#print aa, n, suma, [codon_usage_dict[key] for key in rev_dict[aa]]
		for codon in rev_dict[aa]:
			xi = codon_usage_dict[codon]
			try:
				ret_dict[codon] = float( n*xi )/suma
			except ZeroDivisionError:
				ret_dict[codon] = zero
			#print codon, ret_dict[codon]
	return ret_dict

def cai ( codon_usage_dict, gencode=gencode_SG1, zero=CAI_ZERO ):
	'''Oblicza CAI (Codon adaptation index) dla konkretnych kodonów
	- codon_usage_dict - słownik postaci {kodon:ilość_jego_wystąpień_w_sekwencji}
	- gencode - słownik z kodem genetycznym'''
	ret_dict = {}
	rev_dict = revDict( gencode )
	for aa in rev_dict:
		max_occurence = max( [codon_usage_dict[codon] for codon in rev_dict[aa]] )
		for codon in rev_dict[aa]:
			try:
				ret_dict[codon] = float( codon_usage_dict[codon] )/max_occurence
			except ZeroDivisionError:
				ret_dict[codon] = zero
	return ret_dict

#na podstawie http://www.ncbi.nlm.nih.gov/pubmed/2110097
def encSeparateAA ( aa_dict, gencode ):
	'''oblicza ENC dla pojedyńczego aminokwasu. Argumenty:
	- aa_dict - słownik postaci {kodon1_dla_danego_aminokwasu:ilość_jego_wystąpień, ...}
	- gencode - używany kod genetyczny'''
	n = sum ( aa_dict.values() )
	if n==0 or n==1: 
		#nie występuje dany aminokwas, albo  niemożliwe obliczenie fk
		return None
	s = _s( aa_dict, n )
	fk = _fk(n, s)
	if fk==0:
		#jeden z przypadków, w których papier zaleca, aby nie liczyć tego
		return None
	return 1./fk

#na podstawie http://www.ncbi.nlm.nih.gov/pubmed/2110097
def enc ( codon_usage_dict_, gencode=gencode_SG1, stop=stop_code ):
	#co można zmienić - przy zapisie słownika jako listę krotek (klucz, wartość) powinno byc mniej problemów
	'''oblicza ENC dla genu. Zwraca krotkę (słownik_z_enc_dla_każdego_aa, float_enc_dla_genu). 
	Argumenty:
	- codon_usage_dict - słownik postaci {kodon:ilość_jego_wystąpień_w_sekwencji}
	- gencode - używany kod genetyczny'''
	final_dict = {}
	rev_dict = revDict( gencode )
	#najpierw usuwam kodony STOP
	codon_usage_dict = copy.copy(codon_usage_dict_)
	if stop:
		for codon in gencode:
			if gencode[codon] == stop:
				del codon_usage_dict[codon]
		del rev_dict[stop_code]
	#teraz liczę ENC dla każdego aminokwasu osobno
	#num_of_codons = { aa:len(rev_dict[aa]) for aa in rev_dict }
	#rev_num_of_codons  = revDict( num_of_codons )
	rev_num_of_codons = createRevNumOfCodons( codon_usage_dict, gencode )
	#słownik do liczenia średniej fk dla wielu aa
	average_computation = {}
	#print num_of_codons
	#print rev_num_of_codons
	for aa in rev_dict:
		help_dict = {}
		for codon in rev_dict[aa]:
			help_dict[codon] = codon_usage_dict[codon]
		try:
			average_computation[aa] = 1/encSeparateAA( help_dict, gencode )
		except TypeError:
			#tzn encSeparateAA zwróciło None
			average_computation[aa] = 0
			#print aa, help_dict
		#print aa, 1/average_computation[aa]
	#raise
	#pierwsza iteracja - liczę sumę fk dla każdej ilości kodonów, odrzucając aa z wartościami None
	'''almost_final_dict = {}# słownik postaci:{lista_fk:z_ilu_aa}
	for num in rev_num_of_codons:
		temp_list = [ 1/average_computation[aa]  for aa in rev_num_of_codons[num] if average_computation[aa] ]
		almost_final_dict[ tuple(temp_list) ] = len( temp_list )
	print almost_final_dict
	#ponieważ wywalam aminokwasy, dla których nie liczę sumy, może zdarzyć się, że dla różnych temp_list będziemy mieć ten sam klucz 'z_ilu_aa'. Trzeba je scalić, poza tym, tak czy inaczej, trzeba je odwrócić
	#słownik {('a',):1, ('f',):1, ('b', 'c'):2} powinien dać
	#{ 4:('a', 'b', 'c', 'f') }
	final_dict = mergeDict( almost_final_dict )
	print final_dict
	print average_computation
	#następnie musimy sprawdzić, czy wszystkie z aminokwasów są reprezentowane. Jeśli dany aa nie jest reprezentowany, pomijamy go w obliczeniach średniej (jest to już osiągnięte wcześniej). Jeśli cała para klucz:wartość z rev_num_of_codons (np. 1: ['M', 'W']) nie występuje, to liczymy dla każdego z nich na podstawie aminokwasów "sąsiadujących" z rev_num_of_codons (w tym przypadnu dla 6: ['L', 'S', 'R'] oraz 2: ['C', 'E', 'D', 'F', 'H', 'K', 'N', 'Q', 'Y'] )
	
	jebnąć naajpierw processFkDict, wjebać tam tworzenie almost_final_dict, czyli wyjebywanie aminokwasów wśród wielu
	potem możemy to mergować. Na końcu liczymy średnią'''
	#chwila, chwila... po chuj tu ten merge?
	
	#print average_computation
	#print 'fk', { key:1/average_computation[key] for key in average_computation }
	#print 'revnum', rev_num_of_codons
	#print 'avg', average_computation
	#almost_final_dict = processFkDict( average_computation, rev_num_of_codons )
	almost_final_dict = processFkDict( average_computation, revDict( { aa:len(rev_dict[aa]) for aa in rev_dict } ), rev_num_of_codons )
	#print "almost final:  ", almost_final_dict, '\n'
	#final_dict = mergeDict( almost_final_dict )
	#print [ (key, arithmeticMean(key)) for key in almost_final_dict ]
	ret_val = 0
	# przyjmujemy, że coś/0 = 0
	for key in almost_final_dict:
		try:
			ret_val += almost_final_dict[key]/arithmeticMean(key) 
		except ZeroDivisionError:
			pass
	#return sum( final_dict[key]/arithmeticMean(key) for key in final_dict )
	if ret_val > 61:
		return 61.
	return ret_val

	
def processFkDict( fk_dict, rev_num_of_codons, rev_num_of_codons_real=None ):
	'''Przykładowe dane:
	- fk_dict = {'A': 0.27169274537695587, 'C': 0.48571428571428577, 'E': 0.4966727162734422, 'D': 0.5019230769230769, 'G': 0.23737373737373738, 'F': 0.5253968253968253, 'I': 0.32941176470588235, 'H': 0.4947368421052632, 'K': 0.49656266525647796, 'M': 1, 'L': 0.1669226830517153, 'N': 0.49245063879210227, 'Q': 0.6553030303030303, 'P': 0.24927536231884062, 'S': 0.1875, 'R': 0.23616734143049928, 'T': 0.2890243902439025, 'W': 1, 'V': 0.2740740740740741, 'Y': 0.5076923076923078} - są to wartości fk dla poszczególnych aa
	- rev_num_of_codons = {1: ['M', 'W'], 2: ['C', 'E', 'D', 'F', 'H', 'K', 'N', 'Q', 'Y'], 3: ['I'], 4: ['A', 'G', 'P', 'T', 'V'], 6: ['L', 'S', 'R']} - słownik ile_kodonów:jakie_aa_mają_tyle_kodonów, przy czym mowa jest o o tym, co powinno być
	- rev_num_of_codons_real = {1: ['C', 'M', 'W'], 2: ['E', 'D', 'F', 'H', 'K', 'N', 'Q', 'Y'], 3: ['I'], 4: ['A', 'G', 'P', 'T', 'V'], 6: ['L', 'S', 'R']} - słownik ile_kodonów:jakie_aa_mają_tyle_kodonów, przy czym mowa jest o o tym, co rzeczywiście jest - w tym przypadku w sekwencji wystąpił tylko jeden kodon dla cysteiny
	
	Potem, jeśli w fk_dict nie występuje żaden z aminokwasów dla danego klucza z rev_num_of_codons
	(przykładowo, jeśli dla kodu standardowego nie występują M ani W, czyli wpis 1: ['M', 'W'] z rev_num_of_codons),
	to liczy dla nich fk w oparciu o wpisy "sąsiednie" - w tym przypadku
	6: ['L', 'S', 'R'] oraz 2: ['C', 'E', 'D', 'F', 'H', 'K', 'N', 'Q', 'Y'].
	Jeśli znów któryś z tych wpisów nie występuje, to jedziemy, odpowiednio, w górę lub w dół, aż się znajdą.
	Zwraca słownik postaci:{krotka_fk:z_ilu_aa}'''
	if not all( (fk_dict, rev_num_of_codons) ):
		raise Exception
	fk_dict = copy.copy( fk_dict )
	rev_num_of_codons = copy.copy( rev_num_of_codons )
	rev_num_of_codons_real = copy.copy( rev_num_of_codons_real ) or copy.copy( rev_num_of_codons )
	key_list_real = CyclicList( rev_num_of_codons_real.keys() )
	key_list_real.sort()
	key_list = CyclicList( rev_num_of_codons.keys() )
	key_list.sort()
	for key in key_list:
		#print "key", key
		#if not any( [ aa in fk_dict for aa in rev_num_of_codons_real[key] ] ):
		if key not in rev_num_of_codons_real:
			#czyli żaden z aminokwasów dla tego klucza nie występuje
			#najpierw "dolny" klucz:
			i = 1
			#while not any( [ aa in fk_dict for aa in rev_num_of_codons_real[  key_list_real[key_list_real.index(key)-i]  ] ] ):
			#	i+=1
			while True:
				if key-i < min( key_list_real ):
					lower_key = max( key_list_real )
					break
				if key-i in key_list_real:
					lower_key = key_list_real[ key_list_real.index(key-i) ] 
					break
				else:
					i+=1
			#print 'lower key', lower_key
			#teraz "górny" klucz
			#i = 1
			#while not any( [ aa in fk_dict for aa in rev_num_of_codons_real[  key_list_real[key_list_real.index(key)+i]  ] ] ):
			#	i+=1
			upper_key = key_list_real[ key_list_real.index(lower_key) + i ] 
			#print 'upper key', upper_key
			lower_mean_list = []
			upper_mean_list = []
			for aa in rev_num_of_codons_real[ lower_key ]:
				try:
					lower_mean_list.append( fk_dict[aa] )
				except KeyError:
					pass
			for aa in rev_num_of_codons_real[ upper_key ]:
				try:
					upper_mean_list.append( fk_dict[aa] )
				except KeyError:
					pass
			mean = arithmeticMean( ( arithmeticMean(lower_mean_list), arithmeticMean(upper_mean_list) ) )
			#print '\nkey:', key, mean, arithmeticMean(lower_mean_list), arithmeticMean(upper_mean_list)
			#uwaga - modyfikacja rev_num_of_codons_real i key_list_real!!!
			rev_num_of_codons_real[ key ] = rev_num_of_codons[key]
			key_list_real = CyclicList( rev_num_of_codons_real.keys() )
			key_list_real.sort()
			for aa in rev_num_of_codons[key]:
				fk_dict[aa] = mean
	final_dict = {}# słownik postaci:{krotka_fk:z_ilu_aa}
	for num in rev_num_of_codons_real:
		temp_list = []
		for aa in rev_num_of_codons_real[num]:
			try: 
				temp_list.append(fk_dict[aa])
			except KeyError:
				pass
		temp_list.sort()
		final_dict[ tuple(temp_list) ] = len( temp_list )
	#print 'final\t\t', final_dict
	return final_dict

def mergeDict( a_dict, additional_key_string = 'abrakadabra' ):
	'''Scala słownik { (krotka):długość_krotki } tak, aby wartości się nie powtarzały
	Przykłady:
	>>> mergeDict( {('a',):1, ('f',):1, ('b', 'c'):2} )
	{('a', 'b', 'c', 'f'): 4}'''
	ret_dict = []
	is_not_ok =  ( len( a_dict.values() ) != len( set(a_dict.values()) ) )
	a_dict = [ (key, a_dict[key]) for key in a_dict ]
	while is_not_ok:
		for val in set( x[1] for x in a_dict ):
			keys_for_this_val = []
			for key_for_this_val in [ item[0] for item in a_dict if item[1]==val ]:
				keys_for_this_val.extend( key_for_this_val )
			keys_for_this_val.sort()
			ret_dict.append( (tuple( keys_for_this_val ), len( keys_for_this_val )) )
		is_not_ok =  ( len( ret_dict ) != len( set(item[1] for item in ret_dict) ) )
		a_dict = ret_dict
		ret_dict = []
	return dict(a_dict)

def _fk ( n, s ):
	#f pomocnicza do liczenia ENC
	return ( n*s - 1 ) / float( n - 1 )

def _s ( aa_dict, n ):
	#f pomocnicza do liczenia ENC
	'''
	- aa_dict - słownik postaci {kodon1_dla_danego_aminokwasu:ilość_jego_wystąpień, ...}
	- n - sumaryczna ilość kodonów dla danego aminokwasu, które tu wystąpiły'''
	return sum( [ ( float(ni)/n )**2 for ni in aa_dict.values() ] )

def createRevNumOfCodons( codon_usage_dict, gencode=gencode_SG1 ):
	#kolejna funkcja pomocnicza
	'''Pobiera codon_usage_dict z wyjebanymi STOP'ami i kod genetyczny.
	Zwraca słownik postaci {ile_kodonów:lista_aa_o_danej_ilości_kodonów}.
	Jeśli dany kodon nie występuje w codon_usage_dict, to ilość kodonów dla
	danego aa zmniejsza się o 1'''
	rev_dict = revDict( gencode )
	#print rev_dict
	#słownik aa:ile_kodonów
	num_of_codons = {}
	for aa in rev_dict:
		a_list=[]
		for codon in rev_dict[aa]:
			try:
				if codon_usage_dict[codon]:
					a_list.append( codon )
			except KeyError:
				#kodon STOP w gencode
				pass
		if a_list:
			num_of_codons[ aa ] = len( a_list )
	return revDict( num_of_codons )

if __name__ == "__main__":
	seq = 'ATGAGGCAGTCTCTCCTATTCCTGACCAGCGTGGTTCCTTTCGTGCTGGCGCCGCGACCTCCGGATGACCCGGGCTTCGGCCCCCACCAGAGACTCGAGAAGCTTGATTCTTTGCTCTCAGACTACGATATTCTCTCTTTATCTAATATCCAGCAGCATTCGGTAAGAAAAAGAGATCTACAGACTTCAACACATGTAGAAACACTACTAACTTTTTCAGCTTTGAAAAGGCATTTTAAATTATACCTGACATCAAGTACTGAACGTTTTTCACAAAATTTCAAGGTCGTGGTGGTGGATGGTAAAAACGAAAGCGAGTACACTGTAAAATGGCAGGACTTCTTCACTGGACACGTGGTTGGTGAGCCTGACTCTAGGGTTCTAGCCCACATAAGAGATGATGATGTTATAATCAGAATCAACACAGATGGGGCCGAATATAACATAGAGCCACTTTGGAGATTTGTTAATGATACCAAAGACAAAAGAATGTTAGTTTATAAATCTGAAGATATCAAGAATGTTTCACGTTTGCAGTCTCCAAAAGTGTGTGGTTATTTAAAAGTGGATAATGAAGAGTTGCTCCCAAAAGGGTTAGTAGACAGAGAACCACCTGAAGAGCTTGTTCATCGAGTGAAAAGAAGAGCTGACCCAGATCCCATGAAGAACACGTGTAAATTATTGGTGGTAGCAGATCATCGCTTCTACAGATACATGGGCAGAGGGGAAGAGAGTACAACTACAAATTACTTAATAGAGCTAATTGACAGAGTTGATGACATCTATCGGAACACTTCATGGGATAATGCAGGTTTTAAAGGCTATGGAATACAGATAGAGCAGATTCGCATTCTCAAGTCTCCACAAGAGGTAAAACCTGGTGAAAAGCACTACAACATGGCAAAAAGTTACCCAAATGAAGAAAAGGATGCTTGGGATGTGAAGATGTTGCTAGAGCAATTTAGCTTTGATATAGCTGAGGAAGCATCTAAAGTTTGCTTGGCACACCTTTTCACATACCAAGATTTTGATATGGGAACTCTTGGATTAGCTTATGTTGGCTCTCCCAGAGCAAACAGCCATGGAGGTGTTTGTCCAAAGGCTTATTATAGCCCAGTTGGGAAGAAAAATATCTATTTGAATAGTGGTTTGACGAGCACAAAGAATTATGGTAAAACCATCCTTACAAAGGAAGCTGACCTGGTTACAACTCATGAATTGGGACATAATTTTGGAGCAGAACATGATCCGGATGGTCTAGCAGAATGTGCCCCGAATGAGGACCAGGGAGGGAAATATGTCATGTATCCCATAGCTGTGAGTGGCGATCACGAGAACAATAAGATGTTTTCAAACTGCAGTAAACAATCAATCTATAAGACCATTGAAAGTAAGGCCCAGGAGTGTTTTCAAGAACGCAGCAATAAAGTTTGTGGGAACTCGAGGGTGGATGAAGGAGAAGAGTGTGATCCTGGCATCATGTATCTGAACAACGACACCTGCTGCAACAGCGACTGCACGTTGAAGGAAGGTGTCCAGTGCAGTGACAGGAACAGTCCTTGCTGTAAAAACTGTCAGTTTGAGACTGCCCAGAAGAAGTGCCAGGAGGCGATTAATGCTACTTGCAAAGGCGTGTCCTACTGCACAGGTAATAGCAGTGAGTGCCCGCCTCCAGGAAATGCTGAAGATGACACTGTTTGCTTGGATCTTGGCAAGTGTAAGGATGGGAAATGCATCCCTTTCTGCGAGAGGGAACAGCAGCTGGAGTCCTGTGCATGTAATGAAACTGACAACTCCTGCAAGGTGTGCTGCAGGGACCTTTCTGGCCGCTGTGTGCCCTATGTCGATGCTGAACAAAAGAACTTATTTTTGAGGAAAGGAAAGCCCTGTACAGTAGGATTTTGTGACATGAATGGCAAATGTGAGAAACGAGTACAGGATGTAATTGAACGATTTTGGGATTTCATTGACCAGCTGAGCATCAATACTTTTGGAAAGTTTTTAGCAGACAACATCGTTGGGTCTGTCCTGGTTTTCTCCTTGATATTTTGGATTCCTTTCAGCATTCTTGTCCATTGTGTGGATAAGAAATTGGATAAACAGTATGAATCTCTGTCTCTGTTTCACCCCAGTAACGTCGAAATGCTGAGCAGCATGGATTCTGCATCGGTTCGCATTATCAAACCCTTTCCTGCGCCCCAGACTCCAGGCCGCCTGCAGCCTGCCCCTGTGATCCCTTCGGCGCCAGCAGCTCCAAAACTGGACCACCAGAGAATGGACACCATCCAGGAAGACCCCAGCACAGACTCACATATGGACGAGGATGGGTTTGAGAAGGACCCCTTCCCAAATAGCAGCACAGCTGCCAAGTCATTTGAGGATCTCACGGACCATCCGGTCACCAGAAGTGAAAAGGCTGCCTCCTTTAAACTGCAGCGTCAGAATCGTGTTGACAGCAAAGAAACAGAGTGCTAA'
	
	kodony = codons(seq)
	print kodony
	print revDict( gencode_SG1 )
	#print rscu( kodony ), sum( rscu( kodony ).values() )
	#print cai ( kodony ), sum( cai( kodony ).values() )
	#print enc1 ( kodony )
	#print enc ( kodony )
	#print len(seq)/float(3), sum(kodony.values())
	print encSeparateAA( {'CTA':1, 'CTC':1, 'CTG':1, 'CTT':1, 'TTA':1, 'TTG':1}, gencode_SG1 )
	print enc(kodony)
