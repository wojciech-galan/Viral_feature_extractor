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


gencode_SG1 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG1 = ['ATG', 'CTG', 'TTG']

gencode_SG2 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'_', 'AGC':'S', 'AGG':'_', 'AGT':'S', 
	'ATA':'M', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG2 = ['ATA', 'ATC', 'ATG', 'ATT', 'GTG']

gencode_SG3 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'M', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'T', 'CTC':'T', 'CTG':'T', 'CTT':'T', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG3 = ['ATA', 'ATG']

gencode_SG4 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG4 = ['ATA', 'ATC', 'ATG', 'ATT', 'CTG', 'GTG', 'TTA', 'TTG']

gencode_SG5 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'S', 'AGC':'S', 'AGG':'S', 'AGT':'S', 
	'ATA':'M', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG5 = ['ATA', 'ATC', 'ATG', 'ATT', 'GTG', 'TTG']

gencode_SG6 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'Q', 'TAC':'Y', 'TAG':'Q', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG6 = ['ATG']

gencode_SG9 = {
	'AAA':'N', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'S', 'AGC':'S', 'AGG':'S', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG9 = ['ATG', 'GTG']

gencode_SG10 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'C', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG10 = ['ATG']

gencode_SG11 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG11 = ['ATA', 'ATC', 'ATG', 'ATT', 'CTG', 'GTG', 'TTG']

gencode_SG12 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'S', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG12 = ['ATG', 'CTG']

gencode_SG13 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'G', 'AGC':'S', 'AGG':'G', 'AGT':'S', 
	'ATA':'M', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG13 = ['ATA', 'ATG', 'GTG', 'TTG']

gencode_SG14 = {
	'AAA':'N', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'S', 'AGC':'S', 'AGG':'S', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'Y', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG14 = ['ATG']

gencode_SG15 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'Q', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG15 = ['ATG']

gencode_SG16 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'L', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG16 = ['ATG']

gencode_SG21 = {
	'AAA':'N', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'S', 'AGC':'S', 'AGG':'S', 'AGT':'S', 
	'ATA':'M', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG21 = ['ATG', 'GTG']

gencode_SG22 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'L', 'TAT':'Y', 
	'TCA':'_', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG22 = ['ATG']

gencode_SG23 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'_', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'_', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG23 = ['ATG', 'ATT', 'GTG']

gencode_SG24 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'S', 'AGC':'S', 'AGG':'K', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'W', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG24 = ['ATG', 'CTG', 'GTG', 'TTG']

gencode_SG25 = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 
	'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'_', 'TAC':'Y', 'TAG':'_', 'TAT':'Y', 
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'G', 'TGC':'C', 'TGG':'W', 'TGT':'C', 
	'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F', 
	}
start_SG25 = ['ATG', 'GTG', 'TTG']

