# file: archery.py
# A program that draws an archery target.

from graphics import *

def main():
    win = GraphWin("Archery Target",400,400)

    #center of target 
    center = Point(200,200)
    
    #white circle
    wcirc = Circle(center,150)
    wcirc.setFill("white")
    wcirc.draw(win)

    #black circle
    bkcirc = Circle(center,120)
    bkcirc.setFill("black")
    bkcirc.draw(win)

    #blue circle
    blcirc = Circle(center,90)
    blcirc.setFill("blue")
    blcirc.draw(win)

    #red circle
    rcirc = Circle(center,60)
    rcirc.setFill("red")
    rcirc.draw(win)
    
    #yellow circle
    ycirc = Circle(center,30)
    ycirc.setFill("yellow")
    ycirc.draw(win)

    #center point
    p = Point(200,200)
    p.draw(win)

    win.close
    
main()
