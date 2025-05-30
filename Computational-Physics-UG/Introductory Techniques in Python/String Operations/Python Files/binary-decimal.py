#Accept a string containing binary digits and convert it to corresponding decimal number

s=input('Enter a string with binary digits : ')
n=len(s)
k=n-1
sum1=0
for i in s:
    num=int(i)
    sum1=sum1+(pow(2,k))*num
    k=k-1
print(sum1)