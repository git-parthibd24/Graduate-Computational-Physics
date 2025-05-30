#Solution of Forced Harmonic Motion ODE using odeint()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def fhm(u,t):
    x1=u[0]
    x2=u[1]
    dx1dt1=x2
    x=x1
    x1,x2=u
    dx2dt2=-mu*x2-k*x+F*np.cos(w*t)
    list=[dx1dt1,dx2dt2]    #Packed in a list
    return list
    
mu=eval(input('Enter the value of damping constant : '))
k=eval(input('Enter the value of force constant of oscillation : '))
F=eval(input('Enter peak value of external periodic force : '))
w=eval(input('Enter the angular frequency of periodic force : '))
xo1=eval(input('Enter initial value of displacement : '))
xo2=eval(input('Enter initial value of velocity : '))
u0=[xo1,xo2]                #Initial values of x1 and x2 packed in list
trange=np.linspace(0,10,150)
sol=odeint(fhm,u0,trange)
plt.title('Solution of the differential equation Forced Harmonic Oscillation ')
plt.xlabel('Time')
plt.ylabel('Displacement and Velocity')
plt.plot(trange,sol[:,0],'r--',label='Displacement')
plt.plot(trange,sol[:,1],'b--',label='Velocity')
plt.axhline(c='black',lw=0.5)
plt.axvline(c='black',lw=0.5)
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Built_in_function_based_Implementation/forced_HO.png')
plt.show()
