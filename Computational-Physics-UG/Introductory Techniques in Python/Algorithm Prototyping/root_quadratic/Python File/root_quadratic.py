#Find the roots of a quadratic equation from math import sqrt

import math as m
import cmath as cm
a=eval(input('enter coeficient of x^2 : '))
b=eval(input('enter coefficient of x : '))
c=eval(input('enter constant : '))
if a!=0:
    d=b**2-4*a*c
    if d==0:
       print('roots are real and equal')
       r=-b/2*a
       print(r)
    elif d>0:
        print('roots are real and unequal')
        p=(-b+m.sqrt(d))/(2*a)
        q=(-b-m.sqrt(d))/(2*a)
        print('one root is', p)
        print('other root is',q)
    else:
        print('roots are complex')
        p=(-b+cm.sqrt(d))/(2*a)
        q=(-b-cm.sqrt(d))/(2*a)
        print('one root is',p)
        print('other root is',q)
else:
    print('not a quadratic equation')