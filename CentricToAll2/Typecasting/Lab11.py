##Type casting or Type conversion

print(len("Abhilash"))
print(len('Abhilash vemula'))   ##Note: It counts space as well


print(len('8977507845'))
##print(len(8977507845))   ##It is an integer, which throws an type error. Only "STRINGLENGTH" can be invoked successfully


#length =8977507845
#print(len(length))       ##Cross check.

Name="Abhilash vemula"
print(len(Name))
Name=len("Abhilash")
print("Your name has" + " "+str(Name) + " "+  "characters" )   #Note:Length of the name is a int. So we are using the str() function to convert int to string
print(type(Name))                                               #Since, we are checking the type of variable (length), it suppose to show an int
Length =str(Name)
print(type(Length))                                            #Now, type of the variable is seen as string, since we are convert using str function
