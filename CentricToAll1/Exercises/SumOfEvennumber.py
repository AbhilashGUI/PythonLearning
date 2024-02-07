
#WAP sum of evennumbers from 0 to 1. Including 1 and 100

total=0
for i in range(0,101,2):
    total+=i
print(total)

#Another way not inclding the stepsize. Just by adding the if condition

total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print(total)