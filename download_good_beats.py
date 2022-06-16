import gdown, time, os, math, dictdiffer, ntpath
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
    folder_name_list  = []
    folder_size_list  = []
    folder_mtime_list = []
    folder_ctime_list = []
    file_name_list    = []
    file_size_list    = []
    done              = False
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
        folder_name_list.append(str(x))
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
                    print("File   Size  : "+str(convert_size(os.path.getsize(beat)))+" Bytes")  
                    file_name_list.append(str(i))
                    file_size_list.append(str(convert_size(os.path.getsize(beat))))
                except FileNotFoundError:
                    print(" |-"+str(i)+" not found.")
                    continue
                #
                #  DOESNT WORK WITH WHITE SPACE IN USER PATH
    # COMPARING OLD BEATS WITH NEW BEATS
    if mode == 1:
        print("Checking current beats...") #CHECK OLD BEATS
        time.sleep(1)
        global intel_folder_size, intel_file_size, intel_folder_mtime, intel_folder_ctime

        intel_folder_size = {} # FOLDER LIST: size
        for i,j in zip(folder_name_list,folder_size_list):
            intel_folder_size[i] = j

        intel_folder_mtime = {} # FOLDER LIST: modify time
        for i,j in zip(folder_name_list,folder_mtime_list):
            intel_folder_mtime[i] = j

        intel_folder_ctime = {} # FOLDER LIST: creation time
        for i,j in zip(folder_name_list,folder_ctime_list):
            intel_folder_ctime[i] = j

        intel_file_size = {}   # FILE LIST: size
        for i,j in zip(file_name_list,file_size_list):
            intel_file_size[i] = j

    elif mode == 2:
        print("Checking new beats...") #CHECK NEW BEATS
        time.sleep(1)

        intel2_folder_size = {} # FOLDER LIST: size
        for i,j in zip(folder_name_list,folder_size_list):
            intel2_folder_size[i] = j

        intel2_folder_mtime = {} # FOLDER LIST: modify time
        for i,j in zip(folder_name_list,folder_mtime_list):
            intel2_folder_mtime[i] = j

        intel2_folder_ctime = {} # FOLDER LIST: creation time
        for i,j in zip(folder_name_list,folder_ctime_list):
            intel2_folder_ctime[i] = j

        intel2_file_size = {}   # FILE LIST: size
        for i,j in zip(file_name_list,file_size_list):
            intel2_file_size[i] = j

        # COMPARING BEATS
        print("COMPARING...") # COMPARE OLD BEATS WITH NEW BEATS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        time.sleep(1)
        if intel_folder_size == intel2_folder_size and intel_folder_mtime == intel2_folder_mtime and intel_folder_ctime == intel2_folder_ctime and intel_file_size == intel2_file_size:
            print("NO CHANGES!")
        else:
            print("SOMETHING CHANGED!")
            time.sleep(1)
            ##### DISPLAYING CHANGES ## DISPLAYING CHANGES ## DISPLAYING CHANGES #####

            for dif in list(dictdiffer.diff(intel_folder_size,intel2_folder_size)): # folder size differences

                if dif[0] == "change":
                    name   = str(dif[1]).replace("[","").replace("]","")
                    change = dif[2]
                    print("Folder "+ntpath.basename(name)+ " changed in size from "+change[0]+" to "+change[1]+".")
                elif dif[0] == "remove":
                    name   = str(dif[2]).replace("[","").replace("]","")
                    print("Folder "+ntpath.basename(name)+ " was removed.")
            
            for dif in list(dictdiffer.diff(intel_folder_mtime,intel2_folder_mtime)): # folder mtime differences

                if dif[0] == "change":
                    name   = str(dif[1]).replace("[","").replace("]","")
                    change = dif[2]
                    print("Folder "+ntpath.basename(name)+ " changed in mtime from "+change[0]+" to "+change[1]+".")
                elif dif[0] == "remove":
                    name   = str(dif[2]).replace("[","").replace("]","")
                    print("Folder "+ntpath.basename(name)+ " was removed.")

            for dif in list(dictdiffer.diff(intel_folder_ctime,intel2_folder_ctime)): # folder ctime differences

                if dif[0] == "change":
                    name   = str(dif[1]).replace("[","").replace("]","")
                    change = dif[2]
                    print("Folder "+ntpath.basename(name)+ " changed in ctime from "+change[0]+" to "+change[1]+".")
                elif dif[0] == "remove":
                    name   = str(dif[2]).replace("[","").replace("]","")
                    print("Folder "+ntpath.basename(name)+ " was removed.")

            for dif in list(dictdiffer.diff(intel_file_size,intel2_file_size)): # file size differences

                if dif[0] == "change":
                    name   = str(dif[1]).replace("[","").replace("]","")
                    change = dif[2]
                    print("File "+name+ " changed in size from "+change[0]+" to "+change[1]+".")
                elif dif[0] == "remove":
                    name   = str(dif[2]).replace("(","").replace(")","").split(",")
                    name1  = str(name[0]).replace("[","")
                    name2  = str(name[1]).replace(" '","").replace("]","").replace("'","")
                    print("File "+name1+ " ("+name2+") was removed.")

#################################################################################### PROGRAM START ####################################################################################

#getting intel about current beats
get_info(1)

# DOWNLOADING BEATS BY BRENDLEF
print(clear)
print("DOWNLOADING...")
#gdown.download_folder(url, quiet=True)                         # DOWNLOADING BEATS, NOT NECESSARY FOR EACH TEST
print(clear)
input("DONE!!!") #for debugging only
time.sleep(1)

#getting intel about new beats and comparing with old ones
get_info(2)

# compare without libraries? use multiple dicts (file size, file name, file modify time?)