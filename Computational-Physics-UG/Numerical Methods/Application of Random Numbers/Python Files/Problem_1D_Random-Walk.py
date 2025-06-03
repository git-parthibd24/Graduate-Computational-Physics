#Problem on Random Walk
'''
Someone is tossing coins and performing a 1D random walk. 
Starting at x=0, he/she is flipping a coin, then takes a step of length in the positive x direction if it is a head and a stp of length in the negative x direction if it a tail. 
Let D be the path and the point after the person takes 30 steps. Compute D. Repeat the process for a total 1000 times. Find out the probability that D lies in range -2 to 2. 
Consider the situatons : 
1) coin is unbiased. 2) coin is biased and chance of getting head is 65%.
'''
import random as rm

print('1.Unbiased Coin')
print('2.Biased Coin')
c=int(input('Enter your choice : '))

count=0
D=0
N=int(input('Enter the number of steps : '))

if c==1:
	for i in range(1,N+1):
		if rm.random() < 0.5:
			D=D+1
		else:
			D=D-1
		if D>=-2 and D<=2:
			count=count+1
	count=count/N
	print('The final position is : ',D,'after',N,'steps') 
	print('The probability of getting the values of D in [-2,2] in unbiased coin is :',count)

if c==2:
	for i in range(1,N+1):
		if rm.random() < 0.65:
			D=D+1
		else:
			D=D-1
		if D>=-2 and D<=2:
			count=count+1
	count=count/N
	print('The final position is :',D,'after',N,'steps')
	print('The probability of getting the values of D in [-2,2] in biased coin is :',count)	
