import gdown, time , os
from colorama       import *
init()

clear      = "\033[2J\033[1;1f"

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
    lesgooo = True
elif choice == "2":
    print("Ait f u den")
    time.sleep(1)
    print("busta")
    time.sleep(1)
    os._exit()
else:
    print("That ain't it")
    time.sleep(1)
    os._exit()

if lesgooo == True:
    url = "https://drive.google.com/drive/folders/1WjQxT1s_oW8AXsvmO4rAcL2b5h4fmW95?usp=sharing"
    output = "eagle"
    gdown.download_folder(url, quiet=True)
