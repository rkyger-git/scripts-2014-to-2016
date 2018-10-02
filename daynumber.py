# daynumber.py
# A program that accepts a date as month/day/year,
# verifies that it is valid and then calulates
# the corresponding day number.

def leap(year):

    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True

            else:
                return False        
        else:
            return True
    else:
        return False


def main():

    print("This program accepts a date as month/day/year,"
            "verifies that it is valid and then calulates"
                "the corresponding day number.\n")

    inputstr = input("Please input a date (e.g. mm/dd/yyyy): ")
    print("")
    
    inputlist = inputstr.split("/")
    
    month = int(inputlist[0])
    day = int(inputlist[1])
    year = int(inputlist[2])

    if month not in range(1,12):

        print(">>> Invalid date <<<")

    elif (month == 1 or 3 or 5 or 7 or 8 or 10 or 12) and day > 31:

        print(">>> Invalid date <<<")

    elif (month == 4 or 6 or 9 or 11) and day > 30:
        
        print(">>> Invalid date <<<")

    elif month == 2 and day > 29:
        
         print(">>> Invalid date <<<") 

    elif (leap(year) == False) and month == 2 and day == 29:
        
        print(">>> Invalid date <<<")

    else:
    
        if (leap(year) == True) and month > 2:
            daynum = (31*(month-1) + day) - ((4*(month) + 23)//10) + 1

        elif month > 2:
            daynum = (31*(month-1) + day) - ((4*(month) + 23)//10)

        else:
            daynum = 31*(month-1) + day

        print(">>>",daynum, "<<<")



if __name__ == '__main__':
    main()
    
    

    
    
