#Simpson's 1/3 Method for numerical integation
#Method 2 (increasing accuracy)

import numpy as np
def f(x):
    return x*np.exp(x)
a=eval(input('Enter the value of lower limit : '))
b=eval(input('Enter the value of upper limit : '))

S0=0
S1=f(a)+f(b)
n=2

while abs(S1-S0)>0.0001:
    S0=S1
    h=(b-a)/n
    k=4
    for i in range(1,n):                                     
        S1=S1+k*f(a+i*h)
        k=6-k
    S1=S1*(h/3)
    n=n+2

print('The value of inegral is :',format(S1,'0.4f'))