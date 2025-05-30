#Selection Sort

n=eval(input("How many elements to sort : "))
print("Enter list elements : ")
l=[]
for i in range(n):
    item=int(input())
    l.append(item)
print("Unsorted list is :",l)
for i in range(n-1):                      #Outer loop for passes. Each iteration brings successive smaller numbers at beginning
    index=i                               #Assume the first element of the unsorted list for comparison with next elements
    for j in range(i+1,n):                #Inner loop to find the smallest element
        if l[j]<l[index]:                 #If a smaller element is found
            index=j                       #Update the index of the smallest element
        if l[i]>l[index]:
            l[i],l[index]=l[index],l[i]   #Replace the smallest element with element at 1st position
print("list sorted in ascending order :",l)
