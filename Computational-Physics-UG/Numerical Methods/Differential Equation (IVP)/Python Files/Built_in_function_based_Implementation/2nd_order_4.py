#Solving 2nd order ODE using odeint()
#Example 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(u,x):                                          #odeint() creates array like object u which must contain the function and its derivattive in it
    y1,y2=u
    dy1dx1=y2                                             #1st derivative
    dy2dx2=(-b/m)*x-(g/l)*np.sin(x)             #2nd derivative
    list=[dy1dx1,dy2dx2]                             #Packed in a list
    return list
 
b,g,l,m=0.02,9.81,1,0.1
u0=[0,5]                                                     #Initial values of y1 and dy1dx1 packed in list
xrange=np.linspace(0,10,150)
sol=odeint(model,u0,xrange)
plt.title('Solution of the differential equation')
plt.xlabel('x-values')
plt.ylabel("y=f(x) and y'=f'(x)")
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.plot(xrange,sol[:,0],'g--',label='Solution')
plt.plot(xrange,sol[:,1],'r--',label='Derivative')
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Built_in_function_based_Implementation/2nd_order_4.png')
plt.show()
