#Gaussian Function Approximation

import numpy as np
from scipy.integrate import simpson

def f(x):
    return x**3-x+1    

sigma=eval(input('Enter sigma (width) : '))
mu=eval(input('Enter the shifted x-coordinate : '))

delta=lambda x:1/(np.sqrt(2*np.pi)*sigma)*np.exp(-((x-mu)**2)/(2*sigma**2))

xp=np.linspace(mu-100*sigma,mu+100*sigma,1000)
I=simpson(f(xp)*delta(xp),xp)
Fun=f(mu)

print('Value of Integration for product :',format(I,'0.7f'))
print('Value of the function at peak :',format(Fun,'0.7f'))

if round(I/Fun)==1:
    print('The property of Dirac Delta Function is verified')
else:
    print('The property of Delta Function is not verified')
