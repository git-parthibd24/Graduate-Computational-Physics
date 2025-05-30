#Curve fitting using polyfit of numpy module
#It is used for least square fit of polynomial to data

import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,2,4,6,8,10,12,14,16,18],dtype=float)
y=np.array([1.1,11.1,28.7,55.0,200.5,131.2,181,238.9,305,379])

param=np.polyfit(x,y,2)   #Arguments are x,y and degree of polynomial
newy=param[0]*x**2+param[1]*x+param[2]    #param[] are fitting parameters

plt.plot(x,y,'ro',label='Raw Data')
plt.plot(x,newy,'b-',label='Fitted Data')
plt.legend()
plt.show()

