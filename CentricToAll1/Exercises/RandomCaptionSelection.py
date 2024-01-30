#Write a program, where the captian of the team, will be selected randomly using the random choice()functions.

import random


Players_Enrollment=input("Enter the players names separated by comma:")
Players_list=Players_Enrollment.split(",")
Captain_selection=random.choice(Players_list)
print(f"{Captain_selection} will the captain of the team, for this tournament")