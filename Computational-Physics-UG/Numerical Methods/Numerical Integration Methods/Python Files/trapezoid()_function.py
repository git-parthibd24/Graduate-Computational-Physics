#Numerical Integration using trapezoid() of scipy module  (trapz() function is deprecated in newer versions of scipy)

from scipy.integrate import trapezoid
import numpy as np

def f(x):
    return x*np.exp(x)

a,b=eval(input('Enter lower and upper limits : '))
n=int(input('Enter no. of subintervals : '))
X=np.linspace(a,b,n)
result=trapezoid(f(X),X)
print('The result is :',result)