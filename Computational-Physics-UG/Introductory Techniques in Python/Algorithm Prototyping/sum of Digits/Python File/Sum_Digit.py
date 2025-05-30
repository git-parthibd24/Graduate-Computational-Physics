#Sum of digits of a number with string input

a=str(input('Enter a number: '))
s=0
for i in range(len(a)):
    s=s+int(a[i])
print('Sum of the digits of',a,'=',s)