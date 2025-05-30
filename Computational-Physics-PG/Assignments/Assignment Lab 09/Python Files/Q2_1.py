#Question 2 (1)
#Projectile motion including air resistance

import numpy as np
import matplotlib.pyplot as plt

g=9.81                  #Accelerationduetogravity(m/s²)
m=1.0                   #Massofcannonball(kg)
R=0.08                  #Radiusofcannonball(m)
rho=1.22                #Densityofair(kg/m³)
C=0.47                  #Dragcoefficientforsphere
v0=100                  #Initialvelocity(m/s)
theta=np.radians(30)    #Launchangle(30degrees)

#Initialconditions
x0,y0=0,0    
vx0=v0*np.cos(theta)
vy0=v0*np.sin(theta)
t0,tn,h=0,20,0.0001

#Equationsofmotion
def fx(t,x,y,vx,vy):
    return vx

def fy(t,x,y,vx,vy):
    return vy

def fvx(t,x,y,vx,vy):
    v=np.sqrt(vx**2+vy**2)
    return -(np.pi*R**2*rho*C)/(2*m)*vx*v

def fvy(t,x,y,vx,vy):
    v=np.sqrt(vx**2+vy**2)
    return -g-(np.pi*R**2*rho*C)/(2*m)*vy*v

def RK4(funcs,t0,u0,tn,h):
    steps=int((tn-t0)/h)+2      #2 is used just as buffer
    T=np.zeros(steps)
    R=np.zeros((steps,len(u0)))
    R[0]=u0
    for i in range(len(T)-1):
        t,u=T[i],R[i]
        k1=h*np.array([f(t,*u) for f in funcs])
        k2=h*np.array([f(t+h/2,*(u+k1/2)) for f in funcs])
        k3=h*np.array([f(t+h/2,*(u+k2/2)) for f in funcs])
        k4=h*np.array([f(t+h,*(u+k3)) for f in funcs])
        R[i+1]=u+(k1+2*k2+2*k3+k4)/6
        T[i+1]=t+h
        if R[i+1,1]<=0:
            break
    T=T[0:i+1]
    R=R[0:i+1,:]
    return T,R[:,0],R[:,1],R[:,2],R[:,3]

functions=[fx,fy,fvx,fvy]
T,X,Y,Vx,Vy=RK4(functions,t0,[x0,y0,vx0,vy0],tn,h)
distance=X[-1]

print('Distance traveled horizontally is :',distance,'m')

plt.plot(X,Y,'b-',label='Trajectory')
plt.scatter(X[-1],Y[-1],color='green',s=100,label='Impact (x = {:0.1f} m)'.format(X[-1]))
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Cannonball Trajectory with Air Resistance')
plt.axhline(color='black',linewidth=1)
plt.axvline(color='black',linewidth=1)
plt.legend()
plt.grid()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q2_1_Trajectory.png')
plt.show()
