#Method 5: Greatest Common Divisor of 2 numbers using Euclid's Algorithm

m=int(input('Enter 1st number: '))
n=int(input('Enter 2nd number: '))

if m<n:
    (m,n)=(n,m)
while (m%n)!=0:
    diff=m-n    
    (m,n)=(max(n,diff),min(n,diff))
print('The GCD of two numbers is :',n)
         