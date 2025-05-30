#Solution of TDSE for a ground state wavefunction in harmonic potential using FTCS Crank Nicolson Method
#Taking average of 2nd order in space of both implicit and explicit method to preserve norm 

#>psi[x][t+1]=psi[x][t]+0.5*(i*dt/dx**2)*(psi[x+1][t]-2psi[x][t]+psi[x-1][t])-i*V[x][t]*dt*psi[x][t]
#>psi[x][t+1]=mu*psi[x+1][t]+(1-2*mu-i*dt*V[x][t])*psi[x][t]+mu*psi[x-1][t]
#>where mu=0.5*i*dt/dx**2

#This algorithm preserves stability, accuracy and unitarity 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

#Parameters
L=40            #length of the box
N=1000          #Discretized spatial points
dt=0.01         #Time step (Neumann Stability Condition)
t=0             #Initial time
tf=15           #Final time

#Initial condition
xs,dx=np.linspace(-L/2,L/2,N,retstep=True)
mu=dt/dx**2*(0.+1.j)/2

omega=1.0       #angular frequency of the harmonic oscillator
prefactor=(omega/np.pi)**0.25
us=prefactor*np.exp(-0.5*omega*xs**2)
us=us.astype(complex)

Norm_initial=simpson(np.abs(us)**2,x=xs)
print('The initial norm of the wavefunction is :',Norm_initial)

#Applied potential
Vs=omega**2*xs[1:-1]**2/2    #Only taking inside points which will be updated by M matrix.                              

#Seting Matrix
A1=np.eye(N-2)*(1-mu)+np.diag(-1.j*dt/2*Vs)+mu/2*np.eye(N-2,k=1)+mu/2*np.eye(N-2,k=-1)
A2=np.eye(N-2)*(1+mu)+np.diag(1.j*dt/2*Vs)-mu/2*np.eye(N-2,k=1)-mu/2*np.eye(N-2,k=-1)
B=np.dot(np.linalg.inv(A2),A1)

#Dynamic Plotting
plt.figure(figsize=(10,5))

plt.plot(xs,us,color='lightskyblue',label=r'Initial Wavepacket $\psi(x,0)$')
line1,=plt.plot(xs,us,color='blue',label=r'Evolving Wavepacket $\psi(x,t)$')       #Unpacking from list

plt.plot(xs,np.abs(us)**2,color='peachpuff',label=r'$|\psi(x,0)|^2$')
line2,=plt.plot(xs,np.abs(us)**2,color='red',label=r'$|\psi(x,t)|^2$')             #Unpacking from list

plt.axvline(x=0,color='black',lw=1)
plt.axhline(y=0,color='black',lw=1)
plt.plot(xs[1:-1],Vs,'--',color='green',lw=1,label='Potential')

plt.ylim(-0.8,0.8)
plt.legend()

while t<tf:
    us[1:-1]=np.dot(B,us[1:-1])            #Solution matrix generated over space in a given time slice (except end points) which is being updated with next time slices
    t+=dt
    line1.set_ydata(np.real(us))
    line2.set_ydata(np.abs(us)**2)
    plt.title('Time Evolution of ground state in harmonic potential\n'+r'Time =%10.6f,norm =%10.6f'%(t,simpson(np.abs(us)**2,x=xs)))
    plt.pause(0.000001)

plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TDSE/Harmonic_GS_CN-Method.png')    
plt.show()

#Conservation of norm
Norm_final=simpson(np.abs(us)**2,x=xs)
print('The final norm of the wavefunction is :',Norm_final)

if round(Norm_initial/Norm_final)==1:
    print('The Norm is preserved')
else:
    print('Norm is not preserved')
