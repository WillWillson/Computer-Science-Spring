######################################################################################################################
# Name: William Wilson
# Date: 4/16/2021
# Description: This program allows for different shapes to be displayed using astrix's
######################################################################################################################

# Shape class
class Shape:
    def __init__(self, w, h):
        # allows the width to not be a negative value
        if w <= 0:
            w = 1
        self.width = w
        # allows the height to not be a negative value
        if h <= 0:
            h = 1
        self.height = h

    # getters and setters for width and height
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if(value >= 0):
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if(value >= 0):
            self._height = value

    # string function that allows the rectangle and square to be drawn out  
    def __str__(self):
        # creates the square
        for i in range(self.height):
            print("* " * self.width)
        return " "
    
# rectangle class
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)

# square class
class Square(Shape):
    def __init__(self, w):
        super().__init__(w, w)

# triangle class
class Triangle(Shape):
    def __init__(self, w):
        super().__init__(w, w)

    # allows the triangle to be drawn
    def __str__(self):
        # creates the triangle
        for i in range(self.height):
            print("* " * (self.height - i))
        return " "

# parallelogram class
class Parallelogram(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)

    # allows the different parallelograms to be displayed
    def __str__(self):
        # creates the parallelogram
        for i in range(self.height):
            print("  " * (self.height - 1 - i) + "* " * (self.width))
        return " "
            
        

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print(r1)
s1 = Square(6)
print(s1)
t1 = Triangle(7)
print(t1)
p1 = Parallelogram(10, 3)
print(p1)
r2 = Rectangle(0, 0)
print(r2)
p1.width = 2
p1.width = -1
p1.height = 2
print(p1)

