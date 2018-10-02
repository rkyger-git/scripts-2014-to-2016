# file: ex.py
# A program that prints the first three characters,
# followed by three periods, and then the
# last three characters of an inputed word.
def main():
    print("This program prints the first three characters,")
    print("followed by three periods, and then the")
    print("last three characters of an inputed word.\n")

    word = input("Please enter a word of at least 6 characters: ")

    # slice first 3 letters
    first3 = word[0:3]

    # slice last 3 letters
    last3 = word[-3:]

    # create middle
    midl = "..."

    # add components together
    print("\nOutput:", first3 + midl + last3) 
    
main()
