#Write a program, where the payment of the bill will be selected randomly using the random choice() functions.
import random

Names_string=input("Enter the names separated by comma:")
Names_list=Names_string.split(",")
#print(Names_list)
Random_selection=random.choice(Names_list)
print(f"{Random_selection} will pay the bill,this time")