#Numerical Integration using Gauss-Legendre n-point quadrature formula 
#Implemented using root finding from inbuilt function and file read/write

import numpy as np
from numpy.polynomial.legendre import leggauss

def f(x):
    return x*np.exp(x)

a=eval(input('Enter lower limit : '))
b=eval(input('Enter upper limit : '))
n=int(input('Enter no. of points : '))

t,w=leggauss(n)            #This evaluates the roots of n-th degree Legendre polynomial (n-quadrature points) and the associated weights with them through a relation
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Numerical Methods\\Integration Methods\\Python Files\\Legendre.txt','w')

for i in range(n):
    fp.write(str(t[i]))     #writing the roots for each iteration in 1st column of the file
    fp.write(' ')           #seperating the roots and weights in 2 columns
    fp.write(str(w[i]))     #writing the weights for each iteration in 2nd column of the file
    fp.write('\n')          #changing line for next iteration
fp.close()

Sum=0.0
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Numerical Methods\\Integration Methods\\Python Files\\Legendre.txt','r')
for i in range(n):
    s=fp.readline()         #reading the file line by line and creating a string of root and its weight
    l=s.split()             #making a list of string(root) and its string(weight) by splitting the s string in each iteration
    Sum=Sum+float(l[1])*f(float(l[0])*(b-a)/2+(a+b)/2)    #evaluating the n-point Gaussian quadrature sum by changing x into t
Sum*=(b-a)/2

print('The value of integral is :',format(Sum,'0.3f'))
fp.close()
