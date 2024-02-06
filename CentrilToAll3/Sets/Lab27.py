#Symetric_diffference() function returns a mix of items in a set that are not present in both the sets

set1={"Abhilash","Praveen","Dheeraj","Monty"}
set2={"Bunty","Bagirath","Praveen"}
print(set1.symmetric_difference(set2))     #Excludes the common and returns the combined of two set element as a single set
#Same operation different method
print(set1^set2)

#Multiple sets
set3={"Abhilash","Praveen","Dheeraj","Monty"}
set4={"Bunty","Bagirath","Praveen"}
set5={"Dheeraj","Balu","Saikiran","Sohail"}
#print(set3.symmetric_difference(set4,set5))  #It doesn't accept the multiple arugumet. However it  can be operated as below
print(set3^set4^set5)


#symetric_update_difference() function returns  a mix of items in a set that are not present in both the sets by removing a common element permanently

set3.symmetric_difference_update(set4)
print(set3)
set5.symmetric_difference_update(set3)
print(set5)

#Cross-check
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)