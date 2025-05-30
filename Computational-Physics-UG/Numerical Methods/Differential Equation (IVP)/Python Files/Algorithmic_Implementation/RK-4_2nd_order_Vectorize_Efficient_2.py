#Solution of 2nd order ODE (IVP) by RK-4 Method by vectorization (Better Implementation)-2

import numpy as np
import matplotlib.pyplot as plt

def functions(x,u):
    y,z=u                                                #Unpack  variables
    return np.array([z,6*y-z])               #Return derivatives as a NumPy array

x0=float(input('Enter initial value of x : '))
xn=float(input('Enter desired value of x : '))
y0=float(input('Enter initial value of y : '))
z0=float(input("Enter initial value of y' : "))
h=0.0001

def RK4_system(f,x0,u0,h,xn):
    X=np.arange(x0,10+h,h)
    R=np.zeros((len(X),len(u0)))
    R[0]=u0

    for i in range(len(X)-1):
        x,u=X[i],R[i]
        k1=h*f(x, u)
        k2=h* f(x+h/2,u+k1/ 2)
        k3=h*f(x+h/2,u+k2/2)
        k4=h* f(x+h,u+k3)
        R[i+1]=u+(k1+2*k2+2*k3+k4)/6
    return X,R[:,0],R[:,1]

X,Y,Z=RK4_system(functions,x0,[y0,z0],h,xn)

print('Solution at x =',xn,'is :',format(Y[int((xn-x0)/h)],'0.4f'))

plt.plot(X,Y,color='limegreen',linestyle='-')
plt.xlabel('x-value')
plt.ylabel('Solution y(x)')
plt.title('Solution of 2nd Order ODE using RK-4 Method')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Algorithmic_Implementation/RK_4_2nd_order_Vectorize_Efficient_2.png')
plt.show()
