#Plot 1

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y=np.sin(x)

fig=plt.figure(figsize=(10,8),dpi=100)  #This must be at the beginning of plot
plt.plot(x,y,'r+')
plt.title('Plotting with matplotlib')
plt.xlabel('xvalues')
plt.ylabel('yvalues')
plt.grid()
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_1.png')
plt.show()