#You are rolling two die simultaneously and noting the number of dots. Calculate p, the probability of getting the same number of dots from both the die. (Repeat trials for 50, 500, 5000 times)

import random as rn
choice='Y'
while choice=='Y' or choice=='y':
	n=int(input('Enter no of experiments : '))
	count=0
	for i in range(n):
		v1=rn.randint(1,7)
		v2=rn.randint(1,7)
		if v1==v2:
			count+=1
	p=count/n
	print('The probability is :',p)
	choice=input('Do you want to continue y/n ? :')