#Create an array of any size and apply transpose

import numpy as np
def get_mat(m,n):          #Taking inputs in matrix form one by one
    print('Enter elements of matrix :')
    A=np.empty((m,n))
    for i in range(m):
        for j in range(n):
            A[i][j]=eval(input())
    return A

def show_mat(A):           #Printing array in matrix form(note: The other print method is inapplicable here)
    for i in A:
        for j in i:
            print(j,end=' ')
        print()
        
#for any size matrix
def transpose(A,m,n):
    B=np.empty((n,m))
    for i in range(n):
        for j in range(m):
            B[i][j]=A[j][i]
    return B

m=int(input('Enter row size : '))
n=int(input('Enter column size : '))
A=get_mat(m,n)

print()
print('The input matrix is :')
show_mat(A)

print()
TM=transpose(A,m,n)
print('The matrix after transpose is :')
show_mat(TM)
