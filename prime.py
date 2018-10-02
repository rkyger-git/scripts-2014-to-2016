#file: prime.py
# A program that determines if an integer n is prime.

def main():

    print("This program determines if an inputed integer is prime.\n")

    n = int(input("Enter a positive integer that is greater than 2: ",))
    print("")
    
    numlist = list(range(2,(int(n**0.5)+1)))
 
    for i in numlist:
        if n%i == 0:
            print("Output:",n, "is not a prime number.")
            break

    print("\nNote: If there is no output, the inputed number is prime.")


main()
