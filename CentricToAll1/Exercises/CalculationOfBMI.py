#Calculate BMI#


#Formula:weight/height^2

weight=int(input("Enter the weight in kgs :"))
height=float(input("Enter the height in meters :"))
BMI=(weight)/((height**height))
print(BMI)



##Note:WEIGHT sholuld be int type and HEIGHT should be float type


Weight=input("Enter the Weight in KGS :")
Height=input("Enter the Height in Meters :")

BMI=int(Weight)/float(Height)**2
print(BMI)                  #Output is a float value.
print(int(BMI))            #Since, we declared as int type it will print int value.Hence,this concept is known as type conversion#

