#Note: Union operation using set

set1={"Abhilash","Akash","Avinash","Adarsh","Aditya",}
set2={"Jaidev","Ajay","Vicky","Srikanth","Sachin","Aditya"}
print(set1.union(set2))     #Set2 is passing as an argument to Set1.
#Union function exclude the duplicates by comparing the defined sets

#Uniting the Mutiple sets
set3={"Abhilash","Akash","Avinash","Adarsh","Aditya",}
set4={"Jaidev","Ajay","Vicky","Srikanth","Sachin","Aditya"}
set5={"Ajay","Rakesh","Rajesh"}
print(set3.union(set4,set5))
#The Same operation can be performed using bitwise operator
print(set3 | set4 | set5 )

#Adding the tuple in the set
print(set5.union(("Aravind","Rohan","Ajay")))
#print(set5 | ("Aravind","Rohan","Ajay"))  It throws a type error

#Using the update function
set3.update(set4)         #Updating the set4 values in set3
print(set3)
#Adding the list to set
set3.update(["Abhilash","Uday","Santosh"])
print(set3)
set3 |= set5           #It works same as update function
print(set3)

