#Trapezoidal Method for numerical integration
#Method 1 : Composite Trapezoidal Rule

import numpy as np
def f(x):
    return x*np.exp(x)

a=eval(input(' Enter lower limit : '))
b=eval(input(' Enter upper limit : '))
n=int(input('Enter number of sub intervals : '))
h=(b-a)/n
s=0.0

for i in range(n):
    s=s+f(a+(i+0)*h)+f(a+(i+1)*h)                #Double counting of intermediate elements occurs with next iteration
s=s*(h/2)
print('The value of integral is :',format(s,'0.4f'))
