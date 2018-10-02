# This problem defines a class Sphere
# One instance variable which is the radius
# Three methods: getRadius, surface_area and volume
# Minor changes to code by Megan Lancaster

import math
class Sphere:
    def __init__(self,radius):
        self.radius=radius
        
    def getRadius(self):
        return self.radius
    
    def surface_area(self):
        return(4*math.pi*self.radius**2)
    
    def volume(self):
        return((4/3)*math.pi*self.radius**3)
    
def main():
    
    radius=eval(input("Please enter radius:"))
    
    s=Sphere(radius)
    
    print("The surface area of the sphere is:", round(s.surface_area(),2))
    
    print("The volume of the sphere is:", round(s.volume(),2))
    
main()

