#Question 3
#Heat Diffusion Equation with variable boundary condition

import numpy as np
import matplotlib.pyplot as plt

#Constants and parameters
L=20                #Depth of the crust (in meters)
A=10                #Mean surface temperature (in °C)
B=12                #Amplitude of seasonal variation (in °C)
D=0.1               #Thermal diffusivity (m²/day)
tau=365             #Period of temperature variation (in days)
T=3650              #Total simulation time (10 years in days)
dx=0.1              #Grid spacing (in meters)
dt=0.04             #Time step (in days)
cnt=D*dt/(dx**2)    #Stability condition for the explicit scheme


Space_interval=int(L/dx)
Time_interval=int(T/dt)

x=np.linspace(0,L,Space_interval+1)
time=np.linspace(0,T,Time_interval+1)  
u=np.empty((Space_interval+1,Time_interval+1))

#Initial condition at t=0
u[1:Space_interval,0]=10        #Interior points initialized to 10
u[0,0]=A+B*np.sin(0)            #Surface boundary condition
u[Space_interval,0]=11          #Bottom boundary condition (constant 11°C)

#Time-varying boundary condition
def boundary_condition(t):
    return A+B*np.sin(2*np.pi*t/tau)

#Updating the array by time loop
for k in range(Time_interval):  #Updates all time points except t=0 
    #Update boundary condition
    u[0,k+1]=boundary_condition(time[k+1])  
    u[Space_interval,k+1]=11
    
    #Update interior points 
    for i in range(1,Space_interval):
        u[i,k+1]=u[i,k]+cnt*(u[i+1,k]-2*u[i,k]+u[i-1,k])


time_points=[365*9,365*9+90,365*9+180,365*9+270,365*9+360]

for t_point in time_points:
    t_index=int(t_point/dt)     #Converts days to index
    plt.plot(x,u[:,t_index],label=f'Time = {(t_point-365*9)/30} month',lw=1)
    
plt.axhline(color='black')
plt.axvline(color='black')
plt.axvline(x=x[-1],color='black')
plt.xlabel('Depth (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Profile in the Earth\'s Crust between 9th and 10th year with 3 month interval')
plt.legend()
plt.grid()
plt.show()
