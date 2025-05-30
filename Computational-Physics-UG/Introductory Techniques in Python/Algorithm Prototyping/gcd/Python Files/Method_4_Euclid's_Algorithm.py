#Method 4: Greatest Common Divisor of 2 numbers using Euclid's Algorithm

m=int(input('Enter 1st number: '))
n=int(input('Enter 2nd number: '))
while n>0:
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        print('The GCD of two numbers is :',n)
        break
    else:
        m=m-n
        