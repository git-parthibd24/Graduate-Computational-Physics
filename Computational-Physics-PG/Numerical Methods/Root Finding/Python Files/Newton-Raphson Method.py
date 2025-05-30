#Newton-Raphson Method for root finding

import numpy as np

def f(x): 
    return x**4-6.4*x**3+6.45*x**2+20.538*x-31.752
def df(x): 
    return 4.0*x**3-19.2*x**2+12.9*x+20.538

def NewtonRaphson(x,tol=1.0e-9):
    for i in range(30):
        
        if abs(df(x))<1e-12:                        #Check if the derivative is too small
            return None, i
        
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: 
            return x, i
    print("Too many operations")
    return None,30                                   #when the 'if statement' is not met within the iteration change, then only this line prints as the 'if statement' can't return anything and exit the code
                                                     #by-default returns None if we dont specify it, but we need to return the 2nd number as we are calling 2 variables from the function later

root,numIter=NewtonRaphson(4.5)                      #Initial guess
if root is not None:
    print(f'Root: {root:.6f}')
    print(f'Number of iterations: {numIter}')
else:
    print('Method did not converge, root couldnt be detected')