#Insertion Sort

def insertion_sort(arr):
    for i in range(1,len(arr)):                       #Loop starts from 1 (2nd element)
        key=arr[i]                                    #Current element flagged as key and start comparing with previous elements                                       
        while i>=1 and key<arr[i-1]:                  #Condition to check greater number
            arr[i]=arr[i-1]                           #Shift element to the right (update right element with left element)     
            arr[i-1]=key                              #Insert the old key at left position. This key works only inside the while loop. If the while loop breaks, new key is assigned in main the for loop
            i=i-1                                     #Repeat same for lower indices

arr=[]
n=int(input("Enter no. of elements : "))
print('Enter the numbers :')
for i in range(0,n):
    a=float(input())
    arr.append(a)

print("Unsorted List :")
print(arr)
insertion_sort(arr)
print(" ")
print("Sorted List :")
print(arr)