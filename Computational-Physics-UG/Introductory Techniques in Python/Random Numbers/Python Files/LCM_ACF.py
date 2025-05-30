#Linear congruential method and auto-correlation function of a given time series

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots

#LCM
x0=eval(input('Enter the seed : '))
a=eval(input('Enter the multiplier : '))
c=eval(input('Enter the increment : '))
N=eval(input('Enter the number of random numbers to generate : '))
m=eval(input('Enter the modulus : '))
X=np.zeros(N+1)
X[0]=x0
for i in range(N):
	X[i+1]=(a*X[i]+c)%m
Y=X[1:]							#x0 is predefined, hence excluded
U=Y/m
print()
print('Random Number Series : \n')
print(Y)
print()
print('Normalised Random Number Series : \n')
print(U)

plt.figure()
plt.title('Random Number Generation using Linear Congruential Method')	
plt.hist(Y,bins=20,rwidth=0.9,edgecolor='black',color='cyan')
plt.show()

plt.figure()
plt.title('Normalised Random Numbers')	
plt.hist(U,bins=20,rwidth=0.9,edgecolor='black',color='c')
plt.show()

plt.figure()
plt.title('Exponential Random Number')
plt.hist(-np.log(U),bins=20,rwidth=0.9,edgecolor='black',color='orange')
plt.show()

#ACF
ubar=np.mean(U)
def c(k):
	return (np.sum([(U[i]-ubar)*(U[i+k]-ubar) for i in range(N-k)]))/N
def r(k):
	return c(k)/c(0)
	
corr=[]
for k in range(1,N//10):
	corr.append(r(k))

plt.figure()
plt.title('Autocorrelation as function of  k')
plt.plot(range(1,N//10),corr,'-',color='green')
plt.axhline(color='black',lw=0.5,ls='--')
plt.axvline(color='black',lw=0.5,ls='--')
plt.xlabel('k')
plt.ylabel('Autocorrelation Function')
plt.show()

#Correlogram
fig=tsaplots.plot_acf(U,lags=10,zero=False,color='red',title='Autocorrelation')