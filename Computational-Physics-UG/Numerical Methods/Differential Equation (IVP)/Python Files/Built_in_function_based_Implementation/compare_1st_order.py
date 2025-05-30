#Plotting numerical result and exact solution of an ODE using odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def model(y,x):
    return (x+1)**3+(2/(x+1))*y
    
f_sol=lambda x:(1/2)*(200+402*x+205*x**2+4*x**3+x**4)

y0=100
xval=np.linspace(0,10,100)                     #x0=0,xfinal=10 
sol=odeint(model,y0,xval)

plt.title('Plots of numerical and exact solution')
plt.xlabel('X-value')
plt.ylabel('Y-value')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.plot(xval,sol,'r--',lw=2,label='Numerical Result')
plt.plot(xval[::4],f_sol(xval)[::4],'bo',label='Analytical Result')
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Built_in_function_based_Implementation/compare_1st_order.png')
plt.show()
