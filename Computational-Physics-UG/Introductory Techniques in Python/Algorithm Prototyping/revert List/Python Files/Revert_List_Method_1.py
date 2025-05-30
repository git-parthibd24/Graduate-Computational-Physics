#Revert list by conversion to integer

n=eval(input("Enter no. of list elements : "))
print("Enter list elements : ")
a=[]
for i in range(n):
    digit=int(input())
    a.append(digit)
print("The list is ",a)
m=''.join(str(k) for k in a)
a=int(m)
x=0
while a>0:
    b=a%10     #gives last digit of a
    x=x*10+b   #x*10 Creates numbers with 0 at last which can be replaced with new b
    a=a//10    #removes remainder i.e last digit
print("Reverted number is: ",x)
