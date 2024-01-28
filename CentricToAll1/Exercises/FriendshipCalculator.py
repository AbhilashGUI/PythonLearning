Name1=input("Enter your name:")
Name2=input("Enter your friend-name:")
Concatenate_names=Name1+Name2
Convert_names_tolowercase=Concatenate_names.lower()

t=Convert_names_tolowercase.count('t')
r=Convert_names_tolowercase.count('r')
u=Convert_names_tolowercase.count('u')
e=Convert_names_tolowercase.count('e')

true=t+r+u+e

f=Convert_names_tolowercase.count('f')
r=Convert_names_tolowercase.count('r')
i=Convert_names_tolowercase.count('i')
e=Convert_names_tolowercase.count('e')
n=Convert_names_tolowercase.count('n')
d=Convert_names_tolowercase.count('d')
s=Convert_names_tolowercase.count('s')
h=Convert_names_tolowercase.count('h')
i=Convert_names_tolowercase.count('i')
p=Convert_names_tolowercase.count('p')

friendship=f+r+i+e+n+d+s+h+i+p

Friendship_score=int(str(true)+str(friendship))

if Friendship_score<10 or Friendship_score>90:
    print(f"You Friendship score is {Friendship_score}")
elif Friendship_score<40 and Friendship_score>50:
    print(f"Your Friendship score is {Friendship_score}")
else:
    print(f"You Friendship score is {Friendship_score}")