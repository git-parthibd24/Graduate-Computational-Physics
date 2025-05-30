#Use of user defined module in a sample program

import user_module as md

print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division')
ch=eval(input('Enter your choice: '))
if ch==1:
    a,b=eval(input('Enter two numbers: '))
    print('Result for addition: ',md.add(a,b))
elif ch==2:
    a,b=eval(input('Enter two numbers: '))
    print('Result for subtraction: ',md.subtract(a,b))
elif ch==3:
    a,b=eval(input('Enter two numbers: '))
    print('Result for multiplication: ',md.multiply(a,b))
elif ch==4:
    a,b=eval(input('Enter two numbers: '))
    if b==0:
        print('Undefined')
    else:          
        print('Result for division: ',md.division(a,b))
else:
    print('Choice is incorrect')