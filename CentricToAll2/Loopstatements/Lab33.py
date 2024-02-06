#Forelse : Is executed only if the the for loop is executed successfully

#Using strings

List=["Abhilash","Patel","Pathan"]
for name in List:
    #print(name)
    if name=="Abhilash":
        print(name)

else:
        print("Successfully executed")

print("\n")
Week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
for Days in Week:
    if Days!="Funday":
        print("Not in a tuple")
else:
    print("Successful")
print("End of the program")

print("\n")
Week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
for Days in Week:
    if Days=="Funday":
        break
else:
    print("No such day in a tuple")
print("End of the program")
