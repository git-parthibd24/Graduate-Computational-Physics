#Question 4
#Solution to Lorentz Equations

import numpy as np
import matplotlib.pyplot as plt

def fx(t,x,y,z):
    return sig*(y-x) 

def fy(t,x,y,z):
    return r*x-y-x*z

def fz(t,x,y,z):
    return x*y-b*z

functions=[fx,fy,fz]

h=0.0001
def RK_4(func,t0,u0,tn,h):
    T=np.arange(t0,tn+h,h)
    R=np.zeros((len(T),len(u0)))
    R[0]=u0
    for i in range(len(T)-1):
        t,u=T[i],R[i]
        k1=h*np.array([f(t,*u) for f in func])
        k2=h*np.array([f(t+h/2,*u+k1/2) for f in func])
        k3=h*np.array([f(t+h/2,*u+k2/2) for f in func])
        k4=h*np.array([f(t+h,*u+k3) for f in func])
        R[i+1]=u+(k1+2*k2+2*k3+k4)/6
    return T,R[:,0],R[:,1],R[:,2]

sig,r,b=10,28,8/3         #Given choice of parameters
t0,x0,y0,z0=0,0,1,0     #Initial conditions
tn=50

T,X,Y,Z=RK_4(functions,t0,[x0,y0,z0],tn,h)

plt.figure()
plt.plot(T,Y,'r-',label='y plot')
plt.ylabel('Solution to Lorentz Equations')
plt.xlabel('Time')
plt.axhline(color='black')
plt.axvline(color='black')
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 08/Python Files/Q4_1.png')

plt.figure()
plt.plot(X,Z,'g-')
plt.title('Solution to Lorentz Equations')
plt.ylabel('z value')
plt.xlabel('x value')
plt.axhline(color='black')
plt.axvline(color='black')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 08/Python Files/Q4_2.png')
plt.show()
