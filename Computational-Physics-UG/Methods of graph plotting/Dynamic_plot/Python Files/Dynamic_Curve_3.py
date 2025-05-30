#Propagating wave

import numpy as np
import matplotlib.pyplot as plt

x,dx=np.linspace(0,np.pi,1000,retstep=True)

def u(x,t):
    return np.sin(10*x-5*t)

#Plot initial wave
t=0.0
A, =plt.plot(x,u(x,t))     #This creates an object 'line' that stores the plot x vs y and extracts 1st element of the list
plt.ylabel('y-position')
plt.xlabel('x-position')
plt.ylim(-1,1)
plt.axhline(0,color='black')
plt.axvline(0,color='black')

#Animation loop
while t<5:
    plt.title(r'$t=%10.5f$ s'%t)
    A.set_ydata(u(x,t))
    t+=0.01               #updating y data without disturbing x data
    plt.pause(0.01)       #pauses the curve for this duration

plt.show()    


