import random



phobia_list = ['Achluophobia ', 'Acousticophobia ', 'Acrophobia ', 'Aerophobia ', 'Agoraphobia ', 'Agyrophobia ', 'Aichmophobia ', 'Ailurophobia ', 'Algophobia ', 'Ancraophobia ', 
'Aquaphobia ', 'Arachnophobia ', 'Astraphobia ', 'Autophobia ', 'Bacteriophobia ', 'Basophobia ', 'Batrachophobia ', 'Belonephobia ', 'Bibliophobia ', 'Cacophobia ', 'Carcinophobia ', 
'Catoptrophobia ', 'Chemophobia ', 'Cherophobia ', 'Chiroptophobia ', 'Chromophobia ', 'Chronomentrophobia ', 'Chronophobia ', 'Cibophobia ', 'Claustrophobia ', 'Coimetrophobia ', 
'Coulrophobia ', 'Cyberphobia ', 'Cynophobia ', 'Demonophobia ', 'Dendrophobia ', 'Dentophobia ', 'Domatophobia ', 'Emetophobia ', 'Enochlophobia ', 'Entomophobia ', 'Ephebiphobia ', 
'Equinophobia ', 'Ergophobia ', 'Frigophobia ', 'Gamophobia ', 'Gephyrophobia ', 'Gerascophobia ', 'Germophobia ', 'Globophobia ', 'Glossophobia ', 'Halitophobia ', 'Heliophobia ', 
'Helminthophobia ', 'Hemophobia ', 'Herpetophobia ', 'Hexakosioihexekontahexaphobia ', 'Hodophobia ', 'Hydrophobia ', 'Hypochondria ', 'Ichthyophobia ', 'Insectophobia ', 'Koumpounophobia ', 
'Lepidopterophobia ', 'Lilapsophobia ', 'Mageirocophobia ', 'Melanophobia ', 'Melissophobia ', 'Monophobia ', 'Musophobia ', 'Myrmecophobia ', 'Necrophobia ', 'Neophobia ', 'Noctiphobia ', 
'Nosocomephobia ', 'Numerophobia ', 'Nyctophobia ', 'Obesophobia ', 'Ommetaphobia ', 'Oneirophobia ', 'Ophidiophobia ', 'Ornithophobia ', 'Osmophobia ', 'Ostraconophobia ', 'Panphobia ', 
'pediaphobia ', 'Pharmacophobia ', 'Phasmophobia ', 'Phobophobia ', 'Phonophobia ', 'Pogonophobia ', 'Porphyrophobia ', 'Pteromerhanophobia ', 'Pyrophobia ', 'Radiophobia ', 
'Roller coaster phobia ', 'Siderodromophobia ', 'Sociophobia ', 'Somniphobia ', 'Taphophobia ', 'Technophobia ', 'Tetraphobia ', 'Thalassophobia ', 'Thanatophobia ', 'Thermophobia ', 
'Toxiphobia ', 'Traumatophobia ', 'Trichophobia ', 'Triskaidekaphobia ','Vehophobia ', 'Xanthophobia ', 'Xenophobia '
]

fear_name_list = ['darkness', 'noise', 'heights', 'flying', 'open spaces', 'crossing streets', 'sharp objects', 'cats', 'pain', 'wind', 'water', 'spiders', 'thunder and lightning',
'isolation', 'bacteria', 'falling', 'frogs', 'needles', 'books', 'ugliness', 'cancer', 'mirrors', 'chemicals', 'happiness', 'bats', 'colours', 'clocks', 'time passing', 'food', 
'closed spaces', 'cemetries', 'clowns', 'computers', 'dogs', 'demons', 'trees', 'dentists', 'houses', 'vomiting', 'crowds', 'insects', 'youth', 'horses', 'work', 'cold', 'marriage', 
'bridges', 'aging', 'germs', 'balloons', 'public speaking', 'bad breath', 'sunlight', 'worms', 'blood', 'reptiles', '666', 'travel', 'water', 'illness', 'fish', 'insects', 'buttons', 
'butteflies', 'tornadoes or hurricanes', 'cooking', 'black', 'bees', 'being alone', 'mice', 'ants', 'death', 'new things', 'night', 'hospitals', 'numbers', 'darkness', 
'weight gain', 'eyes', 'dreams', 'snakes', 'birds', 'smells', 'shellfish', 'everything', 'babies and children', 'medicine', 'ghosts', 'fear', 'loud sounds', 'beards', 'purple', 
'flying', 'fire', 'radioactivity', 'roller coasters', 'trains', 'people', 'sleep', 'graves', 'technology', '4', 'sea', 'dying', 'heat', 'poisons', 'injury', 'hair loss', '13', 
'driving', 'yellow', 'foreigners'
]

print(phobia_list)
print(len(phobia_list))

print(fear_name_list)
print(len(fear_name_list))

random_phobia = random.randint(1, len(phobia_list))
correct_phobia = phobia_list[random_phobia]
print("{}is the fear of:".format(correct_phobia))

correct_fear = fear_name_list[random_phobia]
print(correct_fear)
phobia_list.pop(random_phobia)
fear_name_list.pop(random_phobia)
print(len(phobia_list))

random_fear1 = random.randint(1, (len(fear_name_list)-1))
random_fear1_name = fear_name_list[random_fear1]
print(random_fear1_name)
fear_name_list.pop(random_fear1)

random_fear2 = random.randint(1, (len(fear_name_list)-1))
random_fear2_name = fear_name_list[random_fear2]
print(random_fear2_name)
fear_name_list.pop(random_fear2)

random_fear3 = random.randint(1, (len(fear_name_list)-1))
random_fear3_name = fear_name_list[random_fear3]
print(random_fear3_name)
fear_name_list.pop(random_fear3)

print(len(fear_name_list))

fear_name_list.insert(random_fear2, random_fear3_name)
fear_name_list.insert(random_fear2, random_fear2_name)
fear_name_list.insert(random_fear1, random_fear1_name)

print(len(fear_name_list))




print(random_phobia)
print("correct fear for {} is {}".format(correct_phobia, correct_fear))

