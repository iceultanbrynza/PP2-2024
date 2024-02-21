import math
def TrapArea(a, b, h):
    return ((a+b)*h)/2
a = int(input('First base: '))
b = int(input('Second base: '))
h = int(input('Height: '))
print(TrapArea(a, b, h))