#Question 1
#Romberg Method of Numerical Integration

import numpy as np

def trapezoidal(f,a,b,n):                                                             #n is no. of divisions not points
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    y=f(x)
    return (h/2)*(y[0]+2*np.sum(y[1:-1])+y[-1])

def romberg(f,a,b,tol):
    R=[[trapezoidal(f,a,b,1)]]                                                          #Initializing List with 1st element R[0][0]. Using list so that the size dynamically grows with parallel loops top to bottom and left to right
    
    #Calculation of recurrence table
    i=1
    while True:
        R.append([trapezoidal(f,a,b,2**i)])
        
        for j in range(1,i+1):
            R[i].append(R[i][j-1]+(1/(4**j-1))*(R[i][j-1]-R[i-1][j-1]))     #Filling columns (j) for a given row (i)
        
        #Printing of recurrence table and breaking   
        if abs(R[i][i]-R[i-1][i-1])<tol:
            
            print("The recurrence table is: " )
            for a in range(len(R)):
                for b in range(a+1):
                    print(format(R[a][b],'10.4f'), end=' ')
                print()
    
            return R[i][i]                                                                     #breaks with return statement
        
        i+=1

f=lambda x: np.sin(x)
a,b=0,np.pi
result=romberg(f,a,b,tol=1e-10)
print("The integration using Romberg method evaluates as :",format(result,'0.4f'))


