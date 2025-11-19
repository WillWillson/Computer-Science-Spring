######################################################################################################################
# Name: William WIlson
# Date: 3/17/2021
# Description: This program will calculate the distance and midpoint for each of the given points.
######################################################################################################################
import math

# the 2D point class
class Point:
    
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    #Getter for x value
    @property
    def x(self):
        return self._x

    #Setter for x value
    @x.setter
    def x(self, value):
        self._x = float(value)

    #Getter for y value
    @property
    def y(self):
        return self._y

    #setter for the y value
    @y.setter
    def y(self, value):
        self._y = float(value)

    # Function to calculate distance
    def dist(self, point2):
        x = (point2.x-self.x)**2
        y = (point2.y-self.y)**2
        distance = (x+y)**(1/2)
        return distance

    #Function that calculates midpoint
    def midpt(self, point2):
        x = (self.x+point2.x)/2
        y = (self.y+point2.y)/2
        midpoint = Point(x,y)
        return midpoint

    #this function allows the beginning points to be read
    def __str__(self):
        return ("({},{})".format(self.x, self.y))
        
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
# calculate and display some distances
print("distance from p1 to p2:", p1.dist(p2))
print("distance from p2 to p3:", p2.dist(p3))
print("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print("midpt of p1 and p2:", p1.midpt(p2))
print("midpt of p2 and p3:", p2.midpt(p3))
print("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print("p4:", p4)
print("distance from p4 to p1:", p4.dist(p1))
