#Simulation of Radioactive Decay as Stochastic Process
#Method 1

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

Lambda=eval(input('Enter the value of decay constant : '))
N0=eval(input('Enter the initial number of nuclei : '))
tfinal=eval(input('Enter the final time : '))

nloop=number=N0
N,Time=[N0],[0]

for time in range(1,tfinal+1):
	for nuclei in range(1,number+1):
		decay=rn.random()
		if decay<Lambda:
			nloop=nloop-1
	number=nloop
	N.append(number)
	Time.append(time)

T=np.array(Time)
NN=N0*np.exp(-Lambda*T)                                 #can't use list here

plt.plot(Time,N,color='red',label='Simulated')
plt.plot(Time[::10],NN[::10],'o',color='blue',label='Theoretical',ms=2)
plt.title('Simulation of Radioactive Nuclear Decay\n'+r'Initial number of nuclei = %2i, Final number of nuclei = %2i, Time Steps = %2i'%(N0,N[-1],tfinal))
plt.xlabel('Time')
plt.ylabel('Number of Nuclei left')
plt.axhline(color='black')
plt.axvline(color='black')
plt.legend()
plt.grid()
plt.show()
