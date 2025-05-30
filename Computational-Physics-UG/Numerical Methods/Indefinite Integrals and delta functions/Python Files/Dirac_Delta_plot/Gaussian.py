#Gaussian Function Approximation

import numpy as np
import matplotlib.pyplot as plt

def gaussian_function():
    sigma=float(input('Enter sigma i.e width : '))
    delta=lambda x,sigma,mu:1/(np.sqrt(2*np.pi)*sigma)*np.exp(-((x-mu)**2)/(2*sigma**2))
    mu=float(input('Enter the shifted x-coordinate : '))
    x1,x2=-0.5+mu,0.5+mu
    xval=np.linspace(x1,x2,500)
    n=int(input('Enter no. of functions to generate : '))
    for i in range(1,n+1):
        sigma=sigma/i
        plt.plot(xval,delta(xval,sigma,mu),label="$\sigma=%f$"%sigma)
    plt.title('Delta function as limit of Gaussian function')
    plt.xlabel('X values')
    plt.ylabel(r'$\delta(x-a)$')
    plt.axhline(color='gray')
    plt.axvline(x=mu,color='gray')
    plt.legend()
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Dirac_Delta_plot/Gaussian.png')
    plt.show()
gaussian_function()
