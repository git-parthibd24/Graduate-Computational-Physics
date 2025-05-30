#Question 1(1)
#Leapfrog method implementation

import numpy as np
import matplotlib.pyplot as plt

def f_x(t,x,v):
    return v

def f_v(t,x,v):
    return v**2-(x+5)

def Leapfrog(funcs,t0,u0,tn,h):
    T=np.arange(t0,tn+h,h)        #This is a fixed step size array
    R=np.zeros((len(T),len(u0)))
    R_half=np.zeros((len(T),len(u0))) 
    R[0]=u0
    R_half[0]=u0+(h/2)*np.array([f(t0,*u0) for f in funcs])    #Euler half-step for position and velocity initialization   

    for i in range(len(T)-1):
        t,u_half,u=T[i],R_half[i],R[i]
        R[i+1]=u+h*np.array([f(t+h/2,*u_half) for f in funcs])
        R_half[i+1]=u_half+h*np.array([f(t+h,*R[i+1]) for f in funcs])

    return T,R[:,0],R[:,1]  

t0,tn,h=0,50,0.001
x0,v0=1,0

functions=[f_x,f_v]
T,X,V=Leapfrog(functions,t0,[x0,v0],tn,h)

plt.plot(T,X,'b-')
plt.xlabel('Time t (s)')
plt.ylabel(r'Position $x(t)$')
plt.title('Solution of IVP using Leapfrog Method')
plt.axhline(color='black',linewidth=1)
plt.axvline(color='black',linewidth=1)
plt.grid()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 10/Python Files/Q1_Leapfrog.png')
plt.show()
