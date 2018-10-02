# file: cipher
# A program that encodes a Caesar cipher.

import string

def main():
    print("This program encodes a Caesar cipher.\n")
    print("Please input the string you want to encode")

    str1 = input("that contains only letters and spaces: ")
    key = eval(input("\nPlease input the value of the key: "))
    
    str1low = str1.lower()

    # convert string to list
    list1 = str1low.split()

    # list comprehension to convert string into a
    # list of lists (e.g. ['monty', 'python'] to
    # [['m', 'o', 'n', 't', 'y'], ['p', 'y', 't', 'h', 'o', 'n']]
    list2 = [list(i) for i in list1]
    
    # create a list of all letters in the alphabet 
    alphabet = list(string.ascii_lowercase)
    
    # create a list of numbers 0-25
    alphaval = list(range(0,26))

    # pair each letter with each number
    zip1 = zip(alphabet,alphaval)

    # create a dictionary with each pair 
    dict1 = dict(zip1)

    # turn characters in lists into numbers + key
    # using dict1 (dictionary)
    list3 = [[(dict1[i]+key)%26 for i in j] for j in list2]

    # convert numbers in lists back into characters
    # using alphabet list
    list4 = [[alphabet[i] for i in j] for j in list3]

    # convert lists inside the main list into strings
    list5 = ["".join(j)for j in list4]

    # convert the main list into a string
    #(with spaces if there were any originally)
    list6 = " ".join(list5)
    
    
    print("\nThe encoded string is:", list6) 
    

main()
