#Solution of Schrodinger's 1D wave equation for Morse potential
#Using Odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint,simpson

#Define the dimensionless potential
def V(x):
    D=1
    b=1
    return D*(1-np.exp(-(x-b)))**2 

#Define the dimensionless Time Independent Schrodinger Equation in odeint()
def Morse(y,x,E):
    y1=y[0]
    y2=y[1]
    yp1=y2                
    yp2=-2*(E-V(x))*y1
    yp=[yp1,yp2]
    return yp

#Boundary Conditions for a wave function
x0,y0,xn,yn=0,0,9,0
n=1000
h=(xn-x0)/n
x=np.arange(x0,xn,h)
L=len(x)
alpha=0.001         #Initial derivative (can be anything as it doesn't control the solution after normalization)
y0=[0.00,alpha]     #Initial condition for y and y' 
      


#Guessing energy value from plot
def shoot(E):
    u=odeint(Morse,y0,x,args=(E,))
    return u[:,0][-1]

energies=np.arange(0,1.5,0.01)
H=[]
for i in energies:
    hits=shoot(i)
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.ylim(-0.01,0.01)
plt.xlim(0,2)
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Inbuilt Function Method/Primitive Method/Python Files/Morse_hits.png')
plt.show()


#Bisection-shooting method for proper choice of energy
while True:
    E1=eval(input('Enter 1st energy guess : '))
    E2=eval(input('Enter 2nd energy guess : '))
    uA=odeint(Morse,y0,x,args=(E1,))
    uB=odeint(Morse,y0,x,args=(E2,))
    solA=uA[:,0]
    solB=uB[:,0]
    if solA[L-1]*solB[L-1]<0.0:
        break
    else:
        print('Incorrect sssumption of guesses\nEnter new guesses')


itr=0
plt.figure(figsize=(11,6)) 
while True:
    u1=odeint(Morse,y0,x,args=(E1,))
    sol1=u1[:,0]
    u2=odeint(Morse,y0,x,args=(E2,))
    sol2=u2[:,0]
    E3=(E1+E2)/2
    u3=odeint(Morse,y0,x,args=(E3,))
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
    N=1/np.sqrt(simpson(sol3*sol3,x=x))
    sol3=N*sol3
    
#Plotting and printing
    plt.subplot(121)
    plt.plot(x,V(x),'--',color='indigo')
    plt.ylabel(r'Potential $V(x)$')
    plt.xlabel('Distance (x) in 1D')
    plt.title('Morse Potential')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    
    plt.subplot(122)
    plt.cla()
    plt.title('Normalised wave function for Morse Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Distance(x) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.grid()
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=xn,color='blue',lw=1)
    plt.axvline(x=x0,color='black',lw=1,ls='--')
    plt.plot(x,sol3,'r',lw=1.5)
    plt.plot(x[-1],u3[-1,0],'o',color='black',ms=5)
    plt.pause(0.5)
    
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Inbuilt Function Method/Primitive Method/Python Files/Morse.png')
plt.show()
print('The energy satisfying the boundary condition is',E3)
        
    
