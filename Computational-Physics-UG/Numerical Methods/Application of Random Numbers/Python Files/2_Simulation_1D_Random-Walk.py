#Simulation of single random walk from 1st time step
#Method 2

import numpy as np
import random as rm
import matplotlib.pyplot as plt

n=int(input('Enter the number of steps : '))
step=[0]
Y=[0]
y=0
for i in range(1,n+1):
	if rm.random()<0.5:
		y=y-1
	else:
		y=y+1
	
	Y.append(y)
	step.append(i)

plt.title('Simulation for 1D random walk')
plt.plot(step,Y,'b-',lw=0.7)
plt.axhline(0,color='r',lw=0.5)
plt.xlabel('Time Steps')
plt.ylabel('Position at time t')
plt.show()
