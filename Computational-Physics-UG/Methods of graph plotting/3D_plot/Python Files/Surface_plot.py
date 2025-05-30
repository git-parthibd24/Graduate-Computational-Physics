#3D surface plot

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-100,100,1000)   
y=np.linspace(-100,100,1000) 
X,Y=np.meshgrid(x,y)
u=X**2+Y**2

fig=plt.figure(figsize=(5,5),dpi=100)
ax=plt.axes(projection='3d')

ax.plot_surface(X,Y,u,color='green',alpha=0.5)
#ax.plot_surface(X,Y,u,cmap='Greens')   #Used to create gradient of colour. Can use Greys,Grays,Purples,Blues,Oranges,Reds,YlOrRd,OrRd,PuRd,Rd,Pu,BuPu,GnBu,YlGuBu,BuGn,etc
ax.set_title('3D Surface Plot')
ax.set_ylabel('y-axis')
ax.set_xlabel('x-axis')
ax.set_zlabel('z-axis')
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(-10000,20000)

fig.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\3D_plot\\Python Files\\surface.png')
plt.show()