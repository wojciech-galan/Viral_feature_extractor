#! /usr/bin/python
# -*- coding: utf-8 -*-


def read_fasta_file(path):
    with open(path) as f:
        f.readline()
        return ''.join([line.strip() for line in f.readlines()])
