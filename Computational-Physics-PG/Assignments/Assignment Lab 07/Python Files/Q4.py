#Question 4
#Adaptive Trapezoidal Rule (Local Refinement) (Depth 1st approach)

import numpy as np

def trapezoidal(f,a,b,n):
    h=(b-a)/(n)
    x=np.linspace(a,b,n+1)
    y=f(x)
    return (h/2)*(y[0]+2*sum(y[1:-1])+y[-1])

def adaptive_trapezoidal(f,a,b,tol=1e-6,min_step=1e-12):
    intervals=[(a,b)]           #This stores the range of integration (sub-intervals) within a tuple inside a list. This stack will get dynamically updated
    integral=0 

    while intervals:            #The loop will initiate only if intervals is filled
        a,b=intervals.pop()     #Remove the last element of stack i.e the tuple of interval and assign variables to it for current interval of processing
        mid=(a+b)/2  
        I_coarse=trapezoidal(f,a,b,1)  
        I_fine=trapezoidal(f,a,mid,1)+trapezoidal(f,mid,b,1)  

        error=abs(I_fine-I_coarse)/3  
        if error<tol or abs(b-a)<min_step:   #Local convergence check for a given sub-interval (a,b)
            integral+=I_fine                 #Add the area of this trapezoid in (a,b) to integral
        else:
            intervals.append((a,mid))       #Subdivide further to check for convergence of these new intervals from rightmost to leftmost over next iterations
            intervals.append((mid,b))
            
    return integral

    
fx=lambda x:np.cos(np.pi*x/2)
fy=lambda y:np.cos(np.pi*y/2)
result=adaptive_trapezoidal(fx,-1,1)*adaptive_trapezoidal(fy,-1,1)
print("The value of integral using Adaptive Trapezoidal Integral is :",format(result,'0.4f'))

