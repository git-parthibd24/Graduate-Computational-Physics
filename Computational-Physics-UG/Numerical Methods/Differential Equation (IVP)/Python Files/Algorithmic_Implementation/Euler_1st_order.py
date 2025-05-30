#Solution of 1st order ODE (IVP) by Euler's Method

import numpy as np
import matplotlib.pyplot as plt

def fun(x,y):
    return -x*y**2                      #This is dy/dx
    
x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
xn=eval(input('Enter desired x point of evaluation : '))
h=0.00001

def euler(fun,x,y,xn):
    while x<xn:
        y=y+h*fun(x,y)
        x=x+h
    return y
    
print('The solution for the given 1st order ODE at ',x0,'is :',euler(fun,x0,y0,xn))

x_val=np.linspace(x0,10,1000)
y_val=np.array([euler(fun,x0,y0,i) for i in x_val])
plt.plot(x_val,y_val,'g-')
plt.title('Solution of 1st order ODE using Eulers Method ')
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/Euler_1st_order.png')
plt.show()
