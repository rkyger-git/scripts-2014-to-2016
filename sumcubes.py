# file: sumcubes.py
# This program shows the sum of the first n natural numbers
# and the sum of cubes of the first natural numbers.

# returns the sum of the first n natural numbers
def sumN(n):
    sumN = n*(n+1)/2
    return sumN

# returns the sum of cubes of the first n natural numbers    
def sumNCubesN(n):
    sumNCubesN = (n*(n+1)/2)**2
    return sumNCubesN

def main():
    print("This program shows the sum of the first n natural numbers")
    print("and the sum of cubes of the first natural numbers.\n")

    n = eval(input("Enter the value for n: "))

    sumofn = int(sumN(n))
    sumofcube = int(sumNCubesN(n))

    print("\nThe sum of the first", n)
    print("natural numbers is:", sumofn)

    print("\nThe sum of cubes of the first", n)
    print("natural numbers is:", sumofcube) 

main()
