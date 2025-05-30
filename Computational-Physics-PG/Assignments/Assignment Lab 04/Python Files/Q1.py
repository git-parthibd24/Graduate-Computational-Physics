#Question 1
#Find roots using bisection method for given equation

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-4*x+np.exp(-x)

x=np.linspace(-100,100,1000)
plt.plot(x,f(x),'r-')
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.grid()
plt.xlim(-25,25)
plt.ylim(-20,50)
plt.show()

while True:
    a=eval(input('Enter lower limit : '))
    b=eval(input('Enter upper limit : '))
    if f(a)*f(b)<0:
        break
    print("No real roots found in the interval\nEnter new interval")
error=eval(input('Enter error value : '))
i=0
while True:
    i+=1
    x=(a+b)/2
    if f(a)*f(x)<0:
        b=x
    else:
        a=x
    if f(x)==0 or abs(a-b)<=error:
        break
print('The value of real root is in that interval :',format(x,"0.4f"))
print('No. of iterations is :',i)
