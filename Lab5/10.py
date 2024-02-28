import re
file = open("mytext.txt", "r", encoding="utf8")
text = file.read()
pattern = r"(\S)([A-Z])"
results = re.sub(pattern, r"\1_\2", text).lower()
print(results)