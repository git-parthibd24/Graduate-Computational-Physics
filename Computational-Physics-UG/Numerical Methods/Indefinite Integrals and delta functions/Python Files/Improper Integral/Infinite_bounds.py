#Dynamic range update

import numpy as np
a,b,c=4,2,8
f=lambda x:np.exp(-a*x**2+b*x+c)
tol=1e-10

def trapezoidal(f,a,b):
    S0,S=0,0
    n=2
    while True:
        h=(b-a)/n
        S=(2*sum([f(a+i*h) for i in range(1,n)])+f(a)+f(b))*(h/2)
        if abs(S-S0)<0.0000001:
            break
        n+=1
        S0=S
    return S

up=10
low=-up
IO=trapezoidal(f,low,up)
while True:
    I=IO
    up=up+1
    low=low-1
    IO=trapezoidal(f,low,up)
    if abs(IO-I)<tol:
        break
Iexact=np.sqrt(np.pi/a)*np.exp((b**2)/(4*a)+c)
print('The value of integral of Gaussian Integral :',IO,'and the exact value using formula is:',Iexact)
