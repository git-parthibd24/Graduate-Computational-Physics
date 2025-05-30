#Plot 2

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,50)
y=np.cos(x)
z=np.sin(x)

fig=plt.figure(figsize=(10,8),dpi=100)  #This must be at the beginning of plot
plt.plot(x,y,linestyle='dotted',color='red',linewidth=5)
plt.plot(x,z,linestyle='dashed',color='green',linewidth=4)
plt.title('Plotting with matplotlib')
plt.xlabel('xvalues')
plt.ylabel('yvalues')
plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,2,0.2))
plt.legend(['x vs y','x vs z'])
plt.grid()
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_2.png')
plt.show()