#Plot 5

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,100)
y=np.sin(x)

fig=plt.figure(figsize=(10,8),dpi=100)  #This must be at the beginning of plot

ax=plt.axes()
C=ax.plot(x,y)
ax.set_xlabel('x=axis')
ax.set_ylabel('y-axis')
ax.set_title('x vs sin(x)')
ax.set_xlim(-2.5,2.5)
ax.set_ylim(-1.0,1.0)
ax.grid(True)
fig.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_5.png')

plt.show()
