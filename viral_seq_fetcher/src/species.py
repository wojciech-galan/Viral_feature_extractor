#!/usr/bin/python
# -*- coding: utf-8 -*

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

species_dict_ = {
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
    'Aedes camptorhynchus': 'Ochlerotatus camptorhynchus',
    'Cebus apella': 'Sapajus apella',
    'Tadarida plicata': 'Chaerephon plicatus',
    'Canis familiaris': 'Canis lupus familiaris',
    'Camponotus yamaokai': 'Camponotus',
    'Chilli pepper': 'Capsicum annuum',
    'Carios pusillus': 'Carios',
    'Channeled applesnail':'Pomacea canaliculata',
    'Charybdis crab': 'Charybdis',
    'Conehead cricket': 'Neoconocephalus',
    'Coquillettidia albicosta' : 'Coquillettidia',
    'Corynorhinus rafinesquii': 'Plecotus rafinesquii',
    'Culex simpliciforceps': 'Culex',
    'Culex vishunui': 'Culex vishnui',
    'Culicoides insignis': 'Culicoides',
    'Erysiphe cichoracearum': 'Golovinomyces cichoracearum',
    'Euonymus bungeanus': 'Euonymus maackii',
    'Eustoma grandiflorum': 'Eustoma exaltatum subsp. russellianum',
    'Fiddler crab': 'Uca',
    'Hortobagy goose': 'Anserini',
    'Hoya wayetii': 'Hoya',
    'Lycopersicon esculentum': 'Solanum lycopersicum', # take a look at it in taxonomy database!!
    'Mantis shrimp': 'Hoplocarida',
    'Murex snails': 'Murex',
    'Oncopera intricoides': 'Oncopera',
    'Paphia shell': 'Paphia',
    'Penaeid shrimp': 'Penaeidae',
    'Pityohyphantes rubrofasciatus': 'Pityohyphantes',
    'Romanomermis nematode': 'Romanomermis'
}
species_dict = {k.lower(): v for k, v in species_dict_.iteritems()}
#'Petunia hybrida' doesn't work for some reason. Check it!
# neither does 'Phomopsis longicolla'
