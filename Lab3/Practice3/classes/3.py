import math
class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.res1 = 0
        self.res2 = 0
    def Show(self):
        print(f"Coordinates of point are: ({self.x}, {self.y})")
    def Move(self):
        self.res1 = self.x
        self.res2 = self.y
        self.x = int(input("Input new x-coordinate: "))
        self.y = int(input("Input new y-coordinate: "))
    def Dist(self):
        D = math.sqrt((self.x - self.res1)**2 + (self.y - self.res2)**2)
        print(D)
x = int(input("Write x-coordinate of new point: "))
y = int(input("Write y-coordinate of new point: "))
Pt = Point(x, y)
Pt.Show()
Pt.Move()
Pt.Dist()