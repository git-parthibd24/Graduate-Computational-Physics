#Plot 2

import numpy as np
import matplotlib.pyplot as plt

#Data
x=np.linspace(0, 10, 100)
y1=np.sin(x)
y2=np.cos(x)

#Create subplots (2 rows, 1 column)
fig,axes=plt.subplots(1,2,sharex=True,sharey=True,figsize=(12,5))  # 1 row,2 column

#First subplot
axes[0].plot(x,y1,'y',label='1st subplot')
axes[0].set_title('Sine Wave')
axes[0].set_xlabel('x')
axes[0].set_ylabel('sin(x)')
axes[0].grid(True)
axes[0].legend(loc='upper right')

#Second subplot
axes[1].plot(x,y2,'b',label='2nd subplot')
axes[1].set_title('Cosine Wave')
axes[1].set_xlabel('x')
axes[1].set_ylabel('cos(x)')
axes[1].grid(True)
axes[1].legend(loc='upper right')


plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Sub_plot\\Python Files\\fig_2.png')
plt.show()
