#While-else examples

number=int(input("Enter a number(-1 to quit)"))
while number !=1:
    print(number)
    number = int(input("Enter a number(-1 to quit)"))
else:
    print("Else block is executed")
print("Out of the loop")


Count=1
while True:
    print(Count)
    Count+=1
    if Count==5:
        break
else:
    print("Else block is executed")
print("Out from the loop")


