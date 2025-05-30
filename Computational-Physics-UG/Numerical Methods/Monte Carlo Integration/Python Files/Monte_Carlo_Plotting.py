#Monte Carlo Simulation with plotting

import numpy as np
from scipy.integrate import simpson
import numpy.random as rn
import matplotlib.pyplot as plt

f=lambda x : np.sin(x)

a,b=0,np.pi
N=50000
x=np.linspace(a,b,10000)   
y_min=0
y_max=np.max(f(x))+1
A=(b-a)*(y_max-y_min)
z=rn.uniform(a,b,N)
y=rn.uniform(y_min,y_max,N)
n=np.sum([abs(y)<=abs(f(z))])      

def simps(a,b,f):
	x=np.linspace(a,b,1000)
	return simpson(f(x),x=x)

print('The result using Monte-Carlo Integration is :',format(A*n/N,'0.2f'))
print('The result using Simpsons 1/3 rule is :',format(simps(a,b,f),'0.2f'))

#Plotting
p=[];q=[]
for i in range(N):
	if y[i]<f(z)[i]:
		p.append(y[i])
		q.append(z[i])
	
plt.scatter(q[::20],p[::20],marker='o',color='magenta',s=5)
plt.scatter(z[::50],y[::50],marker='+',color='deepskyblue')
plt.plot(x,f(x),color='darkblue',linewidth=2)
plt.show()