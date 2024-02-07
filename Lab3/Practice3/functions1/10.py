def Reverse(stroka):
    return stroka[::-1]
def IsPalindrome(stroka):
    reverse = Reverse(stroka)
    if(reverse == stroka):
        print("YES")
    else:
        print("NO")

s = input()
IsPalindrome(s)