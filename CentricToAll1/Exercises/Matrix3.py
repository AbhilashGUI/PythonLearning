#Nested list example in matrix form

First_floor=[1,2,3]
Second_floor=[4,5,6]
Overall_Flats=[First_floor,Second_floor]
print(f"{First_floor}\n{Second_floor}")

Portion=input("Enter the portion, which is readytomove:")
Flats=int(Portion[0])
Apartment=int(Portion[1])
Flat_selection=Overall_Flats[Flats-1]
Flat_selection[Apartment-1]="ReadyToMove"
print(f"{First_floor}\n{Second_floor}")