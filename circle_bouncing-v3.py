#Description: 
#
#            The function of this program is to animate a circle bouncing around a window.
#
#
#      Author: Yu Liu
#      Date: 2/26/2014

from graphics import *
from random import randrange

def circle_generate(ws,win):
    radius = ws/20
    initial_center = Point(ws/2,ws/2)
    Bcircle = Circle(initial_center,radius)
    Bcircle.setFill("red")
    Bcircle.draw(win)
    return Bcircle

def moving(winsize,steps,BC):
    radius = winsize/20
   
    x = winsize/2
    y = winsize/2
    while(steps >= 0):
        xrand = randrange(-(winsize/2-radius),(winsize/2-radius))
        yrand = randrange(-(winsize/2-radius),(winsize/2-radius))
        
        
        while((x+xrand)< radius or (x+xrand) >(winsize-radius) or (y+yrand) < radius or (y+yrand) >(winsize-radius)):
            xrand = randrange(-(winsize/2-radius),(winsize/2-radius))
            yrand = randrange(-(winsize/2-radius),(winsize/2-radius))

        BC.move(xrand,yrand)
        time.sleep(0.5)
                       
        x = x + xrand
        y = y + yrand        
        steps = steps -1
    
def main():
    winsize = eval(input("please set the size for the graphic window: "))
    move_steps = eval(input("enter the number of moving steps: "))
    
    win = GraphWin("Bouncing Circle",winsize,winsize)
    win.setCoords(0,0,winsize,winsize)
    
    BC = circle_generate(winsize, win)
    moving(winsize, move_steps, BC)
       
    print("click on graphic window to exit!")
    win.getMouse()
    win.close()
main()
