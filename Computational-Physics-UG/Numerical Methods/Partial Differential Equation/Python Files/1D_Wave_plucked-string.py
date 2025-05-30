#Solution of 1D Wave equation for a stretched plucked string

import numpy as np
import matplotlib.pyplot as plt

L=10                      #Length of string
Space_interval=100
Time_interval=100
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
    
        
#PLotting
plt.plot(x,u[:,1],'r',label='Time = 1 unit')
plt.plot(x,u[:,20],'b',label='Time = 20 units')
plt.plot(x,u[:,30],'g',label='Time = 30 units')
plt.plot(x,u[:,40],'y',label='Time = 40 units')
plt.legend()
plt.xlabel('Along the length of the string')
plt.ylabel('Displacement')
plt.title(' State of vibration at different times')
plt.grid()
plt.show()
