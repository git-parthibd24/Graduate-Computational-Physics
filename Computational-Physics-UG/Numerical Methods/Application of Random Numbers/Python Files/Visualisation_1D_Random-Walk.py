#Visualisation of 1D random walk on a plane
#The particle will be seen to be moving the x-axis only

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

x=0
X=[x]
y=0
Y=[y]

for t in range(1,1000):
	step=2*rn.randint(2)-1
	x=x+step
	X.append(x)
	Y.append(0)
	plt.cla()
	plt.title('Simulation for 1D random walk, itr=%2i'%(t))
	plt.plot(X,Y,'-',color='midnightblue',lw=0.8)
	plt.plot(x,y,'ro')
	plt.axhline(0,color='grey',ls='--',lw=0.5)
	plt.axvline(0,color='grey',ls='--',lw=0.5)
	plt.xlim(-50,50)
	plt.ylim(-1,1)
	plt.xlabel('X position')
	plt.ylabel('Y position ')
	plt.pause(0.001)

plt.show()
