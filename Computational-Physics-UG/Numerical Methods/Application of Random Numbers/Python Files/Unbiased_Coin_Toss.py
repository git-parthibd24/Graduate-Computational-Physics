#Simulation of an coin toss experiment consisting of N trials
#Probability of getting head=0.5 when N tends to infinity (Unbiased probability)

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

N=eval(input('Enter the number of trials : '))
m=eval(input('Enter the number of samples for set of trials : '))

x=lambda n: np.mean(rn.choice([0,1],size=n))			# 1 stands for head, 0 stand for tail or vice-versa
xx=[x(N) for i in range(m)]

plt.title('Histogram for tossing of unbiased coin for set of trials =%2i'%(m))
plt.xlim(0,1)
plt.hist(xx,bins=10,rwidth=0.9,histtype='bar',label='Head or Tail',color='c')
plt.legend(loc='upper right')
plt.xlabel('Average number of heads or tails (probability) per set of trials')
plt.show()
