Height=int(input("Enter the height:"))
if Height>=3:
    print("You can ride")                       #Note:Output is based on provided input.
    Age=int(input("Enter the age:"))
    if Age<12:
        print("Please pay 50rs")
    elif Age<15:
        print("Please pay 150rs")
    elif Age<18:
        print("Pleae pay 250rs")
    else:
        print("Please pay 500rs")

else:
    print("You can't ride")
print("End of the program")