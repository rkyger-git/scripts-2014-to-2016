
def recmax(mylist):
    
    if len(mylist) == 1:
        return mylist[0]

    else:  
        maxother = recmax(mylist[1:])

        if mylist[0] > maxother:    
            return mylist[0]

        else:
            return maxother

def main():
    mylist = list(eval(input("Enter a list: ")))
    print(">>>", recmax(mylist), "<<<", sep="")

main()
