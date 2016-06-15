#replace with src and dst

import os, shutil
for root, dirs, files in os.walk('/Users/Weezy/Desktop/Songs'):
    for file in files:
    	if file[-4:].lower() == '.jpg':
    		shutil.copy(os.path.join(root, file), os.path.join('/Users/Weezy/Desktop/b', file))
