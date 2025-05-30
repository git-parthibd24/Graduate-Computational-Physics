#CLT: Normal distribution sampling from a single die throwing population
#Method 1

import numpy as  np
import numpy.random as rn
import matplotlib.pyplot as plt

N=100000000				#size of population
R=rn.randint(1,7,N)
size=100				#size of each sample from the population
number=N/size

P=[];M=[];j=0
for i in range(0,int(number),size):
	P.append(R[0+i:size+i])
	j+=1
	M.append(np.mean(P[j-1]))

plt.title('Distribution in central limit theorem from die throwing population')	
plt.hist(M,bins=30,rwidth=0.9,color='red')
plt.show()