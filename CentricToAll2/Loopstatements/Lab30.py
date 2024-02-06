#Using Numbers

#Mobile_number=8977507845
#for i in Mobile_number:             #Note: It throws an error saying int object is not iterable
#    print(i)


Mobile_number=[8977507845]
for i in Mobile_number:             #Note: It prints a single line statement,because it is not separated by comma(,)
    print(i)

Mobile_number = [8,9,7,7,5,0,7,8,4,5]
for i in Mobile_number:                # Note: It prints each number.
     print(i)


numbers=[11,12,13,14,15,16,17,18,19,20]
Listing=[]                             #Define the empty list, so that the values can be stored in a list
for num in numbers:
    square=num**2
    Listing.append(square)
    print(Listing)                     #In this case it prints one number in every iteration,because the identation is with in the forloop
print(f"The square of the listed numbers are : {Listing}")

