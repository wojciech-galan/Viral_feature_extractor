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
    'chilli': 'Capsicum',  # not sure. There are many species in Capsicum genus.
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
    'mink': 'Mustelinae',  # Mustelinae subfamily consists of many species, not only minks
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
    'Romanomermis nematode': 'Romanomermis',
    'Abelmoscus esculentus': 'Abelmoschus esculentus', # apparently typo
    'Abelmoshus esculentus': 'Abelmoschus esculentus', # apparently typo
    'Acidianus uzoniensis': 'Acidianus',
    'Aedes campestris': 'Ochlerotatus campestris',
    'Aedes harrisoni': 'Aedes',
    'African green monkey': 'Chlorocebus',
    'Albelmoschus esculentus': 'Abelmoschus esculentus', # apparently typo
    'Aporocactus flagelliformis': 'Disocactus flagelliformis',
    'Propionibacterium acnes': 'Cutibacterium acnes ',
    'razor shell': 'Ensis ',
    'freshwater arthropod': 'Arthropoda',
    'peanut worms': 'Sipuncula',
    'freshwater shellfish': 'Bivalvia',
    'freshwater atyid shrimp': 'Atyidae',
    'water striders': 'Gerridae',
    'Clostridium difficile': 'Clostridioides difficile ',
    'horseshoe crab': 'Chelicerata',
    'house centipede': 'Scutigeridae',
    'Sesarmid crab': 'Sesarmidae',
    'hermit crab': 'Paguroidea',
    'snake-associated nematodes': 'Nematoda',
    'fall chinook': "Salmonidae",
    'whitetail deer': 'Odocoileus virginianus',
    'Spirurian nematodes': 'Spirurida',
    'masked palm civet': 'Paguma larvata',
    'sea anemones': 'Actiniaria',
    'sweet potato': 'Ipomoea batatas',
    'freshwater isoptera': 'Insecta',
    'blue swimmer crab': 'Portunidae',
    'Wharf roach': 'Ligia',
    'true flies': 'Diptera',
    'flea and ants': 'Insecta',
    'white pine blister rust fungus': 'Cronartium ribicola',
    'large pig roundworm': 'Ascaris suum',
    'Vernonia cinerea': 'Cyanthillium cinereum',
    'freshwater heteroptera': 'Heteroptera',
    'Penaeus vannamei': 'Litopenaeus vannamei',
    'tomato, cv. Rio Grande': "Solanum lycopersicum",
    'Eucharis grandiflora': 'Eucharis x grandiflora',
    'black currant': 'Ribes nigrum',
    'Touch me not': 'eudicotyledons', # Touch me not is a common name for two unrelated groups of plants
    'Canada goose': 'Branta canadensis',
    'Pekin duck': 'Anas',
    'Dioscorea opposita': 'Dioscorea',
    'Chinese land snail': 'Mastigeulota kiangsinensis',
    'raspberry plant': 'Rubus',
    'large pool of wild-caught Drosophila': 'Drosophila',
    'Turritella sea snails': 'Turritella',
    'fruit bat': 'Megachiroptera',
    'red currant cv. Holandsky cerveny': "Ribes rubrum",
    'freshwater isopoda': 'Isopoda',
    'Lycopersicum escultentum cv. King Kong 2': "Solanum lycopersicum",
    "Vernonia amygdalina": 'Gymnanthemum amygdalinum',
    'rhesus monkey': 'Macaca mulatta',
    'false pimpernel': 'Lindernia dubia',
    'Sida micrantha': 'Malvaceae',
    'Ixodes eudyptidis': 'Ixodes',
    'Heliothis armigera': 'Helicoverpa armigera',
    'large pool of wild-caught Drosophila': 'Drosophila',
    'Ostreococcus lucimarinus': "Ostreococcus 'lucimarinus'",
    'Cercopithecus aethiops': 'Chlorocebus aethiops',
    'bitter gourd': 'Momordica charantia'
}
species_dict = {k.lower(): v for k, v in species_dict_.iteritems()}
#'Petunia hybrida' doesn't work for some reason. Check it!
# neither does 'Phomopsis longicolla'
