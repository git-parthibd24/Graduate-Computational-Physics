#Solution of Schrodinger's 1D wave equation for Coulomb potential
#Numerov Method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


#Define the dimensionless potential
def V(r):
    return -1/r

nodes=int(input('Enter the number of nodes : '))     
    
#Boundary conditions for a wave function
#Large end point to capture many Coulomb Potential states before infinite well states (positive energies) take over when the system actually responds to the finite boundary conditions for higher excited states
#Larger the boundary, more tolerance required for wavefunction to converge
r0,y0,rn,yn=1e-7,0,15,0
#r0,y0,rn,yn=1e-12,0,200,0
n=10000
r,h=np.linspace(r0,rn,n,retstep=True)
psi=np.zeros(n)
psi[0],psi[1]=0,0.001

#Numerov method with shooting parameter E as energy
def Coulomb(E):
    k=2*(E/2-V(r))            #Parameter from Time Independent Schrodinger Equation
    for i in range(1,n-1):   
       psi[i+1]=(2*(1-(5/12)*h**2*k[i])*psi[i]-(1+(1/12)*h**2*k[i-1])*psi[i-1])/(1+(1/12)*h**2*k[i+1])
    return psi 



#Bisection method for proper choice of energy
#Energies are negative (-1/n**2) with maximum value of -1.0 (scaled system) for the Coulomb Potential
energies=np.arange(-1.2,0,0.002)
H=[]
for i in energies:
    hits=Coulomb(i)[-1]
    H.append(hits)

plt.figure(figsize=(11,6))
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
            if Coulomb(E3)[-1]==0:
                break
            if Coulomb(E1)[-1]*Coulomb(E3)[-1]>0:
                E1=E3
            else:
                E2=E3
            itr=itr+1
            acc=abs(E1-E2)
            if acc<0.00000001:
                break
        Eigen_Energy.append(E3)

        
#Normalisation of wave function
N=1/np.sqrt(simpson(Coulomb(Eigen_Energy[nodes])*Coulomb(Eigen_Energy[nodes]),x=r))
solution=N*Coulomb(Eigen_Energy[nodes])

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
plt.plot(r,solution,'r',lw=1.5,label=r'$\psi$')
plt.plot(r,solution**2,'g',lw=1.5,label=r'$|\psi|^2$')
plt.plot(r[-1],Coulomb(Eigen_Energy[nodes])[-1],'o',color='black',ms=5)
plt.title('Normalised wave function for Coulomb Potential\n'+r'Energy =%9.5f, itr=%2i'%(Eigen_Energy[nodes],itr))
plt.xlabel('Distance(r) in 1D')
plt.ylabel(r'Wave Function ($\psi$)')
plt.axhline(color='black',lw=1)
plt.axvline(color='black',lw=1)
plt.axvline(x=r0,color='black',lw=1,ls='--')
plt.axvline(x=rn,color='blue',lw=1)
plt.grid()
plt.legend(loc='best',prop={'size':10}) 

plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-UG/Application to some physics problems/Scrodinger Equation/TISE/Numerov Method/Automated Method/Python Files/Coulomb.png') 
plt.show()
print('The Eigen-Energy satisfying the boundary condition is',Eigen_Energy[nodes])
     
