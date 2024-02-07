#While else loop using input function


total=0
number=int(input("Enter the numbers (0 to quit):"))
while number !=0:
    total=total+number
    number = int(input("Enter the numbers (0 to quit):"))
print("Total number :", total )  #NoteL: To concatenate the int, we use (,)