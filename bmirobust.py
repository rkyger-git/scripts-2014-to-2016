# file: bmirobust.py
# A program that calculates a person's BMI and
# tells them whether or not they are in the
# healthy range of 19-25 for BMI.
# It also can handle name, value, syntax, and type errors.

def main():
    print("This program calculates a person's BMI and tells")
    print("them if they are in the healthy range of 19-25.\n")

    print("Enter your weight (in lbs)")
    print("and your height (in inches)")

    try:
        weight, height = eval(input("separated by a comma (no spaces): "))

        BMI = weight*720 / (height**2)

        if 19 <= BMI <= 25:
            print("\nYour BMI is:", BMI)
            print("This is within the healthy range.")

        elif BMI < 19:
            print("\nYour BMI is:", BMI)
            print("This is below the healthy range!")

        elif BMI > 25:
            print("\nYour BMI is:", BMI)
            print("This is above the healthy range!")

    except ValueError:
        print("\nYou inputed more than 2 inputs or your inputs were not numbers.")

    except SyntaxError:
        print("\nYour inputs were not in the correct form. Missing comma?")

    except TypeError:
        print("\nYou entered less than 2 inputs or your inputs were not numbers.")

    except NameError:
        print("\nYour inputs were not numbers.")
        
        
        
main()
    
    
