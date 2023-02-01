#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

"""
takes the jpeg images from the supplier-data/images
directory that you've processed previously and
uploads them to the web server fruit catalog.
"""
path = 'supplier-data/images/'
url = "http://localhost/upload/"
for f in os.listdir("./supplier-data/images"):
    if f.endswith(".jpeg"):
        with open('./supplier-data/images/' + f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
