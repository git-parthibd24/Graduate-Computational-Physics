#Question 2
#Find roots of using Newton Raphson Method of given equation

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**2-4*x+np.exp(-x)    
def derivative(x):
    return 2*x-4-np.exp(-x)

x=np.linspace(-100,100,1000)
plt.plot(x,function(x),'r-')
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.grid()
plt.xlim(-25,25)
plt.ylim(-20,50)
plt.show()

x=eval(input("Enter initial assumption of root : "))   #Always assume a value that is near to the actual root. otherwise for multiple roots the initial assumption might converge to other roots. It depends on the position of local extremas relative to initial assumption.
error=eval(input("Enter tolerance : "))
i=0
while True:
    i+=1
    k=-function(x)/derivative(x)
    x=x+k
    if abs(k)<=error:
        break
print("The value of the root is :",format(x,"0.4f"))
print('No. of iterations is :',i)
