#3D Plotting of solution Heat Diffusion in 1D 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm          #scalar mapable to create colorbar

#Parameters of system with boundary conditions
x=np.linspace(0,1,101)
t=np.linspace(0,100,101)
u=np.zeros((101,101))        

#Initial Condition
u[0]=np.exp(-((x-0.5)**2)/0.02)

for j in range(1,100):    #Updates all time points except t=0
    u[j]=u[j-1]           #simply copies the solution at previous time to the solution at next time which is going to be updated. This is done simply because the way iteration formula is written   
    for i in range(1,100):
        u[j,i]=u[j,i]+(u[j,i+1]-2*u[j,i]+u[j,i-1])/4
        

#3D PLotting 
X,T=np.meshgrid(x,t,sparse=True)
fig=plt.figure(figsize=(13,13))
ax=plt.axes(projection='3d')
ax.plot_surface(X,T,u,cmap=cm.coolwarm)
ax.set_xlabel('$X$',fontsize=10,rotation=170)
ax.set_ylabel('$t$',fontsize=10)
ax.set_zlabel('$Temperature$',fontsize=10,rotation=60)
plt.show() 

