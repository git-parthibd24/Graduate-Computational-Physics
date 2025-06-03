#Visualisation of 2D Random Walk
#Method 1

from random import choice
import numpy as np
import matplotlib.pyplot as plt

x,y=0,0
X,Y=[0],[0]

itr=0
for i in range(1000):
	itr+=1
	dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
	x,y=x+dx,y+dy
	X.append(x)
	Y.append(y)
	plt.cla()
	plt.xlim(-80,80)
	plt.ylim(-80,80)
	plt.grid()
	plt.plot(X,Y,'b-',label='path traced by the particle')
	plt.plot(x,y,'ro',label='present postion of particle')
	plt.xlabel('X Position')
	plt.ylabel('Y Position')
	plt.legend()
	plt.title('Visualization of 2D random walk for steps =%2i'%(itr))
	plt.pause(0.01)
	
plt.show()
