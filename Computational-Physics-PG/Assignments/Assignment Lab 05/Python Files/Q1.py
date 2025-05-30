#Question 1
#Linear Interpolation by creating dataset

import numpy as np
def interpolate(q,x0):
    f=lambda x : np.exp(-x**2)*np.cos(2*np.pi*x)
    x_mesh=np.linspace(-1,1,q+1)
    y_mesh=f(x_mesh)

    if x_mesh[0]<=x0<=x_mesh[-1]:    
        for i in range(len(x_mesh)-1):
            if x_mesh[i]<x0<x_mesh[i+1]:
                y0=((x_mesh[i+1]-x0)/(x_mesh[i+1]-x_mesh[i]))*y_mesh[i]+((x0-x_mesh[i])/(x_mesh[i+1]-x_mesh[i]))*y_mesh[i+1]
            elif x0==x_mesh[i]:
                y0=y_mesh[i]
        error=abs(f(x0)-y0)
        print(format(y0,'0.5f'),'and',format(error,'0.5f'))
    
    else:
        print('Value out of range of interpolation')
        
    return ()

x0=eval(input('Enter Interpolating point : '))
print()
for i in range(1,5):
    print('The value of function and error at',x0,' when no. of mesh points is',2**i,'is :',end=' ')
    interpolate(2**i,x0)
    print()
