#Plot 1

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,50)
y=np.cos(x)
z=np.sin(x)

fig=plt.figure(figsize=(12,5),dpi=100)  #This must be at the beginning of plot

plt.subplot(121)   #row,column.plot no.
plt.plot(x,y,linestyle='dotted',color='red',linewidth=5)
plt.title('Plotting with matplotlib')
plt.xlabel('xvalues')
plt.ylabel('yvalues')
plt.grid()

plt.subplot(122)
plt.plot(x,z,linestyle='dotted',color='green',linewidth=4)
plt.title('Plotting with matplotlib')
plt.xlabel('xvalues')
plt.ylabel('yvalues')
plt.grid()

#plt.tight_layout()
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Sub_plot\\Python Files\\fig_1.png')
plt.show()