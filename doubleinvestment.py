# futval2.py
# A program that determines how long it takes for an
# investment to double at a given interest rate.

import math

def main():
    print("A program that determines how long it takes")
    print("for an investment to double.\n")

    # Note: the principal does not matter.
    initialprincipal = 100 #is used as a constant in while loop
    principal = 100 

    print("Note: the principal does not matter.")
    apr = eval(input("\nEnter the annual interest rate (%): "))

    rate = apr/100 

    time = 0
    while principal < 2*initialprincipal:
        principal = principal * (1 + rate)
        time = time + 1
    
    print("\nThe investment will double in",time,"years.")

main()
