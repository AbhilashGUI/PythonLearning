list=[7,14,21,["Seven","Fourteen","Twentyone"],28.8,35.5,42.2,49.9]
length=(len(list))
print(length)                 #Displays length of a list
Index=(length-1)              #Displays the indexes in a list
print(Index)


print(list[3])               #Displays the nested list
print(list[-5])              #Displays the nested list

print(len(list[3]))          #Displays the length of nest list

#Using the slicing concept
print(list[3][0:])        #Displays the nested list
print(list[3][0:2])       #Displays two elements from the nested list
print(list[3][0:2:2])     #Displays one elements from the nested list