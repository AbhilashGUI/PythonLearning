#Write a program to find the maximum number from the list of numbers using the length and maxfunction


Numbers=input("Enter the numbers separated by space:")
Numbers_list=Numbers.split()  #Converted to list
print(Numbers_list)
length=len(Numbers_list)
print(length)                  #To find the length
#Using the range function whose arugments starts from 0 to so on
for i in range(0,length):
    Numbers_list[i]=int(Numbers_list[i])      #Coverting string to int
print(Numbers_list)
#Finding  the maximum number using the max function
Max_number=max(Numbers_list)
print(Max_number)

