# file: rectangle.py
# A program that draws a rectangle based on inputs fromthe user
# and displays the perimeter and area of the rectangle.

from graphics import *

def main():
    win = GraphWin("Draw a Rectangle",400,400)
    win.setCoords(0.0,0.0,400,400)

    win.setBackground("white")
     
    # displays user instructions
    message = Text(Point(82,390), "Click on two points.")
    message.draw(win)

    # two mouse clicks for the opposite corners of a rectangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    # use Rectangle object to draw rectangle
    rect = Rectangle(p1,p2)
    rect.draw(win)

    # finds the base of the rectangle
    base = abs(p1.getX() - p2.getX())

    # finds the height of the rectangle
    height = abs(p1.getY() - p2.getY())
    
    # finds the perimeter of the rectangle
    perimeter = 2*base + 2*height

    # prints the perimter of the rectangle
    pstring = "Perimeter: " + str(perimeter)[0:8]
    pmessage = Text(Point(75,10), pstring)
    pmessage.draw(win)
  
    # finds the area of the rectangle
    area = base*height

    # prints the area of the rectangle
    astring = "Area: " + str(area)[0:10]
    amessage = Text(Point(230,10), astring)
    amessage.draw(win)

    # wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()

    win.close

main()
    
