#mergesort


def mergesort(mergelist):

    #mergelist = inlist
    
    n = len(mergelist)

    if n > 1:
        m = n // 2
        mergelist1, mergelist2 =  mergelist[:m], mergelist[m:]

        mergesort(mergelist1)
        mergesort(mergelist2)
        
        if len(mergelist1) == 1: # >
            if mergelist1 > mergelist2:
                mergelist1, mergelist2 = mergelist2, mergelist1
    
        mergelist = mergelist1 + mergelist2


    merge = 
    return mergelist




def main():
    
    print("This program uses a recursive function"
            "to find the largest value in a list.")
    
    print("\nEnter multiple characters separated")
    instr = input("by commas with no quotation marks or spaces: ")

    inlist = instr.split(",")

    map1 = map(int, inlist)

    mergelist = list(map1)

    #print(mergelist)
    
    mlist = mergesort(mergelist)


    print(">>>", mlist ,"<<<")





if __name__ == '__main__':
    main()
