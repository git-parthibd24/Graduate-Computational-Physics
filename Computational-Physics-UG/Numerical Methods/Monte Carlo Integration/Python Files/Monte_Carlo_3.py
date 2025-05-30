#Monte Carlo Simulation
#Alternate Formulation using mean of discrete variable for large points

import numpy as np
from scipy.integrate import simpson
import numpy.random as rn

f=lambda x : np.sin(x)

def MonteCarlo(a,b,f):
	x=rn.uniform(a,b,1000000)
	return (b-a)*np.mean(f(x))

def simps(a,b,f):
	x=np.linspace(a,b,1000)
	return simpson(f(x),x=x)
	
a,b=eval(input('Enter the range of integration : '))

print('The value of integration by Monte-Carlo Simulation is :',MonteCarlo(a,b,f))
print('The result using Simpsons 1/3 rule is :',simps(a,b,f))