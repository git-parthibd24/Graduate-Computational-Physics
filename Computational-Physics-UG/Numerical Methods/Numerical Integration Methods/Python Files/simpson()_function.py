#Numerical Integration using simpson() of scipy module (simps() function is deprecated in newer versions of scipy)

from scipy.integrate import simpson
import numpy as np

def f(x):
    return x*np.exp(x)

a,b=eval(input('Enter lower and upper limits : '))
n=int(input('Enter no. of subintervals : '))

if n%2==0:
    X=np.linspace(a,b,n)
    result=simpson(f(X),x=X)        #old syntax : result=simps(f(X),X)
    print('The result is :',result)
else:
    print('Not Applicable with odd subinterval')
