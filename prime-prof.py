import math

def isPrime(x):
    sqrtx = int(math.sqrt(x))
    for i in range(2, sqrtx + 1):
        if x % i == 0:
            return False
    return True

def main():
    n = int(input("Input a number (>=2): "))
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")

main()
