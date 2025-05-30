#Question 7
#Find all roots using bisection method for infinite discontinuous function for given range (0,20)

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x-np.tan(x)

x=np.linspace(-0.1,20,1000000)
plt.plot(x,f(x),'r-')
plt.axvline(x=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.axhline(y=0,color='gray',linestyle='--',linewidth=2,alpha=1)
plt.xticks(np.linspace(-1,20,10))
plt.ylim(-10,10)
plt.grid()
plt.show()

def bisect(a,b):
    while True:
        x=(a+b)/2
        if f(a)*f(x)<0:
            b=x
        else:
            a=x
        if f(x)==0 or abs(a-b)<=0.0001:
            break
    return x

a,b,L=[],[],[]
for i in range(len(x)-1):
    if f(x[i])*f(x[i+1])<0:
        a.append(x[i])
        b.append(x[i+1])


print('The value of real roots in the interval (0,20) are :')
print()
for i in range(0,(len(a)-2),2):                      #with each root, there is a discontinuity next to it which is mistakenly flagged as root by bisection. Hence those points must be skipped
    print(format(bisect(a[i],b[i]),'0.4f'),end=',')
print(format(bisect(a[-2],b[-2]),'0.4f'))


