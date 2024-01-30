#Nested list example in matrix form
Locker_cabinet1=[1,2,3]
Locker_cabinet2=[4,5,6]
Locker_cabinet3=[7,8,9]
LockerCompartment=[Locker_cabinet1,Locker_cabinet2,Locker_cabinet3]
print(f"{Locker_cabinet1}\n{Locker_cabinet2}\n{Locker_cabinet3}")

locker=input("Enter the locker number, where you want to hide money:")
Locker_horizontal=int(locker[0])
Locker_vertical=int(locker[1])
Locker_selection=LockerCompartment[Locker_horizontal-1]
Locker_selection[Locker_vertical-1]='M'
print(f"{Locker_cabinet1}\n{Locker_cabinet2}\n{Locker_cabinet3}")

