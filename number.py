# file: number.py
# This program calculates the numerical value of a single name.

import string

def main():
    print("This program calculates the numeric values of a single name.\n")

    name = input("Enter the name: ")
    namelow = name.lower() 

    # convert the lowercase name (string) into a list
    list1 = list(namelow)
    
    # create a list of all letters in the alphabet 
    alphabet = list(string.ascii_lowercase)
    
    # create a list of numbers 1-26
    alphaval = list(range(1,27))

    # pair each letter with each number
    zip1 = zip(alphabet,alphaval)

    # create a dictionary with each pair 
    dict1 = dict(zip1)

    # for each letter in list1 covert it to its corresponding
    # numerical value using dict1 (dictionary)
    # and then find the sum of those values
    sum1 = 0
    for i in list1:
        sum1 = sum1 + dict1[i] 

    print("\nThe numerical value of the name is:", sum1)
     
main()
