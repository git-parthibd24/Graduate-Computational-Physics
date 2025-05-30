#Solution of 2nd order ODE (BVP) using euler-bisection-shooting method
#Solving equation of the form y"+p(x)y'+q(x)y=r(x) ; y'=z,z'=r(x)-q(x)*y-p(x)*z within range a<=x<=b, when y(a)=ya and y(b)=yb are the boundary condition
#Using array for memory management

import matplotlib.pyplot as plt
import numpy as np

def fy(x,y,z):
    return z                           #This is dy/dx

def fz(x,y,z):
    return -y                         #This is dz/dx

x0,y0,xn,yn=0,2,np.pi/2,3   #Given boundary conditions
n=10000                             #no. of intervals

def eul(fy,fz,z0): 
    h=(xn-x0)/n
    X=np.linspace(x0,xn,n+1)  
    Y=np.zeros(len(X))
    Z=np.zeros(len(X))
    Y[0]=y0
    Z[0]=z0
    for i in range(len(X)-1):
        x=X[i]
        y=Y[i]             
        z=Z[i]
        Y[i+1]=y+h*fy(x,y,z)
        Z[i+1]=z+h*fz(x,y,z)
    return X,Y,Z,Y[-1]-yn

f='Y'
flag=False
while f=='Y' or f=='y':
    a1,a2=eval(input('Enter the guesses of shooting parameters : ')) 
    if eul(fy,fz,a1)[-1]*eul(fy,fz,a2)[-1]<0:
        flag=True
        break
    print('Root does not exist in the given interval')
    f=input('Want to proceed?(Y/N)')

if flag:
    tol=0.001    
    i=0
    while abs(a2-a1)>=tol:
        a=(a1+a2)/2
        i+=1
        X,Y,Z,delta_a=eul(fy,fz,a)
        if eul(fy,fz,a1)[-1]*delta_a<0:
            a2=a
        else:
            a1=a

        plt.cla()
        plt.ylim(0.5,6)
        plt.title(r'$\alpha$ = %0.5f, $y_n$ = %0.5f, $y_n(evaluated)-y_n(given)$ = %7.5f' %(a,yn,delta_a))
        plt.plot(X[::300],Y[::300],'ro',ms=3,label=r'$y(x)$ for $\alpha$ = %0.5f' %a)
        plt.plot(X,2*np.cos(X)+3*np.sin(X),'b--',label='Exact solution')
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
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (BVP)/Python Files/euler-bisection-shooting_memory_allocation.png')
    plt.show()                                #display the final plot after loop ends and save it
