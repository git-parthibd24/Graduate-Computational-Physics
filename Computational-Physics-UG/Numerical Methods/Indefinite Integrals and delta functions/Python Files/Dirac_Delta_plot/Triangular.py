#Triangular Function Approximation

import numpy as np
import matplotlib.pyplot as plt
def triangular_function():
    delta=lambda x,eps:(1-abs(x)/eps)/eps if -eps<x<eps else 0
    a=float(input('Enter the shifted x-coordinate : '))
    x1,x2=-0.5+a,0.5+a
    xval=np.linspace(x1,x2,1000)
    delta=np.vectorize(delta)
    eps=0.1
    n=int(input('Enter no. of functions to generate : '))
    for i in range(1,n+1):
        eps=eps/i
        plt.plot(xval,delta(xval-a,eps),label="$\epsilon=%f$"%eps)
    plt.title('Delta function as limit of Triangular function')
    plt.xlabel('X values')
    plt.ylabel(r'$\delta(x-a)$')
    plt.axhline(color='gray')
    plt.axvline(x=a,color='gray')
    plt.ylim(-70,70)
    plt.legend()
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Dirac_Delta_plot/Triangular.png')
    plt.show()
triangular_function()
