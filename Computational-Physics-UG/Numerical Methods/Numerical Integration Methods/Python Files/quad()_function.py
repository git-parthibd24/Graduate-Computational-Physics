#Numerical Integration using quad() of scipy module

from scipy.integrate import quad
import math as m

def f(x):
    return x*m.exp(x)

a,b=eval(input('Enter lower and upper limits : '))
result,err=quad(f,a,b)
print('The result is :',result,' and error is :',err)
