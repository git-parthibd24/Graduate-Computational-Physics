#Question 4
#Determination of Wien's Displacement constant by solving the maxima equation from Planck's spectral energy density formula using Bisection Method

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return 5*np.exp(-x)+x-5

x=np.linspace(-100,100,1000)
plt.plot(x,function(x),'r-')
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.xlim(-10,10)
plt.ylim(-2.5,2.5)
plt.grid()
plt.show()

while True:
    a=eval(input('Enter lower limit : '))
    b=eval(input('Enter upper limit : '))
    if function(a)*function(b)<0:
        break
    print('No real root is found in the interval\nEnter new interval')

error=eval(input('Enter tolerance : '))
dx=b-a
n=np.round((abs(np.log(dx/error)))/np.log(2),0)
i=0
while True:
    i+=1
    x=(a+b)/2
    if function(a)*function(x)<0:
        b=x
    else:
        a=x
    if i==n:
        break
print('The value of real root in the givn interval is :',format(x,'0.4f'))
print('No. of iteration is:',i)

h=6.626*10**(-34)   #in J-S
c=3*10**8           #in m/s^2
kB=1.38*10**(-23)   #in J/K
b=h*c/(kB*x)
print('The value of Wiens displacement constant is :',format(b,'0.5f'))

#Estimation of temperature of sun surface
lamda=502           #in nm
print('The surface temperature of sun is :',format(b/(lamda*10**(-9)),'0.4f'),'degree celcius')
