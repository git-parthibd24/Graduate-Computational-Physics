#Method 3: Greatest Common Divisor of 2 numbers

m=int(input('Enter 1st number: '))
n=int(input('Enter 2nd number: '))
i=min(m,n)
while i>0:
    if m%i==0 and n%i==0:
        print('The GCD of two numbers is :',i)
        break
    else:
        i=i-1