#Plotting Maxwell-Boltzmann energy Distribution

import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import simpson

k=8.617*10**(-5) 			# in eV per Kelvin  (can be done in Joule/K)
E=np.linspace(0,0.4,1000) 	# in eV 
n=int(input('Enter number of temperatures to show : '))
t1=eval(input('Enter minimum temperature : '))
t2=eval(input('Enter maximun temprature : '))

def MBf(E,T):
	return (2.0/np.sqrt(np.pi))*(1.0/(k*T)**1.5)*E**0.5*np.exp(-E/(k*T)) 

T=np.linspace(t1,t2,n)		 # Temperature in Kelvin
A=[]

plt.figure(figsize=(12,8))
for t in T:
	plt.plot(E,MBf(E,t),label="T=%8.2f K"%(t)) 
	area=simpson(MBf(E,t),x=E)
	area=np.round(area,2) 
	A.append(area)
	plt.title("Maxwell Boltzmann’s Energy Distribution for various temperature") 
	plt.legend(loc="upper right")
	plt.axhline(color='black',lw=0.5,ls='--')
	plt.axvline(color='black',lw=0.5,ls='--')
	plt.xlabel("E in eV") 
	plt.ylabel("Probability density in 1/eV")
	
print()
print('Temperature\t\tArea under the curve')
print('_____________________________________________')
print()
t=t1-(t2-t1)/(n-1)
for i in range(len(A)):
	t+=(t2-t1)/(n-1)
	print('',format(t,'0.2f'),'\t\t',(A[i]))
print()
	
plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Application to some physics problems\\Plots of Statistical Distributions\\Python Files\\MB_Energy\\MB_Energy.png')
	
plt.show()