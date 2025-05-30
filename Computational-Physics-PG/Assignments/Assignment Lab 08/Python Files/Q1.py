#Question 1
#Calculation of heat flux into the soil using numerical differentiation

import numpy as np
import matplotlib.pyplot as plt

#Given Data
Z=[0,1.25,3.75]
T=[13.5,12,10]

#Interpolating Data
def Lagrange(Z0):
    Sum=0.0
    for i in range(len(Z)):
        product=1.0
        for j in range(len(Z)):
            if i!=j:
                product*=(Z0-Z[j])/(Z[i]-Z[j])
        Sum+=product*T[i]
    return Sum
    
Z_value=np.linspace(Z[0],Z[-1],20)
T_value=Lagrange(Z_value)

plt.plot(Z_value,T_value,'go')
plt.ylabel('Temperature')
plt.xlabel('Depth')
plt.savefig('/home/tux_blue/Documents/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 08/Python Files/Q1.png')
plt.show()

#Numerical Differentiation
h=0.00001
def forward_diff(Lagrange,Z):
    return (Lagrange(Z+h)-Lagrange(Z))/h
    
#Parameters
k=3.5*10**(-7)    #coefficient of thermal diffusivity in m**2/s
p=1800               #soil density in kg/m**3
C=840                 #specific heat of soil in J/kg-celcius

q=-k*p*C*forward_diff(Lagrange,0)
print('The heat flux into the ground at z = 0 is :',q)
