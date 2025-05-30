#Matrix addition using array

import numpy as np  
def get_mat(m,n):                         #Taking inputs in matrix form one by one
    print('Enter elements of matrix : ')
    M=np.empty((m,n))
    for i in range(m):
        for j in range(n):
            M[i][j]=eval(input())
    return M

def show_mat(M,m,n):                      #Printing the array in matrix form    
    for i in M:
        for j in i:
            print(j,end=' ')
        print()

def mat_sum(A1,A2,m,n):
    C=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            C[i][j]+=A1[i][j]*A2[i][j]
    return C

r1=eval(input('Enter row size of 1st matrix : '))
c1=eval(input('Enter column size of 1st matrix : '))
M1=get_mat(r1,c1)
print('The 1st matrix is :')
show_mat(M1,r1,c1)

r2=eval(input('Enter row size of 2nd matrix : '))
c2=eval(input('Enter column size of 2nd matrix : '))
M2=get_mat(r2,c2)
print('The 2nd matrix is :')
show_mat(M2,r2,c2)

if c1==c2 and r1==r2:
    M3=mat_sum(M1,M2,r1,c1)
    print('Resultant matrix is :')
    show_mat(M3,r1,c1)
else:
    print('Matrix adition is not possible')
