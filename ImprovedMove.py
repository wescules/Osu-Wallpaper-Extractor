#replace with src and dst

import os, shutil
from PIL import Image

for root, dirs, files in os.walk('C:\Users\Wesley\AppData\Local\osu!\Songs'):
    for file in files:
    	if file[-4:].lower() == '.jpg':
    		with Image.open(file) as im:
    			width, height = im.size
    			if width >= 1280 && height >= 720:
    				shutil.copy(os.path.join(root, file), os.path.join('C:\Users\Wesley\Desktop\walls', file))

#walks through osu folder and only add wallpapers that are above the 1280x720 dimension range
