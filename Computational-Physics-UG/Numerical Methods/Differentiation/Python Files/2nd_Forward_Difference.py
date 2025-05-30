#Forward Difference Approximation for numerical differentiation
#2nd Order

import numpy as np
import matplotlib.pyplot as plt

h=0.0001
def f(x):
    return x**3+2*x**2-5*x+3
def d2f(x):
    return 6*x+4
def for_diff(f,x):
    return (f(x+2*h)-2*f(x + h)+f(x))/ h**2

x_val=np.linspace(-2*np.pi,2*np.pi,100)

plt.title('Forward Difference Approach to 2nd order numerical differentiation')
plt.plot(x_val,d2f(x_val),'b-',label='Analytic Result')
plt.plot(x_val[::2],for_diff(f,x_val)[::2],'go',ms='3',label='Numerical Result')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differentiation/Python Files/Forward_2nd_order.png')
plt.show()
