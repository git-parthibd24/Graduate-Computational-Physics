#Taylor series of cosx

import math
s1=0.0
s2=0.0
x=eval(input('Enter x-coordinate in radian : '))
i=0
while True:
    s1=s1+(pow(x,2*i)/math.factorial(2*i))*pow(-1,i)
    i=i+1
    if abs(s1-s2)<=0.01:
        break
    s2=s1
print('The value of Taylor series at x =',x,'radian is',s1)