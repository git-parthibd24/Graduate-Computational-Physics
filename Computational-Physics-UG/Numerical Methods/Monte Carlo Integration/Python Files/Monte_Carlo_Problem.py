#Problem
#Generate N random numbers in the interval -2<x<2 and -2<y<2. Find the number n_frac tht falls in the annular region between the circles x**2+y**2=4 and x**2+y**2=1 by evaluating n_frac/N, estimate the area of the annular region

from numpy.random import uniform as u

N=1000000
rbig=2
rsmall=1

nbig=sum((u(-rbig,rbig,N)**2+u(-rbig,rbig,N)**2)<=rbig*rbig)
nsmall=sum((u(-rbig,rbig,N)**2+u(-rbig,rbig,N)**2)<=rsmall*rsmall)
I_annular=4*rbig**2*(nbig-nsmall)/N

print('The area of annular region from Monte-Carlo Integration is :',I_annular)