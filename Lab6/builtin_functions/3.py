def IsPalindrome(word):
    if word == "".join(reversed(word)):
        return True
s = input()

print(IsPalindrome(s))