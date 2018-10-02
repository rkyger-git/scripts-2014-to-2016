#file: sphere.py
# A program that creates a sphere as a class and outputs
# the sphere's inputed radius and its volume and surface area.

import math

class Sphere:

    def __init__(self, radius):
        self.radius = radius
        self.volume = (4/3)*(math.pi)*(radius**3)
        self.surfarea = 4*(math.pi)*(radius**2)

    def getradius(self):
        return self.radius

    def getsurfarea(self):
        return self.surfarea

    def getvolume(self):
        return self.volume

def getInput():
    radius = float(input("Enter the radius of the sphere: "))
    return radius

def main():

    print("This program creates a sphere as a class and outputs\n"
        "the sphere's inputed radius and its volume and surface area.\n")

    radius = getInput()
    
    sphere = Sphere(radius)

    print("\nThe inputed radius of the sphere is:", sphere.getradius())
    print("\nThe volume of the sphere is:", sphere.getvolume())
    print("\nThe surface area of the sphere is:", sphere.getsurfarea())
    

main()
    
                  
