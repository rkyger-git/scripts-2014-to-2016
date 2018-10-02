# diimenhanced.py
# A program that takes an IM message consisting of
# acronyms and converts them full text.



def main():

    print("This program takes an IM message consisting of"
            "acronyms and converts them full text.\n")

    infile = open("abbreviations.txt", "r")

    d = {}

    for line in infile:
        temp = line.split(":")
        d[temp[0]] = temp[1].rstrip()
    
    infile.close()

    im = input("Please input the IM: ")

    im = im.replace(".", " . ")
    im = im.replace(",", " , ")
    im = im.replace("?", " ? ")
    im = im.replace("!", " ! ")
    
    tim = ""
    templist = im.split()

    for i in templist:

        try:
            tim = tim + " " + d[i]

        except KeyError:
            tim = tim + " " + i
    
    tim = tim.replace(" .", ".")
    tim = tim.replace(" ,", ",")
    tim = tim.replace(" ?", "?")
    tim = tim.replace(" !", "!")

    print("")
    print(">>>", tim, "<<<")
    
    
if __name__ == '__main__':
    main()
