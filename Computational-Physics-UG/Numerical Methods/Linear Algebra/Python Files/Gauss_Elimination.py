#Solution of linear simultaneous equation using Gauss Elimination Method
#Without Pivot Check

import numpy as np

#Create the augmented matrix
def get_mat(n,m):
    print('Enter the elements of augmented matrix : ')
    M=np.empty((n,m))
    for i in range(n):
        for j in range(m):
            M[i][j]=eval(input())
    return M

#Print the augmented matrix
def show_mat(M):
    for i in M:
        for j in i:
            print(format(j,'0.3f'),end=' ')
        print()

#Call input augmented matrix function of size (n)*(n+1)  
n=int(input('Enter the number of system of linear equations :'))
m=n+1
AB=get_mat(n,m)
print()

#Print the augmented matrix
print('The augmented matrix is :')
show_mat(AB)
print()

#Create the coefficient matrix of size n*n
A=AB[:,0:n]

if np.linalg.det(A)!=0:
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,n-1):                      #controls the repeated operations on updated matrix
        for i in range(k+1,n):                  #controls row   
            ratio=AB[i][k]/AB[k][k]
            for j in range(0,n+1):              #controls column
                AB[i][j]-=AB[k][j]*ratio
    
    #Print the reduced augmented matrix
    print('The reduced augmented matrix is : ')
    show_mat(AB)
    print()
    
    #Back Substitution
    X=np.empty(n)                #Solution Matrix
    for i in range(n-1,-1,-1):   #Begins from n-1 th index, ends at index before -1 i.e 0
        X[i]=AB[i][n]            #Reduced constant matrix
        for j in range(i+1,n):
            X[i]-=AB[i][j]*X[j]
        X[i]=X[i]/AB[i][i]
    print('The solutions are : ',X)
    
else:
    print('The system of equations are inconsistent')
