#Question 2(1)
#Planetary Motion using Verlet Method

import numpy as np
import matplotlib.pyplot as plt

G=6.67430e-11
M_sun=1.9891e30
GM=G*M_sun

x0,y0=1.4710e11,0
vx0,vy0=0,3.0287e4

def dxdt(t,x,y,vx,vy):
    return vx

def dydt(t,x,y,vx,vy):
    return vy

def dvxdt(t,x,y,vx,vy):
    r=np.sqrt(x**2+y**2)
    return -GM*x/r**3

def dvydt(t,x,y,vx,vy):
    r=np.sqrt(x**2+y**2)
    return -GM*y/r**3

def Verlet(r_funcs,v_funcs,t0,u0,tn,h):
    T=np.arange(t0,tn+h,h)
    X=np.zeros((len(T),2))
    V=np.zeros((len(T),2))
    V_half=np.zeros((len(T),2))
    X[0],V[0]=u0[:2],u0[2:]
    V_half[0]=V[0]+0.5*h*np.array([f(t0,*X[0],*V[0]) for f in v_funcs])
    for i in range(len(T)-1):
        t=T[i]
        X[i+1]=X[i]+h*np.array([f(t+h/2,*X[i],*V_half[i]) for f in r_funcs])
        V[i+1]=V_half[i]+0.5*h*np.array([f(t+h,*X[i+1],*V_half[i]) for f in v_funcs])
        V_half[i+1]=V_half[i]+h*np.array([f(t+h,*X[i+1],*V[i+1]) for f in v_funcs])
    return T,X,V

a=1.496e11
orbital_period=2*np.pi*np.sqrt(a**3/GM)
tn=orbital_period*2
h=3600

r_funcs=[dxdt,dydt]
v_funcs=[dvxdt,dvydt]
T,X,V=Verlet(r_funcs,v_funcs,0,[x0,y0,vx0,vy0],tn,h)

plt.plot(X[:,0],X[:,1],'b-')
plt.plot(0,0,color='orange',marker='o',label="Sun",ms=6)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Earth Orbit')
plt.grid()
plt.axis('equal')
plt.legend()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 10/Python Files/Q2_1_Earth_Orbit.png')
plt.show()

