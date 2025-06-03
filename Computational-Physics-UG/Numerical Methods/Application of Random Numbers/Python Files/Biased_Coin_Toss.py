#Simulation of an coin toss experiment consisting of N trials 
#Biased Probability

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

N=eval(input('Enter the number of trials : '))
m=eval(input('Enter the number of samples for set of trials : '))
pr=eval(input('Enter the probability of getting head : '))

x=lambda n:np.mean(rn.choice([1,0],p=[pr,1-pr],size=n))			# 1 stands for head, 0 stand for tail
#y=lambda n:np.mean(rn.choice([0,1],p=[pr,1-pr],size=n))
y=lambda n:np.mean(1-rn.choice([1,0],p=[pr,1-pr],size=n))

xhead=[x(N) for i in range(m)]
ytail=[y(N) for i in range(m)]

plt.title('Histogram for tossing of biased coin for set of trials =%2i'%(m))
plt.xlim(0,1)
plt.hist(xhead,bins=10,rwidth=0.9,histtype='bar',label='Head',color='c')
plt.hist(ytail,bins=10,rwidth=0.9,histtype='bar',label='Tail',color='orange')
plt.legend(loc='upper right')
plt.xlabel('Probability of getting head and tail per set of trials')
plt.show()
