# Question 2
# Write a program that asks the user to input the x and y coordinates of a point in the Cartesian plane. The program should then calculate and output the polar coordinates of the point. The program should be written in Python and should be well commented. The program should be submitted as a single file named Q2.py.

import numpy as np
x=eval(input('Enter the x coordinate : '))
y=eval(input('Enter the y coordinate : '))

r=np.sqrt(x**2+y**2)

if x==0 and y==0:
    print('The value of r is:',format(r,'0.2f'),'but value of \u03B8 (in deg) is not defined')
if x==0 and y>0:
    print('The value of r and \u03B8 (in deg) is : ',format(r,'0.2f'),'and',format(90,'0.2f'))
if x==0 and y<0:
    print('The value of r and \u03B8 (in deg) is : ',format(r,'0.2f'),'and',format(270,'0.2f'))
if x<0 and y>=0:
    theta=180-abs(np.arctan(y/x)*180/np.pi)
    print('The value of r and \u03B8 (in deg) is : ',format(r,'0.2f'),'and',format(theta,'0.2f'))
if x<0 and y<0:
    theta=180+np.arctan(y/x)*180/np.pi
    print('The value of r and \u03B8 (in deg) is : ',format(r,'0.2f'),'and',format(theta,'0.2f'))
if x>0 and y<0:
    theta=360-abs(np.arctan(y/x)*180/np.pi)
    print('The value of r and \u03B8 (in deg) is : ',format(r,'0.2f'),'and',format(theta,'0.2f'))
if x>0 and y>0:
    theta=np.arctan(y/x)*180/np.pi
    print('The value of r and \u03B8 (in deg) is : ',format(r,'0.2f'),'and',format(theta,'0.2f'))