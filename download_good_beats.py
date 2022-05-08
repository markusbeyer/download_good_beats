import gdown, time, os
from   colorama import *
from   art      import *
from   datetime import datetime
#TO-DO list dirs  + timestamp (OPT: list size and log data for later comparison)
#TO-DO list files + timestamp + highlight most recent changes with colors
#TO-DO highlight new files

#initializing colorama for the "clear" variable being able to clear the screen
init()

# clear var to clear screen
clear      = "\033[2J\033[1;1f"

# Beats By Brendlef link
url = "https://drive.google.com/drive/folders/1WjQxT1s_oW8AXsvmO4rAcL2b5h4fmW95?usp=sharing"

print("You're about to download the newest Beats by Brendlef!")
time.sleep(1)
print("You down?")
time.sleep(1)
print("(1) CHEAH | NAH (2)")
choice = input("")
if choice == "1":
    print("THAT'S WASSUP!")
    time.sleep(1)
    print("Les gooo")
    time.sleep(1)
elif choice == "2":
    print("Ait f u den")
    time.sleep(1)
    print("busta")
    time.sleep(1)
    os._exit(0)
else:
    print("That ain't it")
    time.sleep(1)
    os._exit(0)

# DOWNLOADING BEATS BY BRENDLEF
print(clear)
print("DOWNLOADING...")
gdown.download_folder(url, quiet=True)
print(clear)
print("DONE!!!")
time.sleep(1)
#walking through downloaded folders
filenames = next(os.walk(os.getcwd()), (None, None, []))[2]
#accessing files and folders for information
for x, y, z in os.walk(os.getcwd()): # x = main folder | y = subfolders | z = files
    # avoid getting info about git folder
    if "git" in str(x):
        continue
    folder = str(os.path.basename(x))             #  get main folder name, last accessed time, last modified time, creation time and size in bytes
    tprint(folder, font="cyber")
    print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
    print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(x)).strftime("%A, %B %d, %Y %I:%M:%S")) # MAIN FOLDER
    print("Created      : "+datetime.fromtimestamp(os.path.getctime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
    #print("Folder Size  : "+str(os.path.getsize(x))+" Bytes")  incorrect value
    print("Folder Size  : "+str(sum([os.path.getsize(x) for x in os.listdir('.') if os.path.isfile(x)]))+" Bytes")
    print("-Folders in "+folder+":")
    if not y:
        print(" |NO FOLDERS IN "+folder+"!")
    else:
        for i in y:
            print(" |"+i)                         #  get sub  folder name, last accessed time, last modified time, creation time and size in bytes
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
            #print(pathlib.Path.stat(str(i)))
            #file = str(os.path.abspath(i))
            #file = re.sub(r'^.*?GDrive', 'GDrive', file)
            #file = file.replace("GDrive_Updater","")
            #print(file)
            #print(str(pathlib.Path.stat(pathlib.Path(os.path.relpath(i))))+")")
            #os.path.getatime(os.path.abspath(file))
            #print("done")                         #  get file name, last accessed time, last modified time, creation time and size in bytes
            #print("Last accessed: "+datetime.fromtimestamp(os.path.getatime(os.path.abspath(i))).strftime("%A, %B %d, %Y %I:%M:%S"))
            #print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(os.path.abspath(i))).strftime("%A, %B %d, %Y %I:%M:%S")) # FILES
            #print("Created      : "+datetime.fromtimestamp(os.path.getctime(os.path.abspath(i))).strftime("%A, %B %d, %Y %I:%M:%S"))
            #print("File   Size  : "+str(os.path.getsize(i))+" Bytes")  
            #
            #  DOESNT WORK DUE TO WHITE SPACE IN MY USERNAME1
