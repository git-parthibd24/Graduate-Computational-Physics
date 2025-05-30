#Question 2
#Handling error function

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

a=0
b=np.arange(0,3.1,0.1)

def simps(a,b,f):
    S0=0
    S1=f(a)+f(b)
    n=2
    while abs(S1-S0)>0.0000001:
        S0=S1
        h=(b-a)/n
        k=4
        for i in range(1,n):                                     
            S1=S1+k*f(a+i*h)
            k=6-k
        S1=S1*(h/3)
        n=n+2
    return S1

S1_list=[]
for i in range(len(b)):
    S1=simps(a,b[i],f)
    S1_list.append(S1)
    print('The value of integral for upper limit',np.round(b[i],3),'is :',format(S1,'0.4f'))
    print()

plt.plot(b,S1_list,'bo')
plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('Upper limit of erf() integral')
plt.ylabel('Integral Values')
plt.show()
