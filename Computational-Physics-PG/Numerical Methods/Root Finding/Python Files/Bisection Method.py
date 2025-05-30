import numpy as np

def bisection_method(f,x1,x2,switch=1,tol=1.0e-9):   
    f1=f(x1)
    if f1==0.0: 
        return x1
    f2=f(x2)
    if f2==0.0: 
        return x2
    if np.sign(f1)==np.sign(f2):
        print('Root is not bracketed yet')
        return None
    
    n=int(np.ceil(np.log(abs(x2-x1)/tol)/np.log(2.0)))          #numpy.ceil() rounds up to nearest integer
    for i in range(n):
        x3=0.5*(x1+x2); 
        f3=f(x3)
        
        if switch==1 and abs(f3)>abs(f1) and abs(f3)>abs(f2):   #switch parameter is used as a safeguard to detect cases where the function value at the midpoint is increasing in magnitude rather than decreasing
            return None
        
        if f3==0.0: 
            return x3
        
        if np.sign(f2)!=np.sign(f3): 
            x1=x3; f1=f3

        else: 
            x2=x3; f2=f3

    return x3

def f(x): 
    return x**3-10.0*x**2+5.0

x=bisection_method(f,0.0,1.0,tol=1.0e-4)
if x is None:
    print('No root found in the given interval.')
else:
    print('The root is :','{:6.4f}'.format(x))