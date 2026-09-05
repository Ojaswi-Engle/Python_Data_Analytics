#abstraction
from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Triangle(Shape):
    def area(self):
        print('calculating area of triangle')

class Rectangle(Shape):
    def area(self):
        print('calculating area of Rectangle')

class Circle(Shape):
    def area(self):
        print('calculating area of Circle')

t=Triangle()
r=Rectangle()
c=Circle()
t.area()
r.area()
c.area()

