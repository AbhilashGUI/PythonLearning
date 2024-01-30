#Write a program, where the payment of the bill will be selected randomly without using the random choice()functions.
import random

Names=input("Enter the names separated by comma:")
Names_list=Names.split(",")
#print(Names_list)

Length = len(Names_list)                                    #Note:If you are using randint() function, suppose to provide predefined range.
#print(Length)

Sponsor=random.randint(0,Length-1)                        #Note:Index starts from 0 to so on. Length starts from 1 to so on.

print(f"{Names_list[Sponsor]} will pay the bill")