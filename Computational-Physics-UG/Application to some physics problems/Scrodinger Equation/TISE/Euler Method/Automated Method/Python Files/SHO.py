#Solution of Schrodinger's 1D wave equation for Simple Harmonic Oscillator potential
#Euler Mmethod

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(x):
    omega=1
    return x**2/2
    
nodes=int(input('Enter the number of nodes : '))

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
    alpha=0.001        #Initial derivative (can be anything as it doesn't control the solution after normalization)
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


#Bisection method for proper choice of energy
D=eval(input('Enter the maximum energy value : '))
energies=np.arange(0,D,0.1)
H=[]
for i in energies:
    hits=SHO(i)[1][-1]
    H.append(hits)
    
Eigen_Energy=[]
for i in range(1,len(energies)):
    a=np.signbit(H[i-1])
    b=np.signbit(H[i])
    j=i
    if a!=b:
        E1=energies[i-1]
        E2=energies[i]
        itr=0.0
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
        Eigen_Energy.append(E3)

        
#Normalisation of wave function
N=1/np.sqrt(simpson(np.array(SHO(Eigen_Energy[nodes])[1])*np.array(SHO(Eigen_Energy[nodes])[1]),x=SHO(Eigen_Energy[nodes])[0]))
solution=N*np.array(SHO(Eigen_Energy[nodes])[1])

#Plotting and printing
plt.figure(figsize=(11,6)) 
x=np.array(SHO(Eigen_Energy[nodes])[0])
plt.subplot(121)
plt.plot(x,V(x),'--',color='indigo')
plt.ylabel(r'Potential $V(x)$')
plt.xlabel('Distance (x) in 1D')
plt.title('Simple Harmonic Oscillator Potential')
plt.axvline(color='black',lw=1)
plt.axhline(color='black',lw=1)
    
plt.subplot(122)
plt.plot(x,solution,'r',lw=1.5,label=r'$\psi$')
plt.plot(x,solution**2,'g',lw=1.5,label=r'$|\psi|^2$')
plt.plot(x[-1],SHO(Eigen_Energy[nodes])[1][-1],'o',color='black',ms=5)
plt.title('Normalised wave function for Simple Harmonic Oscillator Potential\n'+r'Energy =%9.5f, itr=%2i'%(Eigen_Energy[nodes],itr))
plt.xlabel('Distance(x) in 1D')
plt.ylabel(r'Wave Function ($\psi$)')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.axvline(x=x0,color='black',lw=1,ls='--')
plt.axvline(x=xn,color='blue',lw=1)
plt.grid()
plt.legend(loc='best',prop={'size':10}) 
   
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Euler Method/Automated Method/Python Files/SHO.png')
plt.show()
print('The Eigen-Energy satisfying the boundary condition is',Eigen_Energy[nodes])
        
