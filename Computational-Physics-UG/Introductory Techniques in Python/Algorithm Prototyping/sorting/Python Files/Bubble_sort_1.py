#Bubble Sort 1

n=eval(input('How many elements : '))
print('Enter elements : ')
l=[]
for i in range(n):            
    item=eval(input())
    l.append(item)
print('The list before sorting : ',l)
for i in range(n-1):                       #In each iteration, successive bigger numbers are send at last. Since there are n elements in list, this loop must run n times
    flag=True
    for j in range(n-i-1):                 #Sorting the unsorted portion remaining. So decrease the count of iteration i.e position of elements who are needed to be sorted
       if l[j]>l[j+1]:
           l[j],l[j+1]=l[j+1],l[j]
           flag=False
    if flag==True:
       break
print('The sorted list is :',l)