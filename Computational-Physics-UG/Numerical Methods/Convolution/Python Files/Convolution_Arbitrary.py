import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def f(x):
	return np.sin(x)
def g(x):
	return np.exp(x)

up=eval(input('Enter upper limit : '))
low=-up
n=int(input('Enter no. of intervals : '))

X=np.linspace(low,up,n)
conv=[]

for x in X:
	xp=np.linspace(0,x,100)              #Finite Convolution
	h=f(x)*g(x-xp)
	conv.append(simpson(h,xp))
	
plt.plot(X,f(X),'r--',label='Sinusoidal Function')
plt.plot(X,g(X),'g--',label='Exponential Function')
plt.plot(X,conv,'b-',label='Convolved function')
plt.title('Convolution of two functions')
plt.axvline(0,c='gray',ls='--',lw=1)
plt.axhline(0,c='gray',ls='--',lw=1)
plt.legend(loc='best',prop={'size':10})
plt.xlim(-10,10)
plt.ylim(-10,10)

plt.show()
