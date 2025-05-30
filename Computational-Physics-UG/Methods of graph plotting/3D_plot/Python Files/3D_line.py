#3D-line in 3D-Space 

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-4*np.pi,4*np.pi,50)
y=np.linspace(-4*np.pi,4*np.pi,50)
z=x**2+y**2

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(x,y,z,'r-',linewidth=1)

ax.set_title('3D Line plot')
ax.set_ylabel('y-axis')
ax.set_xlabel('x-axis')
ax.set_zlabel('z-axis')
ax.set_xlim(-4*np.pi,4*np.pi)
ax.set_ylim(-4*np.pi,4*np.pi)
ax.set_zlim(-10*np.pi,10*np.pi)
ax.grid(True)

ax.set_xticks([0,1,2,3])
#ax.set_yticks([])
#ax.set_zticks([])

fig.set_size_inches(10,10)
fig.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\3D_plot\\Python Files\\line.png')

plt.show()