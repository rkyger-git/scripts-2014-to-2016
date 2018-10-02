# pi.py
# A program that apporximates the value of pi
# by summing n terms in a series
# and shows the difference between the approximated value of pi and
# the value of pi from the math library 

import math

def main():
    print("This program approximates the value of pi")
    print("using a series.\n")
    n = eval(input("Enter the n number of terms: "))
    p = 0
    for i in range(n):   
             p = p + (4/(2*i+1))*((-1)**i)

    print("\nThe approximated pi value:", p)
    print("\nThe absolute value of the difference\nbetween approximated pi and math.pi:", abs(p - math.pi))

main()
