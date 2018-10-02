# file: bmi.py
# A program that calculates a person's BMI and
# tells them whether or not they are in the
# healthy range of 19-25 for BMI.

def main():
    print("This program calculates a person's BMI and tells")
    print("them if they are in the healthy range of 19-25.\n")

    print("Enter your weight (in lbs)")
    print("and your height (in inches)")
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
        
main()
    
    
    
