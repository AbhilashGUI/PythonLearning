#Continue statement:  Is used to skip the remaining statements of the current loop and go to the next iteration.

Count=1
while Count<=10:
    print(Count)
    Count+=1
    if Count==5:
        continue
    print("Continue Number")   #It doesn't print the statment at the specified conditon
print("Out of the loop")


Count=10
while Count>=1:
    print(Count)
    Count-=1
    if Count==4:
        continue
        print("Decrement order")    #Note: This statment will not be executed, since it is with in the if condition
print("Out of the loop")
