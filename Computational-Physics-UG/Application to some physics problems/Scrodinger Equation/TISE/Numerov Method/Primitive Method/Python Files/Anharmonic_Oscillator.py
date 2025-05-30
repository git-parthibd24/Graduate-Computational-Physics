#Solution of Schrodinger's 1D wave equation for Anharmonic Oscillator potential
#Numerov Method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(r):
    b=1
    k=1
    return (k*r**2)/2+(b*r**3)/3

   
#Boundary conditions for a wave function
r0,y0,rn,yn=-1.8,0,1.8,0
n=1000
r,h=np.linspace(r0,rn,n,retstep='True')
psi=np.zeros(n)
psi[0],psi[1]=0,0.001

#Numerov method with shooting parameter E as energy
def AHO(E):
    k=2*(E-V(r))            #Parameter from Time Independent Schrodinger Equation
    for i in range(1,n-1):   
       psi[i+1]=(2*(1-(5/12)*h**2*k[i])*psi[i]-(1+(1/12)*h**2*k[i-1])*psi[i-1])/(1+(1/12)*h**2*k[i+1])
    return psi 



#Guessing energy value from plot
energies=np.arange(0,10,0.1)
H=[]
for i in energies:
    hits=AHO(i)[-1]
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Numerov Method/Primitive Method/Python Files/Anharmonic_hits.png')
plt.show()


#Bisection method for proper choice of energy
while True:
    E1=eval(input('Enter the 1st guess of energy : '))
    E2=eval(input('Enter the 2nd guess of energy : '))
    if AHO(E1)[-1]*AHO(E2)[-1]<0:
        break
    print('Energy does not exist between the guesses\nEnter new guesses')

itr=0.0
plt.figure(figsize=(11,6)) 
while True:
    E3=(E1+E2)/2
    if AHO(E3)[-1]==0:
        break
    if AHO(E1)[-1]*AHO(E3)[-1]>0:
        E1=E3
    else:
        E2=E3
    itr=itr+1
    acc=abs(E1-E2)
    if acc<0.00000001:
        break
          
#Normalisation of wave function
    N=1/np.sqrt(simpson(AHO(E3)*AHO(E3),x=r))
    solution=N*AHO(E3)

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
    plt.plot(r,solution,'r',lw=1.5)
    plt.plot(r[-1],AHO(E3)[-1],'o',color='black',ms=5)
    plt.title('Normalised wave function for Anharmonic Oscillator Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Distance(r) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=r0,color='black',lw=1,ls='--')
    plt.axvline(x=rn,color='blue',lw=1)
    plt.grid()
    plt.pause(0.5)


plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Numerov Method/Primitive Method/Python Files/Anharmonic.png')
plt.show()
print('The energy satisfying the boundary condition is',E3)
     
