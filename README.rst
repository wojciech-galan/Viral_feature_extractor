.. -*- mode: rst -*-
Host taxon predictor - feature extractor
====
The initial repo was split into two parts. This part contains a software designed to fetch complete viral genomic
reference sequences from NCBI Nucleotide, get viral host's lineage from NCBI Taxonomy and transform the sequence into
some features. The second part, available on https://github.com/wojciech-galan/viruses_classifier has been designed to
infer host of previously unknown virus.

Installation
------------

Dependencies
~~~~~~~~~~~~

viral_seq_fetcher requires:

- Python = 2.7
- NumPy >= 1.6.1
- apsw >= 3.7.6.3
- Biopython >= 1.68
- lxml >= 3.3


User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of the dependencies,
the easiest way to install viruses_classifier is using ``pip`` ::

    pip install -U git+https://github.com/wojciech-galan/Host-taxon-predictor.git --user

It is recommended not to install this package system-wide


Source code
-----------

You can check the latest sources with the command::

    git clone https://github.com/wojciech-galan/Host-taxon-predictor



Usage
-----

In the simpliest case:

    fetch_viral_sequences --email your@email

results as well as temporary files will be available in directory "files". You can change the default behaviour:

    fetch_viral_sequences --email your@email --outdir directory_name

By default, results are stored in a file, whose name begins from 'container'. Again, you can change the default behaviour
using --container option. If you experience network issues, you may increase the default connection timeout (5 seconds)
with --timeout option


What to do with the container?
~~~~~~~~~~~~

.. code:: python


Citation
--------

# TODO