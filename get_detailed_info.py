import os, re, pathlib
from art import *
from datetime import datetime

#list dirs  + timestamp (OPT: list size and log data for later comparison)
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
    print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(x)).strftime("%A, %B %d, %Y %I:%M:%S")) # MAIN FOLDER
    print("Created      : "+datetime.fromtimestamp(os.path.getctime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
    print("Folder Size  : "+str(os.path.getsize(x))+" Bytes")
    print("-Folders in "+folder+":")
    if not y:
        print(" |NO FOLDERS IN "+folder+"!")
    else:
        for i in y:
            print(" |"+i)
            print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(i)).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(i)).strftime("%A, %B %d, %Y %I:%M:%S")) # SUB FOLDERS
            print("Created      : "+datetime.fromtimestamp(os.path.getctime(i)).strftime("%A, %B %d, %Y %I:%M:%S"))
            print("Folder Size  : "+str(os.path.getsize(i))+" Bytes")
    print("-Files   in "+folder+":")
    if not z:
        print(" |-NO FILES IN "+folder+"!")
    else:
        for i in z:
            print(" |-"+i)
            print(pathlib.Path.stat(str(i)))
            #file = str(os.path.abspath(i))
            #file = re.sub(r'^.*?GDrive', 'GDrive', file)
            #file = file.replace("GDrive_Updater","")
            #print(file)
            #print(str(pathlib.Path.stat(pathlib.Path(os.path.relpath(i))))+")")
            #os.path.getatime(os.path.abspath(file))
            #print("done")
            #print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(os.path.abspath(i))).strftime("%A, %B %d, %Y %I:%M:%S"))
            #print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(os.path.abspath(i))).strftime("%A, %B %d, %Y %I:%M:%S")) # FILES
            #print("Created      : "+datetime.fromtimestamp(os.path.getctime(os.path.abspath(i))).strftime("%A, %B %d, %Y %I:%M:%S"))
            #print("File   Size  : "+str(os.path.getsize(i))+" Bytes")  
            #
            #  DOESTN WORK DUE TO WHITE SPACE IN MY USERNAME