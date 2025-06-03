#Visualisation of 2D Random Walk
#Method 2

import random as rm
import matplotlib.pyplot as plt

x,y=0,0
x_pos,y_pos=[0],[0]
itr=1000

for i in range(1,itr+1):
	val=rm.randint(1,4)
	if val==1:
		x=x-1
	elif val==2:
		x=x+1
	elif val==3:
		y=y-1
	else:
		y=y+1
	x_pos.append(x)
	y_pos.append(y)
	
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Visualization of 2D random walk for steps = %2i'%(itr))
plt.plot(x_pos,y_pos,color='green',lw=2)
plt.grid()
plt.show()
