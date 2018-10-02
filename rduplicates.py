# file: rduplicates.py
# A program that removes duplicate values form a list.


def removeDuplicates(inlist):
    
    noduplist = []

    for i in inlist:
        if i not in noduplist:
            noduplist.append(i)
         
    return noduplist


def main():

    print("This program removes duplicate values form a list.")
    
 
    print("\nEnter multiple characters separated")
    instr = input("by spaces with no quotation marks: ")

    inlist = instr.split()

    noduplist = removeDuplicates(inlist)

    print("")
    print(">>>", noduplist ,"<<<")


    
    
    
if __name__ == '__main__':
    main()
