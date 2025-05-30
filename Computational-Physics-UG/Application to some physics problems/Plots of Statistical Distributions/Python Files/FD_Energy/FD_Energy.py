#Plotting Fermi-Dirac energy Distribution

import numpy as np
import matplotlib.pyplot as plt 

n=int(input('Enter number of temperatures to show : '))
t2=eval(input('Enter maximum temperature : '))

def f(E,T): 
	return 1.0/(1.0+np.exp((E-Ef)/(K*T))) 
	
Ef=0.1 					# in eV
K=8.617*10**(-5) 		# in eV/K 
E=np.linspace(0,2*Ef,1000) 
T=np.linspace(5,t2,n) 

plt.figure(figsize=(12,8))
for t in T:
	plt.title("Fermi Dirac Distribution for various Temperature") 
	plt.xlabel(r'$\frac{E}{E_f}$')
	plt.ylabel("f(E,T)") 
	plt.axhline(color='black',lw=0.5,ls='--')
	plt.axvline(color='black',lw=0.5,ls='--')
	plt.plot(E/Ef,f(E,t),label="T=%8.2f"%(t)) 
	plt.legend(loc="upper right") 
	plt.pause(0.5)
	
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Application to some physics problems\\Plots of Statistical Distributions\\Python Files\\FD_Energy\\FD_Energy.png')
	
plt.show()