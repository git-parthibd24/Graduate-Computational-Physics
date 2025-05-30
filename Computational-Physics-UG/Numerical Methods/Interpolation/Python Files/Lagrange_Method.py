#Lagrange's Interpolation
#Used when data points may not be equispaced. This method is computationally intensive.

import numpy as np
n=int(input('Enter size : '))
X=np.empty(n)
Y=np.empty(n)
for i in range(n):
    print('Enter X[',i,']=',end=' ')
    X[i]=eval(input())
    print('Enter Y[',i,']=',end=' ')
    Y[i]=eval(input())
    
x=eval(input('Enter the interpolating point : '))
Sum=0.0
for i in range(n):
    product=1.0
    for j in range(n):
        if i!=j:
            product*=(x-X[j])/(X[i]-X[j])
    Sum+=product*Y[i]
print('The value of the function at x =',x,'is :',Sum)