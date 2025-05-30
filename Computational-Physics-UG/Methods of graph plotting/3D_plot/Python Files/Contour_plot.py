#Contour plot

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x=np.linspace(-10,10,1000)   
y=np.linspace(-10,00,1000) 
X,Y=np.meshgrid(x,y)
u=np.sin(X)+np.sin(Y)

fig=plt.figure(figsize=(5,5),dpi=100)
colorinterpolation=20         #make colour gradient
colourMap=plt.cm.coolwarm     #colour representation
#colourMap=plt.cm.jet
plt.contourf(X,Y,u,colorinterpolation,cmap=colourMap,alpha=0.5)

plt.title('Contour Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#set colorbar
plt.colorbar()
fig.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\3D_plot\\Python Files\\contour.png')
plt.show()