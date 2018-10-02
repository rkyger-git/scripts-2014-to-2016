# file: regression.py
# A program that graphically plots a regression line
# based on points graphically inputed by the user.

from graphics import *

def main():

    win = GraphWin("Linear Regression",400,400)
    win.setCoords(0.0,0.0,400,400)

    win.setBackground("white")

    # displays user instructions
    message1 = Text(Point(140,380), "Click on any number of points.\n Then click 'DONE' when you are done.")
    message1.draw(win)
   
    # DONE button 
    done = Text(Point(25,20), "DONE")
    done.draw(win)

    rp1 = Point(0,0)
    rp2 = Point(50,40)
    rect = Rectangle(rp1,rp2)
    rect.draw(win)

    # get list of graphically inputed points from user and
    # stop getting points if user clicks inside DONE button
    plist = []
    
    while True:
        p = win.getMouse()

        if (0<=p.getX()<=100 and 0<=p.getY()<=100) == False:
            p.draw(win)
            plist.append(p)

        else:
            break

    # get number of points
    n = len(plist)    
    
    # get averages
    xsum = 0
    ysum = 0
    for i in plist: 
       xsum = xsum + i.getX()
       ysum = ysum + i.getY()

    xavg = xsum/n
    yavg = ysum/n

    # get value of numerator for m function
    m1 = 0
    for i in plist:
        m1 = m1 + (i.getX()*i.getY() - n*xavg*yavg)

    # get value denominator of m function
    m2 = 0 
    for i in plist:
        m2 = m2 + ((i.getX()**2) - n*(xavg**2))

    # get value of m
    m = m1/m2

    # find endpoints of regression line
    y1 = yavg + m*(0 - xavg)
    y2 = yavg + m*(400 - xavg)

    p1 = Point(0,y1)
    p2 = Point(400,y2)

    # draw regression line
    regline = Line(p1,p2)
    regline.draw(win)   

    # wait for another click to exit
    message1.setText("Click anywhere to quit.")
    win.getMouse()

    win.close
    
main()
