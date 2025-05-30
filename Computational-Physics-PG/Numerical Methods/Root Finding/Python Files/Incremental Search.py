#Incremental Search Method for root finding
#This method is very limited in its capacity

import numpy as np    
import matplotlib.pyplot as plt

def rootsearch(f,a,b,dx):   #[a,b] is interval of searching. dx is increment of search
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)

    while np.sign(f1)==np.sign(f2):
        if x1>=b: 
            return None,None
        x1=x2; f1=f2        #Incrementing along x direction
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2        #The supposed root lies between these

x=np.linspace(-1,1,400)
def f(x): 
    return x**3-10.0*x**2+5.0

a=0.0; b=1.0                #Initial interval of search
for i in range(5):          #Calling the function multiple times to reduce interval of search with each iteration
    dx=(b-a)/10.0
    a_new,b_new=rootsearch(f,a,b,dx)
    if a_new is None or b_new is None:
        break
    else:
        a,b=a_new,b_new

if a_new is None or b_new is None:
    print('No root found in the given interval')
else:
    x=(a+b)/2.0             #This is the approximated root
    print('The root is :','{:6.4f}'.format(x))