#set.difference() function returns the items that are unique to the specified set
set1={'Abhilash','Akash','Rohan','Manoj'}
set2={'Saikrishna','Kiran','Tarun','Manoj'}
print(set1.difference(set2))    #It excludes the common element and print set1
#Same operation can be performed
print(set1-set2)
print(set2.difference(set1))

#Passing the tuple
print(set1.difference(("Abhilash","Akash")))   #It excludes the available elements
print(set1.difference(("Srihansh","Surekha"))) #If no common elements found, it prints set1

#Multiple sets

set3={"Shashi","Sai","Anil","Sunil"}
set4={"Yeshwnath","Pavan","Kiran","Sai"}
set5={"Vinod","Anil","Arvind"}
print(set3.difference(set4,set5))     #Exclude the common elements in compare with other sets
#Same can be performed using
print(set3-set4-set5)

#set.difference() function returns the items that are unique to the original set by removing the common element permanently
set3.difference_update(set4)
print(set3)
set5.difference_update(set3)
print(set5)

#Cross check
print(set3)
print(set4)
print(set5)