# This program read a file which contains sales of different
# types of icecream in different stores and creates a report
# which organizes the sales of icreams in alphabetic order



def readfilecreatedictionary(filename):
    salesdata = {}
    infile = open(filename, "r")
    for line in  infile:
        temp = line.split(":")
        storesales=[]
        for i in range(1, len(temp)):
            storesales.append(float(temp[i]))
        salesdata[temp[0]] = storesales
    infile.close()
    return salesdata


def createreport(salesdata):

    # find the number of stores
    # maximum of the lenght of the value

    numstores = 0
    for storesales in salesdata.values():
        if len(storesales) > numstores:
            numstores = len(storesales)

    # Create a list of stores totals

    storetotals = [0.0]*numstores

    # print the falvor sales

    for flavor in sorted(salesdata):

        print("{0:<15}".format(flavor), end="")
        flavortotal = 0.0
        storesales = salesdata[flavor]
        for i in range(len(storesales)):
            sales = storesales[i]
            flavortotal = flavortotal + sales
            storetotals[i] = storetotals[i] + sales
            print("{0:<15.2f}".format(sales), end="")
        print("{0:<15.2f}".format(flavortotal))

    # print the store totals

    print()
    print("{0:<15}".format(""), end="")
    for i in range(numstores):
        print("{0:<15.2f}".format(storetotals[i]), end="")
    
    print()

def main():
    
    salesdata = readfilecreatedictionary("icecream.txt")
    createreport(salesdata)

main()
