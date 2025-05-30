#Convertion of octal to decimal

import numpy as np
import time

choice='Y'
while choice=='Y' or choice=='y':
	octal=eval(input('Enter the octal number : '))
	#start=time.time()
	integer=str(int(octal//1))
	lenint=len(integer)
	fraction=str(np.round(octal%1,len(str(octal))-lenint-1))
	inarray=np.array([int(x) for x in integer])
	digits='0123456789'
	frarray=np.array([int(i) for i in fraction if i in digits])
	#print(inarray)
	#print(frarray)
	counterin,counterfr=0,0
	for i in inarray:
		if i > 7:
			counterin+=1	
	for i in frarray:
		if i > 7:
			counterfr+=1 
	if counterin==0 and counterfr==0:
		break
	print('Invalid octal number!')
	choice=input('Try Again ?(Y,N) : ')

if choice=='Y' or choice=='y':
	frarray=frarray[1:]			
	decimalint,decimalfrac=0,0
	for i in range(int(len(inarray))):  
		decimalint+=inarray[-i-1]*8**i

	for i in range(int(len(frarray))):
		decimalfrac+=frarray[i]*8**(-(i+1))

	decimal=decimalint+decimalfrac
	#end=time.time()
	print('The decimal equivalent is (approximated) :',decimal)
	#print(end-start)

