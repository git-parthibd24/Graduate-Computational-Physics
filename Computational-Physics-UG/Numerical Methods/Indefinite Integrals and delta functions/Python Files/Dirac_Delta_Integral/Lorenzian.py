#Lorenzian Function Approximation

import numpy as np
from scipy.integrate import simpson

def f(x):
    return x**3-x+1    

gamma=eval(input('Enter the width of Lorentzian : '))
a=eval(input('Enter the shifted x-coordinate : '))

delta=lambda x,gamma:1/np.pi*(gamma/2)/((xp-a)**2+(gamma/2)**2)

xp=np.linspace(a-gamma*10,a+gamma*10,1000)
I=simpson(f(xp)*delta(xp-a,gamma),xp)
Fun=f(a)

print('Value of Integration for product :',format(I,'0.7f'))
print('Value of the function at peak :',format(Fun,'0.7f'))

if round(I/Fun)==1:
    print('The property of Dirac Delta Function is verified')
else:
    print('The property of Delta Function is not verified')
