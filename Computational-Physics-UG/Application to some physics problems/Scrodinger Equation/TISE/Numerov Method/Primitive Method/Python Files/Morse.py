#Solution of Schrodinger's 1D wave equation for Morse potential
#Numerov Method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(x):
    D=1
    b=1
    return D*(1-np.exp(-(x-b)))**2 

   
#Boundary conditions for a wave function
x0,y0,xn,yn=0,0,10,0
n=1000
x,h=np.linspace(x0,xn,n,retstep='True')
psi=np.zeros(n)
psi[0],psi[1]=0,0.001

#Numerov method with shooting parameter E as energy
def Morse(E):
    k=2*(E-V(x))            #Parameter from Time Independent Schrodinger Equation
    for i in range(1,n-1):   
       psi[i+1]=(2*(1-(5/12)*h**2*k[i])*psi[i]-(1+(1/12)*h**2*k[i-1])*psi[i-1])/(1+(1/12)*h**2*k[i+1])
    return psi 



#Guessing energy value from plot
energies=np.arange(0,1.5,0.01)
H=[]
for i in energies:
    hits=Morse(i)[-1]
    H.append(hits)
    
plt.plot(energies,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.ylim(-1.2,1.2)
plt.xlim(0,3)
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Numerov Method/Primitive Method/Python Files/Morse_hits.png')
plt.show()



#Bisection method for proper choice of energy
while True:
    E1=eval(input('Enter the 1st guess of energy : '))
    E2=eval(input('Enter the 2nd guess of energy : '))
    if Morse(E1)[-1]*Morse(E2)[-1]<0:
        break
    print('Energy does not exist between the guesses\nEnter new guesses')

itr=0.0
plt.figure(figsize=(11,6)) 
while True:
    E3=(E1+E2)/2
    if Morse(E3)[-1]==0:
        break
    if Morse(E1)[-1]*Morse(E3)[-1]>0:
        E1=E3
    else:
        E2=E3
    itr=itr+1
    acc=abs(E1-E2)
    if acc<0.00000001:
        break
          
#Normalisation of wave function
    N=1/np.sqrt(simpson(Morse(E3)*Morse(E3),x=x))
    solution=N*Morse(E3)

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
    plt.plot(x,solution,'r',lw=1.5)
    plt.plot(x[-1],Morse(E3)[-1],'o',color='black',ms=5)
    plt.title('Normalised wave function for Morse Potential\n'+r'Energy =%9.5f, itr=%2i'%(E3,itr))
    plt.xlabel('Distance(x) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=x0,color='black',lw=1,ls='--')
    plt.axvline(x=xn,color='blue',lw=1)
    plt.grid()
    plt.pause(0.5)

plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Numerov Method/Primitive Method/Python Files/Morse.png')
plt.show()
print('The energy satisfying the boundary condition is',E3)
     
