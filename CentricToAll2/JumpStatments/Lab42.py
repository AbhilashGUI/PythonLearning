#Break statement examples using nested for loops

List1=["Hi",'Hello',"Welcome"]
List2=["Abhilash","Rahul","Vimal"]
for Greet in List1:
    for Dealer in List2:
        print(Greet,Dealer)
        if Greet=="Welcome" and Dealer=="Abhilash":
            break
            print("Innerloop")             #It never prints
    print("outerloop")
print("Out of the loop")

print("\n")
List1=["Hi",'Hello',"Welcome"]
List2=["Abhilash","Rahul","Vimal"]
for Greet in List1:
    for Dealer in List2:
        print(Greet,Dealer)
        if Greet=="Hello" and Dealer=="Rahul":     #It exit and print the below statement
            break
    print("Out from the innerloop")
print("Out from the outer loop")


print("\n")
List1=["Hi",'Hello',"Welcome"]
List2=["Abhilash","Rahul","Vimal"]
for Greet in List1:
    for Dealer in List2:
        print(Greet,Dealer)
        if Greet=="Hi" and Dealer=="Vimal":
            break
    print("Out from the innerloop")
print("Out from the outer loop")
