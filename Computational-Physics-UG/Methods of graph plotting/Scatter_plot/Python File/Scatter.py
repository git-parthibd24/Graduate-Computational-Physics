#Scatter plot

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2.0*np.pi,2*np.pi,50)
y=np.sin(x)

plt.scatter(x,y,color='red',s=50,alpha=0.7,label='Data Points')
plt.legend()
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Scatter_plot\\Python File\\fig.png')
plt.show()