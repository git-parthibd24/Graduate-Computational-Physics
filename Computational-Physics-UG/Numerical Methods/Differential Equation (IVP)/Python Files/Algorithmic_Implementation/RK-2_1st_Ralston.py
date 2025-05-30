#Solution of 1st order ODE (IVP) by RK-2 Ralston Method

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -x*y**2  

x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
xn=eval(input('Enter desired x point : '))
h=0.00001  

def RK_2(f,x0,y0):
    X=np.arange(x0,10+h,h)  
    Y=np.zeros(len(X))  
    Y[0]=y0
    for i in range(len(X)-1):
        x,y=X[i],Y[i]
        k1=h*f(x,y)
        k2=h*f(x+3*h/4,y+3*k1/4)              #k2=h*f((x0+3x1)/4,(y0+3y1)/4) where x1=x0+h, y1=y0+k1=y0+h*f(x0,y0)
        Y[i+1]=y+(1/3)*k1+(2/3)*k2
    return X,Y

X,Y=RK_2(f,x0,y0)
print('Solution at x =',xn,'is :',format(Y[int((xn-x0)/h)],'0.4f'))

plt.plot(X,Y,color='olive',linestyle='-')
plt.title('Solution of 1st Order ODE using RK-2 Ralston Method')
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/RK_2_1st_ralston.png')
plt.show()
