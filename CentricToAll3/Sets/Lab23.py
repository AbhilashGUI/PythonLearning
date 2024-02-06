#Set: Is the collection of the unordered items. Each element in the set must be unique, immutable, and the sets remove the duplicate elements.
#Set is denoted in the flower braces

set1={10,24,36.4,12.7,True,"Abhilash",1,24,False,0}  #It omits the duplicate elements
print(set1)   #It prints the results in Unordered form.
#0 represents False and 1 represents True
#print(set1[1])   subscript and slicing is not allowed in set

print(len(set1))
set2=set()
print(type(set1))
print(type(set2))

#Manipulation of set
set1.add(63)
print(set1)
print(len(set1)) #+1
set1.remove(24)
print(set1)
set1.discard(10)
print(set1)
print(set1.pop())    #It removes random element from the set




#Adding the tuple in the set.Only tuple can be added in the set,because they are immutable
#set1.add((41,57,79))
#print(set1)
