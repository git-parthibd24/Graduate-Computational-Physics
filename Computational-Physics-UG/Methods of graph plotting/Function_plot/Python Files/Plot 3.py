#Plot 3

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
y=np.sin(x)

fig=plt.figure(figsize=(10,8),dpi=100)  #This must be at the beginning of plot
plt.plot(x,y,'-',color='cyan',linewidth=5)
plt.axis([-5,5,-2,2])
plt.title('Plotting with matplotlib')
plt.xlabel('xvalues')
plt.ylabel('yvalues')
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)

plt.grid()
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_3.png')
plt.show()