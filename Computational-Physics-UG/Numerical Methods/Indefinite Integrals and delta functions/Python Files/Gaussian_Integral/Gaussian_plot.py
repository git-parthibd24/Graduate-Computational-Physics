#To check the similarity with defined Gaussian Integral by numerically evaluating Gausssian integral
#With plotting

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
a,b,c=eval(input('Enter values of a,b,c : '))
up=np.inf
low=-np.inf
f0=lambda x:np.exp(-a*x**2+b*x+c)
I0,err=quad(f0,low,up)
Iexact=np.sqrt(np.pi/a)*np.exp((b**2)/(4*a)+c)
print('The value of integral of Gaussian Function :',I0,'and the exact value is :',Iexact)
if round(I0/Iexact)==1:
    print('The Gaussian Functon is same as the given function with ratio of 1')
else:
    print('Gaussian function is not same to the given function')
    
d=np.linspace(1,11,100)
e=np.linspace(1,11,100)
f=np.linspace(1,11,100)
m=[]
n=[]
o=[]
for i in d:
    g=lambda x:np.exp(-i*x**2+b*x+c)
    I1=quad(g,-np.inf,np.inf)[0]
    m.append(I1)
    
Iexact1=lambda d: np.sqrt(np.pi/d)*np.exp((b**2)/(4*d)+c)
    
for i in e:
    h=lambda x:np.exp(-a*x**2+i*x+c)
    I2=quad(h,-np.inf,np.inf)[0]
    n.append(I2)
    
Iexact2=lambda e: np.sqrt(np.pi/a)*np.exp((e**2)/(4*a)+c)
 
for i in f:
    h=lambda x:np.exp(-a*x**2+b*x+i)
    I3=quad(h,-np.inf,np.inf)[0]
    o.append(I3)
    
Iexact3=lambda f: np.sqrt(np.pi/a)*np.exp((b**2)/(4*a)+f)

fig=plt.figure(figsize=(6,4),dpi=100)
plt.suptitle('Checking the similarity of the Gaussian Integral with the given function for different values of a,b and c')


plt.subplot(2,2,1)   
plt.plot(d,m,'r--',label='Integration value for several a')
plt.plot(d[::8],Iexact1(d)[::8],'bo',label='Expression value for several a')
plt.xlabel('d')

plt.axhline(color='gray')
plt.axvline(color='gray')
plt.legend()



plt.subplot(2,2,2)   
plt.plot(e,n,'r--',label='Integration value for several b')
plt.plot(e[::8],Iexact2(e)[::8],'go',label='Expression value for several b')
plt.xlabel('b')

plt.axhline(color='gray')
plt.axvline(color='gray')
plt.legend()



plt.subplot(2,2,3)   
plt.plot(f,o,'r--',label='Integration value for several c')
plt.plot(f[::8],Iexact3(f)[::8],'yo',label='Expression value for several c')
plt.xlabel('c')

plt.axhline(color='gray')
plt.axvline(color='gray')
plt.legend()

fig.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-UG/Numerical Methods/Indefinite Integrals and delta functions/Python Files/Gaussian_Integral/Gaussian_plot.png')
plt.show()
