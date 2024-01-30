#Nested list example in matrix form

row1=['😊', '😊','😊']
row2=['😊', '😊','😊']
row3=['😊', '😊','😊']
row4=['😊', '😊','😊']
matrix=[row1,row2,row3,row4]
print(f"{row1}\n{row2}\n{row3}\n{row4}")
position=input("Enter the position,where you want to replace the smiley:")
#Example 32: Denotes 3rd row ,2nd column
row_number=int(position[0])                  #Note:[0] represents index
column_number=int(position[1])               #Note:[1] represents length
row_selected=matrix[row_number-1]
row_selected[column_number-1]='X'
print(f"{row1}\n{row2}\n{row3}\n{row4}")
