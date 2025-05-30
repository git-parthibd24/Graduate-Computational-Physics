#Single point in 3d-Space

import matplotlib.pyplot as plt

#Create figure and axes
fig=plt.figure(figsize=(4,4))
ax=fig.add_subplot(111,projection='3d')

#Plot the point
ax.scatter(2,3,4,color='red')
fig.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\3D_plot\\Python Files\\point.png')
plt.show()