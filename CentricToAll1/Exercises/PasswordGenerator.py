#Generating password
import  random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
         'a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

Special_Characters=['!','@','#','$','%','^','&','*']
print("Welcome to Password Generator!")
L_letters=int(input("How may letters would you like to have in password?\n"))
N_numbers=int(input("How may numbers would you like to have in password?\n"))
SC_characters=int(input("How may special characters would you like to have in password?\n"))
password=""
for i in range(1,L_letters+1):
    Char=random.choice(letters)
    password+=Char
#print(password)
for i in range(1,N_numbers+1):
    Char=random.choice(numbers)
    password+=Char
#print(password)
for i in range(1,SC_characters+1):
    Char=random.choice(Special_Characters)
    password+=Char
print(password)