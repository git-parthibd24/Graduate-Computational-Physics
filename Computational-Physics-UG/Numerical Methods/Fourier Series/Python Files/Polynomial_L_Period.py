#Fourier series for polynomial waveform using quad() in [-L/2,L/2] interval

import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

#Defining the polynomial function
N=int(input('Enter order of polynomial : '))
y=lambda x: x**N

#Display limits
L1=eval(input('Enter lower limit of display : '))
L2=eval(input('Enter upper limit of display : '))
x=np.linspace(L1,L2,10000)                               

#Fourier wave parameters
L=eval(input('Enter the period of Fourier Series : '))
Lf=L/2
f=lambda x: x**N
fc=lambda x: x**N*np.cos(2*np.pi*i*x/L)
fs=lambda x: x**N*np.sin(2*np.pi*i*x/L)

#Evaluation of coefficients
n=100                                     #No. of terms used for the series

a0=2/(L)*quad(f,-Lf,Lf,limit=200)[0]

Ai=[]
for i in range(n):
	ai=2/(L)*quad(fc,-Lf,Lf,limit=200)[0]
	Ai.append(ai)

Bi=[]
for i in range(n):
	bi=2/(L)*quad(fs,-Lf,Lf,limit=200)[0]
	Bi.append(bi)

#Performing Fourier Series Sum		   
s=0.0
for i in range(1,n):
	s=s+(Ai[i]*np.cos(2*np.pi*i*x/L)+Bi[i]*np.sin(2*np.pi*i*x/L))      #The wave stretches over the display limits
s=s+a0/2

plt.plot(x,s,'-',color='green',linewidth='1.0',label='Fourier Series')
plt.plot(x,y(x),'r--',label='Original Function')
plt.axhline(color='gray',lw='1.0')
plt.axvline(color='gray',lw='1.0')
plt.title('Fourier Series for polynomial waveform in [-L/2,L/2]')
plt.legend(loc='best',prop={'size':7})
plt.show()
