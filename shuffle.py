# file: shuffle.py
# A program that shuffles a list into a random order.

from random import randrange

def shuffle(myList):
    
    shuflist = []

    # for each item in myList select one of them at random
    # and insert it into a random location in shuflist
    for i in range(len(myList)):
        shuflist.insert(randrange(len(myList)), myList.pop(randrange(len(myList))))
        
    return shuflist      
        
def main():
    
    print("This program shuffles a list into a random order.")
 
    print("\nEnter multiple characters separated")
    myStr = input("by spaces with no quotation marks: ")
    
    myList = myStr.split()

    shuflist = shuffle(myList)
    
   # print("\nThe shuffled list is:", shuflist)
    

main()

