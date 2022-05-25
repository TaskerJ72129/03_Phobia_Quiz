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


random_phobia = random.randint(1, len(phobia_list))
print(random_phobia)
correct_phobia = phobia_list[random_phobia]
print("{}is the fear of:".format(correct_phobia))

