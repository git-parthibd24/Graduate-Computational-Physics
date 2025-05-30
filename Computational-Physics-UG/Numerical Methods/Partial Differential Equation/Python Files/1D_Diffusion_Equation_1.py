#Solution of Heat Diffusion Equation in 1D
#Storing solution for all times

import numpy as np
import matplotlib.pyplot as plt

L=10                     #Length of rod
Space_interval=100
dx=L/Space_interval
Time_interval=10000
T=4.4*10**5              #Final Time
dt=T/Time_interval
alpha2=0.000023          #Diffusion Constant
cnt=(alpha2)*dt/(dx**2)  #For numerical stability (Neumann Stability) this factor needs to be less than 0.5

x=np.linspace(0,L,Space_interval+1)
u=np.empty((Space_interval+1,Time_interval+1))           
for i in range(1,Space_interval):              #For Space_interval points, the index runs from 1 to Space_interval-1
    u[i][0]=np.exp(-(x[i]-5)**2)               #Initial Condition set for each of the space points except boundaries 
    #u[i][0]=np.sin(np.pi*x[i])
    #u[i][0]=np.cos(np.pi/2*x[i])

#Boundary Condition
u[0][0]=0
u[Space_interval][0]=0

#Updating the array by time loop
for k in range(Time_interval):        #Updates all time points except t=0   
    u[0][k+1]=0        
    u[Space_interval][k+1]=0
    for i in range(1,Space_interval):          #Includes interior points only
        u[i][k+1]=u[i][k]+cnt*(u[i+1][k]-2*u[i][k]+u[i-1][k])
    
        
#PLotting
plt.plot(x,u[:,0],label='Time = 0 unit')
plt.plot(x,u[:,500],label='Time = 50 unit')
plt.plot(x,u[:,1000],label='Time = 100 unit')
plt.xlabel('Along the length of the rods')
plt.ylabel('Temperature')
plt.title('Temperature profile after some time')
plt.legend()
plt.grid()
plt.show()
