#Solution of 2nd order ODE (BVP) using numerov-bisection-shooting method
#Solving equation of the form y"+q(x)y=0 ; y'=z,z'+q(x)*y=0 within range a<=x<=b, when y(a)=ya and y(b)=yb are the boundary condition

import matplotlib.pyplot as plt
import numpy as np

def fy(x,y,z):
    return z                            #This is dy/dx
                                        
def k(x):
    return x 

def fz(x,y,z):
    return -k(x)*y                   #This is dz/dx
                                        
x0,y0,xn,yn=0,2,10,1           #Given boundary conditions
n=10000                               #No. of intervals
                                        
def numerov(fy,k,z0): 
    h=(xn-x0)/n
    X=np.linspace(x0,xn,n+1)
    K=k(X)
    Y=np.zeros(len(X))  
    Y[0]=y0
    Y[1]=y0+h*fy(x0,y0,z0)
    for i in range(1,len(X)-1):
        Y[i+1]=(2*(1-(5/12)*h**2*K[i])*Y[i]-(1+(1/12)*h**2*K[i-1])*Y[i-1])/(1+(1/12)*h**2*K[i+1])
    return X,Y,Y[-1]-yn

f='Y'
flag=False
while f=='Y' or f=='y':
	a1,a2=eval(input('Enter the guesses of shooting parameters : '))  
	if numerov(fy,k,a1)[-1]*numerov(fy,k,a2)[-1]<0:
        	flag=True
        	break
	print ('Root do not exist in the given interval')
	f=input('Want to proceed?(Y/N)')

if flag:
    tol=0.001    
    i=0
    while abs(a2-a1)>=tol:
        a=(a1+a2)/2
        i+=1
        X,Y,delta_a=numerov(fy,k,a)
        if numerov(fy,k,a1)[-1]*delta_a<0:
            a2=a
        else:
            a1=a

        plt.cla()
        plt.ylim(-10,10)
        plt.title(r'$\alpha$ = %0.5f, $y_n$ = %0.5f, $y_n(evaluated)-y_n(given)$ = %7.5f' %(a,yn,delta_a))
        plt.plot(X,Y,'b-',label=r'$y(x)$ for $\alpha$ = %0.5f' %a)
        plt.legend(loc='upper left',prop={'size':12})
        plt.xlabel('x-values')
        plt.ylabel('Solution y = f(x)')
        plt.axhline(color='gray',lw=1)
        plt.axvline(color='green',lw=1)
        plt.axvline(x=xn,color='green',lw=1)
        plt.grid()
        plt.pause(1.0)                       #displays the plot

        if delta_a==0:
            break

    print('The value of the shooting parameter is :',a)
    print('The value of the solution at',xn,'is :',Y[-1])		
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (BVP)/Python Files/numerov-bisection-shooting.png')
    plt.show()               #display the final plot after loop ends and save it
