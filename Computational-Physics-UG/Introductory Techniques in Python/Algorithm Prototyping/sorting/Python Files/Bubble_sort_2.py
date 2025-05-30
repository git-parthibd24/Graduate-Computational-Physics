#Bubble Sort 2

#Taking value for list
n=int(input("Number of elements to be entered : "))
p=[]
print("Enter the elements of unsorted list : ")
for i in range(n):
    temp=int(input())
    p.append(temp)
print("Unsorted list is :",p)
ask=int(input("For ascending enter 6 and for descending enter 9 : "))
if ask==6:
    #loop for sorting in ascending order
    for x in range(len(p)-1):
        for y in range(len(p)-1-x):
            if p[y]>p[y+1]:
                p[y],p[y+1]=p[y+1],p[y]
    print("sorted list in ascending order :",p)
elif ask==9:

    #loop for sorting in descending order
    for x in range(len(p)-1):
        for y in range(len(p)-1-x):
            if p[y]<p[y+1]:
                p[y],p[y+1]=p[y+1],p[y]
    print("sorted list in descending order :",p)
else:
    print("error")