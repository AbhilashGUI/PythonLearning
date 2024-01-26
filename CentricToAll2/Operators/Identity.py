#dentity operator : Is all about comparing the objects with the memory location. If both objects are same then they will share the common memory location
##Which can be found/fetch using the operators called is and is not
a=10
b=10
print(id(a))
print(id(b))
print(a is b)


a=20
b=25
print(id(a))
print(id(b))
print(a is b)


a=20
b=25
print(id(a))
print(id(b))
print(a is not b)




a=30                  #Different objects, provide different locations
print(id(a))
a=35
print(id(a))          #Different objects, provide different locations
print(a is a)         #Here, the objects are different, but printing the statement as true. Because variable a is comparing with the other variable a