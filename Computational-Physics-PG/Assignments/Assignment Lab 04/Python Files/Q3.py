#Question 3
#Find roots of using Newton Raphson Method of given equation

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**3-1.2*x**2-8.19*x+13.23    
def derivative(x):
    return 3*x**2-1.2*x-8.19

x=np.linspace(-100,100,1000)
plt.plot(x,function(x),'r-')
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.grid()
plt.xlim(0,4)
plt.ylim(-20,50)
plt.show()

x=eval(input("Enter initial assumption of root : "))
error=eval(input("Enter tolerance : "))
k_in=function(x)/derivative(x)
n=np.round(abs(np.log(abs(k_in/error)))/np.log(2),0)
i=0
while True:
    i+=1
    k=-function(x)/derivative(x)
    x=x+k
    if i==n:
        break
print("The value of the root is :",format(x,"0.4f"))
print('No. of iterations is :',i)
