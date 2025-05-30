#Lorenzian Function Approximation

import matplotlib.pyplot as plt
import numpy as np

def lorenzian_function():
    gamma=eval(input('Enter the width of Lorentzian : '))
    a=eval(input('Enter the shifted x-coordinate : '))
    delta=lambda x,gamma:1/np.pi*(gamma/2)/((x-a)**2+(gamma/2)**2)
    x1,x2=-2.5+a,2.5+a
    xval=np.linspace(x1,x2,500)
    n=int(input('Enter no. of functions to generate: '))
    for i in range(1,n+1):
        gamma=gamma/i
        plt.plot(xval,delta(xval,gamma),label="$\gamma=%f$"%(gamma))
    plt.title('Lorentzian Function Approximation')
    plt.xlabel('X values')
    plt.ylabel(r'$\delta(x-a)$')
    plt.axhline(color='gray')
    plt.axvline(x=a,color='gray')
    plt.legend()
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Dirac_Delta_plot/Lorenzian.png') 
    plt.show()
lorenzian_function()
