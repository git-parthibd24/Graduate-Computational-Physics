#Question 3 (Vectorization)
#Solution of Coupled Radioactive Decay using Euler's Method

import numpy as np
import matplotlib.pyplot as plt

def dNA(NA,NB):
    return (-NA+NB)/1.0

def dNB(NA,NB):
    return (NA-NB)/1.0

NA0,NB0,t0,tn,h=100,0,0,3,0.00001

def euler_system(dNA,dNB,NA0,NB0,t0,tn,h):
    T=np.arange(t0,tn+h,h)
    R=np.zeros((len(T),2))
    R[0,0],R[0,1]=NA0,NB0
    for i in range(len(T)-1):
        R[i+1]=R[i]+h*np.array([dNA(R[i,0],R[i,1]),dNB(R[i,0],R[i,1])])
    return T,R[:,0],R[:,1]

T,NA,NB=euler_system(dNA,dNB,NA0,NB0,t0,tn,h)

plt.plot(T,NA,color='violet',linestyle='-',label='$N_A(t)$')
plt.plot(T,NB,color='chocolate',linestyle='-',label='$N_B(t)$')
plt.axhline(NA[-1],color='orange',linestyle=':',label=r'Steady State $N_A(t)$')
plt.axhline(NB[-1],color='yellow',linestyle=':',label=r'Steady State $N_B(t)$')
plt.axvline(0,color='black')
plt.axhline(0,color='black')
plt.axvline(tn/2,color='green',linestyle='--',label='Half Time')
plt.title(r'Radioactive Decay : $A \rightarrow B$',fontsize=12)
plt.xlabel('Time (s)')
plt.ylabel('Number of Nuclei')
plt.legend()
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 08/Python Files/Q3_Vectorize.png')
plt.show()
        
