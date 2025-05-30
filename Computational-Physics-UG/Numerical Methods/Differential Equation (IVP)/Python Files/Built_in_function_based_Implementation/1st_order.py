#Solution of 1st order ODE using odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(y,x):
    return y-x
    
y0=0
xval=np.linspace(0,1.5,100)                     #x0=0, xfinal=1.5
sol=odeint(model,y0,xval)

plt.title('Curve of the solution of Diffferential Equation')
plt.xlabel('xvalues')
plt.ylabel('y-values')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.plot(xval[::2],sol[::2],'r--',lw=2)		    #Skipping 2 points in plot
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Built_in_function_based_Implementation/odeint_1.png')
plt.show()
