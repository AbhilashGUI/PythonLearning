#List:A collection of different kind of values and items. These are mutable in nature. It is also known as Dynami array.

Numbers=[1,26,47,89,458,7852,369874]                             #It contians only integervalues
Names=["Abhilash","Amit","Dharamveer","Sandeep"]     #It contains only string values
Multi_type=[1,"Sainath",12.37]                        #It contains int,float and string values
#print(Numbers)
#print(Names)
#print(Multi_type)

#print(len(Numbers))
#print(len(Names))
#print(len(Multi_type))


'''print(Numbers[3])    #Prints the value of index 3
print(Numbers[-2])   #Negative index starts from backward, whose index starts from -1. Prints the value of index -2

#This concept is known as Slicing
print(Numbers[1:4])  #Left declartion is an index and right declaration is a length(Results as length-1)
print((Numbers[1:])) #Declaring only the index prints, from index 1 to so on.
print(Numbers[:5])   #Declaring only the length, prints from index 0 to so on.

#Extending slicing skips the first element and prints the next element
print(Numbers[0:5:2])
print(Numbers[0:7:3])'''

Numbers.sort()               #sort() function is used to print the numbers in the default order
print(Numbers)
Numbers.reverse()            #reverse() function is used to print the numbers in reverse order
print(Numbers)


Numbers.append(6897455)      #append() is used to append the declared number in the list
print(Numbers)
Numbers.insert(3,274)   #insert() function is used to insert the number in the declared index
print(Numbers)


Numbers.extend([23,56,74,108])       #extend() function is used to append multiple data elements in a list
print(Numbers)

#Replacing the specific index value with the a new one
Numbers [1]=852
print(Numbers)

#Replacing the specific index value with the a new one's till the declared length
Numbers [1:3]=[712,456,985]
print(Numbers)

Numbers [0]=108              #Replacing the index value 0 with 108
print(Numbers)


Numbers.remove(108)           #remove() function is used to remove the first occurence of number in a list
print(Numbers)



Numbers.pop()                 #pop() fucntion removes the last value in the list bydefault
print(Numbers)


print(Numbers.pop())          #It prints the specific function, which is removed from the list