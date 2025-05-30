#Question 3
#LU Decomposition Method for solution of system of linear equations
#Without Pivot Check

import numpy as np

#Create the coefficient matrix of size 5x5
AB=[[3,-1,4],[-2,0,5],[7,2,-2]]
AB=np.array(AB,dtype=float)

#Initialize L as an identity matrix
L=np.eye(3)

flag=False
if np.linalg.det(AB)!=0:
    flag=True
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,3-1):                     # Controls the repeated operations
        for i in range(k+1,3):                 # Controls row   
            ratio=AB[i,k]/AB[k,k]
            L[i,k]=ratio                       # Store the multiplier in L
            for j in range(0,3):               # Controls column
                AB[i,j]-=AB[k,j]*ratio
    diag_product=1
    for i in range(3):
        diag_product*=AB[i][i]
    print('The determinant of A matrix is :',diag_product)
    print()
else:
    print('The system of equations is inconsistent')

if flag==True:    
    def LU(B):
        #Forward Substitution to solve L*Y=B
        Y=np.empty(3)
        for i in range(3):
            Y[i]=B[i]
            for j in range(i):
                Y[i]-=L[i][j]*Y[j]
            Y[i]=Y[i]/L[i][i]
    
        #Backward Substitution to solve U*X=Y
        X=np.empty(3)
        for i in range(3-1,-1,-1):
            X[i]=Y[i]
            for j in range(i+1,3):
                X[i]-=AB[i][j]*X[j]
            X[i]=X[i]/AB[i][i]

        print('The solutions are : ',X)

B1=np.array([6,3,7],dtype=float)
B2=np.array([-4,2,-5],dtype=float)

LU(B1)
print()
LU(B2)
