n = int(input())

def toPowerOfTwo(n):
    for i in range(1, n+1):
        yield i**2

squares = toPowerOfTwo(n)
for i in squares:
    print(i)