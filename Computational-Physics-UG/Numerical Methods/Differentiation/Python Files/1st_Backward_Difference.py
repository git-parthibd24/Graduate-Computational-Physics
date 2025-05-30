#Backward Difference Approximation for numerical differentiation
#1st Order

import numpy as np
import matplotlib.pyplot as plt

h=0.0001
def f(x):
    return np.sin(x)**2
def df(x):
    return 2*np.sin(x)*np.cos(x)
def back_diff(f,x):
    return (f(x)-f(x-h))/h

x_val=np.linspace(-2*np.pi,2*np.pi,100)

plt.title('Backward Difference Approach to 1st order numerical differentiation')
plt.plot(x_val,df(x_val),'c-',label='Analytic Result')
plt.plot(x_val[::2],back_diff(f,x_val)[::2],'mo',ms='3',label='Numerical Result')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differentiation/Python Files/Backward_1st_order.png')
plt.show()
