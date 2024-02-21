def FromNto0(n):
    for i in reversed(range(0, n+1)):
        yield i
n = int(input())
for i in FromNto0(n):
    print(i)