#Solution of Schrodinger's 1D wave equation for Anharmonic Oscillator Potential
#Euler method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(r):
    b=1
    k=1
    return (k*r**2)/2+(b*r**3)/3

#Define the dimensionless Time Independent Schrodinger Equation
def psi(r,y,u,E):
    f=-2*(E-V(r))*y
    return f

def phi(r,y,u):
	return u
   
#Boundary conditions for a wave function
r0,y0,rn,yn=-1.8,0,1.8,0
n=1000

#Euler method with shooting parameter E as energy
def AHO(E):
    alpha=0.001          #Initial derivative (can be anything as it doesn't control the solution after normalization)
    r,y,u,R,Y,U=r0,y0,alpha,[r0],[y0],[alpha]
    h=(rn-r0)/n
    for i in range(0,n):   
        y=y+h*phi(r,y,u)
        u=u+h*psi(r,y,u,E)
        r=r+h
        R.append(r)
        Y.append(y)
        U.append(u)
    return R,Y,U


#Guessing energy value from plot
energies=np.arange(0,10,0.1)
H=[]
for i in energies:
    hits=AHO(i)[1][-1]
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Euler Method/Primitive Method/Python Files/Anharmonic_hits.png')
plt.show()



#Bisection method for proper choice of energy
while True:
    E1=eval(input('Enter the 1st guess of energy : '))
    E2=eval(input('Enter the 2nd guess of energy : '))
    if AHO(E1)[1][-1]*AHO(E2)[1][-1]<0:
        break
    print('Energy does not exist between the guesses\nEnter new guesses')

itr=0.0
plt.figure(figsize=(11,6)) 
while True:
    E3=(E1+E2)/2
    if AHO(E3)[1][-1]==0:
        break
    if AHO(E1)[1][-1]*AHO(E3)[1][-1]>0:
        E1=E3
    else:
        E2=E3
    itr=itr+1
    acc=abs(E1-E2)
    if acc<0.00000001:
        break
    
#Normalisation of wave function
    N=1/np.sqrt(simpson(np.array(AHO(E3)[1])*np.array(AHO(E3)[1]),x=np.array(AHO(E3)[0])))
    solution=N*np.array(AHO(E3)[1])

#Plotting and printing
    plt.subplot(121)
    r=np.array(AHO(E3)[0])
    plt.plot(r,V(r),'--',color='indigo')
    plt.ylabel(r'Potential $V(r)$')
    plt.xlabel('Distance (r) in 1D')
    plt.title('Anharmonic Oscillator Potential')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    
    plt.subplot(122)
    plt.cla()
    plt.plot(np.array(AHO(E3)[0]),solution,'r',lw=1.5)
    plt.plot(AHO(E3)[0][-1],AHO(E3)[1][-1],'o',color='black',ms=5)
    plt.title('Normalised wave function for Anharmonic Oscillator Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Distance (r) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=r0,color='black',lw=1,ls='--')
    plt.axvline(x=rn,color='blue',lw=1)
    plt.grid()
    plt.pause(0.5)

plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Euler Method/Primitive Method/Python Files/Anharmonic.png')
plt.show()
print('The dimensionless energy satisfying the boundary condition is',E3)
        
