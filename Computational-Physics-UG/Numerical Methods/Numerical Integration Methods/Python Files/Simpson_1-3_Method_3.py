#Simpson's 1/3 Method for numerical integation
#Method 3 (Same implementaion as of Method 2 but in different form)

import numpy as np

def f(x):
    return x*np.exp(x)
a=eval(input('Enter the value of lower limit : '))
b=eval(input('Enter the value of upper limit : '))

S0=0
S1=f(a)+f(b)
n=2

while abs(S1-S0)>0.00001:
    S0=S1
    h=(b-a)/n                                     
    S1_odd=(4*sum([f(a+i*h) for i in range (1,n,2)]))*(h/3)
    S1_even=(2*sum([f(a+i*h) for i in range (1,n,2)]))*(h/3)
    S1=S1_even+S1_odd
    n=n+2
    
print('The value of inegral is :',format(S1,'0.4f'))