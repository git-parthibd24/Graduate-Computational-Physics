#Diagonalizaton of matrix using linalg submodule of numpy and finding eigenvalues,eigenvectors

import numpy as np
A=np.array([[2,0,0],[1,2,1],[-1,0,1]])
print('The given matrix is :')
print(A)
print()

eigval,eigvec=np.linalg.eig(A)

print('The eigenvalues are :', eigval)
print()
print('The eigenvectors are :')

for i in range(len(eigvec)):
    print(eigvec[:,i])

print()   
A_Diag=np.dot(np.dot(np.linalg.inv(eigvec),A),eigvec)    #using PAP^(-1)
print('The diagonal matrix of given matrix is :')
print(A_Diag)

