#Fourier Series of Full Wave Rectifier Signal

import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

#Defining the signal
y=lambda x: abs(np.sin(x))

#Display limits
L1=eval(input('Enter lower limit of display : '))
L2=eval(input('Enter upper limit of display : '))
x=np.linspace(L1,L2,10000)                               #This is the region where the Fourier series is displayed
xs=np.linspace(-np.pi,np.pi,10000)                       #This is the region (1 period) to display the original function 	

#Fourier wave parameters
f=lambda x: abs(np.sin(x))
fc=lambda x,i: abs(np.sin(x))*np.cos(i*x)
fs=lambda x,i: abs(np.sin(x))*np.sin(i*x)

#Evaluation of coefficients
n=100                                     #No. of terms used for the series

a0=2/(2*np.pi)*quad(f,-np.pi,np.pi,limit=200)[0]
ai=lambda i: 2/(2*np.pi)*quad(fc,-np.pi,np.pi,args=(i,),limit=200)[0]      #args=(i,) keeps i constant as 2nd argument as passed in the function and treats x variable for the quad() integration
bi=lambda i: 2/(2*np.pi)*quad(fs,-np.pi,np.pi,args=(i,),limit=200)[0]

#Performing Fourier Series Sum		   
s=0.5*a0+sum([ai(i)*np.cos(i*x)+bi(i)*np.sin(i*x) for i in range(1,n)])


plt.plot(x,s,'-',color='green',linewidth='1.0',label='Fourier Series')
plt.plot(xs,y(xs),'r--',label='Original Function')
plt.axhline(color='gray',lw='1.0')
plt.axvline(color='gray',lw='1.0')
plt.title(r'Fourier Series for full wave rectifier signal in [$\pi$,$-\pi$]')
plt.legend(loc='best',prop={'size':7})
plt.show()
