import numpy as np

def bisect(f,a,b):  
    while True:
        x=(a+b)/2
        if f(a)*f(x)<0:
            b=x
        else:
            a=x
        if f(x)==0 or abs(a-b)<=0.0001:
            break
    return x

x_val=np.linspace(-1,1,10000)

def root_search(f):  
    A,B,L=[],[],[]
    
    for i in range(len(x_val)-1):
        if f(x_val[i])*f(x_val[i+1])<0:
            A.append(x_val[i])
            B.append(x_val[i+1])
    
    for i in range(len(A)):
        L.append(bisect(f,A[i],B[i]))  
           
    L=np.array(L)
    return L
