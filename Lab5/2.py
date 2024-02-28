import re
file = open("mytext.txt", "r", encoding="utf8")
text = file.read()
pattern = "ab{2,3}"
results = re.finditer(pattern, text)
for result in results:
    print(result)