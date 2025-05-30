#Question 2 (2) Method 2
#LU Decomposition Method for solution of system of linear equations
#With Partial Pivot Check

import numpy as np

#Create the coefficient matrix of size 5x5
AB=[[0,1,0,2,-1],[0,0,2,1,2],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]]
AB=np.array(AB,dtype=float)

#Initialize L and P as an identity matrix
L=np.eye(5)
P=np.eye(5)

#Print the matrix
def show_mat(M):
    for i in M:
        for j in i:
            print(format(j,'0.2f'),end=' ')
        print()    

#Print the coefficient matrix
print('The coefficient matrix is : ')
show_mat(AB)
print()

#Swap pivot row with the row containing maximum absolute value of element in same column 
def mat_check(M,start_index):
    for p in range(start_index,5):
        max_index=p+np.argmax(np.abs(AB[p:,p]))   #returns the index of row below pivot row whose element is bigger than the pivot row in the actual matrix
        if max_index!=p:
            M[[p,max_index],:]=M[[max_index,p],:]
    return M
    
    
if np.linalg.det(AB)!=0:
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,5-1):                     # Controls the repeated operations
        AB=mat_check(AB,k)
        P=mat_check(P,k)
        for i in range(k+1,5):                 # Controls row   
            ratio=AB[i,k]/AB[k,k]
            L[i,k]=ratio                       # Store the multiplier in L
            for j in range(0,5):               # Controls column
                AB[i,j]-=AB[k,j]*ratio

    # Print U matrix (upper triangular)
    print('The upper triangular matrix (U) is : ')
    show_mat(AB)
    print()

    # Print L matrix (lower triangular)
    print('The lower triangular matrix (L) is : ')
    show_mat(L)
    print()

    #Create constant matrix B
    B=np.array([-4,1,1,-2,-1],dtype=float)
    B=np.dot(B,P)

    #Forward Substitution to solve L*Y=B
    Y=np.empty(5)
    for i in range(5):
        Y[i]=B[i]
        for j in range(i):
            Y[i]-=L[i][j]*Y[j]
        Y[i]=Y[i]/L[i][i]

    #Backward Substitution to solve U*X=Y
    X=np.empty(5)
    for i in range(5-1,-1,-1):
        X[i]=Y[i]
        for j in range(i+1,5):
            X[i]-=AB[i][j]*X[j]
        X[i]=X[i]/AB[i][i]

    print('The solutions are : ',X)

else:
    print('The system of equations is inconsistent')

