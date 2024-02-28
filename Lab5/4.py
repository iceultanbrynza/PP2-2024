import re
file = open("mytext.txt", "r", encoding="utf8")
text = file.read()
pattern = "[A-Z][a-z]+"
results = re.finditer(pattern, text)
for result in results:
    print(result)