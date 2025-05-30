#Plot 4

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
y=np.sin(x)

fig=plt.figure(figsize=(10,8),dpi=100)  #This must be at the beginning of plot
plt.plot(x,y,'-',color='magenta',linewidth=2)
plt.title('Plotting with matplotlib')
plt.xlabel('xvalues')
plt.xlim(-10,10)
plt.ylabel(r'$\alpha$ values')      #raw string to be used to write latex symbols
plt.ylim(-2,2)

plt.grid()
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_4.png')
plt.show()