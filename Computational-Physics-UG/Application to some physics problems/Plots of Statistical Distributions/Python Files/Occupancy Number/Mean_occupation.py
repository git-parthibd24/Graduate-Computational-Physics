#Plotting mean occupancy number(most probable distribution function) with respect to energy for MB,FD and BE statistics

import numpy as np
import matplotlib.pyplot as plt 

def f(x,a): 
	return 1.0/(np.exp(x) + a) 

x=np.linspace(-2.0,3,100)

plt.figure(figsize=(12,8))
plt.title("Mean occupancy for single particle state") 
plt.xlabel(r'$\frac{\epsilon-\mu}{kT}$') 
plt.ylabel(r'$\langle n_{\epsilon}\rangle$') 
plt.ylim(-0.1,2)
plt.plot(x,f(x,0),label="Maxwell Boltzmann") 
plt.plot(x,f(x,1),label="Fermi Dirac") 
plt.plot(x,f(x,-1),label="Bose Einstein") 
plt.axvline(color='black',ls='--')
plt.axhline(color='black',ls='--') 
plt.legend(loc="upper right")

plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Application to some physics problems\\Plots of Statistical Distributions\\Python Files\\Occupancy Number\\Occupancy_Number.png')
	
plt.show()