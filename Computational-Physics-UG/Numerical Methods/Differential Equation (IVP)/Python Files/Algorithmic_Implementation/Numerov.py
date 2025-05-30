#Solution of 1st order ODE (IVP) by Numerov Method
#Differential equation has to be of form y"(x)=k(x)y(x)

import numpy as np
import matplotlib.pyplot as plt

def fy(x,y,z):
    return z                                                  #This is dy/dx

def k(x):
    return -x

def fz(x,y):
    return k(x)*y                                         #This is dz/dx

x0=eval(input('Enter initial x point : '))
y0=eval(input('Enter initial y point : '))
z0=eval(input("Enter initial y' point : "))
xn=eval(input('Enter desired x point : '))
h=0.00001  

def numerov(fy,k,x0,y0,z0):
    X=np.arange(x0,10+h,h)
    K=k(X)
    Y=np.zeros(len(X))  
    Y[0]=y0
    Y[1]=y0+h*fy(x0,y0,z0)
    for i in range(1,len(X)-1):
        Y[i+1]=(2*(1+(5/12)*h**2*K[i])*Y[i]-(1-(1/12)*h**2*K[i-1])*Y[i-1])/(1-(1/12)*h**2*K[i+1])
    return X,Y

X,Y=numerov(fy,k,x0,y0,z0)
print('Solution at x =',xn,'is :',format(Y[int((xn-x0)/h)],'0.4f'))

plt.plot(X,Y,color='deepskyblue',linestyle='-')
plt.title("Solution of 2nd Order ODE using Numerov Method")
plt.xlabel('x-value')
plt.ylabel('Solution f(x)')
plt.savefig("/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/Numerov.png")
plt.show()
