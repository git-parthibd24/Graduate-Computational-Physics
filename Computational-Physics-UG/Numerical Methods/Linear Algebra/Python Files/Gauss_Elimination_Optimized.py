#Solution of linear simultaneous equation using Gauss Elimination Method
#With Partial Pivoting Check during reduction 

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
n=int(input('Enter the number of system of linear equations : '))
m=n+1
AB=get_mat(n,m)
print()

#Print the augmented matrix
print('The augmented matrix is :')
show_mat(AB)
print()

#Swap pivot row with the row containing maximum absolute value of element in same column 
def mat_check(M,start_index):
    for p in range(start_index,n):
        max_index=p+np.argmax(np.abs(M[p:,p]))   #returns the index of row below pivot row whose element is bigger than the pivot row in the actual matrix
        if max_index!=p:
            M[[p,max_index],:]=M[[max_index,p],:]
    return M

#Create the coefficient matrix of size n*n
A=AB[:,0:n]

flag=True
if np.linalg.det(A)!=0:
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,n-1):
        AB=mat_check(AB,k)
        if AB[k][k]==0:                 #Exits Gaussian Elimination if the initial row swap doesnt' occurs
            flag=False
            break           
        else:
            for i in range(k+1,n):
                if AB[i][k]==0:         #Skips a row iteration if the element below pivot is already zero
                    continue
                ratio=AB[i][k]/AB[k][k] 
                AB[i,:]-=AB[k,:]*ratio  #Iterates over all column at once using vectorization
   
   #Print the reduced augmented matrix
    print('The reduced augmented matrix is : ')
    show_mat(AB)
    print()
    
    #Back Substitution
    if flag==True:
        X=np.empty(n)                #Solution Matrix
        for i in range(n-1,-1,-1):   #Begins from n-1 th index, ends at index before -1 i.e 0
            X[i]=AB[i][n]            #Reduced constant matrix
            for j in range(i+1,n):
                X[i]-=AB[i][j]*X[j]
            X[i]=X[i]/AB[i][i]
        print('The solutions are : ',X)
    else:
        print('Gauss elimination Method is not applicable') #pivot is zero
else:
    print('The system of equations is inconsistent')
