#Adaptive Quadrature to handle Type 2 indefinite integrals
#Changing x to t : t=1/(1+x) , x=(1-t)/t. So limits change to (0,1) from 0 to inf.
#quad() can handle singularities that are removable

import numpy as np
from scipy.integrate import quad
a,b,c=4,2,8
f=lambda x:np.exp(-a*x**2+b*x+c)

def g(t):
    return f((1-t)/t)*(1/t**2)

#g=lambda t:f((1-t)/t)  

low,up=0,1
res,err=quad(g,low,up)
res_or,err=quad(f,0,np.inf)
print('The integral using transformation is :',res)
print('The original integral is :',res_or)
