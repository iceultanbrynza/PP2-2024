import os
filename = "1.txt"
with open(filename, "r") as file:
    print(len(file.readlines()))
