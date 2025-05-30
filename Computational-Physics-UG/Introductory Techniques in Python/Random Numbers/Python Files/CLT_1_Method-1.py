#CLT: Normal distribution (gaussian variate) from die throwing population and exponential distribution
#Method 1

import numpy as  np
import numpy.random as rn
import matplotlib.pyplot as plt
n=int(input('Enter sample size : '))
f=lambda n: np.mean(rn.randint(1,7,n))		#The size of n determines how closer will be the several means in each trial i.e it reduces s.d and makes the histogram smoother
g=lambda n: np.mean(rn.exponential(2,n))
x,y=[],[]
for i in range(10000):						#The size of iteration determines how many samples of mean to be generated i.e increases scope of n and makes the histogram uniformly placed 
	x.append(f(n))
	y.append(g(n))
	
plt.figure()
plt.title('Distribution in central limit theorem from die throwing population')
plt.hist(x,bins=30,rwidth=0.8,color='magenta')

plt.figure()
plt.title('Distribution in central limit theorem from exponential distribution')
plt.hist(y,bins=30,rwidth=0.8,color='red')


plt.show()