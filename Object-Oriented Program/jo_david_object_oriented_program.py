# David Jo. Assignment 6 "Object Oriented Program"
# Program prupose: To implement a geometric object class and its subclasses to practice object oriented programming and inheritance

import datetime
import numpy as np

class GeometricObject:
    def __init__(self, color:str, filled:bool, dateCreated:datetime.datetime):
        self.color = color
        self.filled = filled
        self.dateCreated = dateCreated

    def getColor(self):
        return self.color
    
    def setColor(self, color:str):
        self.color = color

    def isFilled(self):
        return self.filled
    
    def setFilled(self, filled:bool):
        self.filled = filled

    def getDateCreated(self):
        return self.dateCreated
    
    def __str__(self):
        return f"A {type(self).__name__} was created on {self.dateCreated} \nColor of the {type(self).__name__} is {self.color} \nFilled: {self.filled}"

class Circle(GeometricObject):
    def __init__(self, radius:float):
        super().__init__("blue", True, datetime.datetime.now())
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius:float):
        self.radius = radius

    def getArea(self):
        return np.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * np.pi * self.radius

    def __str__(self):
        return f"{super().__str__()} \nThe radius is {self.radius} \nThe area is {self.getArea()} \nThe perimeter is {self.getPerimeter()}"

class Rectangle(GeometricObject):
    def __init__(self, width:float, height:float):
        super().__init__("red", False, datetime.datetime.now())
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width
    
    def setWidth(self, width:float):
        self.width = width

    def getHeight(self):
        return self.height
    
    def setHeight(self, height:float):
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{super().__str__()} \nThe width is {self.width} \nThe height is {self.height} \nThe area is {self.getArea()} \nThe perimeter is {self.getPerimeter()}"

def main():
    radius = float(input("Enter the radius of your circle: "))
    circle = Circle(radius)
    rectangle = Rectangle(5.0, 10.0)

    print()
    print(circle)
    print()
    print(rectangle)


if __name__ == "__main__":
    main()