#Exponential fit to average data of large number of 2D random walks

from random import choice
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def walk(steps):
	x,y=0,0
	p=[]
	for i in range(steps):
		dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
		x,y=x+dx,y+dy
		p.append(x*x+y*y)
	return p

#To create a set of walks
steps,sample=1000,1000
walks=np.array([walk(steps) for i in range(sample)])		#Converting 1D list of list into array of list makes a 2D array of list
m_walk=np.mean(walks,axis=0)


#Time scale and mean distance scale
t=range(1,steps+1)
rms=np.sqrt(m_walk)

#Define the fitting function
def powerfit(t,A,B):
	r=A*t**B
	return r

#Fit Data
A,B=curve_fit(powerfit,t,rms)[0]
rfit=A*t**B
print('The value of the exponential fits are : ',A,'and',B)

#Plotting
plt.figure()
plt.plot(t[::50],rms[::50],'bo',label='$R_{r.m.s}$value')
plt.plot(t,rfit,'r-',label='fitted data')
plt.xlabel('Time',fontsize=10)
plt.ylabel('$r_{rms}$',fontsize=10)
plt.suptitle('Study of r.m.s values w.r.t time steps of a large number of 2D random walks')
plt.title(r'$r_{rms}=%0.2ft^{%0.2f}$'%(A,B))
plt.legend()
plt.grid()
plt.show()
