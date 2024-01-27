#Grade Calculator


Percentage=float(input("Enter the Percentage :"))

if Percentage>=70:
    Grade='A'
    print(f"First class with distinction: {Percentage} and Grade: {Grade}")
elif Percentage>=60 and Percentage<=69.99:
    Grade='B'
    print(f"First class: {Percentage} and Grade: {Grade}")
elif Percentage>50 and Percentage<=59.99:
    Grade = 'C'
    print(f"Second class: {Percentage} and Grade: {Grade}")
elif Percentage>=40 and Percentage<=49.99:
    Grade = 'D'
    print(f"Third class: {Percentage} and Grade: {Grade}")
elif Percentage==35:
    Grade = 'E'
    print(f"You are Just Passed:{Percentage} and Grade: {Grade}")

else:
    print("You are Failed")
print("End of the program")