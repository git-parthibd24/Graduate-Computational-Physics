#Neville's algorithm

import numpy as np
import matplotlib.pyplot as plt

def neville(x_val,y_val,x0):
    m=len(x_val)   
    y=y_val.copy()                #To preserve original data we need to copy it, as we are going to assign and update all the successive recurrence values in the same data array
    
    #For a particular value of i, this array slicing method handles the working of a loop
    for i in range(1,m):
        y[0:m-i]=((x0-x_val[i:m])*y[0:m-i]+(x_val[0:m-i]-x0)*y[1:m-i+1])/(x_val[0:m-i]-x_val[i:m])   #At once according to same index of the sliced arrays, numerical operation is done among them on the succesive index elements
                                                                                                     #The array gets updates with each iteration of i leaving successive last positions unaltered i.e they remain with the previous value. The method is same according to creation of a upper triangular recurrence table except the successive column of the table are updated in the 1st column itself 
    return y[0]    #Final result is stored in the 1st position of the array after successive updates
    
x_data=np.array([0.1,0.2,0.5,0.6,0.8,1.2,1.5])
y_data=np.array([-1.5342,-1.0811,-0.4445,-0.3085,-0.0868,0.2281,0.3824])

X_0=np.linspace(0.1,1.5,10)
Y_0=np.zeros(len(X_0))

for i in range(len(X_0)):
    Y_0[i]=neville(x_data,y_data,X_0[i])
    
    
plt.plot(x_data,y_data,'go',ms=10)
plt.plot(X_0,Y_0,'bo--')
plt.legend(('Actual Data','Nevilles Interpolated Data'),loc='best')
plt.show()