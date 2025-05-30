#Method 1: Greatest Common Divisor of 2 numbers

m=int(input('Enter 1st number: '))
n=int(input('Enter 2nd number: '))
fm=[]
fn=[]
cf=[]
for i in range(1,m+1):
    if m%i==0:
        fm.append(i)
for j in range (1,n+1):
    if n%j==0:
        fn.append(j)
for f in fm:
    if f in fn:
        cf.append(f)
print('The GCD of two numbers is :',cf[-1])