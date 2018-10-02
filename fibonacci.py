# File: fibonacci.py
# A program for finding the nth number in a Fibonacci sequence

def main():
        print("This program finds the nth number in a Fibonacci sequence")
        n = eval(input("Enter the nth number you want to find: "))
        x = (1 + (5**0.5)) / 2  
        y = 1 - x
        z = ((x**n) - (y**n)) / (5**0.5) 
        print(int(z))
main()
