# file: flongestword.py
# A program that takes a list of words and
# returns the longest word and its length.

def find_longest_word(wordlist):
    
    # make list of lengths of inputed words
    numlist = [len(i) for i in wordlist] 
    
    #pair each length with each word
    ziplist = zip(numlist, wordlist)

    # create a dictionary with each pair    
    dict1 = dict(ziplist)

    # find longest word 
    longword = dict1[max(numlist)] 
    
    # find the longest length in the list   
    length = max(numlist)

    return longword, length

def main(): 
    print("This program takes an inputed list of words")
    print("and returns the longest word and its length.")

    print("\nEnter multiple words separated by spaces")
    words = input("with no quotation marks: ")

    # convert inputed string to list
    wordlist = words.split()
    
    longword, length = find_longest_word(wordlist) 
    
    print("\nThe longest word in this list is:", longword)
    print("\nThe length of this word is:", length)


main()
