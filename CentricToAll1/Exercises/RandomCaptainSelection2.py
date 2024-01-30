#Write a program, where the captian of the team, will be selected randomly without using the random choice()functions.


import random


Players_Enrollment=input("Enter the players names separated by comma:")
Players_list=Players_Enrollment.split(",")
#print(Players_list)

Names_Length=len(Players_list)
#print(Names_Length)
Captain_selection=random.randint(0,Names_Length-1)
print(f"{Players_list[Captain_selection]} will the captain of the team, for this tournament")