#Solution of Schrodinger's 1D wave equation for Coulomb potential
#Using Odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint,simpson

#Define the dimensionless potential
def V(r):
    return -1/r

#Define the dimensionless Time Independent Schrodinger Equation in odeint()
def Coulomb(y,r,E):
    y1=y[0]
    y2=y[1]
    yp1=y2
    yp2=-2*(E/2-V(r))*y1
    yp=[yp1,yp2]
    return yp

#Boundary Conditions for a wave function 
#Large end point to capture many Coulomb Potential states before infinite well states (positive energies) take over when the system actually responds to the finite boundary conditions for higher excited states
#Larger the boundary, more tolerance required for wavefunction to converge
r0,y0,rn,yn=1e-7,0,10,0
#r0,y0,rn,yn=1e-12,0,200,0
r=np.arange(r0,rn,0.002)
L=len(r)
alpha=0.001         #Initial derivative (can be anything as it doesn't control the solution after normalization)
y0=[0.00,alpha]     #Initial condition for y and y' 
      


#Guessing energy value from plot
def shoot(E):
    u=odeint(Coulomb,y0,r,args=(E,))
    return u[:,0][-1]

#Energies are negative (-1/n**2) with maximum value of -1.0 (scaled system) for the Coulomb Potential
energies=np.arange(-1.2,0,0.002)
H=[]
for i in energies:
    hits=shoot(i)
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.ylim(-0.021,0.022)
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Inbuilt Function Method/Primitive Method/Python Files/Coulomb_hits.png')
plt.show()


#Bisection-Shooting method for proper choice of energy
while True:
    E1=eval(input('Enter 1st energy guess : '))
    E2=eval(input('Enter 2nd energy guess : '))
    uA=odeint(Coulomb,y0,r,args=(E1,))
    uB=odeint(Coulomb,y0,r,args=(E2,))
    solA=uA[:,0]
    solB=uB[:,0]
    if solA[L-1]*solB[L-1]<0.0:
        break
    else:
        print('Incorrect sssumption of guesses\nEnter new guesses')

itr=0
plt.figure(figsize=(11,6)) 
while True:
    u1=odeint(Coulomb,y0,r,args=(E1,))
    sol1=u1[:,0]
    u2=odeint(Coulomb,y0,r,args=(E2,))
    sol2=u2[:,0]
    E3=(E1+E2)/2
    u3=odeint(Coulomb,y0,r,args=(E3,))
    sol3=u3[:,0]
    if sol1[L-1]*sol3[L-1]==0:
        break
    if sol1[L-1]*sol3[L-1]<0.0:
        E2=E3
    else:
        E1=E3
    itr=itr+1
    acc=abs(E1-E2)
    if acc<0.00000000001:
        break
    
    
#Normalisation of wave function
    N=1/np.sqrt(simpson(sol3*sol3,x=r))
    sol3=N*sol3
    
#Plotting and printing
    plt.subplot(121)
    plt.plot(r,V(r),'--',color='indigo')
    plt.ylabel(r'Potential $V(r)$')
    plt.xlabel('Distance (r) in 1D')
    plt.title('Coulomb Potential')
    plt.xlim(-0.1,0.7)
    plt.ylim(-100,10)
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
  
    plt.subplot(122)
    plt.cla()
    plt.title('Normalised wave function under Coulomb Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Radial Distance(r) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.grid()
    plt.axhline(color='black',lw=1)
    plt.axvline(x=r0,color='blue',lw=1)
    plt.axvline(x=rn,color='black',lw=1,ls='--')
    plt.plot(r,sol3,'r',lw=1.5)
    plt.plot(r[-1],-u3[-1,0],'o',color='black',ms=5)
    plt.pause(0.5)
    
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Inbuilt Function Method/Primitive Method/Python Files/Coulomb.png')  
plt.show()
print('The energy satisfying the boundary condition is',13.6*E3,'eV')
        
    
