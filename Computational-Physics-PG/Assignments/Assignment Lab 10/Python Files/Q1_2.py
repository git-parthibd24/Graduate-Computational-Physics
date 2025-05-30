#Question 1(2)
#Verlet method implementation

import numpy as np
import matplotlib.pyplot as plt

def f_x(t,x,v):
    return v  

def f_v(t,x,v):
    return v**2-(x+5)  

def Verlet(funcs,t0,u0,tn,h):
    T=np.arange(t0,tn+h,h)
    X=np.zeros(len(T))
    V=np.zeros(len(T))
    V_half=np.zeros(len(T))
    X[0],V[0]=u0
    V_half[0]=V[0]+0.5*h*f_v(t0,*u0)  #Initialization of half-step 
    
    for i in range(len(T)-1):
        t=T[i]
        
        #Position update using half-step velocity
        X[i+1]=X[i]+h*f_x(t+h/2,X[i],V_half[i])  
        
        #Velocity update
        V[i+1]=V_half[i]+0.5*h*f_v(t+h,X[i+1],V_half[i])  
        
        #Next half-step velocity update
        V_half[i+1]=V_half[i]+h*f_v(t+h,X[i+1],V[i+1])  
    
    return T,X,V

t0,tn,h=0,50,0.001
x0,v0=1,0

functions=[f_x,f_v]
T,X,V=Verlet(functions,t0,[x0,v0],tn,h)

plt.plot(T,X,'r-')
plt.xlabel('Time t (s)')
plt.ylabel(r'Position $x(t)$')
plt.title('Solution of IVP using Verlet Method')
plt.axhline(color='black',linewidth=1)
plt.axvline(color='black',linewidth=1)
plt.grid()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 10/Python Files/Q1_Verlet.png')
plt.show()
