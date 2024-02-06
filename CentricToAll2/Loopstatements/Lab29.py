#for loop: Executes a block of the code multiple times and abbreviates the code that manages the loop variable

#Using Strings#

name="Abhilash"
for i in name:     #Note:In operator is used in for loop to iterate  right from beginning and till iteration is completed
    print(i)       #Note: Varible i holds the value of every item in sequence.


#Strings in list
names=["Abhilash","Avinash","Arvind","Bunty"]
for name in names:
    print(name)
    if name=="Abhilash":
        print("Hey, it's me")

#Note: The flow of the program will execute & print in a sequence along with the condition(If defined )#
names1=["Abhilash","Avinash","Arvind","Bunty"]
for name in names1:
    print(name)
    if name=="Arvind":
        print("Hey, he is my brother")

