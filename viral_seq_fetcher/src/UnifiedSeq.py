#! /usr/bin/python
# -*- coding: utf-8 -*-

""" This file is a part of an application named viral_seq_fetcher
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

import pdb

import copy
import logging

from codonUsageBias import *
from genetic_codes import *
from constants import *
from hostProcessing import *

from commonFunctions import codons, reverseComplement, weightedArithmeticMean, nucFrequencies, relativeNucFrequencies, \
    weightedStandardDeviation, mergeLists, revSubList, codonFreqs, thirdOrderBias
from simple_classes import BaseXML, MyException
from SeqEntrySeq import StandaloneSeqEntrySeq
from SeqEntrySet import SeqEntrySet

logger = logging.getLogger(__file__)


class UnifiedSeq(BaseXML):
    '''Klasa, która ma zbierać dane z obiektów typu SeqEntrySet i StandaloneSeqEntrySeq.
    Dane, o których mowa, będa potem służyć do wyliczenia odpowiednich współczynników'''

    def __init__(self, obj):
        '''Argumenty:
            - obj - obiekt typu SeqEntrySet lub StandaloneSeqEntrySeq'''
        super(UnifiedSeq, self).__init__()
        if type(obj) == StandaloneSeqEntrySeq:
            self.__dict__.update(copy.copy(obj.__dict__))
        elif type(obj) == SeqEntrySet:
            # te wszystkie "pass" trzeba pozastępować
            self.gi = obj.gi
            if obj.biomol:
                pdb.set_trace()
            self.biomol = obj.sequences[0].biomol
            self.molecule = obj.sequences[0].molecule
            if not obj.lineage:  # do poprawy?
                pdb.set_trace()
            self.lineage = obj.lineage
            if obj.missing_seqs:
                pdb.set_trace()
            if obj.completeness:
                pdb.set_trace()
            # if not obj.virus_name and not 'environmental samples' in obj.lineage:  # może być <lineage>Viruses; ssDNA viruses; Circoviridae; environmental samples</lineage>
            #     pdb.set_trace()
            self.virus_name = obj.virus_name
            if obj.missing_cd_regions:  # w przypadku konfliktu w CdRegion (istnieje CdRegion.conflict)
                pass
            if obj.title:
                pdb.set_trace()
            if not obj.cd_regions:
                pdb.set_trace()
            self.cd_regions = obj.cd_regions
            if obj.genome:
                self.genome = obj.genome
            else:
                self.genome = obj.sequences[0].genome
            self.subsource_subtype = obj.subsource_subtype
            if obj.missing_gene_refs:
                pdb.set_trace()
            if not obj.gencode:
                pdb.set_trace()
            self.gencode = obj.gencode
            if not obj.taxname and not 'environmental samples' in obj.lineage:  # może być <lineage>Viruses; ssDNA viruses; Circoviridae; environmental samples</lineage>
                pdb.set_trace()
            self.taxname = obj.taxname
            self.set_id = obj.set_id
            # generefs, cdregions, sequences
            if obj.cd_regions:
                for sequence in obj.sequences:
                    if sequence.cd_regions:
                        pdb.set_trace()
            self.cd_regions = obj.cd_regions
            self.gene_references = obj.gene_references
            if obj.gene_references:
                for x in range(len(obj.sequences)):  # zdarzają się w Pandoravirus inopinatum i nie tylko
                    sequence = obj.sequences[x]
                    if x != 0 and sequence.gene_references:
                        self.gene_references.extend(
                            sequence.gene_references)  # ważne! - dodaję gene_refferences sekwencji składowych. moga być np. w tej samej lokalizacji, co gene_refferences dla całego setu, ale np na innej nici
            if obj.sequences[0].biomol[0] not in ('genomic', 'cRNA'):
                logger.info("Biomolecule for gi=%s is neither genomic nor cRNA" % self.gi)
            self.seq = obj.sequences[0].seq
            self.textseq_id = obj.sequences[0].textseq_id
            self.strand = obj.sequences[0].strand
            for x in range(1, len(obj.sequences)):
                sequence = obj.sequences[x]
                if sequence.biomol[0] != 'peptide':
                    logger.info("Seq_biomol for gi=%s is not 'peptide', but '%s'" % (self.gi, sequence.biomol[0]))
            if obj.host:
                self.host = obj.host
            else:
                self.host = obj.sequences[0].host
        else:
            pdb.set_trace()
            raise
        # pdb.set_trace()

    def getCdRegions(self):
        '''Zwraca rejony na pewno kodujące białko, czyli bez orf==true, partial=true
        oraz dziwonolgow w stylu:
         <seq_feat_except_text>RNA editing</seq_feat_except_text> - mogą one powodować zmianę cdregion
        w postaci {( id_type, procuct_id ):(gencode, frame, seq)}'''
        ret_list = []
        for cd_region in self.cd_regions:
            if cd_region.partial:
                ret_list.append(
                    SimpleCdRegion(cd_region.product_id, cd_region.product_id_type, cd_region.code, cd_region.frame,
                                   getCdRegionSeqs(self.seq, cd_region), False))
            elif cd_region.orf:
                ret_list.append(
                    SimpleCdRegion(cd_region.product_id, cd_region.product_id_type, cd_region.code, cd_region.frame,
                                   getCdRegionSeqs(self.seq, cd_region), False))
            elif cd_region.seq_feat_except_text:
                # tu jest problem skąd wziąć rzeczywistą sekwencję, bo może być edycja RNA albo ribosomal slippage
                ret_list.append(
                    SimpleCdRegion(cd_region.product_id, cd_region.product_id_type, cd_region.code, cd_region.frame,
                                   getCdRegionSeqs(self.seq, cd_region), False))
            else:
                ret_list.append(
                    SimpleCdRegion(cd_region.product_id, cd_region.product_id_type, cd_region.code, cd_region.frame,
                                   getCdRegionSeqs(self.seq, cd_region), True))
        return ret_list

    def getSeqsOutsideCdRegions(self):
        '''Zwraca rejony spoza tych kodujących białka'''
        start_end_tup = []
        for cd_region in self.cd_regions:
            if type(cd_region.TO) == str:
                start_end_tup.append((int(cd_region.FROM), int(cd_region.TO) + 1))
            elif type(cd_region.TO) == tuple:
                for x in range(len(cd_region.TO)):
                    start_end_tup.append((int(cd_region.FROM[x]), int(cd_region.TO[x]) + 1))
            else:
                pdb.set_trace()
        merged = mergeLists(start_end_tup)
        rev_sub = revSubList(self.seq, merged)
        if len(rev_sub)>1:
            return [self.seq[tup[0]:tup[1]] for tup in rev_sub]
        else:
            return []


class SimpleCdRegion(BaseXML):
    '''Reprezentacja istotnych cech rejonu kodującego'''

    def __init__(self, prod_id, id_type, code, frame, seq, proper=True):
        '''Argumenty:
        - prod_id - ID produktu
        - id_type - typ identyfikatora (zwykle 'gi')
        - code - numer kodu genetycznego
        - frame - string z zakresu chyba (one:six) opisujący ramkę
        - seq - sekwencja nukleotydowa
        - proper - czy jest to prawidłowy rejon kodujący, czy jakiś dziwoląg z cd_region.seq_feat_except_text - w takim przypadku trzebaby brać sekwencję na podstawie prod_id
        '''
        super(SimpleCdRegion, self).__init__()
        self.prod_id = prod_id
        self.id_type = id_type
        self.code = code
        self.frame = frame
        self.seq = seq
        self.proper = proper


class SeqRepresentation(BaseXML):
    '''Klasa licząca współczynniki, które będą potem używane przez AI'''

    def __init__(self, uniSeq, taxonomy_dir, debug, verbose):
        '''Argumenty:
            - uniSeq - obiekt typu UnifiedSequence'''
        super(SeqRepresentation, self).__init__()
        self.gi = uniSeq.gi
        seq_rscu = {}
        seq_cai = {}
        seq_enc = {}
        seq_codons = {}
        # pdb.set_trace()

        # ogólne właściwości
        if uniSeq.strand in strands_to_number:
            self.strand = strands_to_number[uniSeq.strand]
        else:
            self.strand = None
        if uniSeq.molecule in ACID_TO_NUMBER:
            self.molecule = ACID_TO_NUMBER[uniSeq.molecule]
        else:
            self.molecule = None
            logger.info("For gi=%s molecule=%s" % (uniSeq.gi, uniSeq.molecule))
        if uniSeq.seq:
            self.length = len(uniSeq.seq)
        else:
            self.length = None
            logger.info("For gi=%s lengt=%s" % (uniSeq.gi, self.length))
        self.lineage = [s.strip() for s in uniSeq.lineage.split(';')]
        if uniSeq.host:
            self.host = uniSeq.host
            self.host_lineage = findHostLineage(uniSeq.host, taxonomy_dir, debug=debug, verbose=verbose)
        else:
            logger.info("No host for %s" % uniSeq.gi)
            self.host = None
            self.host_lineage = None

        # liczenie mono, di i tri
        if not uniSeq.seq:
            self.nuc_frequencies = None
            self.relative_nuc_frequencies = None
            self.relative_trinuc_freqs = None
            self.relative_nuc_frequencies_one_strand = None
            self.relative_trinuc_freqs_one_strand = None
            cd_regions = None
            logger.info("No seq for %s" % uniSeq.gi)
        else:
            self.nuc_frequencies = nucFrequencies(uniSeq.seq, 2)
            self.relative_nuc_frequencies_one_strand = relativeNucFrequencies(self.nuc_frequencies, 1)
            self.relative_trinuc_freqs_one_strand = thirdOrderBias(uniSeq.seq, 1)
            # print self.nuc_frequencies
            if self.strand in (1, 2):
                self.relative_nuc_frequencies = relativeNucFrequencies(self.nuc_frequencies,
                                                                       strands_to_number[uniSeq.strand])
                self.relative_trinuc_freqs = thirdOrderBias(uniSeq.seq, strands_to_number[uniSeq.strand])
            # print self.relative_nuc_frequencies
            # pdb.set_trace()
            else:
                logger.info("For gi=%s strand=%s" % (uniSeq.gi, uniSeq.strand))
                self.relative_nuc_frequencies = None
                self.relative_trinuc_freqs = None
            cd_regions = uniSeq.getCdRegions()

        # liczenie codon usage bias
        if not cd_regions:
            logger.info("No cd_regions for %s" % uniSeq.gi)
            self.avg_rscu_all = None
            self.std_rscu_all = None
            self.avg_cai_all = None
            self.std_cai_all = None
            self.avg_rscu_proper = None
            self.std_rscu_proper = None
            self.avg_cai_proper = None
            self.std_cai_proper = None
            self.avg_enc_all = None
            self.std_enc_all = None
            self.avg_enc_proper = None
            self.std_enc_proper = None
            self.avg_codons_all = None
            self.std_codons_all = None
            self.avg_codons_proper = None
            self.std_codons_proper = None
            self.num_of_all_cd_regions = None
            self.num_of_proper_cd_regions = None
            self.nuc_frequencies_inside_cd_regions = None
            self.nuc_frequencies_outside_cd_regions = None
            self.relative_nuc_frequencies_inside_cd_regions = None
            self.relative_nuc_frequencies_outside_cd_regions = None
            self.relative_trinuc_freqs_inside_cd_regions = None
            self.relative_trinuc_freqs_outside_cd_regions = None
            return
        none_prod_id = 0
        self.num_of_all_cd_regions = len(cd_regions)
        nuc_freqs_cd = []
        relative_nuc_freqs_cd = []
        relative_trinuc_freqs_cd = []
        weights = []
        weights_rel = []
        for cd_region in cd_regions:
            # liczymy i dla proper cd_regions i dla niewłaściwych
            if cd_region.frame == 'one':
                codon_usage = codons(cd_region.seq)
            elif cd_region.frame == 'two':
                codon_usage = codons(cd_region.seq[1:])
            elif cd_region.frame == 'three':
                codon_usage = codons(cd_region.seq[2:])
            else:
                logger.info("For gi=%s cd_region.frame=%s" % (uniSeq.gi, cd_region.frame))
                pdb.set_trace()  # TODO wyjebać?
            if not cd_region.prod_id:  # TODO what?
                cd_region.prod_id = 'no_id_%d' % none_prod_id
                none_prod_id += 1
            seq_rscu[cd_region.prod_id] = rscu(codon_usage, eval('gencode_SG%s' % cd_region.code))
            seq_cai[cd_region.prod_id] = cai(codon_usage, eval('gencode_SG%s' % cd_region.code))
            seq_enc[cd_region.prod_id] = enc(codon_usage, eval('gencode_SG%s' % cd_region.code))
            seq_codons[cd_region.prod_id] = codonFreqs(cd_region.seq)
            nuc_freqs_one_seq = nucFrequencies(cd_region.seq, 2)
            nuc_freqs_cd.append(nuc_freqs_one_seq)
            weights.append(len(cd_region.seq))
            if self.strand in (1, 2):
                relative_nuc_freqs_cd.append(
                    relativeNucFrequencies(nuc_freqs_one_seq, strands_to_number[uniSeq.strand]))
                relative_trinuc_freqs_cd.append(thirdOrderBias(cd_region.seq, strands_to_number[uniSeq.strand]))
                weights_rel.append(len(cd_region.seq))
        self.nuc_frequencies_inside_cd_regions = {}
        self.relative_nuc_frequencies_inside_cd_regions = {}
        self.relative_trinuc_freqs_inside_cd_regions = {}
        for nuc in nuc_freqs_cd[0]:
            nuc_freqs = [cd_region[nuc] for cd_region in nuc_freqs_cd]
            self.nuc_frequencies_inside_cd_regions[nuc] = weightedArithmeticMean(values=nuc_freqs, weights=weights)
        if len(relative_nuc_freqs_cd) > 0:
            for nuc in relative_nuc_freqs_cd[0]:
                nuc_freqs = [cd_region[nuc] for cd_region in relative_nuc_freqs_cd]
                self.relative_nuc_frequencies_inside_cd_regions[nuc] = weightedArithmeticMean(values=nuc_freqs,
                                                                                              weights=weights_rel)
            for nuc in relative_trinuc_freqs_cd[0]:
                trinuc_freqs = [cd_region[nuc] for cd_region in relative_trinuc_freqs_cd]
                self.relative_trinuc_freqs_inside_cd_regions = weightedArithmeticMean(values=trinuc_freqs,
                                                                                      weights=weights_rel)
        else:
            self.relative_nuc_frequencies_inside_cd_regions = None
            self.relative_trinuc_freqs_inside_cd_regions = None

        nuc_freqs_outside_cd = []
        relative_nuc_freqs_outside_cd = []
        relative_trinuc_freqs_outside_cd = []
        weights = []
        weights_rel = []
        weights_rel_trinuc = []
        self.nuc_frequencies_outside_cd_regions = {}
        self.relative_nuc_frequencies_outside_cd_regions = {}
        self.relative_trinuc_freqs_outside_cd_regions = {}
        for outside_cd_reg in uniSeq.getSeqsOutsideCdRegions():
            if len(outside_cd_reg) > 10:  # krótszych odcinków nie ma sensu brać pod uwagę, zaburzają tylko wyniki
                nuc_freqs_one_seq = nucFrequencies(outside_cd_reg, 2)
                nuc_freqs_outside_cd.append(nuc_freqs_one_seq)
                weights.append(len(outside_cd_reg))
                if self.strand in (1, 2):
                    relative_nuc_freqs_outside_cd.append(
                        relativeNucFrequencies(nuc_freqs_one_seq, strands_to_number[uniSeq.strand]))
                    weights_rel.append(len(outside_cd_reg))
                    relative_trinuc_freqs_outside_cd.append(
                        thirdOrderBias(outside_cd_reg, strands_to_number[uniSeq.strand]))

        if len(nuc_freqs_outside_cd) > 0:
            for nuc in nuc_freqs_outside_cd[0]:
                nuc_freqs = [outside_cd_reg[nuc] for outside_cd_reg in nuc_freqs_outside_cd]
                self.nuc_frequencies_outside_cd_regions[nuc] = weightedArithmeticMean(values=nuc_freqs, weights=weights)
        else:
            self.nuc_frequencies_outside_cd_regions = None
        if len(relative_nuc_freqs_outside_cd) > 0:
            for nuc in relative_nuc_freqs_outside_cd[0]:
                nuc_freqs = [outside_cd_reg[nuc] for outside_cd_reg in relative_nuc_freqs_outside_cd]
                self.relative_nuc_frequencies_outside_cd_regions[nuc] = weightedArithmeticMean(values=nuc_freqs,
                                                                                               weights=weights_rel)
            for nuc in relative_trinuc_freqs_outside_cd[0]:
                trinuc_freqs = [cd_region[nuc] for cd_region in relative_trinuc_freqs_outside_cd]
                self.relative_trinuc_freqs_outside_cd_regions = weightedArithmeticMean(values=trinuc_freqs,
                                                                                       weights=weights_rel)
        else:
            self.relative_nuc_frequencies_outside_cd_regions = None
            self.relative_trinuc_freqs_outside_cd_regions = None

        self.avg_rscu_all = {}
        self.avg_cai_all = {}
        self.std_rscu_all = {}
        self.std_cai_all = {}
        self.avg_codons_all = {}
        self.std_codons_all = {}
        for codon in codon_usage:
            l1 = zip(*[(seq_rscu[cd_region.prod_id][codon], len(cd_region.seq)) for cd_region in cd_regions])
            l2 = zip(*[(seq_cai[cd_region.prod_id][codon], len(cd_region.seq)) for cd_region in cd_regions])
            l3 = zip(*[(seq_codons[cd_region.prod_id][codon], len(cd_region.seq)) for cd_region in cd_regions])
            self.avg_rscu_all[codon] = float(weightedArithmeticMean(values=l1[0], weights=l1[1]))
            self.avg_cai_all[codon] = float(weightedArithmeticMean(values=l2[0], weights=l2[1]))
            self.avg_codons_all[codon] = float(weightedArithmeticMean(values=l3[0], weights=l3[1]))
            if len(cd_regions) > 1:
                self.std_rscu_all[codon] = weightedStandardDeviation(values=l1[0], weights=l1[1])
                self.std_cai_all[codon] = weightedStandardDeviation(values=l2[0], weights=l2[1])
                self.std_codons_all[codon] = weightedStandardDeviation(values=l3[0], weights=l3[1])
            else:
                self.std_rscu_all = None
                self.std_cai_all = None
                self.std_codons_all = None
        l = zip(*[(seq_enc[cd_region.prod_id], len(cd_region.seq)) for cd_region in cd_regions])
        self.avg_enc_all = float(weightedArithmeticMean(values=l[0], weights=l[1]))
        if len(cd_regions) > 1:
            self.std_enc_all = weightedStandardDeviation(values=l[0], weights=l[1])
        else:
            self.std_enc_all = None
        # jeśli wszystkie są proper - to przepisujemy
        if all(cd_region.proper for cd_region in cd_regions):
            self.avg_rscu_proper = self.avg_rscu_all
            self.avg_cai_proper = self.avg_cai_all
            self.avg_enc_proper = self.avg_enc_all
            self.std_rscu_proper = self.std_rscu_all
            self.std_cai_proper = self.std_cai_all
            self.std_enc_proper = self.std_enc_all
            self.num_of_proper_cd_regions = self.num_of_all_cd_regions
            self.avg_codons_proper = self.avg_codons_all
            self.std_codons_proper = self.std_codons_all
        # jeśli nie, to liczymy
        else:
            self.avg_rscu_proper = {}
            self.avg_cai_proper = {}
            self.std_rscu_proper = {}
            self.std_cai_proper = {}
            self.avg_codons_proper = {}
            self.std_codons_proper = {}
            self.num_of_proper_cd_regions = len([cd_region.proper for cd_region in cd_regions])
            if any(cd_region.proper for cd_region in cd_regions):
                for codon in codon_usage:
                    l1 = zip(*[(seq_rscu[cd_region.prod_id][codon], len(cd_region.seq)) for cd_region in cd_regions if
                               cd_region.proper])
                    l2 = zip(*[(seq_cai[cd_region.prod_id][codon], len(cd_region.seq)) for cd_region in cd_regions if
                               cd_region.proper])
                    l3 = zip(*[(seq_codons[cd_region.prod_id][codon], len(cd_region.seq)) for cd_region in cd_regions if
                               cd_region.proper])
                    self.avg_rscu_proper[codon] = float(weightedArithmeticMean(values=l1[0], weights=l1[1]))
                    self.avg_cai_proper[codon] = float(weightedArithmeticMean(values=l2[0], weights=l2[1]))
                    self.avg_codons_proper[codon] = float(weightedArithmeticMean(values=l3[0], weights=l3[1]))
                    if len([cd_region for cd_region in cd_regions if cd_region.proper]) > 1:
                        self.std_rscu_proper[codon] = weightedStandardDeviation(values=l1[0], weights=l1[1])
                        self.std_cai_proper[codon] = weightedStandardDeviation(values=l2[0], weights=l2[1])
                        self.std_codons_proper[codon] = weightedStandardDeviation(values=l3[0], weights=l3[1])
                    else:
                        self.std_rscu_proper = None
                        self.std_cai_proper = None
                        self.std_codons_proper = None
                self.avg_enc_proper = float(weightedArithmeticMean(
                    {seq_enc[cd_region.prod_id]: len(cd_region.seq) for cd_region in cd_regions if cd_region.proper}))
                l = zip(
                    *[(seq_enc[cd_region.prod_id], len(cd_region.seq)) for cd_region in cd_regions if cd_region.proper])
                if len([cd_region for cd_region in cd_regions if cd_region.proper]) > 1:
                    self.std_enc_proper = weightedStandardDeviation(values=l[0], weights=l[1])
                else:
                    self.std_enc_proper = None
            else:
                self.avg_rscu_proper = None
                self.avg_cai_proper = None
                self.avg_enc_proper = None
                self.std_rscu_proper = None
                self.std_cai_proper = None
                self.std_enc_proper = None
                self.avg_codons_proper = None
            self.std_codons_proper = None

        # self.avg_enc = weightedArithmeticMean( self.
        # pdb.set_trace()
        # print self
        # pdb.set_trace()

    @classmethod
    def fromString(cls, string):
        # super(SeqRepresentation, cls).__init__()
        # super(SeqRepresentation, cls).fromString(string)
        raise NotImplementedError('Not implemented yet')


class NoSequenceException(MyException):
    pass


def getCdRegionSeqs(wholeSeq, cd_region):
    '''Pobiera sekwencję składającą się na CdRegion (nawet, jeśli jest w kilku kawałkach)'''
    if type(cd_region.TO) == str:
        return getOneSubSeq(wholeSeq, cd_region.strand, cd_region.FROM, cd_region.TO)
    elif type(cd_region.TO) == tuple:
        ret_str = ''
        for x in range(len(cd_region.TO)):
            ret_str += getOneSubSeq(wholeSeq, cd_region.strand[x], cd_region.FROM[x], cd_region.TO[x])
        return ret_str
    else:
        pdb.set_trace()


def getOneSubSeq(wholeSeq, strand, start, end):
    '''Zbiera pojenyńczą podsekwencję'''
    start = int(start)
    end = int(end)
    if strand == 'plus' or (not strand and wholeSeq[start: start + 3]):
        return wholeSeq[start: end + 1]
    elif strand == 'minus':
        return reverseComplement(wholeSeq[start: end + 1])
    else:
        pdb.set_trace()


if __name__ == '__main__':
    pass
