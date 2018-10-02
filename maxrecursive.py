# file: maxrecursive.py
# A program that uses a recursive function
# to find the largest value in a list.


def merge(lst1,lst2,lst3):

    i1,i2,i3 = 0,0,0

    n1,n2 = len(lst1),len(lst2)
    
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] =  lst1[i1]
            i1 = i1 + 1

        else:
            lst3[i3] = lst2[i2]
            i2 = i2 +1
        i3 = i3 + 1

    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1

    while i2 < n2:
        lst3[i3] < lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1
        
        
def mergeSort(list1):

    mergelist = list1
    
    n = len(mergelist)

    if n > 1:
        m = n // 2
        mergelist1, mergelist2 =  mergelist[:m],mergelist[m:]

        mergeSort(mergelist1)
        mergeSort(mergelist2)

        merge(mergelist1,mergelist2,mergelist)

    return mergelist[-1]


def main():
    
    print("This program uses a recursive function"
            "to find the largest value in a list.")
    
    print("\nEnter multiple characters separated")
    instr = input("by commas with no quotation marks or spaces: ")
    print("")

    inlist = instr.split(",")

    map1 = map(int, inlist)

    list1 = list(map1)
    
    maxnum = mergeSort(list1)


    print(">>>", maxnum ,"<<<")





if __name__ == '__main__':
    main()
