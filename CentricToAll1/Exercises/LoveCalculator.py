#Love Calculator

Name1=input("Enter his name:")
Name2=input("Enter her name:")
Concatenate_names=(Name1+Name2)
Covert_to_lowercase=Concatenate_names.lower()

#Count fucntion(): count() method returns the number of times element appears in the list.
t=Covert_to_lowercase.count('t')
r=Covert_to_lowercase.count('r')
u=Covert_to_lowercase.count('u')
e=Covert_to_lowercase.count('e')

true=t+r+u+e

l=Covert_to_lowercase.count('l')
o=Covert_to_lowercase.count('o')
v=Covert_to_lowercase.count('v')
e=Covert_to_lowercase.count('e')

love=l+o+v+e

Love_score=int(str(true)+str(love))

if Love_score <10 or Love_score>90:
    print(f"Your love score is {Love_score}")

elif Love_score<40 and Love_score>50:
    print(f"Your love score is {Love_score}")

else:
    print(f"Your love score is {Love_score}")