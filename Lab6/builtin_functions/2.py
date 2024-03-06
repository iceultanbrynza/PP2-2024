s =input()
def isupp(s):
    for i in s:
        if i.isupper():
            return True
        else:
            return False
IsUp = list(map(isupp, s))
amount_of_uppercases = sum(IsUp)
print(f"Amount of uppercases: {amount_of_uppercases}\nAmount of lowercases: {len(s) - amount_of_uppercases}")