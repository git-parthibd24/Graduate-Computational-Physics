#Fourier series for triangular waveform using quad() in [-pi,pi] interval

import matplotlib.pyplot as plt
from scipy.signal import sawtooth
from scipy.integrate import quad
import numpy as np

#Defining the triangular wave function
L=eval(input('Enter the period of the triangular wave : '))
m=2*np.pi/L                                              #Periodicity of the function 
y=lambda x: sawtooth(m*x,width=0.5)

#Display limits
L1=eval(input('Enter lower limit of display : '))
L2=eval(input('Enter upper limit of display : '))
x=np.linspace(L1,L2,10000)                               #This is the region where the Fourier series is displayed
xs=np.linspace(-L/2,L/2,10000)                           #This is the region (1 period) to display the original function 	

#Fourier wave parameters
f=lambda x: sawtooth(m*x,width=0.5)
fc=lambda x: sawtooth(m*x,width=0.5)*np.cos(i*x)
fs=lambda x: sawtooth(m*x,width=0.5)*np.sin(i*x)

#Evaluation of coefficients
n=100                                     #No. of terms used for the series

a0=2/(2*np.pi)*quad(f,-np.pi,np.pi,limit=200)[0]

Ai=[]
for i in range(n):
	ai=2/(2*np.pi)*quad(fc,-np.pi,np.pi,limit=200)[0]
	Ai.append(ai)

Bi=[]
for i in range(n):
	bi=2/(2*np.pi)*quad(fs,-np.pi,np.pi,limit=200)[0]
	Bi.append(bi)

#Performing Fourier Series Sum		   
s=0.0
for i in range(n):
	if i==0:
		s=s+a0/2
	else:
		s=s+(Ai[i]*np.cos(i*x)+Bi[i]*np.sin(i*x))      #The wave stretches over the display limits

plt.plot(x,s,'-',color='green',linewidth='1.0',label='Fourier Series')
plt.plot(xs,y(xs),'r--',label='Original Function')
plt.axhline(color='gray',lw='1.0')
plt.axvline(color='gray',lw='1.0')
plt.title(r'Fourier Series for triangular waveform in [$-\pi$,$\pi$]')
plt.legend(loc='best',prop={'size':7})
plt.show()
