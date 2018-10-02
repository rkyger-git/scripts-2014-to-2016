# file: projectilebounce.py
# A program that graphically depicts two bouncing balls.

from math import sin, cos, radians
from random import randrange
from graphics import *

class Projectile:

    def __init__(self,angle,velocity,height, distance):
        
        self.xpos = distance 
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

    #reset parameters at boundaries to make cballs bounce
    def flreset(self,xpos): 

        angle = randrange(181) #45 
        velocity = randrange(81) #80
        theta = radians(angle)
        self.yvel = velocity*sin(theta)
        self.xvel = velocity*cos(theta)
        self.ypos = 5
        self.xpos = xpos

    def clreset(self,xpos):

        angle = randrange(181,361) #190 
        velocity = randrange(81) #80
        theta = radians(angle)
        self.yvel = velocity*sin(theta)
        self.xvel = velocity*cos(theta)
        self.ypos = 395
        self.xpos = xpos

    def lwreset(self,ypos):

        randlist = [randrange(91),randrange(91),randrange(91),
                    randrange(270,361),randrange(270,361),randrange(270,361)]
    
        angle = randlist[randrange(6)] #45  
        velocity = randrange(81) #80
        theta = radians(angle)
        self.yvel = velocity*sin(theta)
        self.xvel = velocity*cos(theta)
        self.ypos = ypos
        self.xpos = 5

    def rwreset(self,ypos):

        angle = randrange(90,271) #100  
        velocity = randrange(81) #80
        theta = radians(angle)
        self.yvel = velocity*sin(theta)
        self.xvel = velocity*cos(theta)
        self.ypos = ypos
        self.xpos = 395

class Tracker:
    
    def __init__(self,win,objToTrack,circle):

        # make inputs part of the constructor
        self.win = win
        self.objToTrack = objToTrack
        self.circle = circle
        
    def update(self):

        # difference between new and old positions
        dx = self.objToTrack.getX() - self.circle.getCenter().getX()
        dy = self.objToTrack.getY() - self.circle.getCenter().getY()

        # move cball
        self.circle.move(dx,dy)
        
        self.circle.draw(self.win)
        self.circle.undraw()

def Inputs():
    
    ang = 45
    vel = 50
    hgt = 1
    dis = 1
    time = 0.01
    
    return ang, vel, hgt, dis, time

def main():

    win = GraphWin("Cannonball Tracker",400,400)
    win.setCoords(0.0,0.0,400,400)
    win.setBackground("white")
    
    angle, vel, h0, dis, time = Inputs()

    # make first cball
    cball = Projectile(angle,vel,h0,dis)
    
    center = Point(cball.getX(),cball.getY())
    circle = Circle(center,10)
    circle.setFill("red")

    tracker1 = Tracker(win,cball,circle)

    # make second cball
    cball2 = Projectile(angle,vel,h0,dis)
    
    center2 = Point(cball2.getX(),cball2.getY())
    circle2 = Circle(center2,10)
    circle2.setFill("blue")
    
    tracker2 = Tracker(win,cball2,circle2)
    
    # set boundary and position update paramters
    while True:

        if cball.getY() <= 0:
            cball.flreset(cball.getX())
            cball2.flreset(cball.getX())

        elif cball.getY() >= 400:
            cball.clreset(cball.getX())
            cball2.clreset(cball.getX())

        elif cball.getX() <= 0:
            cball.lwreset(cball.getY())
            cball2.lwreset(cball.getY())

        elif cball.getX() >= 400:
            cball.rwreset(cball.getY())
            cball2.lwreset(cball.getY())
                 
        else:
            cball.update(time)
            tracker1.update()
            cball2.update(time)
            tracker2.update()

main()
        
        
    
