#Revert list

n=eval(input("Enter no. of list elements : "))
print("Enter list elements : ")
a=[]
for i in range(n):
    digit=int(input())
    a.append(digit)
print("The list is ",a)
i=0
j=len(a)-1    #Counting starts from zero in list
while i<j:
    t=a[i]
    a[i]=a[j] #swapping
    a[j]=t
    i=i+1
    j=j-1
print("Reverted list is: ",a)
