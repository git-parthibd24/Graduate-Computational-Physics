#Question 1 (1)
#RK-4 Implementation in Simple Pendulum Problem with Animation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g=9.81                  #Acceleration due to gravity (m/s²)
l=0.1                   #Length of the pendulum (m)
theta0=np.radians(179)  #Initial angle (converted to radians) (numpy.sin() expects radians as input)
w0=0                    #Initial angular velocity

t0,tn,h=0,5,0.001  

def f_theta(t,theta,w):
    return w

def f_w(t,theta,w):
    return -(g/l)*np.sin(theta)

def RK4(funcs,t0,u0,tn,h):
    T=np.arange(t0,tn+h,h)
    R=np.zeros((len(T),len(u0)))
    R[0]=u0   
    for i in range(len(T)-1):
        t,u=T[i],R[i]
        k1=h*np.array([f(t,*u) for f in funcs])
        k2=h*np.array([f(t+h/2,*(u+k1/2)) for f in funcs])
        k3=h*np.array([f(t+h/2,*(u+k2/2)) for f in funcs])
        k4=h*np.array([f(t+h,*(u+k3)) for f in funcs])
        R[i+1]=u+(k1+2*k2+2*k3+k4)/6    
    return T,R[:,0],R[:,1]

functions=[f_theta,f_w]
T,Theta,W=RK4(functions,t0,[theta0,w0],tn,h)

plt.figure()
plt.plot(T,np.degrees(Theta),'b-')
plt.xlabel('Time (s)')
plt.ylabel(r'Angle $\theta(t)$ (degrees)')
plt.title('Non linear Pendulum Motion')
plt.axhline(color='black',linewidth=1)
plt.axvline(color='black',linewidth=1)
plt.grid()
plt.savefig('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q1_1.png')
plt.show()


x=l*np.sin(Theta)   #Horizontal position of bob
y=-l*np.cos(Theta)  #Vertical position of bob

#Plotting and making animation
plt.xlim(-l-0.02,l+0.02)  
plt.ylim(-l-0.02,l+0.02)   
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Pendulum Motion Animation")
plt.grid()

#Draw hinge
plt.plot(0,0,'ko',markersize=8)  
plt.axhline(0,color='black',linewidth=1)  
plt.axvline(0,color='black',linewidth=1)  

#Pendulum components
lines,=plt.plot([],[],'go-',lw=2,markersize=10,markerfacecolor='b')  #Plots (x,y) points of bob,'o-' ensures line connecting points with hinge later
trace,=plt.plot([],[],color='blue',linestyle='--',lw=1,alpha=0.5)   #Trace of bob's motion

#Trace storage
trace_x=[]        #Stores x positions of bob
trace_y=[]        #Stores y positions of bob

def next_frame(i):
    x_bob=x[i]  #Get current x position of bob from the list index wise
    y_bob=y[i]  #Get current y position of bob from the list index wise
    
    #Update pendulum rod and bob
    lines.set_data([0,x_bob],[0,y_bob])  #Connect hinge (0,0) to bob's position with line as initialized in intial plot
    
    #Update trace
    trace_x.append(x_bob)                #Append new x position to trace
    trace_y.append(y_bob)                #Append new y position to trace
    trace.set_data(trace_x,trace_y)      #Plots all the previous points and connects them with line
    
    return lines,trace  

#Set the aspect ratio
plt.gca().set_aspect('equal',adjustable='box')

ani=FuncAnimation(plt.gcf(),next_frame,frames=len(T),interval=10,blit=True)  #Create animation for duration of displaying len(T) points. interval is duration between each frame and frames is no of frames. From here we get framerate of the video that is being displayed with the execution of code

#Save animation to file with a certain framerate for the video file. Large dpi gives clearer plot
ani.save('/home/tux_blue/Desktop/GitHub/Computational-Physics-PG/Assignments/Assignment Lab 09/Python Files/Q1_1_Pendulum_Animation.mp4',fps=60,dpi=300)  
plt.show()
