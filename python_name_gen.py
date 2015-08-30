# Python port from startup name generator (js) github.com/lifeonhoth
# Construct "startup names" by randomly selecting from pre-populated templates

# TO DO: connect web using flask

import random

# build list of first words ending in a vowel
	#assign to a variable one from list selected at random
word_vow = [
        "Natura",
        "Form",
        "Inova",
        "Ino",
        "Agri",
        "Aero",
        "Ampli",
        "Archi",
        "Ardu",
        "Wiffle",
        "Bibbli",
        "Chroma",
        "Compu",
        "Forma",
        "Prime",
        "Chrono"
    ]

# build list of first words ending in a consonant
	#assign to a variable one from list selected at random
word_con = [
        "Bit",
        "Gen",
        "Form",
        "Inov",
        "Box",
        "Vox",
        "Amp",
        "Alt",
        "Arc",
        "Box",
        "Cash",
        "Pocket",
        "Bibbl",
        "Vid",
        "Cloud",
        "Phlux",
        "Fab", 
        "Narc",
        "Pharm", 
        "Paint"
    ]

# build list of suffix to go with consonants
	#assign to a variable one from list selected at random
suffix_con = [
        "r",
        ".io",
        ".ly",
        ".js",
        "able",
        "r",
        ".tv"     
    ]


# build list of suffix to go with vowels
	#assign to a variable one from list selected at random
suffix_vow = [
        ".ly",
        "sense",
        ".js",
        "dyn",
        "gen",
        "co",
        "ble",
        "hub"
    ]

# build word: random-word-consonant + random-suffix-consonant
# build word: random-word-vowel + random-suffix-vowel

# output: randomly select as output, one of the built words
#print word.randomchoice()

#print word_con[2] + suffix_con[random.randint(0, 7)] # for testing	
print word_con[random.randint(0, len(word_con) - 1)] + suffix_con[random.randint(0, len(suffix_con) - 1)]



	