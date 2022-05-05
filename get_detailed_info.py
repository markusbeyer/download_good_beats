import os, pathlib
from art import *

#list dirs + timestamp (OPT: list size and log data for later comparison)
#list files + timestamp + highlight most recent changes with colors
#highlight new files

filenames = next(os.walk(os.getcwd()), (None, None, []))[2]
lis = []
for x, y, z in os.walk(os.getcwd()):
    if "git" in str(x):
        continue
    folder = str(os.path.basename(x))
    tprint(folder, font="cyber")
    print(str(pathlib.Path.stat(pathlib.Path(x)))+")")
    print("-Folders in "+folder+":")
    if not y:
        print(" |NO FOLDERS IN "+folder+"!")
    else:
        for i in y:
            print(" |"+i)
    print("-Files   in "+folder+":")
    if not z:
        print(" |-NO FILES IN "+folder+"!")
    else:
        for i in z:
            print(" |-"+i)
