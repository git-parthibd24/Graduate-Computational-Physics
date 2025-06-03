#Probability Plot of Coin Tossing

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

N=range(1,1000)
pr=eval(input('Probability of getting Head : '))
X=rn.choice([1,0],p=[pr,1-pr],size=1000)

H=[np.sum(X[:i])/float(i) for i in N]
T=[1-(np.sum(X[:i])/float(i)) for i in N]

plt.title('Plot to show average no. of Heads/Tails with imcreasing no. of tosses')
plt.plot(N,H,label='Average no. of Heads per toss')
plt.plot(N,T,label='Average no. of Tails per toss')
plt.xlabel('No. of tosses')
plt.ylabel('No. of Heads/Tails per toss')
plt.legend(loc='upper right')
plt.axhline(0.5,color='r')
plt.axvline(color='black',ls='--')
plt.show()
