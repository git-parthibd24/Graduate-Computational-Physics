#Question 6
#Find roots of following function using bisection and Newton Raphson method and compare which is more efficient

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**2-4*x+np.exp(-x)

def derivative(x):
    return 2*x-4-np.exp(-x)

x=np.linspace(-100,100,1000)
plt.plot(x,function(x),'r-')
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.xlim(-10,10)
plt.ylim(-2.5,2.5)
plt.grid()
plt.show()

f=int(input('Enter 0 for Bisection Method and 1 for Newton raphson Method : '))

#Bisection Method
if f==0:
    for i in range(2):
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
        print('No. of iteration in Bisection Method is:',i)


#Newton Raphson Method
if f==1:
    error=eval(input('Enter tolerance : '))
    for i in range(2):
        x0=eval(input('Enter initial guess of root : '))
        k_in=function(x0)/derivative(x0)
        n=np.round((abs(np.log(abs(k_in)/error)))/np.log(2),0)
        i=0
        while True:
            i+=1
            k=-function(x0)/derivative(x0)
            x0=x0+k
            if i==n:
                break
        print('The value of real root in the given interval is :',format(x0,'0.4f'))
        print('No. of iteration in Newton Raphson Method is :',i)
