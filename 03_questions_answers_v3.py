# Achluophobia is the fear of:

# darkness  noise
# heights   flying

# what is the fear of darkness called:

# Achluophobia  Enochlophobia 
# Pogonophobia  Traumatophobia 

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
'butterflies', 'tornadoes or hurricanes', 'cooking', 'black', 'bees', 'being alone', 'mice', 'ants', 'death', 'new things', 'night', 'hospitals', 'numbers', 'darkness', 
'weight gain', 'eyes', 'dreams', 'snakes', 'birds', 'smells', 'shellfish', 'everything', 'babies and children', 'medicine', 'ghosts', 'fear', 'loud sounds', 'beards', 'purple', 
'flying', 'fire', 'radioactivity', 'roller coasters', 'trains', 'people', 'sleep', 'graves', 'technology', '4', 'sea', 'dying', 'heat', 'poisons', 'injury', 'hair loss', '13', 
'driving', 'yellow', 'foreigners'
]


# get random phobia and correct fear name
random_phobia = random.randint(1, len(phobia_list))
correct_phobia = phobia_list[random_phobia]
print("{}is the fear of:".format(correct_phobia))
correct_fear = fear_name_list[random_phobia]
print(correct_fear)

# remove used phobia and fear name from list
print(len(phobia_list))
phobia_list.pop(random_phobia)
fear_name_list.pop(random_phobia)
print(len(phobia_list))

# generate 3 random (different) fear names
random_fears = random.sample(range(1, len(fear_name_list)-1), 3)
print(random_fears)

random_fear_1 = random_fears[0]
print(random_fear_1)
random_fear1_name = fear_name_list[random_fear_1]
print(random_fear1_name)

random_fear_2 = random_fears[1]
print(random_fear_2)
random_fear2_name = fear_name_list[random_fear_2]
print(random_fear2_name)

random_fear_3 = random_fears[2]
print(random_fear_3)
random_fear3_name = fear_name_list[random_fear_3]
print(random_fear3_name)

# put all 4 answers in random order
random_num = random.sample(range(1,5),4)
print(random_num)

fear_answers_list = [correct_fear, random_fear1_name, random_fear2_name, random_fear3_name]
print(fear_answers_list)

answer1 = fear_answers_list[random_num[0]-1]
print(answer1)
answer2 = fear_answers_list[random_num[1]-1]
print(answer2)
answer3 = fear_answers_list[random_num[2]-1]
print(answer3)
answer4 = fear_answers_list[random_num[3]-1]
print(answer4)




