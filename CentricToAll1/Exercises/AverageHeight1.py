#Calculate the average height from the list of heights

Heights=input("Enter the heights separated by space:")
Heights_List=Heights.split()
#print(Heights_List)
Count=0                #To find the length
for i in Heights_List:
    Count=Count+1
print(Count)
for i in range(0,Count): #range() function returns an immutable sequence of numbers starting from 0, increments by 1 and ends at a specified number.
    Heights_List[i]=int(Heights_List[i])    #To convert string to int based on indexes
print(Heights_List)
Total=0
for i in Heights_List:
    Total+=i                #Finding the average of heights/number of listed height elements/items
    print(Total)

Average=Total/Count
print(f"Average of heights :{round(Average)}") #Using round function to get the int value