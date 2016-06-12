#replace scr with src of Osu! songs folder
#replace dst with destination folder


import os, shutil

for folderName, subfolders, filenames in os.walk('scr'):

    for filename in filenames:
        if filename.endswith('.jpg'):
            print(filename)
            shutil.move('scr'+filename, 'dst')

    print('')
    
    
    
