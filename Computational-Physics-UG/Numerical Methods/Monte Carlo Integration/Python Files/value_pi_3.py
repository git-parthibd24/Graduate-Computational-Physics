#Computation of value of pi by Monte-Carlo Integration
#Alternate Formulation using mean of discrete variable for large points

import numpy as np
import numpy.random as rn

r=eval(input('Enter the radius of circle : '))
def f(x):
	return np.sqrt(r**2-x**2)
def MonteCarlo(a,b,f):
	x=rn.uniform(a,b,1000000)
	return (b-a)*np.mean(f(x))
I=MonteCarlo(0,r,f)
print('The value of pi from Monte-Carlo Integration is :',format(4*I/r**2,'0.4f'))