#!/usr/bin/python
# -*- coding: utf-8 -*

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

species_dict = {
    'mulberry': 'Morus nigra',
    'cucumber': 'Cucumis sativus',
    'Yacon': 'Smallanthus sonchifolius',
    'pepper': 'Piper',
    'chilli': 'Capsicum',  # nie jest to pewne. Do rodzaju Capsicum należy kilka gatunków papryczek chili oraz inne
    'Canna': 'Canna indica',
    'lettuce': 'Lactuca sativa',
    'banana': 'Musa',
    'blackberry': 'Rubus',
    'finch': 'Fringillidae',
    'gull': 'Laridae',
    'grapevine': 'Vitis',
    'sugarcane': 'Saccharum hybrid cultivar',
    'barley': 'Hordeum vulgare',
    'cowpea': 'Vigna unguiculata',
    'maize': 'Zea mays',
    'mouse': 'Mus musculus',
    'Pigeonpea': 'Cajanus cajan',
    'mosquito': 'Culicidae',
    'canine': 'Canis lupus',
    'wigeon': 'Mareca',
    'penguin': 'Spheniscidae',
    'dove': 'Columbidae',
    'mink': 'Mustelinae',  # norki. Ta rodzina zawiera więcej gatunków.
    'rose': 'Rosa',
    'pigeon': 'Columba livia domestica',
    'porcine': 'Sus scrofa',
    'sparrow': 'Passer domesticus',
    'cricket': 'Gryllidae',
    'rat': 'Rattus norvegicus',
    'night-heron': 'Ardeidae',
    'cucurbit': 'Cucurbitaceae',
    'melon': 'Cucumis melo',
    'baboon': 'Papio',
    'Equus': 'Equus caballus',
    'fig': 'Ficus carica',
    'olive': 'Olea europaea',
    'raspberry': 'Rubus',
    'bat': 'Chiroptera',
    'magpie-robin': 'Muscicapidae',
    'plaintain': 'Musa',
    'blueberry': 'Vaccinium',
    'groundnut': 'Arachis hypogaea',
    'cherry': 'Prunus cerasus',
    'white-eye': 'Zosteropidae',
    'asymptomatic piglets': 'Sus scrofa',
    'sentinel monkey': 'Simiiformes',
    'Culicoides': 'Ceratopogoninae',
}
species_dict = {k.lower(): v for k, v in species_dict.iteritems()}
