#Question 1
#Handling improper integral by mapping x to z (z=x/(c+x))

import numpy as np

def f_old_integrand(x):
    return x**3/(np.exp(x)-1)  #Integral runs from 0 to inf

def f_old_derivative(x):
    return ((np.exp(x)*3*x**2)-(x**3*(np.exp(x))))/(np.exp(x)-1)**2

X=np.linspace(0.01,10,10000)
for i in range(len(X)):
    if f_old_derivative(X[i])*f_old_derivative(X[i+1])<0:   #point of maxima. Its good to use c near the maximum point for f_old_integrand 
        c=X[i]
        break

#z=x/(c+x) is applied transformation
def f_new_integrand(z):
    return ((z*c)**3)*c/((1-z)**5*(np.exp(z*c/(1-z))-1))

a=0.01
b=0.99
S0,S=0,0
n=10
              
while True:
    h=(b-a)/n
    a=a*0.7
    b=b+(1-b)*0.4
    S=(2*sum([f_new_integrand(a+i*h) for i in range (1,n)])+f_new_integrand(a)+f_new_integrand(b))*(h/2)                
    if abs(S-S0)<0.0001:
        break
    n=n+1
    S0=S
    
print('The value of integral is :',format(S,'0.4f'))
