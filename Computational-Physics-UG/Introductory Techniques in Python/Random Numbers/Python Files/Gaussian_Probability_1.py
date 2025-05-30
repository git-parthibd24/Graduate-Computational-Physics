#A sample of dry battery cells tested to find the length of life produced the following result: xmean = 12 hours, standard deviation = 3 hours. Assuming that the data are normally distributed, what percentage of battery are expected to have life between 10-14 hours?
#Method 1

import numpy.random as rn

N=int(input('Enter size of sample of battery cells : '))
low,up=10,14
u=rn.normal(loc=12,scale=3,size=N)
n=len([u[i] for i in range(N) if u[i]<14 and u[i]>10])

print('The percentage of cells with battery life between',low,'and',up,'hours is :',n/N*100,'%')