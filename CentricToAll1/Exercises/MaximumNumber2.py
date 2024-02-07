#Write a program to find the maximum number from the list of numbers without using the length and max function

Numbers=input("Enter the numbers separated by comma:")
Number_list=Numbers.split(",")
#print(Number_list)

#Get the count of the inputs
Count=0
for numbers in Number_list:
    Count+=1
print(f"length of the list :{Count}")

 #Convert str to int
for i in range(0,Count):   #Passing the arguments
    Number_list[i]=int(Number_list[i])
print(Number_list)   #Converted to int in a list

#Finding the maximum number using standard method
Max_number=Number_list[0]      #Fetcing through indexes and comparing the 1st index with the next. That's how the finding the max number
for number in Number_list:
    if number>Max_number:
        Max_number=number
print(Max_number)