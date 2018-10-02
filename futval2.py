# futval2.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program computes the future value")
    print("of a 10 year investment.\n")

    principal = eval(input("Enter the initial principal: "))

    apr = eval(input("Enter the annual interest rate (%): "))
    rate = apr/100 

    period = eval(input("Enter the compounding rate (period): "))

    futrval = principal*((1 + rate/period)**(period*10)) 

    print("\nThe value (in $) in 10 years is:", futrval)

main()
