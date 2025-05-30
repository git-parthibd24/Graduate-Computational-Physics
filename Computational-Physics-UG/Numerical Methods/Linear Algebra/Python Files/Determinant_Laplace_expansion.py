#Determinant of a matrix using function recursion

import numpy as np

def determinant(matrix,n):
    if n==1:                                               #base case for 1x1 matrix
        return matrix[0,0]                             
    if n==2:                                               #base case 2x2 matrix
        return matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
    
    det=0
    reduced_matrix=matrix[1:,:]                            #remove the first row
    for j in range(n):
        submatrix=np.concatenate((reduced_matrix[:,:j],reduced_matrix[:,j+1:]),axis=1)            #create submatrix by excluding the j-th column using 2D array slicing and joining left and right side of jth column
        det+=((-1)**j)*matrix[0,j]*determinant(submatrix,n-1)                                     #laplace expansion formula
    
    return det

n=4
A=np.random.randint(1,10,size=(n,n))
print("Matrix A is :")
print()
print(A)
print()

print('The determinant of the matrix is :',determinant(A,n))

