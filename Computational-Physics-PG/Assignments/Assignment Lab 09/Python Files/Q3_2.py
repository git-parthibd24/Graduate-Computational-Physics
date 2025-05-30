# Question 3 (2)
#Plotting comet orbit in astronomical scales using Adaptive RK-4 Method
#(This code is very rigid to range of parameters taken)

import numpy as np
import matplotlib.pyplot as plt


G=6.67430e-11  
M_sun=1.9885e30  
GM=G*M_sun

#Initial conditions
x0=4e12        # 4 billion km = 4e12 m
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

def rk4_step(funcs,t,u,h):
    k1=h*np.array([f(t,*u) for f in funcs])
    k2=h*np.array([f(t+h/2,*(u+k1/2)) for f in funcs])
    k3=h*np.array([f(t+h/2,*(u+k2/2)) for f in funcs])
    k4=h*np.array([f(t+h,*(u+k3)) for f in funcs])
    return u+(k1+2*k2+2*k3+k4)/6

def adaptive_rk4(funcs,t0,u0,tn,h,tol=1e3):
    t=t0
    u=u0
    time=[t]
    trajectory=[u[0:2]]  # Store (x,y)

    while t<tn:                            # Compute two RK4 steps : one full step (h), two half-steps (h/2)        
        u1=rk4_step(funcs,t,u,h)
        u_half1=rk4_step(funcs,t,u,h/2)  
        u2=rk4_step(funcs,t+h/2,u_half1,h/2)  

        r1=np.sqrt((u1[0]-u[0])**2+(u1[1]-u[1])**2)  
        r2=np.sqrt((u2[0]-u[0])**2+(u2[1]-u[1])**2)  
        error=abs(r2-r1) 

        if error<tol/100:    #Accounts for the region where a big h produces small error
            h*=1.25  
        elif error>tol:      #Accounts for the region where a small h produces significant error
            h*=0.5  
        else:
            u=u2  
            t+=h
            time.append(t)
            trajectory.append(u[0:2])

    return np.array(time),np.array(trajectory)


a=x0/2                                   #Semi-major axis (m)
orbital_period=2*np.pi*np.sqrt(a**3/GM)  #Kepler's 3rd Law
tn=2*orbital_period  

#This h can be taken from a very tiny number to a very huge number, even 10**6 times more than tn. The proper h required will be automatically adjusted
h=(365*24*3600)/10000                    #Initial step size (52.56 mins)
functions=[dxdt,dydt,dvxdt,dvydt]


T,R=adaptive_rk4(functions,0,[x0,y0,vx0,vy0],tn,h)

# Extract (x,y) positions
x,y=R[:,0],R[:,1]

# Plot the orbit
plt.figure(figsize=(8,6))
plt.plot(x[::15],y[::15],'bo',label="Comet Orbit",ms=2)
plt.plot(0,0,color='orange',marker='o',label="Sun",ms=6)  
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.title("Comet Orbit (Adaptive RK4 with Dynamic Step Size)")
plt.legend()
plt.axis('equal')
plt.grid()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q3_2_Comet_Orbit_Adaptive.png')
plt.show()
print('The orbital period is :',orbital_period/(365*24*3600),'years')
