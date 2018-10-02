# file: randomwalk.py
# A program that models a drunkard walking randomly in 1 of 4
# directions for each street intersection starting at (0,0) for n times.

import random

def main():

    print("This program models a drunkard walking randomly in 1 of 4 "
            "directions for each street intersection starting at (0,0) for n times.\n")

    drunk10 = [0,0]
    
    list1 = [0,1,2,3]

    for i in range(10): 
        x = random.choice(list1)
    
        if x == 0:
            drunk10[0] = drunk10[0]+1
          
        elif x == 1:      
            drunk10[0] = drunk10[0]-1
          
        elif x == 2:
            drunk10[1] = drunk10[1]+1
          
        else:                   
            drunk10[1] = drunk10[1]-1
    

    drunk100 = [0,0]

    list2 = [0,1,2,3]

    for i in range(100): 
        y = random.choice(list2)
    
        if y == 0:
            drunk100[0] = drunk100[0]+1
          
        elif y == 1:      
            drunk100[0] = drunk100[0]-1
          
        elif y == 2:
            drunk100[1] = drunk100[1]+1
          
        else:                   
            drunk100[1] = drunk100[1]-1


    drunk1000 = [0,0]

    list3 = [0,1,2,3]

    for i in range(1000): 
        z = random.choice(list3)
    
        if z == 0:
            drunk1000[0] = drunk1000[0]+1
          
        elif z == 1:      
            drunk1000[0] = drunk1000[0]-1
          
        elif z == 2:
            drunk1000[1] = drunk1000[1]+1
          
        else:                   
            drunk1000[1] = drunk1000[1]-1


    print(">>>")
    print(drunk10[0],drunk10[1])
    print(drunk100[0],drunk100[1])
    print(drunk1000[0],drunk1000[1])
    print("<<<")
    



if __name__ == '__main__':
    main()
