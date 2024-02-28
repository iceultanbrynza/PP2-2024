import re
file = open("mytext.txt", "r", encoding="utf8")
text = file.read()
pattern = r"a[\S]+b"
results = re.finditer(pattern, text)
for result in results:
    print(result)