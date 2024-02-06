#Calculate the average height from the list of heights  using the length and sum function

Heights=input("Enter the heights separated by space:")
Height_list=Heights.split()
print(Height_list)
length=(len(Height_list))
#print(length)

#Covert string to int and using the range function
for i in range(0,length):           #range() function returns an immutable sequence of numbers starting from 0, increments by 1 and ends at a specified number.
    Height_list[i]=int(Height_list[i])
print(Height_list)

#Finding the average using sum fucntion
Sum=sum(Height_list)
print(Sum)
Average=Sum/length
print(Average)