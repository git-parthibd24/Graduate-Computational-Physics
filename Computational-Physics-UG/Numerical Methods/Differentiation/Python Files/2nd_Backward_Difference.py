#Backward Difference Approximation for numerical differentiation
#2nd Order

import numpy as np
import matplotlib.pyplot as plt

h=0.0001
def f(x):
    return np.exp(2*x)
def d2f(x):
    return 4*np.exp(2*x)
def back_diff(f,x):
    return  (f(x)-2*f(x-h)+f(x-2*h))/h**2

x_val=np.linspace(-1,2,100)

plt.title('Backward Difference Approach to 2nd order numerical differentiation')
plt.plot(x_val,d2f(x_val),'y-',label='Analytic Result')
plt.plot(x_val[::2],back_diff(f,x_val)[::2],'mo',ms='3',label='Numerical Result')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differentiation/Python Files/Backward_2nd_order.png')
plt.show()
