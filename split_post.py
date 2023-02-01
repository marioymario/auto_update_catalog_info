#!/usr/bin/env python3

import os
import requests

# Defining an empty dictionary with the keys
# and and index starting at 0.
fruits = {}
keys = ['name', 'weight', 'description', 'image_name']
index = 0

# Paths
path_in  = './suppliers-data/descriptions'
img_path = './suppliers-data/images'
externalip = ''
# Iterating over files in the directory of descriptions.
# Opening each file, reading the lines looking for 'lbs',
# then transforming it to an integer, storing it in a variable wght,
# and then value for the key weight, previously defined.
# if 'lbs' not found, it means is the description and
# storing the rest of the text in the key value 'description'.
# we increment the index by one each loop
for file in os.listdir(path_in):
    with open(path_in + '/' + file) as doc:
        for lineas in doc:
            line = lineas.strip()
            if 'lbs' in line:
                new_line = line.split()
                peso = int(new_line[0])
                fruit['weight'] = peso
                index += 1
            else:
                try:
                    fruit[key[index]] = line
                except:
                    fruits['description'] = line
        index = 0
        split_doc = doc.split('.')
        name = split_doc[0] + '.jpeg'
        # image part
        for image in os.listdir(img_path):
            if image == name:
                fruit['image_name'] = name

        r_post = requests.post(f'http://{externalip}/fruits/', json=fruits)
        fruits.clear()





    
