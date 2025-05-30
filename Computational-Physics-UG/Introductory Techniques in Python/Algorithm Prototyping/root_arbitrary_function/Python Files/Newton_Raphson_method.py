#Newton Raphson Method

def function(x):
    return (x**2)-2    
def derivative(x):
    return 2*x
x=eval(input("Enter initial assumption of root : "))
error=eval(input("Enter tolerance : "))
while True:
    k=-function(x)/derivative(x)
    x=x+k
    if abs(k)<=error:
        break
print("The value of the root is :",format(x,"0.4f"))