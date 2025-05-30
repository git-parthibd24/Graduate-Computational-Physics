#Monte Carlo Integration (using loop)

import numpy as np
from scipy.integrate import simpson
import random as rm

f=lambda x : x*np.exp(x)
a,b=eval(input('Enter lower limit, upper limit of integration : '))
sidex=b-a
x=np.linspace(a,b,1000)
sidey=np.max(f(x))
area_rectangle=sidex*sidey
N=10000000
count=0
for i in range(N):
	x=rm.uniform(a,b)
	y=rm.uniform(0,sidey)
	if y<=f(x):
		count=count+1

A=area_rectangle*(count/N)

def simps(a,b,f):
    x=np.linspace(a,b,1000)
    return simpson(f(x),x=x)  #need to pass x as keyword argument instead of positional argument in simpson()
	
print('The value of integration by Monte-Carlo Simulation is :',format(A,'0.2f'))
print('The result using Simpsons 1/3 rule is :',format(simps(a,b,f),'0.2f'))