#In While-else, else block is executed if the while block is false


Count=1
while Count<=5:
    print(Count)
    Count += 1
else:
    print("Else is executed")
print("Out of the loop")


Count=5
while Count>=1:
    print(Count)
    Count-=1
else:
    print("Else block is executed")
print("Out of the loop")

#When forcefully breaking the while loop,else block will not be executed
Count=5
while Count>=1:
    print(Count)  #In this case, it prints only one item, which depends on the condition
    Count-=1
    if Count==4:
        break
else:
    print("Else block is executed")
print("Out of the loop")
