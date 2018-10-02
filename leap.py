# file: leap.py
# A program that can determine if a year is a leap year.

def main():
    print("This program determines if a year is a leap year.\n")

    year = eval(input("Enter a year: "))
    
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("\nThis year is leap year.")

            else:
                print("\nThis year is not a leap year.")        
        else:
            print("\nThis year is leap year.")
    else:
        print("\nThis year is not a leap year.")
                        
main()
    
    
