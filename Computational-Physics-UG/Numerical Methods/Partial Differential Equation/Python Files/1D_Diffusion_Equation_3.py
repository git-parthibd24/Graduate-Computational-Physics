#Solution of 1D Heat Diffusion Equation and compare with exact solution

import numpy as np
import matplotlib.pyplot as plt

L=10                     #Length of rod
Space_interval=100
dx=L/Space_interval
Time_interval=100000
T=107                    #Final Time
dt=T/Time_interval
alpha2=0.000023          #Diffusion Constant
cnt=(alpha2)*dt/(dx**2)  #For numerical stability (Neumann Stability) this factor needs to be less than 0.5
T0=20                    #Initial Temperature

x=np.linspace(0,L,Space_interval+1)
u=T0*np.ones((Space_interval+1))                 #Initial Condition        
u[0],u[Space_interval]=0,0                       #Boundary Condition              

#Updating the array by time loop
for j in range(Time_interval):     
    for i in range(1,Space_interval):
        u[i]=u[i]+cnt*(u[i+1]-2*u[i]+u[i-1])
        
    
#Exact result
t=107
f=lambda m:4*T0/(np.pi*(2*m-1))*np.sin((2*m-1)*np.pi*x/L)*np.exp(-((2*m-1)*np.pi/L)**2*alpha2*t)
Exact_solution=sum([f(m) for m in range(1,20)])    
        
#PLotting
plt.plot(x,u,'r',label='By numerical method')
plt.plot(x,Exact_solution,'b--',label='Exact solution')
plt.legend()
plt.xlabel('Along the length of the rods')
plt.ylabel('Temperature')
plt.title('Temperature profile after some time')
plt.grid()
plt.show()
