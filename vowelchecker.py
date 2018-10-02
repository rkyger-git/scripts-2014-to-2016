# file: vowelchecker.py
# A program that takes a character and
#returns True if it is a vowel, False otherwise.

def vowel_checker(char):

    if char == "a":
        return True

    elif char == "e":
        return True

    elif char == "i":
        return True

    elif char == "o":
        return True

    elif char == "u":
        return True
        
    elif char == "y":
        return True

    elif char == "A":
        return True

    elif char == "E":
        return True

    elif char == "I":
        return True

    elif char == "O":
        return True

    elif char == "U":
        return True

    elif char == "Y":
        return True

    else:
        return False   

def main():
    print("This program takes a inputed character and")
    print("returns True if it is a vowel, False otherwise.\n")

    print("Enter one character")
    char = input("with no quotation marks: ")
    
    output = vowel_checker(char)

    print("")
    print(output)
   
main()
          
