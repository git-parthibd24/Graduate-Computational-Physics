#Sum of reciprocal of numbers from -4 to 4

sum=0.0
i=-5
while i<=3:
    i+=1
    if i==0:
        continue
    sum+=1/i
    
print('Sum of reciprocal of numbers is :',sum)