#pass statement: Is also known as the null statement.We can use the pass statement as a placeholder when unsure of the code to provide.

Count=1
while Count<=10:
    print(Count)
    Count+=1
    if Count==5:
       pass      #It does nothing, just a placeholder to replace the statment with some conditions/statments/random thing in a future
       print("Increment Number")
print("Out of the loop")


Count=10
while Count>=1:
    print(Count)
    Count-=1
    if Count==4:
        pass
        print("Decrement order")
print("Out of the loop")


def fun():    #Failing to provide pass, throws an indentation error
    pass