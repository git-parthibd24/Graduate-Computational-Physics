#Simulation of Radioactive Decay as Stochastic Process
#Method 2

import random as rm
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(N,t):
	return -N*Lambda
	
Lambda=eval(input('Enter the decay constant : '))
N0=int(input('Enter initial number of nuclei : '))
tfinal=int(input('Enter final time : '))
t=np.arange(0,tfinal,1)
sol=odeint(model,N0,t)[:,0]

N=[]
for i in t:
	N.append(N0)
	count=0
	for j in range(N0):
		if rm.random() < Lambda:
			count=count+1 
	N0=N0-count
	
plt.plot(t,N,color='red',label='Simulated')
plt.plot(t[::10],sol[::10],'o',color='blue',label='Theoretical',ms=2)
plt.title('Simulation of Radioactive Nuclear Decay\n'+r'Initial number of nuclei = %2i, Final number of nuclei = %2i, Time Steps = %2i'%(N0,N[-1],tfinal))
plt.xlabel('Time')
plt.ylabel('Number of Nuclei left')
plt.axhline(color='black')
plt.axvline(color='black')
plt.legend()
plt.grid()
plt.show()	
