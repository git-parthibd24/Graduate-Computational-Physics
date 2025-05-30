#Question 1 (Method 2 : Faster Processing)
#Solution of Laplace's equation in 2D square plane using Gauss Seidel Relaxation Technique

import numpy as np
import matplotlib.pyplot as plt
from numba import njit

L=1                         #Length of the 2D surface (in m)
dx=0.01                     #Grid spacing (in m)
N=int(L/dx+1)
max_iteration=20000
tol=1e-6

#Boundary and Initial conditions at boundaries and top surface of the plane
u=np.zeros((N,N))         
u[N-1,:]=100                #Top surface at 100 V, this is the last row in the matrix since it has the maximum row index which corresponding to top surface in right-handed cartesian coordinate system         		          

w=1.93                      #w_optimal=2/(1+np.sin(np.pi/N)), w lies between 1 and 2 for fast convergence (over-relaxation), above 2 solution diverges (aggressive over-relaxation), below 1 (under-relaxation), solution converges after very long time
E=np.zeros(max_iteration)   #njit works on arrays only

#Numba-optimized solver function
@njit
def gauss_seidel(u,w,N,tol,max_iteration,E):     #need to make all variables and parameters local variables being used in the function for njit to work
    for iteration in range(max_iteration):
        u0=u.copy()	            #Store old values for error calculation
    
        #updating the array using four nearby points with initial guess and current values of updated points
        for i in range(1,N-1):
            for j in range(1,N-1):
                phi=0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1])
                u[i,j]=(1-w)*u[i,j]+w*phi       #Relaxation Scheme (over-relaxation for faster and aggressive convergence when 1<w<2) 
			
        err=np.sum(np.abs(u-u0))
        E[iteration]=err

        if err<tol:
            break
    
    return u,iteration,E[:iteration+1]

u,iteration,E=gauss_seidel(u,w,N,tol,max_iteration,E)

print('Solution Converged after',iteration,'iterations')

#For plotting of the error with iterations
plt.plot(range(1,iteration+2),E,'r-',lw=1)
plt.title('Error with increase in number of iterations')
plt.ylabel('Error')
plt.xlabel('No. of iterations')
plt.axhline(color='black')
plt.axvline(color='black')
plt.show()

#Contour plotting and colour mapping
plt.title('Voltage Distribution')
x=np.linspace(0,L,N)
y=np.linspace(0,L,N)
plt.xlabel('x-direction')
plt.ylabel('y-direction')
img=plt.imshow(u,cmap='coolwarm',origin='lower',extent=[0,L,0,L])  #cmap='viridis'
plt.colorbar(img,label='Voltage')
plt.show()
