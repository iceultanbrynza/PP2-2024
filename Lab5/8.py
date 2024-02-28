import re
file = open("mytext.txt", "r", encoding="utf8")
text = file.read()
results = re.findall("[A-Z][^A-Z]*", text)
print(results)