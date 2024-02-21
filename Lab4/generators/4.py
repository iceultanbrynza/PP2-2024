def Squares(a,b):
    for i in range(a,b):
        yield i**2
a = int(input())
b = int(input())
for value in Squares(a,b):
    print(value)