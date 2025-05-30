#Curve fitting using curve_fit of scipy module

import numpy as np 
from scipy.optimize import curve_fit 
from matplotlib import pyplot as plt 

#raw data
x=np.linspace(0,10,num=50) 
y=7*8*np.exp(x)

#guessing function that can fit the data
def test(x,a,b): 
	return a*b*np.exp(x)

param,param_cov=curve_fit(test,x,y) 
print("Parameters") 
print(param) 
print("Covariance") 
print(param_cov)

#generating the curve
ans=param[0]*param[1]*np.exp(x)

plt.plot(x,y,'o',color='red',label="data") 
plt.plot(x, ans,'--',color='blue',label="optimized data") 
plt.legend()
plt.show()
