#Linear Search 2

def linear_search(x,l):
    n=len(l)    
    i=0
    while i<n:
        if x==l[i]:
            break
        i+=1
    return i
n1=int(input('Enter the number of elements to be inserted : '))
print('Enter elements in the list : ')
l1=[]
for i in range(0,n1):
    l1.append(eval(input()))
x1=eval(input('Enter element to search in the list : '))
pos=linear_search(x1,l1)
if pos==n1:                             #or pos>n1-1
    print(x1,'not found in the list')
else:    
    print(x1,'found in position :',pos+1)