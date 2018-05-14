# file: overnight_yeast_cultures.py
# This program calculates the volume of yeast culture needed to make a
# yeast culture for an experiment the next day. 
# Originally written back in 2014 

def main():

    print("This program calculates the volume of yeast culture needed to make a yeast culture for an experiment the next day\n")
    print("NOTE: This program assumes all concentrations are times 10^7 cells/mL.")
    print("So, for a concentration of 5.4X10^7 cells/mL, you only need to input 5.4\n")

    growth_time = float(input("Enter the overnight growth time in hours (without lag time): "))
    current_conc = float(input("Enter the current yeast concentration: "))
    target_vol = float(input("Enter the target volume for your new culture in mL: "))
    target_conc = float(input("Enter the target concentration for your new culture: "))
    double_time = float(input("Enter the doubling time in minutes: "))
    
    num_double = (growth_time*60)/double_time
    density = (2**num_double)*current_conc
    conc_over_density = (target_conc*current_conc)/density
    dilution_factor = conc_over_density/current_conc
    volume = (dilution_factor*target_vol)*1000

    print("\nThe volume you need for your overnight culture is:", volume, "μL")
    



if __name__ == '__main__':
    main()
