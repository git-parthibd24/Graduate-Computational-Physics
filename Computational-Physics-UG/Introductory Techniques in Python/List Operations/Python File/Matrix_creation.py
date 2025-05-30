#Read numbers and create a matrix using list

m=eval(input('Enter the number of row :'))
n=eval(input('Enter the number of column :'))
print('Enter the elements rowwise :')
A=[]
for i in range(m):              #Reading elements in matrix by following code
    B=[]
    for j in range(n):
        item=input()
        B.append(item)
    A.append(B)

print('The matrix is :')
for i in A:                     #print the elements in matrix form
    for j in i:
        print(j,end=' ')
    print()
