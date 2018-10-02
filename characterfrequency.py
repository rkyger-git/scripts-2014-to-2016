# file: charfreq.py
# A program that analyzes character frequency in a file
# prints a report on the n most frequent words.


def byFreq(pair):
    return pair[1]


def main():

    print("This program analyzes character frequency in a file.\n")

    fname = input("File to analyze: ")
    text = open(fname,"r").read()

    
    # get rid of punctutation
    for ch in '!"#$%&()*+,-./:;<=>?@[\]^_{\}`~':
        text = text.replace(ch, ' ')

    words = text.split()

    list1 = []

    #create list of lists for each line
    for i in words:
        list1.append(list(i))

    # create list of characters
    charlist = []
    
    for lists in list1:
        for ch in lists:
            charlist.append(ch)

    # create dictionary of word counts
    counts = {}
    
    for ch in charlist:
        counts[ch] = counts.get(ch,0) + 1    


    n = int(input("Output analysis of how many words?: "))
    print("")

    # sort items 
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse = True)

    print(">>>")
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))
    print("<<<")


if __name__ == '__main__':
    main()
    

    
