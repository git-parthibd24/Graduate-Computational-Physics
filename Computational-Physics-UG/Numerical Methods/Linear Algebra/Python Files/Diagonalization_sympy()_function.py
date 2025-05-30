#Diagonalization of matrix using sympy module 

from sympy import *  #import statement that imports all functions, classes and variables from the sympy module 
import numpy as np
M=[[1,2,3],[4,5,6],[7,8,9]]
M1=Matrix(M)         #change to matrix object
P,D=M1.diagonalize()
print(D)
