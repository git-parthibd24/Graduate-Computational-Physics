#Curve fitting using curve_fit of scipy module

import numpy as np 
from scipy.optimize import curve_fit 
from matplotlib import pyplot as plt 

#raw data
T=np.array([400,800,1200,1600,2000,2400,2800]) 
R=np.array([0.42,1.00,1.63,2.33,3.05,3.89,4.75])

#guessing function that can fit the data
def test(x,a,b): 
	return a*(x)+b

a=curve_fit(test,T,R)[0][0]
b=curve_fit(test,T,R)[0][1]

#generating the curve
def f(x):
	return a*x+b

plt.plot(T,R,'o',color='red',label="data") 
plt.plot(T,f(T),'--',color='blue',label="optimized data") 
plt.legend()
plt.xlabel('$T(K)$')
plt.ylabel('${R_t}/{R_d}$')
plt.show()
