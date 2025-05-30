#Question 4
#Gauss Elimination Method for solving tridiagonal system of simultaneous linear equations of motion of N harmonic oscillators in a 1D chain 
#(Modelling of vibration of atoms in a solid)
'''
>(a-k)x_1-kx_2=C
#>ax_i-kx_(i-1)-kx_(i+1)=0 ; 2<=i<=N-1
#>(a-k)x_N-kx_(N-1)=0
; where a=2k-mw^2
'''

import numpy as np
import matplotlib.pyplot as plt

#Given Constants
N=26
C=1.0
m=1.0
k=6.0
omega=2.0
a=2*k-m*omega**2

#Create the augmented matrix
AB=np.zeros((N,N+1),dtype=float)
for i in range(N-1):
    AB[i,i]=a
    AB[i,i+1]=-k
    AB[i+1,i]=-k
AB[0,0]=a-k
AB[N-1,N-1]=a-k
AB[:,-1]=0
AB[0,-1]=C


#Swap pivot row with the row containing maximum absolute value of element in same column 
def mat_check(M):
    for p in range(n):
        max_index=p+np.argmax(np.abs(M[p:,p]))   #returns the index of row below pivot row whose element is bigger than the pivot row in the actual matrix
        if max_index!=p:
            M[[p,max_index],:]=M[[max_index,p],:]
    return M


#Create the coefficient matrix of size N*N
A=AB[:,0:N]

#Gauss Elimination
flag=True
if np.linalg.det(A)!=0:
    print('Solution for given set of equation is consistent')
    print()
    for k in range(0,N-1):
        if AB[k][k]==0:                 #Exits Gaussian Elimination if the initial row swap doesnt' occurs
            flag=False
            break           
        else:
            for i in range(k+1,k+2):    #Performs row operation only on the element just below pivot (lower tridiagonal elements)      
                ratio=AB[i][k]/AB[k][k] 
                AB[i,:]-=AB[k,:]*ratio  #Iterates over all column at once using vectorization. For optimal procedure we need to keep the column iteration only on the tridiagonal elements and ignore the rest except the last row 
    
    #Back Substitution
    if flag==True:
        Y=np.empty(N)                   #Solution Matrix
        for i in range(N-1,-1,-1):      #Begins from n-1 th index, ends at index before -1 i.e 0
            Y[i]=AB[i][N]               #Reduced constant matrix
            for j in range(i+1,N):
                Y[i]-=AB[i][j]*Y[j]
            Y[i]=Y[i]/AB[i][i]

        #Plotting
        X=np.linspace(0,25,N)
        plt.plot(X,Y,'bo')
        plt.plot(X,Y,'r-')
        plt.axhline(color='black')
        plt.axvline(color='black')
        plt.ylabel('Amplitude of vibration')
        plt.xlabel('Along length of the chain')
        plt.grid()
        plt.show()
        
    else:
        print('Gauss elimination Method is not applicable')     #pivot is zero
else:
    print('The system of equations is inconsistent')
