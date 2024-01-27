Number = int(input("Enter the number:"))
if Number % 2 == 0:
    print("Given number is an even number")  # Note: If the condition one is true,it executes the second condition or third condition depends on the inputs provided
if Number < 50:
    print("Given number is less than 50")  # Note: If the condition one is false,it executes the second condition or third condition depends on the inputs provided
else:
    print("Given number is Greater than 50")