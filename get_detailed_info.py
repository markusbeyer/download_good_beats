import os, re
from art import *
from datetime import datetime

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
    print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
    print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
    print("Created      : "+datetime.fromtimestamp(os.path.getctime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
    print("Folder Size  : "+str(os.path.getsize(x))+" Bytes")
    print("-Folders in "+folder+":")
    if not y:
        print(" |NO FOLDERS IN "+folder+"!")
    else:
        for i in y:
            print(" |"+i)
            print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(i)).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(i)).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Created      : "+datetime.fromtimestamp(os.path.getctime(i)).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Folder Size  : "+str(os.path.getsize(i))+" Bytes")
    print("-Files   in "+folder+":")
    if not z:
        print(" |-NO FILES IN "+folder+"!")
    else:
        for i in z:
            print(" |-"+i)
            file = str(os.path.abspath(i))
            file = re.sub(r'^.*?GDrive', 'GDrive', file)
            file = file.replace("GDrive_Updater","")
            print(file)
            os.path.getatime(os.path.abspath(file))
            print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(os.path.abspath(file))).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(os.path.abspath(file))).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Created      : "+datetime.fromtimestamp(os.path.getctime(os.path.abspath(filei))).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("File   Size  : "+str(os.path.getsize(file))+" Bytes")
