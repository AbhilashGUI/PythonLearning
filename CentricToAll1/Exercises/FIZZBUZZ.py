#WAP of Fizzbuzz for first 100 numbers


for i in range(1,101):
    if i%2==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%2==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)