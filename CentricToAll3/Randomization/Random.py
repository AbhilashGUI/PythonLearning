#The Python Random module is a built-in module for generating random integers in Python.
# These numbers occur randomly and does not follow any rules or instructions.
# We can therefore use this module to generate random numbers, display a random item for a list or string, and so on.


import random

a=random.randint(1,8)          #The random.randint() function generates a random integer from the range of numbers supplied.
print(a)


b=random.randrange(1,8)   #The random.randrange() function selects an item randomly from the given range defined by the start and the stop.
print(b)                             #Note: In randrange() function, it exclude the declared stop range.

c=random.random()                   #The random.random() function gives a float number that ranges from 0.0 to 1.0.There are no parameters required for this function.
print(c)


d=random.uniform(1,8)         #The random.uniform() function gives a float number of the specified range
print(d)

list=[45,6,75,89,78,64,26]          #The random.choice() function selects an item from the list
e=random.choice(list)
print(e)

random.shuffle(list)                #The random.shuffle() function shuffles the given list randomly.
print(list)
