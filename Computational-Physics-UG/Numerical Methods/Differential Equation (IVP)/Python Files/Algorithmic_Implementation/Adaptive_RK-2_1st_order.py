#Solution of 1st order ODE (IVP) by RK-2 Heun's Method with adaptive approach

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -x*y**2  

x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
xn=eval(input('Enter desired x point : '))
h_initial=0.00001  
tol=1e-8  

def RK2(f,x0,y0,h):
    k1=h*f(x0,y0)
    k2=h*f(x0+h,y0+k1)
    return  y0+0.5*(k1+k2)

def adaptive_RK2(f,x0,y0,xn,h_initial,tol):
    X,Y,h=[x0],[y0],h_initial 
    while x0<=10:
        y_RK2=RK2(f,x0,y0,h)
        y_half=RK2(f,x0,y0,h/2)
        y_adaptive=RK2(f,x0+h/2,y_half,h/2)

        error=np.abs(y_RK2-y_adaptive)
        if error>tol:
            h*=(tol/error)**0.5  
        else:
            x0+=h
            y0=y_adaptive
            X.append(x0)
            Y.append(y0)

    return np.array(X),np.array(Y)

X,Y=adaptive_RK2(f,x0,y0,xn,h_initial,tol)

print('Solution at x =', xn, 'is:', format(Y[int((xn-x0)/h_initial)],'0.4f'))

plt.plot(X, Y, color='gold', linestyle='-')
plt.title("Solution of 1st order ODE using Adaptive RK-2 (Heun's Method)")
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig("/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/Adaptive_RK_2_1st_heun's.png")
plt.show()

