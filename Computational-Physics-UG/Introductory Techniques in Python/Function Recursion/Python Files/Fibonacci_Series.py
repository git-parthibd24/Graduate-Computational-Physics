#Finding nth term of a Fibonacci Series using recurssion of function
#It is a series whose 1st two terms can be anything and next terms will be sum of previous two terms
#eg:0,1,1,2,3,5,8,13,21,34,55,89...

def fibo(n):
    if n<0:
        print('wrong input')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
N=int(input('Enter order of term: '))
m=fibo(N)
print('Fibonacci number at index',N,'is :',fibo(N))