#Solution of Schrodinger's 1D wave equation for Anharmonic Oscillator potential
#Using Odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint,simpson

#Define the dimensionless potential
def V(r):
    b=1
    k=1
    return (k*r**2)/2+(b*r**3)/3

#Define the dimensionless Time Independent Schrodinger Equation in odeint()
def AHO(y,r,E):
    y1=y[0]
    y2=y[1]
    yp1=y2  
    yp2=-2*(E-V(r))*y1
    yp=[yp1,yp2]
    return yp

#Boundary Conditions for a wave function
r0,y0,rn,yn=-1.8,0,1.8,0           
n=1000
h=(rn-r0)/n
r=np.arange(r0,rn,h)         
L=len(r)
alpha=0.001         #Initial derivative (can be anything as it doesn't control the solution after normalization)
y0=[0.00,alpha]     #Initial condition for y and y' 
      

#Guessing energy value from plot
def shoot(E):
    u=odeint(AHO,y0,r,args=(E,))
    return u[:,0][-1]

energies=np.arange(0,10,0.1)
H=[]
for i in energies:
    hits=shoot(i)
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Inbuilt Function Method/Primitive Method/Python Files/Anharmonic_hits.png')
plt.show()


#Bisection-Shooting method for proper choice of energy
while True:
    E1=eval(input('Enter 1st energy guess : '))
    E2=eval(input('Enter 2nd energy guess : '))
    uA=odeint(AHO,y0,r,args=(E1,))
    uB=odeint(AHO,y0,r,args=(E2,))
    solA=uA[:,0]
    solB=uB[:,0]
    if solA[L-1]*solB[L-1]<0.0:
        break
    else:
        print('Incorrect sssumption of guesses\nEnter new guesses')


itr=0
plt.figure(figsize=(11,6)) 
while True:
    u1=odeint(AHO,y0,r,args=(E1,))
    sol1=u1[:,0]
    u2=odeint(AHO,y0,r,args=(E2,))
    sol2=u2[:,0]
    E3=(E1+E2)/2
    u3=odeint(AHO,y0,r,args=(E3,))
    sol3=u3[:,0]
    if sol1[L-1]*sol3[L-1]==0:
        break
    if sol1[L-1]*sol3[L-1]<0.0:
        E2=E3
    else:
        E1=E3
    itr=itr+1
    acc=abs(E1-E2)
    if acc<0.00000001:
        break
   
    

#Normalisation of wave function
    N=1/np.sqrt(simpson(sol3*sol3,x=r))
    sol3=N*sol3
    
#Plotting and printing
    plt.subplot(121)
    plt.plot(r,V(r),'--',color='indigo')
    plt.ylabel(r'Potential $V(r)$')
    plt.xlabel('Distance (r) in 1D')
    plt.title('Anharmonic Oscillator Potential')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
  
    plt.subplot(122)
    plt.cla()
    plt.title('Normalised wave function under Anharmonic Oscillator Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Radial Distance(r) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.grid()
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=rn,color='blue',lw=1)
    plt.axvline(x=r0,color='black',lw=1,ls='--')
    plt.plot(r,sol3,'r',lw=1.5)
    plt.plot(r[-1],-u3[-1,0],'o',color='black',ms=5)
    plt.pause(0.5)
    
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Inbuilt Function Method/Primitive Method/Python Files/Anharmonic.png')
plt.show()
print('The energy satisfying the boundary condition is',E3)
        
    
