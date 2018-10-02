def main():
    #s1="spam"
    #s2="ni!"
    #print(s2.upper().ljust(4)*3)
    n = eval(input("Enter a number: "))
    sumcubex = (n*(n+1)/2)**3
    for i in range(n):
        sumcubes = sumcubex + sumcubex
        print(sumcubes)
   
main()
