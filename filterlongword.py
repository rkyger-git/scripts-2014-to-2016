# file: filterlongword.py
# A program that takes a file of words and an
# integer n and returns the list of words that are longer than n.

def filter_long_words(wordlist,n):

    # finds the positions (indices) of words in wordlist with a length
    # that is greater than n  
    indices = [i for i in range(len(wordlist)) if len(wordlist[i])>n]

    # finds the words in wordlist with the corresponding index 
    longwords = [wordlist[i] for i in indices]
    
    return longwords

def main():
    print("This program takes a file of words and an integer n")
    print("and returns the list of words that are longer than length n.\n")

    fname = input("Enter filename: ")
    
    infile = open(fname, "r") 

    # read imported file
    wordfile = infile.read()

    # split input at spaces into list
    wordlist = wordfile.split()
    
    n = int(input("Please input an integer length for n: "))

    longwords = filter_long_words(wordlist,n)

    print("\nThe words that are longer than length",n,"are:", longwords)

    infile.close
    
main()
