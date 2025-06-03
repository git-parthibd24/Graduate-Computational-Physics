#Simulation of random walk with dynamic plotting

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

x=int(input('Enter the initial position : '))
X=[x]
T=[0]

for t in range(1,1000+1):
	step=2*rn.randint(0,2)-1
	x=x+step
	X.append(x)
	T.append(t)
	plt.cla()
	plt.title('Simulation for 1D random walk, itr=%2i'%(t))
	plt.plot(T,X,'b-',lw=0.8)
	plt.axhline(0,color='r',lw=0.5)
	plt.xlim(0,1001)
	plt.xlabel('Time Steps')
	plt.ylabel('Position at time t')
	plt.pause(0.001)

plt.show()
