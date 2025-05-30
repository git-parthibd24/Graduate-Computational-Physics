#Solution of TDSE for a free gaussian wavepacket using FTCS Implicit Method
#Implementing tridiagonal matrix method to evaluate solution (with dead wall boundary condition)

#>psi[x][t+1]=psi[x][t]+0.5*(i*dt/dx**2)*(psi[x+1][t+1]-2psi[x][t+1]+psi[x-1][t+1])-i*V[x][t+1]*dt*psi[x][t+1]
#>psi[x][t]=-mu*psi[x+1][t+1]+(1+2*mu+i*dt*V[x][t+1])*psi[x][t+1]-mu*psi[x-1][t+1]
#>where mu=0.5*i*dt/dx**2

#Norm is not preserved for approximation (norm decreases)

import numpy as np
import matplotlib.pyplot as plt

#Constants
a=1.0         #standard deviation of gaussian
x0=-5.0       #mean of gaussian
k=20.0        #wave-vector

#Parameters
L=20.0        #length of the box
N=1000        #Discretized spatial points
dt=0.00005    #Time step (Neumann Stability Condition)
t=0           #Initial time
tf=0.1        #Final time

#Initial condition
xs,dx=np.linspace(-L/2,L/2,N,retstep=True)
us=np.exp(-(xs-x0)**2/a+(0.0+1.j)*k*xs)    #This is same as the 1st column (initial time) of 2D array used in 1D diffusion equation. This 1D array will be updated with time
mu=dt/dx**2*(0.+1.j)/2

#Applied potential
Vs=0*xs[1:-1]    #Only taking inside points which will be updated by M matrix.                            

#Explicit Algorithm to create tridiagonal matrix M
M=np.eye(N-2)*(1+2*mu)+np.diag(1.j*dt*Vs)-mu*np.eye(N-2,k=1)-mu*np.eye(N-2,k=-1)      #np.eye() creates identity matrix. k parameter shifts the leading diagonal to submajor or subminor position. np.diag() creates a diagonal matrix with elements of Vs array
M=np.linalg.inv(M)

#Dynamic Plotting
line,=plt.plot(xs,np.abs(us)**2,color='green')           #',' means unpacking the list. Can also use line=plt.plot(xs,np.abs(us)**2)[0]
plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.axhline(y=1,color="red")
plt.ylim(-0.5,1.1)
while t<tf:
    us[1:-1]=np.dot(M,us[1:-1])            #Solution matrix generated over space in a given time slice (except end points) which is being updated with next time slices
    t+=dt
    plt.title(r'Probability Distribution of Free Gaussian wavepacket (implicit method)'+'\n$Time = %10.6f$'%(t-dt))
    line.set_ydata(np.abs(us)**2)
    plt.pause(0.000001)
    
plt.show()
