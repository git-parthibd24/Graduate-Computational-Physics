#Question 2
#Lagrange's Interpolation

import numpy as np

f=lambda x : np.sin(x)
X=np.linspace(0,np.pi,5)
Y=f(X)

def L(i,x0):
    product=1.0
    for j in range(len(X)):
        if i!=j:
            product*=(x0-X[j])/(X[i]-X[j])
            
    return product

def y_interpolate(x0):
    Sum=0.0
    for i in range(len(X)):
        product=L(i,x0)
        Sum+=product*Y[i]

    return Sum

def test_error():
    for i in X:
        error=abs(y_interpolate(i)-f(i))
        print('The difference between actual value and interpolated value corresponding to',i,'is',format(error,'0.4f'))

    return

x0=eval(input('Enter the interpolating point : '))
print('The value of the function at x =',x0,'is :',format(y_interpolate(x0),'0.4f'))
print()
test_error()
