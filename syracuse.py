import string
def syrc(x):
    print(x)
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            print(x)
        else:
            x = 3*x + 1
            print(x)
def main():
    n = eval(input("Please enter a natural number   "))
    syrc(n)
main()
    
