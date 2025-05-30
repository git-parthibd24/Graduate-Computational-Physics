#Question 2
#Solution of drag equation by Euler's Method

import numpy as np
import matplotlib.pyplot as plt

def fun(t,v):
    return 10-1.0*v                    #dv/dt=a-bv
    
t0=eval(input('Enter initial time : '))
v0=eval(input('Enter initial velocity : '))
tn=eval(input('Enter final time : '))

h=0.0001                                   
def euler(fun,t0,v0,tn,h):
    T=np.arange(t0,tn+h,h)  
    V=np.zeros(len(T))  
    V[0]=v0
    for i in range(len(T)-1):
        t,v=T[i],V[i]
        V[i+1]=v+h*fun(t,v)  
    return T,V
    
t_values,v_values=euler(fun,t0,v0,tn,h)
plt.plot(t_values,v_values,'b-',label="Euler's Solution")
plt.axhline(10,color='r',linestyle='--',label='Terminal Velocity')
plt.axhline(0,color='black',linestyle='--')
plt.axvline(0,color='black',linestyle='--')
plt.title("Solution of drag equation using Euler's Method")
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 08/Python Files/Q2.png')
plt.show()
