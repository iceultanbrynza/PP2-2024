import os
filename = '1.py'
with open(filename, 'r') as file:
    fileread = file.read()
with open('1copy.py', 'w') as file2:
    file2.write(fileread)
