#Solution of Schrodinger's 1D wave equation for Coulomb potential
#Euler Method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(r):
    return -1/r

nodes=int(input('Enter the number of nodes : '))

#Define the dimensionless Time Independent Schrodinger Equation
def psi(r,y,u,E):
    f=-2*(E/2-V(r))*y
    return f

def phi(r,y,u):
	return u
   
#Boundary conditions for a wave function
#Boundary Conditions for a wave function 
#Large end point to capture many Coulomb Potential states before infinite well states (positive energies) take over when the system actually responds to the finite boundary conditions for higher excited states
#Larger the boundary, more tolerance required for wavefunction to converge
#Larger the boundary, more error accumulates in RK2 Method which shifts all energy levels
r0,y0,rn,yn=1e-5,0,10,0
#r0,y0,rn,yn=1e-12,0,200,0
n=10000


#Modified Euler method with shooting parameter E as energy
def Coulomb(E):
    alpha=0.001       #Initial derivative (can be anything as it doesn't control the solution after normalization)
    r,y,u,R,Y,U=r0,y0,alpha,[r0],[y0],[alpha]
    h=(rn-r0)/n
    for i in range(0,n):   
        y_old=y
        u_old=u
        y=y+h*u
        y_old1=y
        u=u+h*psi(r,y,u,E)
        y=y_old+0.5*h*(phi(r,y_old,u_old)+phi(r+h,y,u))
        u=u_old+0.5*h*(psi(r,y_old,u_old,E)+psi(r+h,y_old1,u,E))
        r=r+h
        R.append(r)
        Y.append(y)
        U.append(u)
    return R,Y,U


#Bisection method for proper choice of energy
#Energies are negative (-1/n**2) with maximum value of -1.0 (scaled system) for the Coulomb Potential
energies=np.arange(-1.2,0,0.002)
H=[]
for i in energies:
    hits=Coulomb(i)[1][-1]
    H.append(hits)

Eigen_Energy=[]
for i in range(1,len(energies)):
    a=np.signbit(H[i-1])
    b=np.signbit(H[i])
    if a!=b:
        E1=energies[i-1]
        E2=energies[i]
        itr=0.0
        while True:
            E3=(E1+E2)/2
            if Coulomb(E3)[1][-1]==0:
                break
            if Coulomb(E1)[1][-1]*Coulomb(E3)[1][-1]>0:
                E1=E3
            else:
                E2=E3
            itr=itr+1
            acc=abs(E1-E2)
            if acc<0.0000000001:
                break
        Eigen_Energy.append(E3)

        
#Normalisation of wave function
N=1/np.sqrt(simpson(np.array(Coulomb(Eigen_Energy[nodes])[1])*np.array(Coulomb(Eigen_Energy[nodes])[1]),x=Coulomb(Eigen_Energy[nodes])[0]))
solution=N*np.array(Coulomb(Eigen_Energy[nodes])[1])

#Plotting and printing
plt.figure(figsize=(11,6)) 
r=np.array(Coulomb(Eigen_Energy[nodes])[0])
plt.subplot(121)
plt.plot(r,V(r),'--',color='indigo')
plt.ylabel(r'Potential $V(r)$')
plt.xlabel('Distance (r) in 1D')
plt.title('Coulomb Potential')
plt.xlim(-0.1,0.7)
plt.ylim(-100,10)
plt.axvline(color='black',lw=1)
plt.axhline(color='black',lw=1)
    
plt.subplot(122)
plt.plot(r,solution,'r',lw=1.5,label=r'$\psi$')
plt.plot(r,solution**2,'g',lw=1.5,label=r'$|\psi|^2$')
plt.plot(r[-1],Coulomb(Eigen_Energy[nodes])[1][-1],'o',color='black',ms=5)
plt.title('Normalised wave function for Coulomb Potential\n'+r'Energy =%9.5f, itr=%2i'%(Eigen_Energy[nodes],itr))
plt.xlabel('Distance(r) in 1D')
plt.ylabel(r'Wave Function ($\psi$)')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.axvline(x=r0,color='black',lw=1,ls='--')
plt.axvline(x=rn,color='blue',lw=1)
plt.grid()
plt.legend(loc='best',prop={'size':10}) 

plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Euler Method/Automated Method/Python Files/Coulomb.png')
plt.show()
print('The Eigen-Energy satisfying the boundary condition is',Eigen_Energy[nodes])
        
