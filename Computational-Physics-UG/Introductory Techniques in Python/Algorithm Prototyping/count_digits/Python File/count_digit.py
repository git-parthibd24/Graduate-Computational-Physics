#Count the digits in a number

num=eval(input('Enter a number : '))
count=0
while num!=0:
    count+=1
    num=num//10
print('The number of digits in the number are: ',count)