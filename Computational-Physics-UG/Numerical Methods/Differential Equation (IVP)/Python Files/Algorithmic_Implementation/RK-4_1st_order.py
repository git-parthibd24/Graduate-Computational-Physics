#Solution of 1st order ODE (IVP) by RK-4 Method

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -x*y**2                      #This is dy/dx
    
x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
xn=eval(input('Enter desired x point of evaluation : '))
h=0.00001

def RK_4(f,x,y,xn):
    while x<xn:         #conditional check is slower than prefixed range
        k1=h*f(x,y)
        k2=h*f(x+h/2,y+k1/2)
        k3=h*f(x+h/2,y+k2/2)
        k4=h*f(x+h,y+k3)
        y=y+(1/6)*(k1+2*(k2+k3)+k4)
        x=x+h
    return y
    
print('The solution for the given 1st order ODE at ',x0,'is :',RK_4(f,x0,y0,xn))

x_val=np.linspace(x0,10,1000)
y_val=np.array([RK_4(f,x0,y0,i) for i in x_val])
plt.plot(x_val,y_val,'b-')
plt.title('Solution of 1st order ODE using RK-4 Method ')
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/RK_4_1st_order.png')
plt.show()
