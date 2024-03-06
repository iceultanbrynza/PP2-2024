import os
path = 'A.txt'
if (os.path.exists(path)):
    os.remove(path)
else: print("no such dir")