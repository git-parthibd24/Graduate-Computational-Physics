#Question 1
#Find the nth Fibonacci number and the ratio of the nth Fibonacci number to the (n-1)th Fibonacci number. (Approaches Golden Mean when n is large)
#Function Recurssion Method

f='Y' 
while f=='Y' or f=='y':
    n=eval(input('Enter index of Fibonacci series (starting from 1) : '))
    if n<1 or n//1!=n:
        print('Wrong Input')
        f=input('Do you wish to retry? (Y/N) : ')  
   
    if n==1:
        print('Fibonacci number at index',n,'is :',n-1)
        print('Fibonacci number at index',n-1,'is not defined')
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is not defined')
        break

    if n==2:
        print('Fibonacci number at index',n,'is :',n-1)
        print('Fibonacci number at index',n-1,'is :',n-2)
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is not defined')
        break

    if n>=3:
        def fib(n):
            if n==1:
                return 0
            elif n==2:
                return 1
            else:
                return fib(n-1)+fib(n-2)
        
        print('Fibonacci number at index',n,'is :',fib(n))
        print('Fibonacci number at index',n-1,'is :',fib(n-1))
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is : ',format(fib(n)/fib(n-1),'0.2f'))
        break