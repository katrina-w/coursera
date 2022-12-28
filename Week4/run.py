#! /usr/bin/env python3

import os
import requests
import json


dirs=[]

path = "supplier-data/descriptions/"

for dir in os.listdir(path):
    if "txt" in dir:
        name, ext = os.path.splitext(dir)

        with open(path + "/" + dir) as f:
          lines = [line.rstrip('\n') for line in f]

          desc={}
          desc["name"] = lines[0]
          desc["weight"] = lines[1].strip(" lbs")
          desc["description"] = lines[2]
          desc["image_name"] = f"{name}.jpeg"

          response = requests.post("http://34.28.179.72/fruits/", json=desc)
          response.raise_for_status()
