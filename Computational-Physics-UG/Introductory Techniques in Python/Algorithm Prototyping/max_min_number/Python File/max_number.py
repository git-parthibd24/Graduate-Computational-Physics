#Find maximum of three numbers

x=eval(input('enter num1 : '))
y=eval(input('enter num2 : '))
z=eval(input('enter num3 : '))
if x>y and x>z:
    print(x,'is max')
elif y>x or y>z:
    print(y,'is max')
else:
    print(z,'is max')