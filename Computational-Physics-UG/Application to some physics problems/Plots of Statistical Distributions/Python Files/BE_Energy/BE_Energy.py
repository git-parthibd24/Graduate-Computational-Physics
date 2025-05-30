#Plotting Bose-Einstein energy Distribution

import numpy as np
import matplotlib.pyplot as plt 

n=int(input('Enter number of temperatures to show : '))
t2=eval(input('Enter maximum temperature : '))

def f(E,T): 
	return 1.0/(np.exp((E-mu)/(K*T)-1)) 
	
mu=0.1 					# in eV
K=8.617*10**(-5) 		# in eV/K 
E=np.linspace(1*mu,1.8*mu,1000) 
T=np.linspace(5,t2,n) 

plt.figure(figsize=(12,8))
for t in T:
	plt.title("Bose-Einstein Distribution for various Temperature") 
	plt.xlabel(r'$\frac{E}{\mu}$')
	plt.ylabel("f(E,T)") 
	plt.axhline(color='black',lw=0.5,ls='--')
	plt.axvline(x=0.9,color='black',lw=0.5,ls='--')
	plt.plot(E/mu,f(E,t),label="T=%8.2f"%(t)) 
	plt.legend(loc="upper right") 
	plt.pause(0.5)
	
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Application to some physics problems\\Plots of Statistical Distributions\\Python Files\\BE_Energy\\BE_Energy.png')
	
plt.show()