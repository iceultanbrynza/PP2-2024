import os
path = "/Users/iceultan/Documents/Python/Lab1/PP2-2024/Lecture6/file_handling"
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK)) 
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))