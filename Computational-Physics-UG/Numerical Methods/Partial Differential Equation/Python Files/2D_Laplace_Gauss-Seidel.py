#Solution of Laplace's equation in 2D square plane using Gauss Seidel Scheme

import numpy as np
import matplotlib.pyplot as plt

#Total no. of grid points
N=101
iteration=100
L=10                        #Length of the 2D surface
#Boundary and Initial conditions at boundaries and top surface of the plane
u=np.zeros((N,N))         
u[N-1,:]=100                #Top surface at 100 V, this is the last row in the matrix since it has the maximum row index which corresponding to top surface in right-handed cartesian coordinate system         		          

E=[]
for _ in range(iteration):
    u0=u.copy()	            #Store old values for error calculation
    
    #updating the array using four nearby points with initial guess and current values of updated points
    for i in range(1,N-1):
        for j in range(1,N-1):
            u[i,j]=0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1])
			
    err=np.sum(abs(u-u0))
    E.append(err)

#For plotting of the error with iterations
plt.plot(range(1,iteration+1),E,'r-',lw=1)
plt.title('Error with increase in number of iterations')
plt.ylabel('Error')
plt.xlabel('No. of iterations')
plt.axhline(color='black')
plt.axvline(color='black')
plt.show()

#3D plotting
x=np.linspace(0,L,N)
y=np.linspace(0,L,N)
X,Y=np.meshgrid(x,y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,u,cmap='coolwarm')
ax.set_title("Solution of Laplace's Equation in 2D")
ax.set_xlabel('$X$',fontsize=10,rotation=170)
ax.set_ylabel('$Y$',fontsize=10)
ax.set_zlabel('$Voltage$',fontsize=10,rotation=60)
plt.show()


#Contour plotting and colour mapping
colourMap=plt.cm.coolwarm
colorinterpolation=20
plt.title('Voltage Distribution')
x=np.linspace(0,L,N)
y=np.linspace(0,L,N)
X,Y=np.meshgrid(x, y)
X,Y=np.meshgrid(x,y)
plt.xlabel('x-direction')
plt.ylabel('y-direction')
cf=plt.contourf(X,Y,u,colorinterpolation,cmap=colourMap)
cbar=plt.colorbar(cf)
'''
img=plt.imshow(u,cmap='coolwarm',origin='lower',extent=[0,L,0,L])  #cmap='viridis'
plt.colorbar(img,label='Voltage')
'''
cbar.set_label('Voltage',rotation=0,labelpad=20) 
plt.show()
