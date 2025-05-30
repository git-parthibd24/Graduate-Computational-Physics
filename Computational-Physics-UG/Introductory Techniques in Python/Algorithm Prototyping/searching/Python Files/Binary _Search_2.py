#Binary Search (2nd Method)
#Works iff dataset is sorted
#high and low are decremented or incremented by 1 from low to prevent getting stuck in a loop

def read_data(n):
    l=[]
    print('Enter elemnts to insert in the list : ')
    for i in range(n):
        l.append(eval(input()))
    return l
def b_search(key,L):
    high=len(L)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if key==L[mid]:
            return mid
        elif key<L[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
#main part
n1=eval(input('no. of elements to be inserted : '))
l1=[]
l1=read_data(n1)
k=eval(input('Enter the element to search : ')) #Only in sorted order
val=b_search(k,l1)
if val!=False:
    print(k,'found in position :',val+1)
else:
    print(k,'not found in the list')