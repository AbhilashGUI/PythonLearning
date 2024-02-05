
#Nestedtupple

tuple1=(36,12,25,36,45,'Abhilash')
tuple2=(78,25,14,)
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[0])
print(tuple3[1])
print(len(tuple3))
tuple3=tuple1+tuple2   #Post contatenating the tuples it is merging as a single tupple
print(len(tuple3))

#Using some function in tuple
#print(min(tuple1))    #Note: It throws an error,since the tuple cotains both int and string data types
print(min(tuple2))
print(max(tuple2))
print(tuple1.index(36)) #Note: Though we have duplicate values it retrieves the firt occurence index


#Printing the element on the tuple multiple times
num=(10,)*10
print(num)
name=("Abhilash",)*3
print(name)

#Converting the list to tuple
List=[1,2,3,4,5]
print(tuple(List))
