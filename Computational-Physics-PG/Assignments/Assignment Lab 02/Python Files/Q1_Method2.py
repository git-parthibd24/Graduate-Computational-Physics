#Question 1
#Find the nth Fibonacci number and the ratio of the nth Fibonacci number to the (n-1)th Fibonacci number. (Approaches Golden Mean when n is large)
#Explicitly evaluation of all terms of Fibonacci Series using list

fib=[0,1]
f='Y' 
while f=='Y' or f=='y':
    n=eval(input('Enter index of Fibonacci series (starting from 1) : '))
    if n<1 or n//1!=n:
        print('Wrong Input')
        f=input('Do you wish to retry? (Y/N) : ')  
    
    if n==2:
        print('Fibonacci number at index',n,'is :',fib[1])
        print('Fibonacci number at index',n-1,'is :',fib[0])
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is not defined')
        break

    if n==1:
        print('Fibonacci number at index',n,'is :',fib[0])
        print('Fibonacci number at index',n-1,'is not defined')
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is not defined')
        break
    
    else:
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])

        print('Fibonacci number at index',n,'is :',fib[-1])
        print('Fibonacci number at index',n-1,'is :',fib[-2])
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is : ',format(fib[-1]/fib[-2],'0.2f'))
        break