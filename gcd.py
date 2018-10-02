# file: gcd.py
# A program that finds the GCD
# (greatest common divisor) of two integers.

def main():
    print("This program finds the GCD of two integers.\n")
    
    m, n = eval(input("Enter two integers separated by a comma (no spaces): "))     
    
   # use simultaneous assignment
   # stop loop when n = 0
   # when n = 0, m = gcd
    while n != 0:
         m, n = n, m%n

    print("\nThe GCD is:",m)
    
main()
