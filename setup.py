#! /usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="viral_seq_fetcher",
    version='0.0.3',
    description='blah',#TODO
    url='https://github.com/wojciech-galan/Viral_feature_extractor',
    author='Wojciech Gałan',
    license='GNU GPL v3.0',
    install_requires=[
        'apsw',
        'numpy',
        'biopython',
        'lxml'
    ],
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points = {
        'console_scripts':[
            'fetch_taxonomy = viral_seq_fetcher.__main__:main_for_host_processing',
            'fetch_viral_sequences = viral_seq_fetcher.__main__:main'
        ]

    },
    include_package_data=True
)
