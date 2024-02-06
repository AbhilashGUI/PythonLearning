#Indexerror:list index out of range
#It occurs basically when try to fetch the index which is not available in the list.

Names=["Abhilash","Amit","Amrith","Bunty","Dheeraj"]
#print(Names[5])   #It throws an error, since there is no index 5
print(Names[-5])  #It prints the first index. Since the negative index starts from backward
print(Names[-6])  #It throws an error, since there is no index -6
