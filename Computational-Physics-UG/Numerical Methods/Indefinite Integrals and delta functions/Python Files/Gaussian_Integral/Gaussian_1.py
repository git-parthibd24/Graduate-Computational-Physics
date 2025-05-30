#To check the similarity with defined Gaussian Integral by numerically evaluating Gausssian integral
#Using boolean while loop and quad()

import numpy as np
from scipy.integrate import quad
a,b,c=eval(input('Enter values of a,b,c : '))
up=eval(input('Enter upper limit : '))
low=-up
f=lambda x:np.exp(-a*x**2+b*x+c)
tol=1e-10
IO,err=quad(f,low,up)
while True:
    I=IO
    up=up+1
    low=low-1
    IO,err=quad(f,low,up)
    if abs(IO-I)<tol:
        break
Iexact=np.sqrt(np.pi/a)*np.exp((b**2)/(4*a)+c)
print('The value of integral of Gaussian Function :',IO,'and the exact value is :',Iexact)
if round(IO/Iexact)==1:
    print('The Gaussian Functon is same as the given function with ratio of 1')
else:
    print('Gaussian function is not same to the given function')
