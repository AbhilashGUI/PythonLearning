#Percentage calculator


Percentage=float(input("Enter the Percentage :"))
if Percentage>=75:
    print(f"First class with distinction: {Percentage}")
elif Percentage>60 and Percentage<=69.99:
    print(f"First class: {Percentage}")
elif Percentage>50 and Percentage<=59.99:
    print(f"Second class: {Percentage}")
elif Percentage>=40 and Percentage<=49.99:
    print(f"Third class: {Percentage}")
elif Percentage>=35 and Percentage<=35:
    print(f"You are failed: {Percentage}")

else:
    print("Extra-ordinary")
print("End of the program")