import os
l = [1,2,3,4,5]
filename = '2.txt'
with open(filename, 'w') as file:
    file.write(str(l))