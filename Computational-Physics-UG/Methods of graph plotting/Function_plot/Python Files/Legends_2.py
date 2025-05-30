#Plot 2
#Demonstration of many plots with same axis in single figure

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1.0,1000)
w1=np.sqrt(np.abs(x))
w2=x
w3=x**2
w4=x**3
w5=x**4

plt.xlabel('x-values',fontsize=12)
plt.ylabel('y-values',fontsize=12)
plt.plot(x,w1,label=r'$\sqrt{x}$')
plt.plot(x,w2,label=r'$x$')
plt.plot(x,w3,label=r'$x^2$')
plt.plot(x,w4,label=r'$x^3$')
plt.plot(x,w5,label=r'$x^3$')

plt.axis([-1,1,-1,2])
plt.title('Polynomial Plots',fontsize=14)
plt.axhline(color='black',lw=0.5)
plt.axvline(color='black')

plt.legend(loc='best',prop={'size':10})

plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_legend_2.png')
plt.show()

