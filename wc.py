# wc.py
# A program that counts the number of
# lines, words, and characters in a file

def main():

    print("This program shows the number of characters (without spaces),")
    print("words, and lines (with blanks) in a file.\n")

    fname = input("Enter filename: ")
    # The file has to be opened in binary mode to avoid
    # a counting error caused by automatic decoding (from DOS to UNIX).
    infile = open(fname, "rb")
    data = infile.read()

    lengthd = len(data)
    length = lengthd - data.count(b" ") 
    words = len(data.split())
    linec = data.count(b"\n")
    lines = linec + 1
    
    print("\nThe number of characters in this file:", length) 
    print("The number of words in this file:", words)
    print("The number of lines in this file:", lines)
    
    infile.close()

main()
