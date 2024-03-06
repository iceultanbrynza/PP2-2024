import os
path = "/Users/iceultan/Documents/Python/Lab1/PP2-2024/Lecture6/file_handling"
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])