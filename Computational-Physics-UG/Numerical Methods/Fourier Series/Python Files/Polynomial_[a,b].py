#Fourier series for polynomial waveform using quad() in [a,b] interval
#Using List Comprehension

import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

#Defining the polynomial function
N=int(input('Enter order of polynomial : '))
y=lambda x: x**N

#Display limits
L1=eval(input('Enter lower limit of display : '))
L2=eval(input('Enter upper limit of display : '))
x=np.linspace(L1,L2,10000)                               #This is the region where the Fourier series is displayed
xs=np.linspace(-Ls/2,Ls/2,10000)                         #This is the region (1 period) to display the original function 	

#Fourier wave parameters
a,b=eval(input('Enter lower and upper limits of the period : '))
L=b-a
f=lambda x: x**N
fc=lambda x,i: x**N*np.cos(2*np.pi*i*x/L)
fs=lambda x,i: x**N*np.sin(2*np.pi*i*x/L)

#Evaluation of coefficients
n=100                                     #No. of terms used for the series

a0=2/(L)*quad(f,a,b,limit=200)[0]
ai=lambda i: 2/(L)*quad(fc,a,b,args=(i,),limit=200)[0]      #args=(i,) keeps i constant as 2nd argument as passed in the function and treats x variable for the quad() integration
bi=lambda i: 2/(L)*quad(fs,a,b,args=(i,),limit=200)[0]

#Performing Fourier Series Sum		   
s=0.5*a0+sum([ai(i)*np.cos(2*np.pi*i*x/L)+bi(i)*np.sin(2*np.pi*i*x/L) for i in range(1,n)])


plt.plot(x,s,'-',color='green',linewidth='1.0',label='Fourier Series')
plt.plot(x,y(x),'r--',label='Original Function')
plt.axhline(color='gray',lw='1.0')
plt.axvline(color='gray',lw='1.0')
plt.title('Fourier Series for polynomial waveform in [a,b]')
plt.legend(loc='best',prop={'size':7})
plt.show()
