Weight=int(input("Enter the weight in kgs:"))
Height=float(input("Enter the height in meters:"))
BMI=Weight/Height**2    #Note: To roundoff to BMI,use round() function.
if BMI<16:
    print(f"Your BMI is {BMI}, which represents underweight")
elif BMI<24.9:
    print(f"Your BMI is {BMI},which represents normal range")
elif BMI<29.9:
    print(f"Your BMI is {BMI}, which represents over weight")
elif BMI<39.9:
    print(f"Your BMI is {BMI}, which represents obese")
else:
    print(f"Your BMI is {BMI}, which represents to be unhealthy")
