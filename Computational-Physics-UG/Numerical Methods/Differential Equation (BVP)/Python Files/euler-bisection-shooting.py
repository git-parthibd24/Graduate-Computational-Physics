#Solution of 2nd order ODE (BVP) using euler-bisection-shooting method
#Solving equation of the form y"+p(x)y'+q(x)y=r(x) ; y'=z,z'=r(x)-q(x)*y-p(x)*z within range a<=x<=b, when y(a)=ya and y(b)=yb are the boundary condition

import matplotlib.pyplot as plt
import numpy as np

def fy(x,y,z):
    return z                             #This is dy/dx
                                        
def fz(x,y,z):
    return -y                           #This is dz/dx
                                        
x0,y0,xn,yn=0,2,np.pi/2,3     #Given boundary conditions
n=10000                               #No. of intervals
                                        
def eul(fy,fz,z0): 
    x,y,z=x0,y0,z0
    X,Y,Z=[x0],[y0],[z0]
    h=(xn-x0)/n
    for i in range(n):               #no. of intervals is 1 less than no. of points
	    y_old=y
	    y=y+h*fy(x,y,z)
	    z=z+h*fz(x,y_old,z)
	    x=x+h
	    X.append(x)
	    Y.append(y)
	    Z.append(z)
    return X,Y,Z,Y[-1]-yn

f='Y'
flag=False
while f=='Y' or f=='y':
	a1,a2=eval(input('Enter the guesses of shooting parameters : '))  
	if eul(fy,fz,a1)[-1]*eul(fy,fz,a2)[-1]<0:
        	flag=True
        	break
	print ('Root do not exist in the given interval')
	f=input('Want to proceed?(Y/N)')

if flag==True:
    tol=0.001    	
    i=0
    while abs(a2-a1)>=tol:
	    a=(a1+a2)/2
	    i=i+1
	    if eul(fy,fz,a1)[-1]*eul(fy,fz,a)[-1]<0:
		    a2=a
	    else:
		    a1=a
	
	    plt.cla()
	    plt.ylim(0.5,6)
	    plt.title(r'$\alpha$ = %0.5f, $y_n$ = %0.5f, $y_n(evaluated)-y_n(given)$ = %7.5f' %(a,yn,eul(fy,fz,a)[1][-1]-yn))
	    plt.plot(eul(fy,fz,a)[0][::300],eul(fy,fz,a)[1][::300],'ro',ms=3,label=r'$y(x)$ for $\alpha$ = %0.5f' %a)
	    plt.plot(eul(fy,fz,a)[0],2*np.cos(np.array(eul(fy,fz,a)[0]))+3*np.sin(np.array(eul(fy,fz,a)[0])),'b--',label='Exact solution')
	    plt.legend(loc='upper left',prop={'size':12})
	    plt.xlabel('x-values')
	    plt.ylabel('Solution y = f(x)')
	    plt.axhline(color='gray',lw=1)
	    plt.axvline(color='green',lw=1)
	    plt.axvline(x=xn,color='green',lw=1)
	    plt.grid()
	    plt.pause(1.0)     #displays the plot
	
	    if eul(fy,fz,a)[-1]==0:
		    break
		
    print('The value of the shooting parameter is :', a)
    print('The value of the solution at',xn,'is :',eul(fy,fz,a)[1][-1])		
    plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Differential Equation (BVP)/Python Files//euler-bisection-shooting.png')
    plt.show()              #display the final plot after loop ends and save it
