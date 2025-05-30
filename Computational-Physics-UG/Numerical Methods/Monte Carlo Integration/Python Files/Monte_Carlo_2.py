#Monte Carlo Integration (faster approach with vectorization)

import numpy as np
from scipy.integrate import simpson
import numpy.random as rn

f=lambda x : np.sin(x)
def MonteCarlo(a,b,f):
	N=10000000
	x=np.linspace(a,b,1000)
	y_min=0                             #lies in 1st quadrant
	y_max=np.max(f(x))+1                #any valuec>=f_max
	A=(b-a)*(y_max-y_min)
	x=rn.uniform(a,b,N)
	y=rn.uniform(y_min,y_max,N)
	n=np.sum(abs(y)<abs(f(x)))		#Summing an array returns the sum of the elements in number form. The inequality condition returns array of 'True/False' i.e boolean
	return A*n/N

def simps(a,b,f):
	x=np.linspace(a,b,1000)
	return simpson(f(x),x=x)
	
print('The result using Monte-Carlo Integration is :',MonteCarlo(0,np.pi,f))
print('The result using Simpsons 1/3 rule is :',simps(0,np.pi,f))