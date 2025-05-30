#Generating exponential variates from uniform variate using transformation
#Method 1

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

x=rn.random(100000)
y=-np.log(x)

fig=plt.figure(figsize=(5,10),dpi=100)
plt.subplot(2,1,1)
plt.hist(x,bins=30,rwidth=0.9,color='brown')

plt.subplot(2,1,2)
plt.hist(y,bins=30,rwidth=0.9,color='orange')

plt.show()