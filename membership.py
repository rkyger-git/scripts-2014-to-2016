# file: membership.py
# A program that tells a user if a character is in the list they inputed
# by returning True or False. 

def isin(myList,x):

    try:
        if myList.index(x) == myList.index(x):
            return True

    except ValueError:
        return False

def main():

    print("This program that tells a user if a character")
    print("is in the list they inputed by returning True or False.")

    print("\nEnter multiple characters separated")
    myStr = input("by spaces with no quotation marks: ")
    
    print("\nEnter a character that you want to")
    x = input("verify is in the list you inputed: ")

    myList = myStr.split()

    output = isin(myList,x)

    print('')
    print(output)

main()
