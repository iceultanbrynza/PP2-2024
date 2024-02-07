class Shape:
    def Area(self):
        A = 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def Area(self):
        A = self.length**2
        print(A)
class Rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def Area(self):
        A = self.length * self.width
        print(A)
dlina = int(input())
Figure = Square(dlina)
Figure.Area()

L = int(input())
W = int(input())
Rect = Rectangle(L, W)
Rect.Area()