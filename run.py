from PIL import Image
import os
import glob

files = glob.glob("./*.jpg")

for file in files:
    im = Image.open(file)
    newfile = file.replace('.jpg', '')
    im.save(newfile + '.png')
    os.remove(file)