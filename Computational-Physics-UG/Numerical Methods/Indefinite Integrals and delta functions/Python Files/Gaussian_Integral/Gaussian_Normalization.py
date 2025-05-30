#Plotting and thereby cheking constancy of Gaussian Integral for any sigma

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
sigma=np.linspace(1,11,100)
mu=eval(input('Enter the mu value : '))
m=[]
for i in sigma:
    f=lambda x:1/(np.sqrt(2*np.pi)*i)*np.exp((-(x-mu)**2)/(2*i**2))
    I=quad(f,-np.inf,np.inf)[0]
    m.append(I)
   
plt.plot(sigma,m,'r--')
plt.title('Showing constancy of Gaussain integral for change in its width')
plt.xlabel(r'$\sigma$')
plt.ylabel('Value of Gaussian Integral')
plt.axhline(color='gray')
plt.axvline(color='gray')
plt.xlim(-12,12)
plt.ylim(-2,2)

plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Gaussian_Integral/Normalization.png')
plt.show()
