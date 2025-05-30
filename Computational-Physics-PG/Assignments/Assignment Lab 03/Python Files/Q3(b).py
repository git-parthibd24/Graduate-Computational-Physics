#Question 3(b)
#Test implementation of finite difference approximation in the case of constant velocity V. Set t0 = 0; t1 = 0:5; t2 = 1:5 and t3 = 2:2, and xi=V*ti 

import numpy as np

V=eval(input("Enter the value of constant velocity V : "))     
t=[0,0.5,1.5,2.2]
x=[V*ti for ti in t]

def kinematics(i,x,t):
    v=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    return v

def test_kinematics():
    for i in range(1,len(x)-1):
        v=kinematics(i,x,t)
        if abs(v-V)<=0.0001: 
            print('Actual Velocity was defined by :',V,'m/s')
            print("Velocity at time t =",t[i],"s is",np.round(v,3),'m/s')
            print("Test case for velocity passed")
            print()
        else:
            print('Actual Velocity was defined by :',V,'m/s')
            print("Velocity at time t =",t[i],"s is",np.round(v,3),'m/s')
            print('Test case for velocity failed')
            print()

test_kinematics()
