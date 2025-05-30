#Method 2: Greatest Common Divisor of 2 numbers

m=int(input('Enter 1st number: '))
n=int(input('Enter 2nd number: '))
fm=[]
cf=[]
for i in range(1,min(m,n)+1):
    if m%i==0 and n%i==0:
        cf.append(i)
print('The GCD of two numbers is :',cf[-1])