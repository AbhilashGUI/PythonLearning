#Break statment:The break statement breaks the loops one by one

Count=1
while Count<=10:
    print(Count)
    Count+=1
    if Count==5:
        break
    print("Increment Number")
print("Out of the loop")


Count=10
while Count>=1:
    print(Count)
    Count-=1
    if Count==4:
        break
        print("Decrement order")    #Note: This statment will not be executed, since it is with in the if condition
print("Out of the loop")
