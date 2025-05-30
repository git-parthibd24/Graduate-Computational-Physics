#Check a year is leap year or not

y=eval(input('enter a year : '))
if y%400==0 or y%100!=0 and y%4==0:
    print(y,'is a leap year')
else:
    print(y,'is not a leap year')
