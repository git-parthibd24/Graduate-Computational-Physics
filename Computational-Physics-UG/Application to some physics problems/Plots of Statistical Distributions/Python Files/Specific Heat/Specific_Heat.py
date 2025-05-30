#Plotting three laws of specific heat

import numpy  as  np
import matplotlib.pyplot as plt 
from scipy.integrate import quad

Theta_E=eval(input("Enter a value for the Einstein temperature : ")) 
Theta_D=eval(input("Enter a value for the Debye temperature : ")) 
Temp=np.linspace(0.0001,1000,10000)

def integrate(T):
	I=quad(lambda x:np.exp(x)*x**4/(np.exp(x)-1)**2,0,Theta_D/T) 
	return I[0]

Dulong_Petit=np.ones(10000)
Einstein=lambda Temp:(Theta_E/Temp)**2*np.exp(Theta_E/Temp)/(np.exp(Theta_E/Temp)-1)**2 
Debye=[3*(T/Theta_E)**3*integrate(T) for T in Temp] 

plt.figure(figsize=(12,8))
plt.plot(Temp,Dulong_Petit,Temp,Einstein(Temp),Temp,Debye)
plt.suptitle(r'Plot  of  the  $\frac{C_v}{3R}$  vs.  $T$  curves')
plt.title("For Dulong & Petit’s Law, Einstein’s Theory and the Debye Approximation") 
plt.xlim(0,50)
plt.ylim(0,1.15) 
plt.grid() 
plt.xlabel("Temperature")
plt.ylabel(r'$\frac{C_v}{3R}$',fontsize=15)
plt.legend(["Dulong & Petit’s Law","Einstein’s Theory","Debye Approximation"],loc="best") 

plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Application to some physics problems\\Plots of Statistical Distributions\\Python Files\\Specific Heat\\Specific_Heat.png')
	
plt.show()