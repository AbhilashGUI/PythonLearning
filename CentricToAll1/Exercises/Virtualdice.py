import random

Dice=random.randrange(1,7)
print(Dice)
if Dice==1:
    print("Move 1 step forward")
elif Dice==2:
    print("Move 2 steps forward")
elif Dice==3:
    print("Move 3 steps forward")
elif Dice==4:
    print("Move 4 steps forward")
elif Dice==5:
    print("Move 5 steps forward")
else:
    print("Move 6 steps forward")