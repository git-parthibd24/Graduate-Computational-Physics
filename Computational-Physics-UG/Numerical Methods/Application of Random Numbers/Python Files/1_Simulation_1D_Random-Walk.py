#Simulation of single random walk from 1st time step
#Method 2

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

x=2*rn.randint(0,2,size=1000)-1

#print(np.cumsum(x))

plt.plot(np.cumsum(x),color='blue',lw=0.8)
plt.axhline(0,color='r',lw=0.5)
plt.xlabel('Time Steps')
plt.ylabel('Position at time t')
plt.title('Simulation of 1D random walk')
plt.show()
