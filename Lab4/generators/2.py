n = int(input())

def onlyEvens(n):
    for i in range(0, n+1):
        if(i%2==0):
            yield i

evens = onlyEvens(n)
for i in evens:
    print(i)