#Trapezoidal Method for numerical integration
#Method 2 : Adaptive Trapezoidal Rule (Global Refinement)

import numpy as np
def f(x):
    return np.sin(x)
a=eval(input(' Enter lower limit : '))
b=eval(input(' Enter upper limit : '))
S0,S=0,0
n=2              #The interval will be splitted mimimum in 2 parts

while True:
    h=(b-a)/n
    S=(2*sum([f(a+i*h) for i in range (1,n)])+f(a)+f(b))*(h/2)                #The sum excludes 1st and last point. Intermediate points are doubly counted
    if abs(S-S0)<0.0000001:
        break
    n=n+1
    S0=S
print('The value of integral is :',format(S,'0.4f'))
