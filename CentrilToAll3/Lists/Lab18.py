#Nestedlist: List within a list is known as nested list.



list=[12,24,36,48,[60,72,84,96],108,110]   #Note:Nested list is considered as a single unit
print(len(list))                        #Fetching the length of the list
print(len(list[4]))                    #Fetching the length of the nested list
print(list[4][0])
print(list[4][1])
print(list[4][2])
print(list[4][3])


print(len(list[-3]))                  #Fetching the length of the nested list
print(list[-3])                       #Fetching the elements in the nested list

#Using the slicing/subscript concept for nested list
print(list[-3][0:2])                  #Displays 2 elements from the nested list
print(list[4][0:2:2])                 #Displays only element from the nested list

print(len(list)-2)                    #It removes 2 elements in a list
print(len(list))


