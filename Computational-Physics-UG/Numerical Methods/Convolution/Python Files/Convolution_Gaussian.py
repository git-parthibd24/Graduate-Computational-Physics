## import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def f(x,sigma,mu):
	return 1/(np.sqrt(2*np.pi)*sigma)*np.exp((-(x-mu)**2)/(2*sigma**2))

up=eval(input('Enter upper limit : '))
low=-up
n=int(input('Enter no. of intervals : '))
sigma1,sigma2=eval(input('Enter sigma values for Gaussian functions : '))
mu1,mu2=eval(input('Enter mu values for Gaussian functions : '))

X=np.linspace(low,up,n)
conv=[]
for x in X:
	h=f(X,sigma1,mu1)*f(x-X,sigma2,mu2)
	conv.append(simpson(h,X))
	
plt.plot(X,f(X,sigma1,mu1),'r--',label='1st Gaussian')
plt.plot(X,f(X,sigma2,mu2),'g--',label='2nd Gaussian')
plt.plot(X,conv,'b-',label='Convolved function')
plt.title('Convolution of Gaussian integrals')
plt.axvline(0,c='gray',ls='-',lw=1)
plt.axhline(0,c='gray',ls='-',lw=1)
plt.legend(loc='best',prop={'size':10})

plt.show()
