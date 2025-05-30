#Check if a number is factorial of a number or not

def factorial(n):
    i=1
    f=1
    while f<n:        
        i+=1
        f*=i
    if f==n:
        print(n,'is factorial of some number')
    else:
        print(n,'is not a factorial of any number')
        
N=int(input('Enter number to check :'))
factorial(N)