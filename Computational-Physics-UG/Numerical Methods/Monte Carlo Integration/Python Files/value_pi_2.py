#Computation of value of pi by Monte-Carlo Integration (faster approach with vectorization)

from numpy.random import uniform as u
N=1000000
r=eval(input('Enter the radius of the circle : '))
inside=sum((u(-r,r,N)**2+u(-r,r,N)**2)<=r*r)
pi=4*inside/N
print('The value of pi from Monte-Carlo Integration is :',format(pi,'0.4f'))