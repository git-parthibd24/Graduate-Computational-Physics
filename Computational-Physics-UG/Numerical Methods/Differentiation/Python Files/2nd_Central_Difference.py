#Central Difference Approximation for numerical differentiation
#2nd Order

import numpy as np
import matplotlib.pyplot as plt

h=0.0001
def f(x):
    return np.sin(x)
def d2f(x):
    return -np.sin(x)
def cen_diff(f,x):
    return 4*(f(x+h/2)-2*f(x)+f(x-h/2))/h**2

x_val=np.linspace(-2*np.pi,2*np.pi,100)

plt.title('Central Difference Approach to 2nd order numerical differentiation')
plt.plot(x_val,d2f(x_val),'r-',label='Analytic Result')
plt.plot(x_val[::2],cen_diff(f,x_val)[::2],'bo',ms='3',label='Numerical Result')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differentiation/Python Files/Central_2nd_order.png')
plt.show()
