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
(which are viral sequence representations) could contain bunch of different sequence features:

.. code:: python

	from viral_seq_fetcher.src import SeqContainer
	container = SeqContainer.Container.fromFile('files/container_Fri_Oct__6_14:26:35_2017.dump') # replace with your container file path
	print len(container), "reference genomic viral sequences"
	with_host = container.getVirusesWithHost()
	print len(with_host), "of the sequences sequences"
	print '---------------------------------------------------'
	print dir(with_host[0])
	print with_host[0].nuc_frequencies # mono- and dinucleotide frequencies
	print with_host[0].host_lineage
	print with_host[0].relative_nuc_frequencies # 'second order bias'
	print with_host[0].relative_trinuc_freqs # 'third order bias'

Citation
--------

# TODO
