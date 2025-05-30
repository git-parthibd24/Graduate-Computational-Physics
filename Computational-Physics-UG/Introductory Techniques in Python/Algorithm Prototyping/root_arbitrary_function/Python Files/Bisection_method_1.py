#Bisection Method (Without new inputs)

def f(x):
    return (x**3)-(x**2)+2   
def bisection_method(a,b,error):
    if (f(a)*f(b)>=0):
        print("Incorrect assumption of a and b")
    else:
        while abs(a-b)>=error:
            c=(a+b)/2           
            if f(c)*f(a)<0: #true if sign of function evaluated at midpoint c and a are opposite
                b=c
            else:
                a=c
            if f(c)==0.0 or abs(a-b)<=error:
                break
        print("The value of root is :",c)
A=eval(input('Enter lower limit : '))
B=eval(input('Enter upper limit : '))
Error=eval(input('Enter error : '))
bisection_method(A,B,Error)