#Solution of linear simultaneous equation using Gauss Elimination Method
#With Initial Pivot Check (Semi partial pivoting : Doesn't searches for largest element while swapping)

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

#Check and perform row swap if zeros found in the diagonal elements i.e pivot points
def mat_check(M):
    for p in range(0,n):
        for t in range(p+1,n):               #looks for rows below pivot row to prevent modifying previous pivot row
            if M[p][p]==0 and M[t][p]!=0:    #Checks for zero in diagonal position and searches a non zero element in the same column and swaps the rows if found
                M[[p,t],:]=M[[t,p],:]        #This is equivalent of : temp = AB[p,:].copy(), AB[p,:]=AB[t,:], AB[t,:]=temp
    return M

AB=mat_check(AB)
print('The augmented matrix with necessary swapping is :')
show_mat(AB)
print()

#Create the coefficient matrix of size n*n
A=AB[:,0:n]

flag=True
if np.linalg.det(A)!=0:
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,n-1):
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
