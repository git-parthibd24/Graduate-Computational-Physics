#Binary Search using recurssion
#Works iff dataset is sorted
#high and low are decremented or incremented by 1 from low to prevent getting stuck in a loop

def b_search(l,key,low,high):
    if high>=low:
        mid=(high+low)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            return b_search(l,key,low,mid-1)  
        else:
            return b_search(l,key,mid+1,high)
    else:
        return -1
n1=int(input("Enter the number of elements of the list : "))
print("Enter the elements")   #Only in sorted order
L1=[]
for i in range(0,n1):
    L1.append(eval(input()))
x=eval(input("Enter the element to search : "))
pos=b_search(L1,x,0,len(L1)-1)
if pos!=-1:
    print("element present in index",pos+1)
else:
    print("element not present")