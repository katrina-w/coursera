#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = "supplier-data/images"

dirs=[]

for dir in os.listdir(path):
    if "jpeg" in dir:
        name, ext = os.path.splitext(dir)
        full_loc = path + "/" + dir
        with open(full_loc, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
