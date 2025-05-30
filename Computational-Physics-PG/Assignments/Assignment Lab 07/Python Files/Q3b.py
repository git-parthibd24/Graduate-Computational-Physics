#Question 3b
#Plot of Harmonic Oscillator Wavefunctions using user defined Hermite Polynomial

import matplotlib.pyplot as plt
import numpy as np
import math


def H(n,x):     #Computing Hermite polynomial H_n(x) using its recurrence relation but through iteration
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        H0,H1=1,2*x                                                            #Base cases
        for k in range(2,n+1):
            Hn=2*x*H1-2*(k-1)*H0
            H0,H1=H1,Hn  
        return Hn
        
x=np.linspace(-10,10,10000)
def psi(n,x):
	return 1/np.sqrt(2**n*math.factorial(n)*np.pi**0.5)*np.exp(-x**2/2)*H(n,x)

plt.plot(x,psi(30,x),'red',label='n=30 state')
plt.legend()
plt.axvline(x=0,color='black',linestyle='--',linewidth='0.5')
plt.axhline(y=0,color='black',linestyle='--',linewidth='0.5')
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')
plt.title('Plot of scaled harmonic oscillator wavefunctions')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 07/Python Files/SHO_30.png')
plt.show()
