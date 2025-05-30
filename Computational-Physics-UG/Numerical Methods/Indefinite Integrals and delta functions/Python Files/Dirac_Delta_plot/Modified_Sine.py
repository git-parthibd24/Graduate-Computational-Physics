#Modified Sine Function Approximation

import matplotlib.pyplot as plt
import numpy as np

def modified_sine_function():
    delta=lambda x,eps:(np.sin((1+2/eps)*x/2))/np.sin(x/2)*1/(2*np.pi)
    a=eval(input('Enter the shifted x-coordinate : '))
    eps=1.0
    x1,x2=-0.5+a,0.5+a
    xval=np.linspace(x1,x2,500)
    n=int(input('Enter no. of functions to generate : '))
    for i in range(1,n+1):
        eps=eps/i
        plt.plot(xval,delta(-a+xval,eps),label="$\epsilon=%f$"%(eps))
    plt.title('Modified Sine Function Approximation')
    plt.xlabel('X values')
    plt.ylabel(r'$\delta(x-a)$')
    plt.axhline(color='gray')
    plt.axvline(x=a,color='gray')
    plt.legend()
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Dirac_Delta_plot/Modified_Sine.png') 
    plt.show()
modified_sine_function()
