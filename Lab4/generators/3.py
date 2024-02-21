n = int(input())

def onlyEvens(n):
    for i in range(0, n+1):
        if(i%3==0 and i%4==0):
            yield i

TnF = onlyEvens(n)
for i in TnF:
    print(i)