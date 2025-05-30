#CLT: Normal distribution (gaussian variate) from die throwing population and exponential distribution
#Method 2

import numpy as  np
import numpy.random as rn
import matplotlib.pyplot as plt
n=int(input('Enter sample size : '))
f=rn.randint(1,7,n)		
g=rn.exponential(2,n)
x,y=[],[]
for i in range(10000): 
	x.append(np.mean(rn.choice(f,100)))
	y.append(np.mean(rn.choice(g,100)))
	
plt.figure()
plt.title('Distribution in central limit theorem from die throwing population')
plt.hist(x,bins=30,rwidth=0.8,color='magenta')

plt.figure()
plt.title('Distribution in central limit theorem from exponential distribution')
plt.hist(y,bins=30,rwidth=0.8,color='red')

plt.show()