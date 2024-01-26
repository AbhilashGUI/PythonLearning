#round function is used to roundoff the given number.It contains number and the number of digits for float number(Which is optional)#

print(round(7.365,2))   #7.37
print((round(2.1)))     #2
print(round(5.5))       #6(The nearest even number)
print(round(6.5))       #6(The nearest even number)
print(round(93.633,3))  #93.333
print(round(66.666,2))  #66.67





#Note: The second number is to make the number visible in output by transiting in the form-of roundoff#

print(round(5.34,1))
print(round(236,0))    #Bydefault, if you don't give the value of 0. It would be the same.

print(round(263,-1))   #This would be 260
print(round(263,-2))   #This would be 300

print(round(454,-1))     #Logic: If the last digit is <5 and the number of digits is -1. Then the o/p be 45*10=450
print(round(456,-1))    #Logic: If the last digit is >5 and the number of digits is -1. Then the o/p be 46*10=460

print(round(234,-2))
print(round(876,-2))

print(round(67154,-3))