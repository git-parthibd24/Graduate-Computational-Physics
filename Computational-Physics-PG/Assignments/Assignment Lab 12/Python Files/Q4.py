#Question 4 
#Solution of Poisson's equation in 2D square plane around two square opposite charge densities in space using Gauss Seidel Relaxation Technique

import numpy as np
import matplotlib.pyplot as plt

L=100                  #Length of the 2D surface (in m)
dx=1                   #Grid spacing (in m)
N=int(L/dx+1)
max_itr=20000
tol=1e-3

#Given constants
pho=1
epsilon=1

#Boundary and Initial conditions at boundaries and top surface of the plane
u=np.zeros((N,N))
u[N-1,:]=100

w=1.9                  #w_optimal=2/(1+np.sin(np.pi/N)), w lies between 1 and 2 for fast convergence (over-relaxation), above 2 solution diverges (aggressive over-relaxation), below 1 (under-relaxation), solution converges after very long time
E=[]                   
for iteration in range(max_itr):
    u0=u.copy()        #Store old values for error calculation
    
    #updating the array using four nearby points with initial guess and current values of updated points
    for i in range(1,N-1):
        for j in range(1,N-1):
            if 20<i<40 and 60<j<80:
                phi=dx**2*pho/epsilon+0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1])
                u[i,j]=(1-w)*u[i,j]+w*phi    #Relaxation Scheme (over-relaxation for faster and aggressive convergence when 1<w<2) 
            
            elif 60<i<80 and 20<j<40:
                phi=-dx**2*pho/epsilon+0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1])
                u[i,j]=(1-w)*u[i,j]+w*phi     #Relaxation Scheme (over-relaxation for faster and aggressive convergence when 1<w<2) 
            
            else:
                phi=0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1])
                u[i,j]=(1-w)*u[i,j]+w*phi

    err=np.sum(np.abs(u-u0))
    E.append(err)
    
    if err<tol:
        break

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
plt.title('Voltage Distribution for given charge distribution')
plt.xlabel('x-direction')
plt.ylabel('y-direction')
img=plt.imshow(u,cmap='coolwarm',origin='lower',extent=[0,L,0,L])  #cmap='viridis'
plt.colorbar(img,label='Voltage')
plt.show()          
