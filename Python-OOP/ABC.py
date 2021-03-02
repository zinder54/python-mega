from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCmeta):
    @abstractmethod
    def area(self):
        return 0

class Square:
    sides = 4
    def area(self):
        print("the area of a squeare is: ",self.sides * self.sides)

class Rectangle:
    width = 5
    length = 10
    def area(self):
        print("the area of a rectangle is: ", self.width * self.length)
square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()