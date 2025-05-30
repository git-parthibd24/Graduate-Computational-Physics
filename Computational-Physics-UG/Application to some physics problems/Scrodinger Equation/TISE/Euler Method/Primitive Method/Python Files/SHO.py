#Solution of Schrodinger's 1D wave equation for Simple Harmonic Oscillator Potential
#Euler Method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(x):
    omega=1
    return x**2/2

#Define the dimensionless Time Independent Schrodinger Equation
def psi(x,y,u,E):
    f=-2*(E-V(x))*y
    return f

def phi(x,y,u):
	return u
   
#Boundary conditions for a wave function
x0,y0,xn,yn=-2.5,0,2.5,0
n=1000

#Euler method with shooting parameter E as energy
def SHO(E):
    alpha=0.001          #Initial derivative (can be anything as it doesn't control the solution after normalization)
    x,y,u,X,Y,U=x0,y0,alpha,[x0],[y0],[alpha]
    h=(xn-x0)/n
    for i in range(0,n):   
        y=y+h*phi(x,y,u)
        u=u+h*psi(x,y,u,E)
        x=x+h
        X.append(x)
        Y.append(y)
        U.append(u)
    return X,Y,U


#Guessing dimensionless energy value from plot
energies=np.arange(0,10,0.1)
H=[]
for i in energies:
    hits=SHO(i)[1][-1]
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.ylim(-0.02,0.02)
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Euler Method/Primitive Method/Python Files/SHO_hits.png')
plt.show()


#Bisection method for proper choice of energy
while True:
    E1=eval(input('Enter the 1st guess of energy : '))
    E2=eval(input('Enter the 2nd guess of energy : '))
    if SHO(E1)[1][-1]*SHO(E2)[1][-1]<0:
        break
    print('Energy does not exist between the guesses\nEnter new guesses')

itr=0.0
plt.figure(figsize=(11,6)) 
while True:
    E3=(E1+E2)/2
    if SHO(E3)[1][-1]==0:
        break
    if SHO(E1)[1][-1]*SHO(E3)[1][-1]>0:
        E1=E3
    else:
        E2=E3
    itr=itr+1
    acc=abs(E1-E2)
    if acc<0.00000001:
        break
          
#Normalisation of wave function
    N=1/np.sqrt(simpson(np.array(SHO(E3)[1])*np.array(SHO(E3)[1]),x=np.array(SHO(E3)[0])))
    solution=N*np.array(SHO(E3)[1])

#Plotting and printing
    plt.subplot(121)
    x=np.array(SHO(E3)[0])
    plt.plot(x,V(x),'--',color='indigo')
    plt.ylabel(r'Potential $V(x)$')
    plt.xlabel('Distance (x) in 1D')
    plt.title('SHO Potential')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    
    plt.subplot(122)
    plt.cla()
    plt.plot(np.array(SHO(E3)[0]),solution,'r',lw=1.5)
    plt.plot(SHO(E3)[0][-1],SHO(E3)[1][-1],'o',color='black',ms=5)
    plt.title('Normalised wave function for Simple Harmonic Oscillator Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Distance(x) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=x0,color='black',lw=1,ls='--')
    plt.axvline(x=xn,color='blue',lw=1)
    plt.grid()
    plt.pause(0.5)
   
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Euler Method/Primitive Method/SHO.png')
plt.show()
print('The dimensionless energy satisfying the boundary condition is',E3)
        
