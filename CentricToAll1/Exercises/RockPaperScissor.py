#Rock wins against scissor
#Scissor wins against paper
#Paper wins against rock

import random

User_Choice=int(input("Enter the user choice: Where 0 represents Rock, 1 represents paper and 2 represents scissor:"))
if User_Choice>=3 and User_Choice<0:
    print("It is an invalid input, exit from the game")
else:
    Computer_Choice=random.randint(0,2)
    print("Automatic Generator")
    print(Computer_Choice)
    if User_Choice == Computer_Choice:
        print("It's a draw")
    elif User_Choice==0 and Computer_Choice==2:
        print("You wins")
    elif User_Choice==2 and Computer_Choice==0:
        print("You loose")
    elif User_Choice > Computer_Choice:
        print("You wins")
    elif User_Choice < Computer_Choice:
        print("You loose")

