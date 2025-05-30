#Double Integration using Trapezoidal Rule (variable limits)
#x limits run from 0 to  y

import numpy as np
def f(x,y):
    return np.sin(x+y)

ax=0
ay=0
by=np.pi/4

def x_int(ax,bx,y):
	s0x,sx=0,0
	nx=2
	while True:
		hx=(bx-ax)/nx
		sx=(2*sum([f(ax+i*hx,y) for i in range (1,nx)])+f(ax,y)+f(bx,y))*(hx/2)        
		if abs(sx-s0x)<0.00001:
			break
		nx=nx*2
		s0x=sx
	return sx

s0y,sy=0,0
ny=2
while True:
	hy=(by-ay)/ny
	sy=(2*sum([x_int(ax,ay+i*hy,ay+i*hy) for i in range (1,ny)])+x_int(ax,ay,ay)+x_int(ax,by,by))*(hy/2)        
	if abs(sy-s0y)<0.00001:
		break
	ny=ny*2
	s0y=sy
	
print('The value of integral is :',format(sy,'0.4f'))
