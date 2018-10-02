# file: reverse.py
# A program that reverses elements in a list.

def reverse(numlist):

    revlist = []
    for i in numlist:
        revlist.insert(0,i)

    return revlist

def main():

    print("A program that takes an inputed list of numbers and prints")
    print("out the inputed list and the reversed form of the list.\n")

    print("Enter multiple numbers separated by spaces")
    numbers = input("with no quotation marks: ")

    # convert inputed string to list
    numlist = numbers.split()

    revlist = reverse(numlist)

    print("\nThe original list is:", numlist)
    print("\nThe reversed list is:", revlist)
    
main()

    
