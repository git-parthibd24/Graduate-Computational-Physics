#Question 3c
#Evaluation of uncertainity for a given Harmonic Oscillator State

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.legendre import leggauss
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
        
def psi(n,x):
	return 1/np.sqrt(2**n*math.factorial(n)*np.pi**0.5)*np.exp(-x**2/2)*H(n,x)
	
	
node,weight=leggauss(100)
Sum=0.0
n=5
a,b=-10,10
for i in range(100):
    x=node[i]*(b-a)/2+(a+b)/2
    Sum=Sum+weight[i]*(x*psi(n,x))**2    #evaluating the n-point Gaussian quadrature sum by changing x into t
Sum*=(b-a)/2
result=np.sqrt(Sum)

print('The uncertainity for n =',n,'is :',format(result,'0.3f'))   
         
