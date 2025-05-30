#Rectangular Function Approximation

import matplotlib.pyplot as plt
import numpy as np

def rectangular_function():
    delta=lambda x,eps:1/eps if -eps/2<x<eps/2 else 0
    a=float(input('Enter the shifted x-coordinate : '))
    x1,x2=-0.2+a,0.2+a
    xval=np.linspace(x1,x2,500)
    delta=np.vectorize(delta)
    eps=0.1
    n=int(input('Enter no. of functions to generate : '))
    for i in range(1,n+1):
        eps=eps/i
        plt.plot(xval,delta(xval-a,eps),label="$\epsilon=%f$"%eps)
    plt.title('Delta function as limit of Rectangular function')
    plt.xlabel('X values')
    plt.ylabel(r'$\delta(x-a)$')
    plt.axhline(color='gray')
    plt.axvline(x=a,color='gray')
    plt.ylim(-70,70)
    plt.legend()
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Dirac_Delta_plot/Rectangular.png') 
    plt.show()
rectangular_function()
