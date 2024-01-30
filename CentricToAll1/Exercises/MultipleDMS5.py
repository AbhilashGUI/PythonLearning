#Menu for Breakfast#


Breakfast=input("Enter the items :")
Bill=0
if Breakfast=='Idly':
    Bill+=30
    print("Please pay 30rs")
elif Breakfast=='Wada':
    Bill+=45
    print("Please pay 45rs")
elif Breakfast=='Dosa':
    Bill+=50
    print("Please pay 50rs")
elif Breakfast=='Puri':
    Bill+=55
    print("Please pay 55rs")
else:
    Bill+=10
    print("Kitchen is closed")

Add_sabzi=input("Would you like to add sabzi(Y/N):")
if Add_sabzi=='Y':
  if Breakfast=='Puri':
    Bill+=5
else:
    Bill+=15

Add_waterbottle=input("Would you like to add waterbottle(Y/N):")
if Add_waterbottle=='Y':
    Bill+=20

print(f"Final bill is : {Bill}")