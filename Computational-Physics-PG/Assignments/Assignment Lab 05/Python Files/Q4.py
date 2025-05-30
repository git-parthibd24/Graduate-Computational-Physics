#Question 4
#Cubic Spline Interpolation with analytical solution of tridiagonal equations
#y"[j-1]*(x[j]-x[j-1])/6 + y"[j]*(x[j+1]-x[j-1])/3 + y"[j+1]*(x[j+1]-x[j])/6 = (y[j+1]-y[j])/(x[j+1]-x[j]) - (y[j]-y[j-1])/(x[j]-x[j-1])

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([13,15,12,9,13])

x0=3.4  #Interpolation point

def interpolate(x0):

    if x[0]<=x0<=x[-1]:
        coeff=[[4,1,0],[1,4,1],[0,1,4]]     #We get these by analytically forming the simultaneous equations since data size is small
        const=[-30,0,42]
        y_derivative=np.linalg.solve(coeff,const)
        y_derivative=np.insert(y_derivative,0,0)
        y_derivative=np.insert(y_derivative,len(y_derivative),0)      #y_derivative initially have size 4 which will become size 5 after inserting 0 at end
  
        for i in range(len(x)-1):
            if x[i]<x0<x[i+1]:
                A=(x[i+1]-x0)/(x[i+1]-x[i])
                B=(x0-x[i])/(x[i+1]-x[i])
                C=(A**3-A)*((x[i+1]-x[i])**2)/6
                D=(B**3-B)*((x[i+1]-x[i])**2)/6
                y0=A*y[i]+B*y[i+1]+C*y_derivative[i]+D*y_derivative[i+1]
                return y0
                break
            elif x0==x[i]:
                y0=y[i]
                return y0
                break

    else:
        print('Value out of range of interpolation')
        return None

print('The value of function at',x0,'is :',interpolate(x0))
