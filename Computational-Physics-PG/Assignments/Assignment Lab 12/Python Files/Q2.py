#Question 2 
#Solution of Laplace's equation in 2D square plane around a charged capacitor using Gauss Seidel Relaxation Technique

import numpy as np
import matplotlib.pyplot as plt
from numba import njit

L=10                       #Length of the 2D surface (in m)
dx=0.1                     #Grid spacing (in m)
N=int(L/dx+1)
max_iteration=20000
tol=1e-6

#Boundary and Initial conditions for capacitor-like configuration 
#(The plates are located at x=2 and x=8 m and streches from y=2 to y=8 vertically)
u=np.zeros((N,N))         
u[20:81,20]=1
u[20:81,80]=-1

skip=np.array([20,80])      #Columns with fixed potential (plates)

w=1.94                      #w_optimal=2/(1+np.sin(np.pi/N)), w lies between 1 and 2 for fast convergence (over-relaxation), above 2 solution diverges (aggressive over-relaxation), below 1 (under-relaxation), solution converges after very long time
E=np.zeros(max_iteration)   #njit works on arrays only

@njit
def gauss_seidel(u,w,N,tol,max_iteration,E):
    for iteration in range(max_iteration):
        u0=u.copy()
        for i in range(1,N-1):
            for j in range(1,N-1):
                if 20<i<80 and j in skip:
                    continue
                phi=0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1])
                u[i,j]=(1-w)*u[i,j]+w*phi
        err=np.sum(np.abs(u-u0))
        E[iteration]=err
        if err<tol:
            break
    return u,iteration,E[:iteration+1]

u,iteration,E=gauss_seidel(u,w,N,tol,max_iteration,E)

print('Solution Converged after',iteration,'iterations')

plt.plot(range(1,iteration+2),E,'r-',lw=1)
plt.title('Error with increase in number of iterations')
plt.ylabel('Error')
plt.xlabel('No. of iterations')
plt.axhline(color='black')
plt.axvline(color='black')
plt.show()

plt.title('Voltage Distribution around a charged capacitor')
plt.xlabel('x-direction')
plt.ylabel('y-direction')
img=plt.imshow(u,cmap='coolwarm',origin='lower',extent=[0,L,0,L])
plt.colorbar(img,label='Voltage')
plt.show()
