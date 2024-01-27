
#Understanding: The year which is divisible by 4. If it is divisible by 100 then it is mandate to divisible by 400. It is a leap year.

Year=int(input("Enter the Year:"))
if (Year%4==0 and Year%100!=0 or Year%400==0):
    print("It is a leap year")
else:
    print("Not a leap year")