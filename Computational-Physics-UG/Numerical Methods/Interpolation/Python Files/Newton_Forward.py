#Newton's Forward Interpolation
#Used when data points are equispaced

import numpy as np
n=int(input('Enter number of data : '))
X=np.empty(n)
Y=np.empty((n,n))
for i in range(n):
    print('X[',i,']=',end=' ')
    X[i]=eval(input())
    print('Y[',i,'][ 0 ]=',end=' ')
    Y[i][0]=eval(input())
h=X[1]-X[0]
for i in range(1,n-1):
    if X[i+1]-X[i]==h:
        flag=True
    else:
        flag=False
        break
if flag==True:
#Calculation of difference table
#All indexing is done looking at the nature of lower triangular difference table
    for j in range(1,n):                       
        for i in range(j,n):                        #Looking at the lower triangular difference table, for each successive j index, i for that column starts from same j index i.e from the diagonal position
            Y[i][j]=Y[i][j-1]-Y[i-1][j-1]           #In rhs, i index tells for current position, i-1 index tells about position just above current position along a column, j-1 index takes the column previous of current column
    print("The difference table is: " )
#Printing of difference table
    for i in range(n):
        for j in range(i+1):                        #For each increment along row downwards, same increment happens along column rightwards i.e j_max and i values are equal So j goes max to i+1 (+1 since count starts from 0)
            print(format(Y[i][j],'7.3f'),end=' ')
        print()
    x1=eval(input('Enter interpolating point : '))
    u=(x1-X[0])/h
    Sum=Y[0][0]
    term=1.0
    for i in range(1,n):
        term=term*(u-i+1)/i
        Sum=Sum+term*Y[i][i]
    print('The value of the function at x =',X,'is :',Sum)
else:
    print('Newtons Forward Interpolation is not applicable')
