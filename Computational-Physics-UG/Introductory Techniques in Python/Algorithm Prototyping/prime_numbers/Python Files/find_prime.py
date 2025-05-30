#Prime numbers within a range

lower=int(input("Enter lower range :"))  
upper=int(input("Enter upper range :"))  
for num in range(lower,upper+1):  
   if num>1:  
       for i in range(2,num):  
           if num%i==0:  
               break  
       else:  
           print('The prime number is :',num) 