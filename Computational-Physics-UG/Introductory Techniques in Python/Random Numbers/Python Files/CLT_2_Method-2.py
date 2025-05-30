#CLT: Normal distribution sampling from a single die throwing population
#Method 2

import numpy.random as rn
import numpy as np
import matplotlib.pyplot as plt

N=1000000					#Population size
P=rn.randint(1,7,N)			#Population having elements 1,2,3,4,5,6 randomly stored in an array

size=200					#Size of each sample to be generated
number=N/size				#No. of samples generated from the population

def index(n):
	position=[rn.randint(0,N-1) for j in range(size)]		#Storing index values from the whole size of population randomly generated for a sample
	sample=[P[k] for k in position]							#Creating a sample picking  from the population corresponding to the random index postions for the defined sample size
	return np.mean(sample)									#returning mean of the sample

M=[index(i) for i in range(int(number))]					#Creating many samples for defined sample number to store the mean values of each such samples

fig=plt.figure(figsize=(10,5),dpi=100)
plt.subplot(1,2,1)
plt.hist(M,bins=30,rwidth=0.9,color='green',label='Distribution from CLT')
plt.legend()
plt.subplot(1,2,2)
plt.hist(P,bins=30,rwidth=0.9,color='blue',label=' Original Distribution')
plt.legend()
plt.show()