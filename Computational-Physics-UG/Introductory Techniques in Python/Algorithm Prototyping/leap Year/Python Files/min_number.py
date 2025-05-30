#Find minimum of three numbers

x=eval(input('enter num1 : '))
y=eval(input('enter num2 : '))
z=eval(input('enter num3 : '))
if x<y and x<z:
    print(x,'is min')
elif y<x or y<z:
    print(y,'is min')
else:
    print(z,'is min')