#Solution of  1st order Radioactive decay equation using odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(n,t):
    return -lamda*n

lamda=eval(input('Enter the decay constant : '))
n0=100
tval=np.linspace(0,10,100)                     #tinitial=0, tfinal=10
sol=odeint(model,n0,tval)

plt.title('Radioactive Decay Curve')
plt.xlabel('Time')
plt.ylabel('Number of atoms')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.grid()
plt.plot(tval[::2],sol[::2],'r--',lw=2)		#Skipping 2 points in plot
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Built_in_function_based_Implementation/radioactive_decay.png')
plt.show()
