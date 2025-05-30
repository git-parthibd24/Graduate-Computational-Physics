#Question 5
#Find all 6 roots of given function using Newton Raphson Method

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1
def derivative(x):
    return 6*924*x**5-5*2772*x**4+4*3150*x**3-3*1680*x**2+2*420*x-42
    

x=np.linspace(-100,100,1000000)
plt.plot(x,function(x),'r-')
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.xlim(0,1)
plt.ylim(-2.5,2.5)
plt.grid()
plt.show()

error=eval(input('Enter tolerance : '))
for i in range(6):
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
    print('The value of real root in the given interval is :',format(x0,'0.10f'))
    print('No. of iteration is:',i)
