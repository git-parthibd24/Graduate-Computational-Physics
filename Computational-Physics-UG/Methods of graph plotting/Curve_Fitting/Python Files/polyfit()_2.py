#Curve fitting using polyfit and polyval of submodule in numpy 
#It is used for least square fit of polynomial to data

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

x=np.array([0,2,4,6,8,10,12,14,16,18],dtype=float)
y=np.array([1.1,11.1,28.7,55.0,200.5,131.2,181,238.9,305,379])
coeffs=poly.polyfit(x,y,2)      #The polynomial coefficients are stored in 0,1,2 positions of the array
rmsfit=poly.polyval(x,coeffs)   #Generates fitted datapoints at designated raw data points

def s(x):
    return coeffs[0]+coeffs[1]*x+coeffs[2]*x**2

plt.plot(x,rmsfit,'ro',label='rmsfit')
plt.plot(x,s(x),'b-',label='polyfit')
plt.plot(x,y,'go',label='raw data')
plt.legend()
plt.show()