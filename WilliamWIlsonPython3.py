####################################################################
# Name: William Wilson
# Date: 4/14/21
# Description: This program creates a fractal out of triangles to display a pyramid shape with 50,000 points
####################################################################
from tkinter import *
from random import *

# the 2D point class
class Point:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

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

    #This function allows the beginning points to be read
    def __str__(self):
        return("({},{})".format(self.x, self.y))

# the chaos game class
class ChaosGame(Canvas):
    # establishes the canvas
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    # Function that plots the points on the canvas
    def plotPoints(self, NUM_POINTS):
        # point list
        pointsList = []
        # establishes a main point
        P = Point(250, 250)

        # allows a random point to be displayed in the fractal
        for i in range(0, NUM_POINTS):
            pointsList.append(P.x)
            pointsList.append(P.y)
            J = randint(0,3)
            if J == 0:
                Px = P.x + (A.x - P.x) / 2
                Py = P.y + (A.y - P.y) / 2
                P = Point(Px, Py)
            if J == 1:
                Px = P.x + (B.x - P.x) / 2
                Py = P.y + (B.y - P.y) / 2
                P = Point(Px, Py)
            if J == 2:
                Px = P.x + (C.x - P.x) / 2
                Py = P.y + (C.y - P.y) / 2
                P = Point(Px, Py)

        # displays the points of the fractal
        for i in range(len(pointsList) - 1):
            if i % 2 == 0:
                self.plot(pointsList[i], pointsList[i + 1])

        # displays the vertices
        self.plotV(A.x, A.y)
        self.plotV(B.x, B.y)
        self.plotV(C.x, C.y)
    

    # Function that chooses the color for the border and the inside of each of the points
    def plot(self, x, y):
        POINT_COLORS = ["black"]
        POINT_RADIUS = 0
        color = POINT_COLORS
        self.create_oval(x, y, x + POINT_RADIUS * 2, y + POINT_RADIUS * 2, outline = color, fill = color)

    # Function that plots the vertecies
    def plotV(self, x, y):
        POINT_COLORS = ["red"]
        POINT_RADIUS = 3
        color = POINT_COLORS
        self.create_oval(x, y, x + POINT_RADIUS * 2, y + POINT_RADIUS * 2, outline = color, fill = color)

# main part of program
# creates the window
WIDTH = 600
HEIGHT = 520
# the number of points to plot
NUM_POINTS = 50000
# the vertecies
MAX_X = 593
MIN_X = 4
MAX_Y = 510
MIN_Y = 4
MID_X = int((MIN_X + MAX_X) / 2)
MID_Y = int((MIN_Y + MAX_Y) / 2)
Midpoint = Point(MID_X, MID_Y)
# creates the points
A = Point(MIN_X, MAX_Y)
B = Point(MID_X, MIN_Y)
C = Point(MAX_X, MAX_Y)
# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
#create the coordinate system as a Tkinter canvas insode the window
s = ChaosGame(window)
# plot the chaos game
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()


