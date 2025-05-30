#Question 8
#Perform linear interpolation to find refractive index corresponding to an unknown wavelength

import numpy as np
import matplotlib.pyplot as plt

loadfile=np.loadtxt('S:\\Documents\\Github\\Computational-Physics-PG\\Assignments\\Assignment Lab 04\\Python Files\\refractive_index.txt', skiprows=1)
wavelength=loadfile[:,0]
refractive_index=loadfile[:,1]
plt.plot(wavelength,refractive_index,'r-')
plt.axhline(y=0,color='black',linestyle='--',linewidth=2,alpha=1)
plt.axvline(x=0,color='black',linestyle='--',linewidth=2,alpha=1)
plt.ylim(1.48,1.54)
plt.xlabel('Wavelength in Angstrom')
plt.ylabel('Refractive Index')
plt.grid()
plt.show()

#Linear Interpolation
x=eval(input('Enter wavelength : '))

if wavelength[0]<=x<=wavelength[-1]:    
    for i in range(len(wavelength)-1):
        if wavelength[i]<x<wavelength[i+1]:
            y=((wavelength[i+1]-x)/(wavelength[i+1]-wavelength[i]))*refractive_index[i]+((x-wavelength[i])/(wavelength[i+1]-wavelength[i]))*refractive_index[i+1]
        elif x==wavelength[i]:
            y=refractive_index[i]
    print('The refractive index for',x,'Angstrom is :',format(y,'0.5f'))

else:
    print('Value out of range of interpolation')


        
