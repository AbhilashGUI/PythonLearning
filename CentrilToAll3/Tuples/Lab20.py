#Tupple: A comma-separated group of items is called a Python triple. These are denoted in the round brackets and  immutable in nature.

num_tuple=(21,25,45,78,664,12)
print(num_tuple)
print(num_tuple[0])    #Note:while fetching the index value in tupple will declare in square brackets
print(num_tuple[2])
#print(num_tuple[7])    #It throws a indexerror.
print(type(num_tuple))     #It displays as an tuple
num_tuple1=(12,)           #It displays as an tuple
print(type(num_tuple1))
num_tuple2=(12)            #Note: If it not a comma separated, then it displays the data type. It is common for all other data types
print(type(num_tuple2))


name_tuple=("Abhilash","Srikanth","Sirisha","Ankit")
print(name_tuple)
print(name_tuple[0])
print(name_tuple[-2])
print(type(num_tuple))     #It displays as an tuple
name_tuple2=("Vishal")
print(type(name_tuple2))


Combined_tuple=(58,45.25,"Mohan","Suji",True)
print(Combined_tuple)
print(type(Combined_tuple))        #It displays as an tuple


