#Study of average behavior of large number of 2D random walks

from random import choice
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

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
rms=np.sqrt(m_walk)

#Time scale mean distance log scale
t=np.log(range(1,steps+1))
r=np.log(m_walk)

#Fit data in linear scale
coeffs=poly.polyfit(t[100:],r[100:],1)
rfit=poly.polyval(t,coeffs)
print('The value of straight line constant after curve fitting is :',coeffs[0],'and value of the slope is :',coeffs[1])

#Data plot
plt.plot(t[::50],r[::50],'bo',label='$log_{r.m.s}$value')
plt.plot(t,rfit,'r-',label='fitted data')
plt.xlabel('log(time)',fontsize=10)
plt.ylabel('log($R_{rms}$)',fontsize=10)
plt.suptitle('Study of r.m.s values w.r.t time steps of a large number of 2D random walks ')
plt.title(r'$\log(r_{rms})=$%0.4f+%0.5f$\times\log t$'%(coeffs[0],coeffs[1]))
plt.legend()
plt.grid()
plt.show()
