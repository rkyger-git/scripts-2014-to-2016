# file: longestrun.py
# A program that finds the length of
# the longest run in a list of numbers.

from itertools import groupby

def findlongestrun(inputlist):
     
    # for the second item i in the grouped version of inputlist
    # convert it to a list and find the length of that list
    # then use max to find the length of the the longest i
    # (which is the length of the longest run)
    longestrun = max(len(list(i)) for (_,i) in groupby(inputlist))

    return longestrun

def main():
    
    print("This program the finds the length of the "
          "longest run in a list of numbers.")
 
    print("\nEnter multiple numbers separated")
    inputstr = input("by spaces with no quotation marks: ")
    
    inputlist = inputstr.split()

    longestrun = findlongestrun(inputlist)
    
    print("")
    print(">>>", longestrun ,"<<<")



if __name__ == '__main__':
    main()
