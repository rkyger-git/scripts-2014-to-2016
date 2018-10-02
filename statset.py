# file: tatset.py
# A program that does statistics on housing data.


class StatSet:

    def __init__(self,inputlist):
        
        self.statset = inputlist

    def addNumbers(self,x):

        self.statset = (self.statset).append(x)
        
        return self.statset

    def mean(self):

        sum = 0.0

        for num in self.statset:
            sum = sum + num
            
        return sum/len(self.statset)

    def median(self):

        (self.statset).sort()
        size = len(self.statset)
        midPos = size//2

        if size%2 == 0:
            median = (self.statset[midPos] + self.statset[midPos-1]) / 2.0

        else:
            median = self.statset[midPos]

        return median

    def stdDev(self):

        sum = 0.0

        for num in self.statset:
            sum = sum + num
            
        xbar =  sum/len(self.statset)

        sumDevSq = 0.0

        for num in self.statset:
            dev = num - xbar
            sumDevSq = sumDevSq + dev*dev

        return (sumDevSq/len(self.statset)-1)**0.5


    def count(self):

        return len(self.statset)

    def min(self):

        return min(self.statset)

    def max(self):

        return max(self.statset)

def main():

    infile = open("housing-data-final.txt", "r")

    # use list comprehension to make list of lists from infile
    data = [line.split(" ") for line in infile]
     
    # remove white spaces from data
    data = [[j.rstrip() for j in i ] for i in data]

    # remove first list from data
    data.remove(data[0])

    # remove all spaces from lists in data
    data = [[j for j in i if j != ''] for i in data]
    
    # remove all \t from strings in data 
    data =  [[j.replace("\t","") for j in i] for i in data]

    #create lists of data for each region    
    usdata = []

    for i in data:
        usdata.append(int(i[1]))

    nedata = []

    for i in data:
        nedata.append(int(i[2]))

    mwdata = []

    for i in data:
        mwdata.append(int(i[3]))

    sdata = []

    for i in data:
        sdata.append(int(i[4]))

    wdata = []

    for i in data:
        wdata.append(int(i[5]))
    


    # create Statset object for each region
    usset = StatSet(usdata)
    neset = StatSet(nedata)
    mwset = StatSet(mwdata)
    sset = StatSet(sdata)
    wset = StatSet(wdata)

    # create list of statistics for each region
    usoutput = [usset.min(),usset.max(),usset.mean(),usset.median(),usset.stdDev()]
    neoutput = [neset.min(),neset.max(),neset.mean(),neset.median(),neset.stdDev()]
    mwoutput = [mwset.min(),mwset.max(),mwset.mean(),mwset.median(),mwset.stdDev()]
    soutput = [sset.min(),sset.max(),sset.mean(),sset.median(),sset.stdDev()]
    woutput = [wset.min(),wset.max(),wset.mean(),wset.median(),wset.stdDev()] 
    
    print(">>>")
    
    # title of table
    print("             Home Sales In U.S. (2013)\n")

    # rows of table
    print(" ".join(['          ', 'Min', '   Max', '   Mean', '  Median', 'StdDev']))

    print("US" + "         " + " ".join(["{0:0.2f}".format(i) for i in usoutput]))

    print("North-East" + "  " + "  ".join(["{0:0.2f}".format(i) for i in neoutput]))

    print("MidWest" + "     " + "  ".join(["{0:0.2f}".format(i) for i in mwoutput]))

    print("South" + "      " + " ".join(["{0:0.2f}".format(i) for i in soutput]))

    print("West" + "        " + " ".join(["{0:0.2f}".format(i) for i in woutput]))

    print("<<<")
    


if __name__ == '__main__':
    main()


    
        
