# file: chill.py
# A program that displays different windchill values in a table.

# define windchill function
def windchill(V,T):
    chill = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    return chill 


def main():

    #list of air temperatures  
    Temp = list(range(-20,61,10))

    #list of wind velocity
    Vel = list(range(0,51,5))

    # nested list compreshension to get a list of lists of windchill values
    # for each temperature for each velocity 
    chilloutput = [[windchill(V,T) for T in Temp] for V in Vel]

    # title of table
    print("                               Windchill Table\n")

    # top row of table
    print(" ".join(['    ', '   -20degF', '-10degF', '0degF', '  10degF', ' 20degF', ' 30degF', ' 40degF', ' 50degF', ' 60degF']))

    
    # for each row, print the row lable plus the windchill values in chilloutput
    # formated to 2 decimal places that corresponds to each row
    for i in range(len(Vel)):
        print(str(Vel[i]) + " mph\t" + "\t".join(["{0:0.2f}".format(j) for j in chilloutput[i]]))
    
main()
