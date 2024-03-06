import os

path = '/Users/iceultan/Documents/Python/Lab1/PP2-2024/Lecture6/file_handling'
if os.path.exists(path):    
    files = os.path.basename(path)
    directories = os.path.dirname(path)    
print("Files: ", files)    
print("Directories: ", directories)