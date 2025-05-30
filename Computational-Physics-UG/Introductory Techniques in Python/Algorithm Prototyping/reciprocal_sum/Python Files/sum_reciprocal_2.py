sum=0.0
i=-4
while i<=4:
    if i==0:
        i+=1  # Increment i to avoid infinite loop
        continue
    sum+=1/i
    i+=1
    
print('Sum of reciprocal of numbers is :',sum)