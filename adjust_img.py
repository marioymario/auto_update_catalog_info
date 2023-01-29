import os
from PIL import Image

path = '/suppliers-data/images/'
for file in os.listdir('/suppliers-data/images'):
    if file.endswith('.tiff'):
        split_file = file.split('.')
        name = split[0] + '.jpeg'
        imagen = Image.open(path + file).convert('RGB')
        imagen.resize((600, 400))
        imagen.save(path + name, 'JPEG')


