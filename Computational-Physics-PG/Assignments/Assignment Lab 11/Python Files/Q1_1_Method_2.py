#Question 1 (1) (Without scaling)
#Solution of Schrodinger's 1D wave equation for Simple Harmonic Oscillator Potential
#Use linspace to avoid appropriate choice of interval

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

#Parameters and boundary conditions for a wave function
m=9.1*10**(-31)
hbar=1.054*10**(-34)
V0=50*1.602*10**(-19)
eV=1.602*10**(-19)
a=1e-11
x0,y0,xn,yn=-10*a,0,10*a,0

#Define the potential
def V(x):
    return V0*(x/a)**2

#Define the Time Independent Schrodinger Equation
def psi(x,y,z,E):
    return -2*(m/hbar**2)*(E-V(x))*y

def phi(x,y,z,E):
	return z
   

funcs=[phi,psi]
u0=[y0,0.001]
h=(xn-x0)/1000
def SHO(E):
    X=np.linspace(x0,xn,1000)
    R=np.zeros((len(X),len(u0)))
    R[0]=u0                                             

    for i in range(len(X)-1):
        x,u=X[i],R[i]
        k1=h*np.array([f(x,*u,E) for f in funcs])             
        k2=h*np.array([f(x+h/2,*(u+k1/2),E) for f in funcs])
        k3=h*np.array([f(x+h/2,*(u+k2/2),E) for f in funcs])
        k4=h*np.array([f(x+h,*(u+k3),E) for f in funcs])
        R[i+1]=R[i]+(1/6)*(k1+2*(k2+k3)+k4)
    return X,R[:,0],R[:,1],R[-1,0]-yn


#Guessing energy value from plot
energies=np.linspace(100*eV,2000*eV,100)
H=[]
for i in energies:
    hits=SHO(i)[-1]
    H.append(hits)
    
plt.plot(energies/eV,H,'b-')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.xlabel('Energy')
plt.ylabel('End-point')
plt.ylim(-0.002,0.003)
plt.minorticks_on()
plt.grid(which='minor',color='green',ls='--')
plt.show()

#Bisection method for proper choice of energy
def bisect(E1,E2):
    while True:
        E3=(E1+E2)/2
        if SHO(E3)[-1]==0:
            break
        if SHO(E1)[-1]*SHO(E3)[-1]>0:
            E1=E3
        else:
            E2=E3
        acc=abs(E1-E2)
        if acc<10e-28:
            break
      
    #Normalisation of wave function
    N=1/np.sqrt(simpson(SHO(E3)[1]*SHO(E3)[1],x=SHO(E3)[0]))
    solution=N*SHO(E3)[1]

    plt.plot(SHO(E3)[0],solution,'r',lw=1.5)
    plt.title('Normalised wave function for Simple Harmonic Oscillator Potential')
    plt.xlabel('Distance(x) in 1D')
    plt.ylabel(r'Wave Function ($\psi$)')
    plt.axhline(color='black',lw=1)
    plt.axvline(color='black',lw=1)
    plt.axvline(x=x0,color='black',lw=1,ls='--')
    plt.axvline(x=xn,color='blue',lw=1)
    plt.grid()   
    plt.show()
    return E3
       
print('The ground state energy is',bisect(120*eV,250*eV)/eV,'eV')
print('The 1st excited state energy is',bisect(250*eV,500*eV)/eV,'eV')
print('The 2nd excited state energy is',bisect(500*eV,750*eV)/eV,'eV')
