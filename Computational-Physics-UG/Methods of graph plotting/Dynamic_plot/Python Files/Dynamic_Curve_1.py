#Propagating wave

import numpy as np
import matplotlib.pyplot as plt

x,dx=np.linspace(0,np.pi,1000,retstep=True)

def u(x,t):
    return np.sin(10*x-5*t)
t=0.0
while t<5:
    plt.cla()        #clears the previous figure
    plt.title(r'$t=%10.5f$ s'%t)
    plt.ylabel('y-position')
    plt.xlabel('x-position')
    plt.ylim(-1,1)
    plt.plot(x,u(x,t))
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    t+=0.01
    plt.pause(0.01)  #pauses the curve for this duration

#keeping the last figure
plt.title(r'$t=%10.5f$ s'%t)
plt.ylabel('y-position')
plt.xlabel('x-position')
plt.ylim(-1,1)
plt.plot(x,u(x,t))
plt.axhline(0,color='black')
plt.axvline(0,color='black')

plt.show()    


