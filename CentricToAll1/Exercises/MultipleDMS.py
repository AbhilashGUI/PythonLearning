#Riding of roller coaster

Height=int(input("Please enter the height in feets:"))
Bill=0
if Height>=3:                                             #Note: If the first condition is false, It terminates the program and displays the desired output
    print("You can ride")
    Age=int(input("Enter the age:"))
    if Age<12:
        Bill=50
        print("Ticket price is 50rs")
    elif Age<18:
        Bill=150
        print("Ticket price is 150rs")
    elif Age<21:
        Bill=250
        print("Ticket price is 250rs")
    elif Age<30:
        Bill=500
        print("Ticket price is 500")
    else:
        print("Ticket price is 750rs")

    Add_Photograph=input("Would you like to have photograpph (Y/N):")
    if Add_Photograph=='Y':
        Bill=Bill+50
        print(f"Your total bill is {Bill}")

else:
    print("You can't ride")
print("End of the program")