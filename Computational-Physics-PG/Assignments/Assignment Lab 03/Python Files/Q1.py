#Question 1
#Generate two NxN matrices A and B with random elements and then computes their product C = AB and evaluate the sum of all elements of C

import numpy as np
from datetime import datetime

ti=datetime.now()
N=int(input("Enter the size of the NxN square matrix : "))

A=np.empty((N,N))
for i in range(N):
    for j in range(N):
        A[i][j]=i*j/100

print()
print('The matrix A is :')
print()
for i in range(N):                  # Iterates over each row
    for j in range(N):              # Iterates over each column in the row
        print(A[i][j], end=' ')     # Prints the element without a newline with a space
    print()                         # Prints a newline after finishing the row

B=np.empty((N,N))
for i in range(N):
    for j in range(N):
        B[i][j]=(i+1)*(j+1)/100

print()
print('The matrix B is : ')
print()
for i in range(N):                  # Iterates over each row
    for j in range(N):              # Iterates over each column in the row
        print(B[i][j], end=' ')     # Prints the element without a newline with a space
    print()                         # Prints a newline after finishing the row

C=np.zeros((N,N))
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j]+=A[i][k]*B[k][j]

print()
print('The matrix C=AB is : ')
print()
for i in C:
    for j in i:
        print(j, end=' ')
    print()

S=0
for i in range(N):
    for j in range(N):
        S+=C[i][j]

tf=datetime.now()

print()
print('The sum of all elements of matrix C is :',np.round(S,3))
print('The time taken to execute the code is :',tf-ti)
