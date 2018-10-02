# intersection.py
# A program that takes in two lists and returns a list of unique items
# that are common to both the lists.


def commonItems(inlist1,inlist2):
    
    comnoduplist = []

    for i in inlist1:
        if i not in comnoduplist and i in inlist2:
            comnoduplist.append(i)
         
    return comnoduplist




def main():

    print("This program  takes in two lists and returns a list of unique items"
             "that are common to both lists.")
    
    print("\nFor list1, enter multiple characters separated")
    instr1 = input("by commas with no quotation marks or spaces: ")

    inlist1 = instr1.split(",")

    print("\nFor list2, enter multiple characters separated")
    instr2 = input("by commas with no quotation marks or spaces: ")

    inlist2 = instr2.split(",")
    
    comnoduplist = commonItems(inlist1,inlist2)

    print("")
    print(">>>", comnoduplist ,"<<<")


    
    
    
if __name__ == '__main__':
    main()
  
