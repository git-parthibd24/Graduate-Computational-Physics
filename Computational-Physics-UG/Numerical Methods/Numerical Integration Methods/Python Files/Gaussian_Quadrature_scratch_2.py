#Gaussian Quadrature method for numerical integration from scratch using user defined root finding  module
#Without using lambda()

import numpy as np
import sys
sys.path.append('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Numerical Integration Methods/Python Files')
import Gauss_bisect_2    #importing user defined module from its path

def legendre_poly(n,x):     #Computing Legendre polynomial P_n(x) using its recurrence relation but through iteration
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        P0,P1=1,x                                                            #Base cases
        for k in range(2,n+1):
            Pn=((2*k-1)*x*P1-(k-1)*P0) / k
            P0,P1=P1,Pn  
        return Pn
    
def legendre_poly_derivative(n,x):   #recurrence relation involving derivative of Legendre Polynomial
    Pn= legendre_poly(n,x)
    Pn_1=legendre_poly(n-1,x)
    return n/(x**2-1)*(x*Pn-Pn_1)
    
def nodes_and_weights(n):
    nodes=Gauss_bisect_2.root_search(legendre_poly,n)    #We have to use function reference, otherwise x is not defined. If we use x, values will be passed instead of function (premature evaluation). Since we are not defining n inside legendre_poly we need to pass n itself seperately and use it in f() inside root_search() itself. n is not  binded with x and it is registered as 2nd argument.   
    weights=2/((1-nodes**2)*(legendre_poly_derivative(n,nodes)**2))
    return nodes,weights
    
def gauss_quadrature(f,a,b,n):
    nodes,weights=nodes_and_weights(n)
    integral=0
    for i in range(n):
        t=(b-a)/2*nodes[i]+(a+b)/2
        integral=integral+(weights[i])*f(t)
    integral=integral*(b-a)/2
    return integral

#Example Integration
f=lambda x:np.exp(x)
a,b=0,5
result=gauss_quadrature(f,a,b,n=1000)
print("The integral using Gaussian_Quadrature method is :", format(result,'0.4f'))



