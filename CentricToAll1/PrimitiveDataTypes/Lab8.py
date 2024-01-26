
#Declare the string variable and then check the type#

variable_3="Abhilash Vemula"       #Note: The index of the character starts from 0
print(type(variable_3))
print(variable_3[8])                #It prints space, since we have a space in b/w the declared string
variable_4="8977507845"
print(type(variable_4))


#Taking the input from the user
variable_5=input("Enter the mobile number:")
print("Primary No: "+variable_5 + " and " + "Secondary No: "+variable_4)


#Checking the concatenation for string and int
variable_6=512
#print(variable_6 + variable_5 )          ##It throws error, since string cannot concatenate with int
print(variable_3 + " "+ variable_4 )
