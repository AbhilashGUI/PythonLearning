#Forelse Using integers

Numbers=(12,15,18,21,24)
for num in Numbers:
    if num%3==0:
        print(num)

else:
    print("Numbers  are the multiples of 3")



#Other case

Numbers1 = (21, 35, 49, 21, 56)
for num1 in Numbers1:
    if num1 % 7 != 0:
        break

else:
    print("Numbers  are the multiples of 7")

