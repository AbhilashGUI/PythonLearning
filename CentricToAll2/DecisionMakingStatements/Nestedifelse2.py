
#Riding of roller coaster

Height=int(input("Please enter the height in feets:"))

if Height>=3:                                             #Note: If the first condition is false, It terminates the program and displays the desired output
    print("You can ride")
    Age=int(input("Enter the age:"))
    if Age<12:
        print("Please pay  50rs")
    else:
        print("Please Pay 150rs")
else:
    print("You can't ride")
print("End of the program")