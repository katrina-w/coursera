#!/usr/bin/env python3

from PIL import Image
import os

path = "supplier-data/images"

dirs=[]

for dir in os.listdir(path):
    if "tiff" in dir:
        name, ext = os.path.splitext(dir)
        full_loc = path + "/" + dir
        im = Image.open(full_loc)
        im = im.resize((600,400)).convert("RGB")
        im.save(path + "/" + name + ".jpeg", "JPEG")
    
