#Central Difference Approximation for numerical differentiation
#1st Order

import numpy as np
import matplotlib.pyplot as plt

h=0.0001
def f(x):
    return 1+0.5*(np.exp(2*x)-np.exp(-2*x))/(np.exp(2*x)+np.exp(-2*x))
def df(x):
    return 4/(np.exp(2*x)+np.exp(-2*x))**2
def cen_diff(f,x):
    return (f(x+h/2)-f(x-h/2))/h

x_val=np.linspace(-2,2,100)

plt.title('Central Difference Approach to 1st order numerical differentiation')
plt.plot(x_val,df(x_val),'r-',label='Analytic Result')
plt.plot(x_val[::2],cen_diff(f,x_val)[::2],'bo',ms='3',label='Numerical Result')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differentiation/Python Files/Central_1st_order.png')
plt.show()
