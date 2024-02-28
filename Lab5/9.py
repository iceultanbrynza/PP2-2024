import re
file = open("mytext.txt", "r", encoding="utf8")
text = file.read()
results = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(results)