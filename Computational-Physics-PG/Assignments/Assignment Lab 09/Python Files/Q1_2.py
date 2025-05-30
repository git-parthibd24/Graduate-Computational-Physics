#Question 1 (2)
#Pendulum with driving force

import numpy as np
import matplotlib.pyplot as plt

g=9.81      #Acceleration due to gravity (m/s²)
l=0.1       #Length of the pendulum (m)
C=2         #Constant for the oscillating force (s⁻²)
Omega=5     #Driving frequency (s⁻¹)

theta0,w0,t0,tn,h=0,0,0,100,0.001    

def f_theta(t,theta,w):
    return w

def f_w(t,theta,w):
    return -(g/l)*np.sin(theta)+C*np.cos(theta)*np.sin(Omega*t)

def RK4(funcs,t0,u0,tn,Omega,h):
    T=np.arange(t0,tn+h,h)
    R=np.zeros((len(T),len(u0)))
    R[0]=u0   
    for i in range(len(T)-1):
        t,u=T[i],R[i]
        k1=h*np.array([f(t,*u) for f in funcs])
        k2=h*np.array([f(t+h/2,*(u+k1/2)) for f in funcs])
        k3=h*np.array([f(t+h/2,*(u+k2/2)) for f in funcs])
        k4=h*np.array([f(t+h,*(u+k3)) for f in funcs])
        R[i+1]=u+(k1+2*k2+2*k3+k4)/6    
    return T,R[:,0],R[:,1]

functions=[f_theta,f_w]
T,Theta,W=RK4(functions,t0,[theta0,w0],tn,Omega,h)

plt.plot(T,np.degrees(Theta),'b-')
plt.xlabel('Time (s)')
plt.ylabel(r'Angle $\theta(t)$ (degrees)')
plt.title(r'Pendulum with Oscillating Force')
plt.axhline(color='black',linewidth=1)
plt.axvline(color='black',linewidth=1)
plt.grid()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q1_2_Pendulum_Oscillating_Force.png')
plt.show()


Omega_values=np.arange(8,11,0.1)  
max_amplitudes=[]

for Omega in Omega_values:     #have to have Omega as the variable name to update the global Omega defined earlier
    functions=[f_theta,f_w]
    T,Theta,W=RK4(functions,t0,[theta0,w0],tn,Omega,h)
    max_amplitude=np.max(np.abs(Theta))  
    max_amplitudes.append(max_amplitude)

Omega=Omega_values[np.argmax(max_amplitudes)]   #np.argmax() returns index of the max element  

functions=[f_theta,f_w]
T,Theta,W=RK4(functions,t0,[theta0,w0],tn,Omega,h)

plt.plot(T,np.degrees(Theta),color='forestgreen',label=f'Resonant Frequency = {Omega:0.1f} s⁻¹')
plt.xlabel('Time (s)')
plt.ylabel(r'Angle $\theta(t)$ (degrees)')
plt.title('Pendulum at Resonance')
plt.axhline(color='black',linewidth=1)
plt.axvline(color='black',linewidth=1)
plt.grid()
plt.legend()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q1_2(b)_Pendulum_Resonance.png')
plt.show()

