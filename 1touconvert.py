# file: 1touconvert
# A program that changes all the letters in a text file
# into upper case and adds upper to the file name.
# It also shows the number of lines and the average number of words per line.

def main():
    print("This program adds upper to the file name")
    print("and converts all letters in the file into uppercase.")
    print("It also shows the number of lines and\nthe average number of words per line.\n")
    
    fname = input("Enter filename: ")
    # The file has to be opened in binary mode to avoid
    # a counting error caused by automatic decoding (from DOS to UNIX).
    infile = open(fname, "rb")

    # read imported file
    data = infile.read()

    # convert characters in file to uppercase
    upper = data.upper()

    # make output file name
    outfilename = fname.replace(".txt","upper.txt")

    # open output file
    outfile = open(outfilename, "wb") 

    # write information to file
    outfile.write(upper)
    
    print("\nThe text in the file has been converted to upper case.")
    print("The file is now called:", outfilename)   

    outfile.close()
    
    # number of lines 
    linec = data.count(b"\n")
    lines = linec + 1

    # avg number words per line
    words = len(data.split())
    avnwrdpln = words/lines

    print("\nThe number of lines in this file:", lines)
    print("The average number of words per line:", avnwrdpln)

    infile.close()
     
    
main()
