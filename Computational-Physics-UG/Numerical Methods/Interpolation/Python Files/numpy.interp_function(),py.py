#Interpolation using numpy module

import numpy as np
n=int(input('Enter no. of data : '))
X=np.empty(n)
Y=np.empty(n)
print('Enter the values of X and Y')
for i in range(n):
    X[i]=eval(input())
    Y[i]=eval(input())
x=eval(input('Enter the interpolating point : '))
if X[0]<=x<=X[n-1]:
    print('Interpolation')
    y=np.interp(x,X,Y)
    print('The value of interpolation at x =',x,'is =',y)
else:
    print('Extrapolating point')