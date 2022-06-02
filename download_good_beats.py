import gdown, time, os, math, dictdiffer
from   colorama import *
from   art      import *
from   datetime import datetime

# fix file details
# fix comparison

#initializing colorama for the "clear" variable being able to clear the screen
init()

# clear var to clear screen
clear      = "\033[2J\033[1;1f"

# Beats By Brendlef link
url = "https://drive.google.com/drive/folders/1WjQxT1s_oW8AXsvmO4rAcL2b5h4fmW95?usp=sharing"

# Function to convert size to displayable information
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# Function to get info about beats in program folder, compare and deliver report
def get_info(mode):
    folder_main_list  = []
    folder_size_list  = []
    folder_mtime_list = []
    folder_ctime_list = []
    file_main_list    = []
    file_size_list    = []
    #accessing files and folders for information
    for x, y, z in os.walk(os.getcwd()): # x = main folder | y = subfolders | z = files
        # avoid getting info about git folder
        if "git" in str(x):
            continue
        folder_size = 0
        for f in z:
                fp = os.path.join(x, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    folder_size += os.path.getsize(fp)
        folder = str(os.path.basename(x))             #  get main folder name, last accessed time, last modified time, creation time and size in bytes
        tprint(folder, font="cyber")
        print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(x)).strftime("%A, %B %d, %Y %I:%M:%S")) # MAIN FOLDER
        print("Created      : "+datetime.fromtimestamp(os.path.getctime(x)).strftime("%A, %B %d, %Y %I:%M:%S"))
        print("Folder Size  : "+str(convert_size(folder_size)))
        folder_main_list.append(str(x))
        folder_size_list.append(str(convert_size(folder_size)))
        folder_mtime_list.append(str(datetime.fromtimestamp(os.path.getmtime(x)).strftime("%A, %B %d, %Y %I:%M:%S")))
        folder_ctime_list.append(str(datetime.fromtimestamp(os.path.getctime(x)).strftime("%A, %B %d, %Y %I:%M:%S")))
        print("-Folders in "+folder+":")
        if not y:
            print(" |NO FOLDERS IN "+folder+"!")
        else:
            for i in y:
                print(" |"+i)                         #  get sub  folder name, last accessed time, last modified time, creation time and size in bytes
                print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(i)).strftime("%A, %B %d, %Y %I:%M:%S")) # SUB FOLDERS
                print("Created      : "+datetime.fromtimestamp(os.path.getctime(i)).strftime("%A, %B %d, %Y %I:%M:%S"))
                #print("Folder Size  : "+str(os.path.getsize(i))+" Bytes")                                                      incorrect value
                #print("Folder Size  : "+str(sum([os.path.getsize(i) for i in os.listdir('.') if os.path.isfile(i)]))+" Bytes") also wrong?
        print("-Files   in "+folder+":")
        if not z:
            print(" |-NO FILES IN "+folder+"!")
        else:
            for i in z:
                try:
                    print(" |-"+i)                        #  get file name, last accessed time, last modified time, creation time and size in bytes
                    beat = str(x)+"\\"+str(i)                    
                    print("Last modified: "+datetime.fromtimestamp(os.path.getmtime(os.path.abspath(beat))).strftime("%A, %B %d, %Y %I:%M:%S")) # FILES
                    print("Created      : "+datetime.fromtimestamp(os.path.getctime(os.path.abspath(beat))).strftime("%A, %B %d, %Y %I:%M:%S"))
                    print("File   Size  : "+str(os.path.getsize(beat))+" Bytes")  
                    file_main_list.append(str(i))
                    file_size_list.append(str(convert_size(os.path.getsize(beat))))
                except FileNotFoundError:
                    print(" |-"+str(i)+" not found.")
                    continue
                #
                #  DOESNT WORK DUE TO WHITE SPACE IN MY USERNAME1
    # COMPARING OLD BEATS WITH NEW BEATS
    if mode == 1:
        print("Checking current beats...")
        time.sleep(1)
        global intel_folder, intel_file
        fields = ["Folder Name", "Folder Size",  "Folder Modify Time", "Folder Creation Time"]
        values = [folder_main_list,folder_size_list, folder_mtime_list, folder_ctime_list]
        intel_folder = dict(zip(fields,values))
        fields = ["File Name", "File Size"]
        values = [file_main_list,file_size_list]
        intel_file = dict(zip(fields,values))
    elif mode == 2:
        print("Checking new beats...")
        time.sleep(1)
        fields = ["Folder Name", "Folder Size",  "Folder Modify Time", "Folder Creation Time"]
        values = [folder_main_list,folder_size_list, folder_mtime_list, folder_ctime_list]
        intel2_folder = dict(zip(fields,values))
        fields = ["File Name", "File Size"]
        values = [file_main_list,file_size_list]
        intel2_file = dict(zip(fields,values))
        # COMPARING BEATS
        print("COMPARING...")
        time.sleep(1)
        if intel_folder == intel2_folder:
            print("NO CHANGES!")
        else:
            print("SOMETHING CHANGED!")
            time.sleep(1)
            # DISPLAYING CHANGES
            for diff in list(dictdiffer.diff(intel_folder, intel2_folder)):
                foldif = diff
                if   foldif[0] == "change": # if Folder Size in info1[0] or if Modify Time
                    info1 = foldif[1]
                    info2 = foldif[2]
                    print(str(info1[0])+" of Folder '"+str(info1[1])+"' changed from "+str(info2[0])+" to "+str(info2[1])+".")
                    for dif in list(dictdiffer.diff(intel_file,intel2_file)):
                        fildif = dif
                        if   fildif[0] == "change" and "File Size" in fildif[1]:
                            print("File "+str(fildif[2])+" changed in Size.")
                            #print(str(fildif[3]))
                        elif fildif[0] == "remove" and "File Name" in fildif[1]:
                            print("File "+str(fildif[2])+" was removed.")
                elif  foldif[0] == "remove" and "Folder Creation Time" in foldif[1]:
                    info = str(foldif[2]).replace("(","").replace(")","")
                    info = info.replace("[","").replace("'","").replace("]","")
                    info = info.split(",") # splits still too much
                    dt   = str(info[1])+str(info[2])+str(info[3])
                    print("Folder '"+str(info[0])+"' was removed. It's recorded Creation Date is"+dt+".")
                for dif in list(dictdiffer.diff(intel_file,intel2_file)):
                    fildif = dif
                    if fildif[0] == "change" and "File Name" in fildif[1]:
                        info = fildif[2]
                        print("File "+str(info[0])+" was renamed to "+str(info[1]+"."))
                for dif in list(dictdiffer.diff(intel_file,intel2_file)):
                        fildif = dif
                        if fildif[0] == "remove" and "File Name" in fildif[1]:
                            print("File "+str(fildif[2])+" was removed.")
                    

#################################################################################### PROGRAM START ####################################################################################

#getting intel about current beats
get_info(1)

# DOWNLOADING BEATS BY BRENDLEF
print(clear)
print("DOWNLOADING...")
#gdown.download_folder(url, quiet=True)                       # DOWNLOADING BEATS, NOT NECESSARY FOR EACH TEST
print(clear)
input("DONE!!!")
time.sleep(1)

#getting intel about new beats and comparing with old ones
get_info(2)