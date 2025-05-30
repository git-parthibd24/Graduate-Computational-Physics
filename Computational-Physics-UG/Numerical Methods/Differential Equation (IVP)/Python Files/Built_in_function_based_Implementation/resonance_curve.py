#PLotting Resonance Curve for Forced Harmonic Motion ODE using odeint()

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
xo1=eval(input('Enter initial value of displacement : '))
xo2=eval(input('Enter initial value of velocity : '))
u0=[xo1,xo2]                #Initial values of x1 and x2 packed in list
trange=np.arange(0,100,0.1)
freq=np.arange(0.5,10,0.02)
a=[]
v=[]

for w in freq:
    sol=odeint(fhm,u0,trange)
    amp=np.max(sol[:,0][-200:])           #removing transient portion
    a.append(amp)
for w in freq:
    sol=odeint(fhm,u0,trange)
    vel=np.max(sol[:,1][-200:])              #removing transient portion
    v.append(vel)

plt.subplot(121)
exactAmp=F/np.sqrt((k-freq**2)**2+mu**2*freq**2)
plt.title('Amplitude Resonance Curve ')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.plot(freq[::4],a[::4],'o',color='magenta',label='numerical value',ms=4)
plt.plot(freq,exactAmp,'-',color='blue',label='exact value')
plt.xlim(0,5)
plt.axhline(c='black',lw=0.5)
plt.axvline(c='black',lw=0.5)


plt.subplot(122)
exactVel=(F*freq)/np.sqrt((k-freq**2)**2+mu**2*freq**2)
plt.title('Velocity Resonance Curve ')
plt.xlabel('Frequency')
plt.ylabel('Velocity')
plt.plot(freq[::4],v[::4],'go',label='numerical value',ms=4)
plt.plot(freq,exactVel,'-',color='blue',label='exact value')
plt.xlim(0,5)
plt.axhline(c='black',lw=0.5)
plt.axvline(c='black',lw=0.5)
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (IVP)/Python Files/Built_in_function_based_Implementation/resonance_curve.png')
plt.show()
