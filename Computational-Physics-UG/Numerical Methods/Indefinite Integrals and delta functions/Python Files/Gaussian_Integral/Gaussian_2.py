#To check the similarity with defined Gaussian Integral by numerically evaluating Gausssian integral
#Using conditional while loop and simpson()

import numpy as np
from scipy.integrate import simpson

def f(x,a,b,c):
    return np.exp(-a*x**2+b*x+c)
    
a,b,c=eval(input('Enter values of a,b,c : '))
up=eval(input('Enter upper limit : '))
low=-up
dn=eval(input('Enter width of subinterval :'))        #dn=(up-low)/n
X=np.arange(low,up,dn)
tol=1e-10

IO=simpson(f(X,a,b,c),X) 
diff=1000 
                                         #TO enter into the loop such that I0-I!=0
while diff>tol:
    I=IO
    up=up+1
    low=low-1
    X=np.arange(low,up,dn)
    IO=simpson(f(X,a,b,c),X)
    diff=abs(I-IO)
Iexact=np.sqrt(np.pi/a)*np.exp((b**2)/(4*a)+c)

print('The value of integral of Gaussian Function :',IO,'and the exact value is :',Iexact)
print(IO//Iexact)
if round(IO/Iexact)==1:
    print('The Gaussian Functon is same as the given function with ratio of 1')
else:
    print('Gaussian function is not same to the given function')
