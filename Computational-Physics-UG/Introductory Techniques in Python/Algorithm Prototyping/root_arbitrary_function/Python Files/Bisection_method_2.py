#Bisection Method (With new inputs)

def f(x):
    return x**3-x**2+2
while True:
    a=eval(input('enter lower limit : '))
    b=eval(input('enter upper limit : '))
    if f(a)*f(b)<0:
        break
    print("No real roots found in the interval\nEnter new interval")
error=eval(input('enter error value : '))
while True:
    x=(a+b)/2
    if f(a)*f(x)<0:
        b=x
    else:
        a=x
    if f(x)==0 or abs(a-b)<=error:
        break
print('The value of real root is in that interval :',format(x,"0.4f"))