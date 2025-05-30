#Question 3
#Neville's Interpolation

import numpy as np

X=[0,0.5,1,1.5,2]
y_val=[-1.00,1.75,4.00,5.75,7.00]

Y=np.zeros((len(X),len(X)))
x0=eval(input('Enter the interpolating point : '))

for i in range(len(X)):
    Y[i][0]=y_val[i]

#Calculation of recurrence table
for j in range(1,len(X)):
    for i in range(j,len(X)):
        Y[i][j]=((x0-X[i-j])*Y[i][j-1]-(x0-X[i])*Y[i-1][j-1])/(X[i]-X[i-j])


#Printing of recurrence table
print("The recurrence table is: " )
for i in range(len(X)):
    for j in range(i+1):
        print(format(Y[i][j],'7.3f'),end=' ')
    print()

print('The value of the function at x =',x0,'is :',format(Y[len(X)-1][len(X)-1],'0.4f'))
