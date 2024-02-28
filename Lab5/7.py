import re
file = open("snake.txt", "r", encoding="utf8")
text = file.read()
pattern = r"_"
def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


print(snake_to_camel(text))