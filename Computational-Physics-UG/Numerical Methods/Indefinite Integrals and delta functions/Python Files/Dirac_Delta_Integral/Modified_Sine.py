#Modified Sine Function Approximation

import numpy as np
from scipy.integrate import simpson

def f(x):return x**3-x+1

delta=lambda x,eps:(np.sin((1+2/eps)*x/2))/np.sin(x/2)*1/(2*np.pi) if x!=0 else (0.5+1/eps)/np.pi
delta=np.vectorize(delta)

a=eval(input('Enter the shifted x-coordinate : '))
eps=eval(input('Enter the value of eps : '))
xp=np.linspace(a-100*eps,a+100*eps,1000)

I=simpson(f(xp)*delta(xp-a,eps),xp)
Fun=f(a)
print('Value of Integration for product :',format(I,'0.7f'))
print('Value of the function at peak :',format(Fun,'0.7f'))
if round(I/Fun)==1:
    print('The property of Dirac Delta Function is verified')
else:
    print('The property of Delta Function is not verified')
