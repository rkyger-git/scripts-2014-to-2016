# distance.py
# A program that detremines the distance to a lightning strike
# based on the time elapsed between the flash and the sound of the thunder.

def main():

    print("This program determines the distance to a")
    print("lightning strike.\n")
    print("Please input the time elapsed\nbetween the lightning flash") 

    time = eval(input("and the sound of thunder (in seconds): "))
    spdsnd = 1100/5280
    distancex = spdsnd * time
    distancey = str(distancex)
    distance = distancey[0:4]
    
    print("\nThe distance to the lightning strike (in miles):", distance)


main()
    
