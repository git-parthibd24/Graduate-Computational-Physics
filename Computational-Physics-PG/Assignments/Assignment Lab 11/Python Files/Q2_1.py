#Question 2 (1)
#Gauss Elimination Method for solution of system of linear equations
#Without Pivot Check

import numpy as np

#Create the augmented matrix of size 5*6 by row swapping to avoid zero in initial pivot
AB=[[1,2,0,-2,0,-4],[0,1,0,2,-1,1],[0,0,2,1,2,1],[0,0,0,-1,1,-2],[0,1,-1,1,-1,-1]]
AB=np.array(AB)

#Print the augmented matrix
def show_mat(M):
    for i in M:
        for j in i:
            print(format(j,'0.0f'),end=' ')
        print()

#Print the augmented matrix
print('The augmented matrix is : ')
show_mat(AB)
print()

#Create the coefficient matrix of size 5*5
A=AB[:,0:5]

if np.linalg.det(A)!=0:
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,5-1):                      #controls the repeated operations on updated matrix
        for i in range(k+1,5):                  #controls row   
            ratio=AB[i][k]/AB[k][k]
            for j in range(0,5+1):              #controls column
                AB[i][j]-=AB[k][j]*ratio
    
    #Print the reduced augmented matrix
    print('The reduced augmented matrix is : ')
    show_mat(AB)
    print()
    
    #Back Substitution
    X=np.empty(5)                #Solution Matrix
    for i in range(5-1,-1,-1):   #Begins from n-1 th index, ends at index before -1 i.e 0
        X[i]=AB[i][5]            #Reduced constant matrix
        for j in range(i+1,5):
            X[i]-=AB[i][j]*X[j]
        X[i]=X[i]/AB[i][i]
    print('The solutions are : ',X)
    
else:
    print('The system of equations are inconsistent')
