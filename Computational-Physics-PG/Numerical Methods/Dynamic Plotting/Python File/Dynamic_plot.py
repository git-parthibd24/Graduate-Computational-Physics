#Plotting and making movie

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x,m,s):   #m is mean, s is standard deviation
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m=0; s_start=2; s_stop=0.2
s_values=np.linspace(s_start,s_stop,30) #we will update the graph for these values of s

x=np.linspace(-3*s_start,3*s_start,1000)

max_f=f(0,m,s_stop)
plt.axis([x[0],x[-1],0,max_f])  #create the x and y axis in the given range
plt.xlabel('x')
plt.ylabel('y')

min_f=f(x,m,s_start)
lines=plt.plot(x,min_f) #initial plot to create the lines object
def next_frame(s): 
    y=f(x,m,s)
    lines[0].set_ydata(y) #plot the updated graph
    return lines

ani=FuncAnimation(plt.gcf(),next_frame,frames=s_values,interval=50)  #calling the function
ani.save('S:\\Documents\\Github\\Computational-Physics-PG\\Numerical Methods\\Dynamic Plotting\\Python File\\movie.mp4',fps=60)
plt.show()
