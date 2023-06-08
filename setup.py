#! /usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="viral_seq_fetcher",
    version='0.0.8',
    description='blah',#TODO
    url='https://github.com/wojciech-galan/Viral_feature_extractor',
    author='Wojciech Gałan',
    license='GNU GPL v3.0',
    install_requires=[
        'apsw==3.8.11.1.post1',
        'biopython==1.68',
        'numpy==1.13.3',
        'lxml==3.3'
    ],
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points = {
        'console_scripts': [
            'fetch_taxonomy = viral_seq_fetcher.__main__:main_for_host_processing',
            'fetch_viral_sequences = viral_seq_fetcher.__main__:main'
        ]

    },
    include_package_data=True
)
