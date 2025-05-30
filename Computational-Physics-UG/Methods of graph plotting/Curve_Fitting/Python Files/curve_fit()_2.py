#Curve fitting using curve_fit of scipy module

import numpy as np 
from scipy.optimize import curve_fit 
from matplotlib import pyplot as plt 

#raw data
x=np.linspace(0,10,num=50) 
y=2*np.sin(x)+3

#guessing function that can fit the data
def test(x,a,b): 
	return a*np.sin(x)+b

param,param_cov=curve_fit(test,x,y) 
print("Parameters") 
print(param) 
print("Covariance") 
print(param_cov)

#generating the curve
ans=param[0]*np.sin(x)+param[1]

plt.plot(x,y,'o',color='red',label="data") 
plt.plot(x, ans,'--',color='blue',label="optimized data") 
plt.legend()
plt.show()
