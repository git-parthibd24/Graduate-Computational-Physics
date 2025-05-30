#Solution of 2nd order ODE (IVP) by RK-4 Method

import numpy as np
import matplotlib.pyplot as plt

def f1(x,y,z):
    return z                     #This is dy/dx

def f2(x,y,z):
    return 6*y-z              #This is dz/dx

x0=float(input('Enter initial value of x : '))
xn=float(input('Enter desired value of x : '))
y0=float(input('Enter initial value of y : '))
z0=float(input("Enter initial value of y' : "))
h=0.0001

def RK4_2nd_order(f1,f2,x0,y0,z0):
    X=np.arange(x0,10+h,h)
    Y=np.zeros(len(X))
    Z=np.zeros(len(X))
    Y[0]=y0
    Z[0]=z0    
    for i in range(len(X)-1):
        x,y,z=X[i],Y[i],Z[i]
        
        k1=h*f1(x,y,z)
        l1=h*f2(x,y,z)
        
        k2=h*f1(x+h/2,y+k1/2,z+l1/2)
        l2=h*f2(x+h/2,y+k1/2,z+l1/2)
        
        k3=h*f1(x+h/2,y+k2/2,z+l2/2)
        l3=h*f2(x+h/2,y+k2/2,z+l2/2)
        
        k4=h*f1(x+h,y+k3,z+l3)
        l4=h*f2(x+h,y+k3,z+l3)
        
        Y[i+1]=y+(1/6)*(k1+2*(k2+k3)+k4)
        Z[i+1]=z+(1/6)*(l1+2*(l2+l3)+l4)
    return X,Y

X,Y=RK4_2nd_order(f1,f2,x0,y0,z0)
print('Solution at x =',xn,'is :',format(Y[int((xn-x0)/h)],'0.4f'))

plt.plot(X,Y,color='teal',linestyle='-')
plt.xlabel('x-value')
plt.ylabel('Solution y(x)')
plt.title('Solution of 2nd Order ODE using RK-4 Method')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/RK_4_2nd_order.png')
plt.show()
