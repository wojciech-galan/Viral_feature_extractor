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
- git (required for installation with pip)
- (for Windows users only) Visual C++ Compiler for Python 2.7 


User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of the dependencies,
the easiest way to install viruses_classifier is using ``pip`` ::

    pip install -U git+https://github.com/wojciech-galan/Viral_feature_extractor.git --user

and assure that the directory you have installed the program to (for Ubuntu it's /home/username/.local/bin/, for win7 C:\\Users\\username\\AppData\\Roaming\\Python\\Scripts) is in your system PATH. It is recommended not to install this package system-wide.

Windows installation issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip fails when installing apsw (at least on Win7), so you have to install it manually.


Source code
-----------

You can check the latest sources with the command::

    git clone https://github.com/wojciech-galan/Viral_feature_extractor



Usage
-----

In the simpliest case:

    fetch_viral_sequences --email your@email --verbose

results as well as temporary files will be available in directory "files". You can change the default behaviour:

    fetch_viral_sequences --email your@email --outdir directory_name --verbose

By default, results are stored in a file, whose name begins from 'container'. Again, you can change the default behaviour
using --container option. If you experience network issues, you may increase the default connection timeout (5 seconds)
with --timeout option.


What to do with the container?
~~~~~~~~~~~~

The container can be easily read. Depending on the content of the source NCBI Nucleotide files, elements of the container
(which are viral sequence representations) could contain bunch of different sequence features.
How to load the container:

.. code:: python

    >>> from viral_seq_fetcher.src.SeqContainer import Container
    >>> container = Container.fromFile('container_Wed_Jan__2_13:05:06_2019.dump') # replace with your container file path

The container contains lots of getter methods suitable for viruses

.. code:: python

    >>> dir(container)
    ['__add__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', \
    '__hash__', '__init__', '__iter__', '__len__', '__module__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', \
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', 'correct_path', \
    'created', 'fromFile', 'getDependoviruses', 'getDsDNAViruses', 'getDsRNAViruses', 'getIds', 'getRetroViruses', \
    'getSsDNAViruses', 'getSsRNANegativeStrandViruses', 'getSsRNAPositiveStrandViruses', 'getSsRNAViruses', \
    'getUnassignedSsRNAViruses', 'getUnclasifiedSsRNAViruses', 'getVirusesInfectingSpeciviedGroup', \
    'getVirusesOfLineage', 'getVirusesWithHost', 'removeIds', 'seqs']

For example you could easily obtain container of  either dsDNA viruses or retroviruses:

.. code:: python

    >>> retro = container.getRetroViruses()
    >>> dsDNA = container.getDsDNAViruses()

Containers are iterable and know about their length. You can also add or subtract them:

.. code:: python

    >>> container2 = retro + dsDNA
    >>> print len(container2)
    3136
    >>> container3 = container2 - dsDNA
    >>> print len(container3)
    19
    >>> print len(retro)
    19

You could pick viruses of some specific lineage. The lineage is the same as in NCBI Taxonomy database. Supposing you'd
like to pick Orthomyxoviridae, you also have to specify level of the taxon in NCBI Taxonomy:

.. code:: python

    >>> container4 = container.getVirusesOfLineage(3, 'Orthomyxoviridae')
    >>> len(container4)
    111

Similarly, you can pick viruses which infect specific host taxon:

.. code:: python

    >>> container5 = container.getVirusesInfectingSpecifiedGroup(17, 'Mammalia')
    >>> len(container5)
    1193

Elements of the container posses specific attributes and you can check them out:

.. code:: python

    >>> dir(container5[0])
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', \
    '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', \
    '__str__', '__subclasshook__', '__weakref__', 'avg_cai_all', 'avg_cai_proper', 'avg_codons_all', 'avg_codons_proper', \
    'avg_enc_all', 'avg_enc_proper', 'avg_rscu_all', 'avg_rscu_proper', 'fromString', 'gi', 'host', 'host_lineage', \
    'length', 'lineage', 'molecule', 'nuc_frequencies', 'nuc_frequencies_inside_cd_regions', \
    'nuc_frequencies_outside_cd_regions', 'num_of_all_cd_regions', 'num_of_proper_cd_regions', 'relative_nuc_frequencies', \
    'relative_nuc_frequencies_inside_cd_regions', 'relative_nuc_frequencies_one_strand', \
    'relative_nuc_frequencies_outside_cd_regions', 'relative_trinuc_freqs', 'relative_trinuc_freqs_inside_cd_regions', \
    'relative_trinuc_freqs_one_strand', 'relative_trinuc_freqs_outside_cd_regions', 'std_cai_all', 'std_cai_proper', \
    'std_codons_all', 'std_codons_proper', 'std_enc_all', 'std_enc_proper', 'std_rscu_all', 'std_rscu_proper', 'strand', \
    'toXML']
    >>> container5[0].host_lineage
    [u'cellular organisms', u'Eukaryota', u'Opisthokonta', u'Metazoa', u'Eumetazoa', u'Bilateria', u'Deuterostomia', \
    u'Chordata', u'Craniata', u'Vertebrata', u'Gnathostomata', u'Teleostomi', u'Euteleostomi', u'Sarcopterygii', \
    u'Dipnotetrapodomorpha', u'Tetrapoda', u'Amniota', u'Mammalia', u'Theria', u'Eutheria', u'Boreoeutheria', \
    u'Euarchontoglires', u'Glires', u'Rodentia', u'Myomorpha', u'Muroidea', u'Cricetidae', u'Sigmodontinae', \
    u'Oligoryzomys']
    >>> container5[0].relative_nuc_frequencies_one_strand
    {'AA': 1.0565006899536655, 'AC': 0.8168992503202865, 'GT': 0.8668581432207304, 'AG': 1.1108863816197967, \
    'CC': 1.2290949346612152, 'CA': 1.2912278472804528, 'CG': 0.2211828767496193, 'TT': 1.0224296856926356, \
    'GG': 1.121613797281987, 'GC': 0.9707470701788848, 'AT': 1.002957437343382, 'GA': 1.0819067368818889, \
    'TG': 1.385185692775394, 'TA': 0.6835442407372095, 'TC': 1.023907185238434, 'CT': 1.0807909177516801}

Citation
--------
If you use this software in a scientific publication, we would appreciate citations: 

    Gałan W, Bąk M, Jakubowska M. Host Taxon Predictor - A Tool for Predicting Taxon of the Host of a Newly Discovered Virus. Sci Rep. 2019;9(1):3436. Published 2019 Mar 5. doi:10.1038/s41598-019-39847-2

If you'd like to reffer to stable version of the software only, you can use DOI below

.. image:: https://zenodo.org/badge/55834194.svg
   :target: https://zenodo.org/badge/latestdoi/55834194

Questions/comments?
-------------------

Contact me via e-mail  wojciech.galan at gmail.com
