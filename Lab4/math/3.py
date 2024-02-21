import math
def Polygon(sides, length):
    A = (sides*length**2) / (4 * math.tan(math.pi/sides))
    return A
a = int(input())
l = int(input())
print(Polygon(a, l))