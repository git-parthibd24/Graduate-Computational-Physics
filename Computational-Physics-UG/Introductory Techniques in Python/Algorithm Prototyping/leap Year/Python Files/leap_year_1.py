#Check a year is leap year or not

y=eval(input('enter a year : '))
if y%100==0:
    if y%400==0:
        print(y,'is leap year')
    else:
        print(y,'is not a leap year')
else:
    if y%4==0:
        print(y,'is leap year')
    else:
        print(y,'is not a leap year')