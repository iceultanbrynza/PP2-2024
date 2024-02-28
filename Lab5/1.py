import re
file = open("row.txt", "r", encoding="utf8")
text = file.read()
pattern = "ab*"
results = re.finditer(pattern, text)
for result in results:
    print(result)