#Safe_Root_Search_General_Method

import numpy as np
def root_safe(f,df,a,b,tol):
    if f(a)==0.0: 
        return a
    if f(b)==0.0: 
        return b
    if np.sign(f(a))==np.sign(f(b)): 
        print('Root is not bracketed')
        return 
    x=0.5*(a+b)                    #Initialize 1st bisection
    for i in range(30):
        if f(x)==0.0: 
            return x
        #Tighten the brackets on the root
        if np.sign(f(a))!=np.sign(f(x)): 
            b=x
        else: 
            a=x
        
        #Implement newton-raphson step as it converges faster when root is nearby
        #If division by zero occuurs, exit newton-raphson for current iteration
        try: 
            dx=-f(x)/df(x)
        except ZeroDivisionError: 
            dx=b-a                    
        x=x+dx                        #This either converges to the root if newton-raphson succeeds or pushes x far away in case of a flat derivative and gives newton-raphson a chance to converge in next iteration, otherwise newton raphson will never get implemented and get stuck at same x value.
        
        #If the above step pushed x outside the brackets, implement bisection
        if (b-x)*(x-a)<0.0:
            x=0.5*(a+b)
                                
        #Check for convergence
        if abs(dx)<tol*np.maximum(abs(b),1.0):            #If 𝑏 is large, the condition ensures that the error is relative to b               
            return x
    print('Too many iterations')


def f(x): 
    return x**4-6.4*x**3+6.45*x**2+20.538*x-31.752
def df(x): 
    return 4.0*x**3-19.2*x**2+12.9*x+20.538

x=root_safe(f,df,0.0,5.0,tol=1.0e-9)                        #At 2.00 there is a root but bisection fails there since that root is tangent point of x axis for the curve 
if x is None:
    print('No root found in the given interval.')
else:
    print('The root is :','{:6.4f}'.format(x))