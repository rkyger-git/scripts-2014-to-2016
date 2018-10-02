# file: tracker.py
# A program that graphically depicts the flight of a cannonball.

from math import sin, cos, radians
from graphics import *

class Projectile:

    def __init__(self,angle,velocity,height):
        
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)

    def update(self,time):
        
        self.xpos = self.xpos + time*self.xvel
        yvel1 = self.yvel - 9.8*time
        self.ypos = self.ypos + time*(self.yvel + yvel1)/2.0
        self.yvel = yvel1

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

class Tracker:
    
    def __init__(self,win,objToTrack):
        # make inputs part of the constructor
        self.win = win
        self.objToTrack = objToTrack
        
    def update(self):
        
        # use the methods of objToTrack (cball) to make a point
        center = Point(self.objToTrack.getX(),self.objToTrack.getY())
        
        # draw a circle using the point;
        # as the X and Y values of objToTrack (cball) change,
        # a circle will be drawn a each new point
        circle = Circle(center,5)
        circle.draw(self.win)
        

def getInputs():
    
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in m/s): ")) 
    h = eval(input("Enter the in initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))
    return a,v,h,t

def main():

    win = GraphWin("Cannonball Tracker",400,400)
    win.setCoords(0.0,0.0,400,400)
    win.setBackground("white")
    
    angle, vel, h0, time = getInputs()

    cball = Projectile(angle,vel,h0)

    # tracker has a graphwin and the object
    # that needs to be tracked (cball) as inputs
    tracker = Tracker(win,cball)
    
    while cball.getY() >= 0:
        cball.update(time)
        # draws objToTrack (cball) until
        # cball.getY() >= 0
        tracker.update()

        
    print("\nDistance traveled: {0:0.2} meters.".format(cball.getX()))

main()
        
        
    
