#Solution of linear simultaneous equation using solve() function of linalg submodule of numpy

import numpy as np 

n=int(input('Enter no. of unknowns : '))
A=np.empty((n,n))
B=np.empty(n)

print('Enter elements of co-efficient matrix : ')
for i in range(n):
    for j in range(n):
        A[i][j]=eval(input())

print('Enter RHS Constant Matrix :')
for i in range(n):
    B[i]=eval(input())

X=np.linalg.solve(A,B)
print('The solutions are :',X)
