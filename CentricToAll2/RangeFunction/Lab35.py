#range() function returns an immutable sequence of numbers starting from 0, increments by 1 and ends at a specified number.


numbers=range(0,4)
print(numbers[0])   #We can only fetch the first index using range(), because it increment by one in every iteration

#Using for loop
for num in range(0,14):
    print(num)    #It prints from 0 to 13


for numerous in range(0,15,3):  #argements represents start,stop and step size(Skip)
    print(numerous)

for des in range(-10,-1,1):
    print(des)


for desstep in range(-10,-1,2):
    print(desstep)


