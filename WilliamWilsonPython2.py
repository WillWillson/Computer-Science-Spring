######################################################################################################################
# Name: William Wilson
# Date: 3/24/21
# Description: The task is to implement a coordinate system using tkinter that will plot points on a graph.
######################################################################################################################

from tkinter import *
from random import randint

# the 2D point class
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    #The getter for the x value
    @property
    def x(self):
        return self._x

    #The setter for the x value
    @x.setter
    def x(self, value):
        self._x = float(value)

    #The getter for the y value
    @property
    def y(self):
        return self._y

    #The setter for the y value
    @y.setter
    def y(self, value):
        self._y = float(value)

    # Function that calculates the distance
    def dist(self, point2):
        x = (point2.x-self.x)**2
        y = (point2.y-self.y)**2
        distance = (x+y)**(1/2)
        return distance

    # Function that calculates the midpoint
    def midpt(self, point2):
        x = (self.x+point2.x)/2
        y = (self.y+point2.y)/2
        midpoint = Point(x,y)
        return midpoint

    # This function allows the beginning points to be read
    def __str__(self):
        return("({},{})".format(self.x, self.y))

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter

# Class to display the cordinate system
class CoordinateSystem(Canvas):

    # establishes the canvas
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    # Function that plots the points on the canvas
    def plotPoints(self, n):
        for i in range(n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x, y)

    # Function that chooses the color for the border and the inside of each of the points
    def plot(self, x, y):
        POINT_COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        POINT_RADIUS = 0
        color = POINT_COLORS[randint(0, len(POINT_COLORS) - 1)]
        color2 = POINT_COLORS[randint(0, len(POINT_COLORS) - 1)]
        self.create_oval(x, y,\
                         x + POINT_RADIUS * 2,\
                         y + POINT_RADIUS * 2,\
                         outline = color, fill=color2)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
