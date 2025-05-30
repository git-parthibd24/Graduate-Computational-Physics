#Solution of 1st order ODE (IVP) by Modified Euler's Method

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -x*y**2  

x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
xn=eval(input('Enter desired x point : '))
h=0.00001  

def mod_eul(f,x0,y0):
    X=np.arange(x0,10+h,h)  
    Y=np.zeros(len(X))  
    Y[0]=y0
    for i in range(len(X)-1):
        x,y=X[i],Y[i]
        y_eul=y+h*f(x,y)                                            #1st order prediction using Euler's Method
        Y[i+1]=y+0.5*h*(f(x,y)+f(x+h,y_eul))           #2nd order correction using RK-2 Heun's Method
        while True:
            y_old=Y[i+1]
            Y[i+1]=y+0.5*h*(f(x,y)+f(x+h,y_eul))       #refining the correction
            if abs(y_old-Y[i+1])<0.0001:
                break
    return X,Y

X,Y=mod_eul(f,x0,y0)
print('Solution at x =',xn,'is :',format(Y[int((xn-x0)/h)],'0.4f'))

plt.plot(X,Y,color='indigo',linestyle='-')
plt.title("Solution of 1st Order ODE using Modified Euler's Method")
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig("/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/Modified_Euler_1st_order.png")
plt.show()
