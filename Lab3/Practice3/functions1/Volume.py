import math
def Volume(radius):
    return (4/3) * math.pi * radius**3
r = int(input("Введите радиус: "))
print(Volume(r))