import math
class Shape:
    def area(self):
        print("Area of shapes")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
c1 = Circle(3)
print("Area of circle :",c1.area())
s1 = Square(6)
print("Area of Square :",s1.area())
tr1 = Triangle(25,20)
print("Area of Triangle :",tr1.area())