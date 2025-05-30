#Forward Difference Approximation for numerical differentiation
#1st Order

import numpy as np
import matplotlib.pyplot as plt

h=0.0001
def f(x):
    return np.sin(x)
def df(x):
    return np.cos(x)
def for_diff(f,x):
    return (f(x+h)-f(x))/h

x_val=np.linspace(-2*np.pi,2*np.pi,100)

plt.title('Forward Difference Approach to 1st order numerical differentiation')
plt.plot(x_val,df(x_val),'g-',label='Analytic Result')
plt.plot(x_val[::2],for_diff(f,x_val)[::2],'yo',ms='3',label='Numerical Result')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differentiation/Python Files/Forward_1st_order.png')
plt.show()
