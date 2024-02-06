#Note: Intersection operation using set

set1={"Abhilash","Akash","Avinash","Adarsh","Aditya",}
set2={"Jaidev","Ajay","Vicky","Srikanth","Sachin","Aditya"}
print(set1.intersection(set2))     #It prints the common among them
#Same operation can be done using the bitwise &
print(set1 & set2)


set1={"Abhilash","Akash","Avinash","Adarsh","Aditya",}
set2={"Jaidev","Ajay","Vicky","Srikanth","Sachin","Aditya"}
set3={"Akash","Avinash","Adarsh","Ajay","Vicky","Srikanth"}
print(set1.intersection(set2,set3))   #Set2 prints the common element, set3 returns empty, since there is nothing common
#Same operation can be done using the bitwise &
print(set1 & set2 & set3)

#Using the update function
set2.intersection_update(set1)
print(set1)
print(set2)    #It prints the common element

#Updating the list to set
set1.intersection_update(["Raghu","Rajinikanth","Abhilash"])
print(set1)   #It prints the common element

