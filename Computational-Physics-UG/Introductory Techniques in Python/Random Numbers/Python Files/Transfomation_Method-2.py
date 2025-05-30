#Generating exponential variates from uniform variate using transformation
#Method 2

import numpy.random as rn
import numpy as np
import matplotlib.pyplot as plt

N=100000
U=rn.uniform(0,1,N)
X=[]
m=np.mean(U)
for i in U:
	X.append(-(m*np.log(1-i)))
	
fig=plt.figure(figsize=(10,5),dpi=100)
plt.suptitle('Transformation of uniform distribuion to exponential distribution')

plt.subplot(1,2,1)
plt.hist(U,bins=30,rwidth=0.9,color='orange',label='Uniform disribution')
plt.legend()

plt.subplot(1,2,2)
plt.hist(X,bins=30,rwidth=0.9,color='magenta',label='Exponential disribution')
plt.legend()

plt.show()