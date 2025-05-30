import numpy.random as rn
import numpy as np
import matplotlib.pyplot as plt

r=rn.random(1000000)

fig=plt.figure(figsize=(10,8),dpi=100)  #This must be at the beginning of plot
plt.title('Histogram for Random number generation')
plt.hist(r,bins=30,rwidth=0.9,range=None,density=False,color='green',label='numpy.random.random()',histtype='bar')
plt.legend(loc='best')

plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Histogram_plot\\Python File\\histogram.png')
plt.show()
