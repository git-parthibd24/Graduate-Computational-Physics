#Solution of 1st order ODE (IVP) by RK-4 Method
#Faster approach by memory allocation

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -x*y**2  

x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
xn=eval(input('Enter final x point : '))
h=0.00001  

def RK_4(f,x0,y0,xn):
    X=np.arange(x0,xn+h,h)  
    Y=np.zeros(len(X))  
    Y[0]=y0
    for i in range(len(X)-1):
        x=X[i]
        y=Y[i]
        k1=h*f(x,y)
        k2=h*f(x+h/2,y+k1/2)
        k3=h*f(x+h/2,y+k2/2)
        k4=h*f(x+h,y+k3)
        Y[i+1]=y+(1/6)*(k1+2*k2+2*k3+k4)
    return X,Y

X,Y=RK_4(f,x0,y0,xn)

plt.plot(X,Y,'r-')
plt.title('Solution of 1st Order ODE using RK-4 Method')
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/RK_4_fast_1st_order.png')
plt.show()
