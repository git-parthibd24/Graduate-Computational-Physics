#Solution of 2nd order ODE (IVP) by RK-4 Method by vectorization

import numpy as np
import matplotlib.pyplot as plt

def f1(x,y,z):
    return z

def f2(x,y,z):
    return 6*y-z

x0=float(input('Enter initial value of x : '))
xn=float(input('Enter desired value of x : '))
y0=float(input('Enter initial value of y : '))
z0=float(input("Enter initial value of y' : "))
h=0.0001

def RK4_2nd_order(f1,f2,x0,y0,z0):
    X=np.arange(x0,10+h,h)
    R=np.zeros((len(X),2))
    R[0,0],R[0,1]=y0,z0
    
    for i in range(len(X)-1):
        x,y,z=X[i],R[i,0],R[i,1]
        k1=h*np.array([f1(x,y,z),f2(x,y,z)])
        k2=h*np.array([f1(x+h/2,y+k1[0]/2,z+k1[1]/2),f2(x+h/2,y+k1[0]/2,z+k1[1]/2)])
        k3=h*np.array([f1(x+h/2,y+k2[0]/2,z+k2[1]/2),f2(x+h/2,y+k2[0]/2,z+k2[1]/2)])
        k4=h*np.array([f1(x+h,y+k3[0],z+k3[1]),f2(x+h,y+k3[0],z+k3[1])])
        R[i+1]=R[i]+(1/6)*(k1+2*(k2+k3)+k4)
    return X,R[:,0]

X,Y=RK4_2nd_order(f1,f2,x0,y0,z0)
print('Solution at x=',xn,'is :',format(Y[int((xn-x0)/h)],'0.4f'))

plt.plot(X,Y,color='deepskyblue',linestyle='-')
plt.xlabel('x-value')
plt.ylabel('Solution y(x)')
plt.title('Solution of 2nd Order ODE using RK-4 Method')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/RK_4_2nd_order_Vectorize.png')
plt.show()

