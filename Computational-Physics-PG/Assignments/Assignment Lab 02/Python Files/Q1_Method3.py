#Question 1
#Find the nth Fibonacci number and the ratio of the nth Fibonacci number to the (n-1)th Fibonacci number. (Approaches Golden Mean when n is large)
#Explicitly evaluation of all terms of Fibonacci Series using dynamically updated variables

f='Y' 
while f=='Y' or f=='y':
    n=eval(input('Enter index of Fibonacci series (starting from 1) : '))
    a,b=0,1
    if n<1 or n//1!=n:
        print('Wrong Input')
        f=input('Do you wish to retry? (Y/N) : ')  

    if n==3:
        print('Fibonacci number at index',n,'is :',b+a)
        print('Fibonacci number at index',n-1,'is :',b)
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is :',(b+a)/b)
        break
    
    if n==2:
        print('Fibonacci number at index',n,'is :',b)
        print('Fibonacci number at index',n-1,'is :',a)
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is not defined')
        break

    if n==1:
        print('Fibonacci number at index',n,'is :',a)
        print('Fibonacci number at index',n-1,'is not defined')
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is not defined')
        break
    
    else:
        def fibo(n):
            a,b=0,1               #When global and local variables have same name, global variable can't be modified in a function. So we have to define the variables again in the function. We can also access the global variable inside function by copying it to a local variable as x=globals()['a'] or by using global a,b in the function          
            for i in range(n-2):  #can't perform n=3 as it will give 0 iterations for n-1 th term
                c=a+b
                a=b               #a is read as local here but it is read as global in c=a+b if they are not defined locally in the function, so they contradicts and a is treated as local variable
                b=c               #b=b+a means modification of global variable b in local scope having same name if b is already not defined in local scope
            return c              #local variables can be accessed outside the function by returning them. If global and local variable have same name, local variable is always preferred inside a function
            
        print('Fibonacci number at index',n,'is :',fibo(n))
        print('Fibonacci number at index',n-1,'is :',fibo(n-1))   #We can also get this simply by printing updated b and use of function can be avoided in this case.
        print('The ratio of Fibonacci number at index',n,'to Fibonacci number at index',n-1,'is : ',format(fibo(n)/fibo(n-1),'0.2f'))
        break
