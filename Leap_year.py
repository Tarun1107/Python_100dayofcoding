#leap year
year = int(input(f"Enter a leap year: "))
if (year%4 == 0):
    if (year%100 == 0):
        if (year%400==0):
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not leap year")