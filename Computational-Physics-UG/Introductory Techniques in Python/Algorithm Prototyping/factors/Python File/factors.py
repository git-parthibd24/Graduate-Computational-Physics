#Factors of a number

n=eval(input('Enter the number : '))
i=1
while i<=n:
    if n%i==0:
        print('factors are',i)
    i+=1