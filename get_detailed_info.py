import os

#list dirs + timestamp (OPT: list size and log data for later comparison)
#list files + timestamp + highlight most recent changes with colors
#highlight new files

filenames = next(os.walk(os.getcwd()), (None, None, []))[2]
first = 0
lis = []
for x in os.walk(os.getcwd()):
    if first != 0:
        print(x)
        print(type(x))
        lis.append(x)
    else:
        first += 1

