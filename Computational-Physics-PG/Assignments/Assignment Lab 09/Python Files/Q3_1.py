#Question 3 (1)
#Plotting comet orbit in astronomical scales using RK-4 Method 
#(This code is extremely sensitive to parameters taken. Apparent small deviation causes complete erronous solution)

import numpy as np
import matplotlib.pyplot as plt

G=6.67430e-11
M_sun=1.9885e30
GM=G*M_sun

x0=4e12  # 4 billion km = 4e12 m
y0=0
vx0=0
vy0=500

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

def rk4(funcs,t0,u0,tn,h):
    steps=int((tn-t0)/h)+1
    T=np.zeros(steps)
    R=np.zeros((steps,len(u0)))
    R[0]=u0
    for i in range(steps-1):
        t,u=T[i],R[i]
        k1=h*np.array([f(t,*u)for f in funcs])
        k2=h*np.array([f(t+h/2,*(u+k1/2))for f in funcs])
        k3=h*np.array([f(t+h/2,*(u+k2/2))for f in funcs])
        k4=h*np.array([f(t+h,*(u+k3))for f in funcs])
        R[i+1]=u+(k1+2*k2+2*k3+k4)/6
        T[i+1]=t+h
    return T,R


a=x0/2                                             #Assuming it to be Semi-major axis (m)
orbital_period=2*np.pi*np.sqrt(a**3/GM)            #Kepler's 3rd Law
tn=orbital_period*2

h=(365*24*3600)/10000                              #Order of 1 to 10 hours
functions=[dxdt,dydt,dvxdt,dvydt]
T,R=rk4(functions,0,[x0,y0,vx0,vy0],tn,h)
x,y=R[:,0],R[:,1]

plt.plot(x,y,'b-')
plt.plot(0,0,color='orange',marker='o',label="Sun",ms=6)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Comet Orbit')
plt.grid()
plt.axis('equal')
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q3_1_Comet_Orbit.png')
plt.show()
print('The orbital period is :',orbital_period/(365*24*3600),'years')
