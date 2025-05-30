#Linear Search 1

def linear_search(l,x):
    for i in range(0,len(l)):
        if x==l[i]:            
            return i
L=[]
n=int(input('Enter the number of elements of the list : '))
print('Enter elements to insert in the list : ')
for i in range(n):
    L.append(eval(input()))
n1=len(L)
x1=eval(input('Enter the number to search : '))
pos=linear_search(L,x1)
if pos==n1:
    print('Element not found')
else:
    print(x1,'found in position :',pos+1)