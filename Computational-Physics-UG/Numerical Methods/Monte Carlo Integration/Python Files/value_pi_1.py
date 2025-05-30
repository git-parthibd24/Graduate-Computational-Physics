#Evaluate value of pi using Monte Carlo Integration 

import random as rm
N=10000000
count=0
r=eval(input('Enter the radius of circle : '))
for i in range(N):
	x=rm.uniform(-r,r)
	y=rm.uniform(-r,r)
	if x*x+y*y<=r*r:
		count=count+1
pi=4*(count/N)

print('The value of pi by Monte-Carlo integration is :',format(pi,'0.4f'))