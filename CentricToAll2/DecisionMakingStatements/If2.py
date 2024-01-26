
#Examples: Taking the inputs from the user only for if statements#

number=int(input("Enter the number:"))  #Passing the even number , will return the desired output
                                        #Passing the odd number, will return nothing, because we are using only if condition


if number%2==0:                         #Modulus(%) consider remainder as an output
    print("Given number is an even number")




number1=int(input("Enter the number:"))       #Passing the numbers, which are multiples of 12 like  144 and 4
number2=int(input("Enter the other number :"))
if number1/12==12 and number2/4==12:                  #Division(/) consider quotient as an output
    print("Entered numbers are multiples of 12")