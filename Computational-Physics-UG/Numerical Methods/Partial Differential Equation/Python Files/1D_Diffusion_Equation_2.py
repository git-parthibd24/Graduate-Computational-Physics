#Solution of Heat Diffusion Equation in 1D
#Updating previous solutions

import numpy as np
import matplotlib.pyplot as plt

L=10                     #Length of rod
Space_interval=100
dx=L/Space_interval
Time_interval=10000
T=107                    #Final Time
dt=T/Time_interval
alpha2=0.000023          #Diffusion Constant
cnt=(alpha2)*dt/(dx**2)  #For numerical stability (Neumann Stability) this factor needs to be less than 0.5

x=np.linspace(0,L,Space_interval+1)
u=np.zeros(Space_interval+1)           #Boundary condition upon which the array will be updated as time passes from recursion relation
u[len(x)//2]=1                         #Initial Condition (midpoint heating)


#Updating the array by time loop
for j in range(Time_interval):     
    for i in range(1,Space_interval):
        u[i]=u[i]+cnt*(u[i+1]-2*u[i]+u[i-1])
    
        
#PLotting
plt.plot(x,u,color='magenta',lw=1)          
plt.xlabel('Along the length of the rod')
plt.ylabel('Temperature')
plt.title('Temperature profile after some time')
plt.grid()
plt.show()
