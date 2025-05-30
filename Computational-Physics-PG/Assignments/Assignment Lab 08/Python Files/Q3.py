#Question 3
#Solution of Coupled Radioactive Decay using Euler's Method

import numpy as np
import matplotlib.pyplot as plt

def dNA(NA,NB):
    return (-NA+NB)/1.0            #dNA/dt=-NA/tau+NB/tau

def dNB(NA,NB):
    return (NA-NB)/1.0             #dNB/dt=NA/tau-NB/tau

NA0=100                            #Initial number of A nuclei
NB0=0                              #Initial number of B nuclei
t0=0                               #Initial time
tn=3                               #Finaltime
h=0.00001 

def euler_system(dNA,dNB,NA0,NB0,t0,tn):
    T=np.arange(t0,tn+h,h)
    NA=np.zeros(len(T))
    NB=np.zeros(len(T))
    NA[0]=NA0
    NB[0]=NB0
    for i in range(len(T)-1):
        NA[i+1]=NA[i]+h*dNA(NA[i],NB[i])
        NB[i+1]=NB[i]+h*dNB(NA[i],NB[i])
    return T,NA,NB
    
T,NA,NB=euler_system(dNA,dNB,NA0,NB0,t0,tn)

plt.plot(T,NA,'r-',label='$N_A(t)$')
plt.plot(T,NB,'b-',label='$N_B(t)$')
plt.axhline(NA[-1],color='orange',linestyle=':',label=r'Steady State $N_A(t)$')
plt.axhline(NB[-1],color='yellow',linestyle=':',label=r'Steady State $ N_B(t)$')
plt.axvline(0,color='black')
plt.axhline(0,color='black')
plt.axvline(tn/2,color='green',linestyle='--',label='Half Time')
plt.title(r'Radioactive Decay : $A \rightarrow B$',fontsize=12)
plt.xlabel('Time (s)')
plt.ylabel('Number of Nuclei')
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 08/Python Files/Q3.png')
plt.show()

