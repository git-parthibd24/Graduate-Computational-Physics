#Solution of 1D Wave equation for a stretched plucked string

import numpy as np
import matplotlib.pyplot as plt

L=10                      #Length of string
Space_interval=100
Time_interval=500
C2=0.5                    #Courant Number 0<C2<1

x=np.linspace(0,L,Space_interval+1)
u=np.zeros((Space_interval+1,Time_interval+1))            

for i in range(1,Space_interval):     #For Space_interval points, the index runs from 1 to Space_interval-1
    u[i,0]=x[i]*(L-x[i])              #Initial Condition set for each of the space points except boundaries

#Initialization for the iterative step from taylor expansion of 'u' wrt time assuming initial velocity is zero
for i in range(1,Space_interval):     #Loop at iteration j=0 (t=0)
    u[i,1]=u[i,0]+0.5*C2*(u[i+1,0]+u[i-1,0]-2*u[i,0])

#Updating the array by time loop
for t in range(1,Time_interval):
    u[0][t+1]=0        
    u[Space_interval][t+1]=0
    for i in range(1,Space_interval):
        u[i,t+1]=2*u[i,t]-u[i,t-1]+C2*(u[i+1,t]+u[i-1,t]-2*u[i,t])
    
    plt.cla()
    plt.plot(x,u[:,t],'b',lw=1.5)
    plt.xlabel('Along the length of the string')
    plt.ylabel('Displacement')
    plt.title(' State of vibration')
    plt.ylim(-28,28)
    plt.axhline(color='black')
    plt.axvline(x=0,color='Black')
    plt.axvline(x=L,color='black')
    plt.pause(0.0001)

plt.show()
