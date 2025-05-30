#Prime factors of a number

n=eval(input('Enter the number : '))
i=1

l=[]
while i<=n:
    if n%i==0:
        flag=False
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    flag=True
                    break
            if flag==False:
                l.append(i)
                #print('prime factors are :',i)
    i+=1
if len(l)>0:
    print('The prime factors are :')
    for i in range(len(l)):
        print(l[i])
else:
    print('There are no prime factors')