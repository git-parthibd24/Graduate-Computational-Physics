#Create an array of any size using list input and apply transpose using function

import numpy as np
m=[]
r,c=eval(input("Enter no. of rows and columns : "))
for i in range(r):
    a=[]
    for j in range(c):
        item=eval(input("enter no. : "))
        a.append(item)
    m.append(a)

#list to array
arr=np.array(m)

print('The matrix is :')
for i in range(r):
    for j in range(c):
        print(arr[i][j],end=" ")
    print()

#Transpose of array
print()
print('The transpose of the array is :')  
print(np.transpose(arr))
