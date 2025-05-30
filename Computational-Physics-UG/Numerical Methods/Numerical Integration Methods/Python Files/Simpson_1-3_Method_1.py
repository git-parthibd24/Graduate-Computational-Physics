#Simpson's 1/3 Method for numerical integation
#Method 1

import numpy as np

def f(x):
    return x*np.exp(x)
a=eval(input('Enter the value of lower limit : '))
b=eval(input('Enter the value of upper limit : '))
n=int(input('Enter value of sub interval : '))

if n%2==0:
    h=(b-a)/n
    s=0.0
    for i in range(0,n,2):                                     #Give lower range value as must (as 0 here)
        s=s+f(a+(i+0)*h)+4*f(a+(i+1)*h)+f(a+(i+2)*h)           #End points are even points. With each iteration, the even points are doubled except extreme end points
    s=s*(h/3)
    print('The value of inegral is :',format(s,'0.4f'))

else:
    print("Enter subinterval as multiple of 2")