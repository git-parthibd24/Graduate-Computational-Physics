#Plotting Maxwell-Boltzmann velocity Distribution

import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import simpson

m=10*6.67*10**(-27) 			# 10 times the mass of proton in kg 
k=1.38*10**(-23) 				# in Joule per Kelvin 
v=np.linspace(0,2000,1000) 		# in m/s
n=int(input('Enter number of temperatures to show : '))
t1=eval(input('Enter minimum temperature : '))
t2=eval(input('Enter maximun temperature : '))

def MBf(v,T):
	a=np.sqrt(k*T/m)
	return (np.sqrt(2.0/np.pi))*(1.0/a**3)*v**2*np.exp(-v**2/(2*a**2)) 
	
T=np.linspace(t1,t2,n) 			# Temperature in Kelvin
A=[]

plt.figure(figsize=(12,8))
for t in T:
	plt.plot(v,MBf(v,t),label="T=%8.2f K"%(t)) 
	area=simpson(MBf(v,t),x=v)
	A.append(area)
	plt.title("Maxwell Boltzmann’s Velocity Distribution for various temperature")
	plt.axhline(color='black',lw=0.5,ls='--')
	plt.axvline(color='black',lw=0.5,ls='--')
	plt.legend(loc="upper right") 
	plt.xlabel("Velocity in m/s") 
	plt.ylabel("Probability density in s/m")
	
print()
print('Temperature\t\tArea under the curve')
print('_____________________________________________')
print()
t=t1-(t2-t1)/(n-1)
for i in range(len(A)):
	t+=(t2-t1)/(n-1)
	print('',format(t,'0.2f'),'\t\t',(A[i]))
print()

plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Application to some physics problems\\Plots of Statistical Distributions\\Python Files\\MB_Velocity\\MB_Velocity.png')
	
plt.show()