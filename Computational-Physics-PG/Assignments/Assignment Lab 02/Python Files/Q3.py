#Question 3
#Add 1st 10 terms of e^x, x being positive integer

n=int(input("Enter the number of terms to add : "))
x=int(input("Enter the value of x : "))

def factorial(n):                    #We can also use math.factorial
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def e_x(x,n):
    sum = 0
    for i in range(n):
        sum += x**i/factorial(i)
    return sum

print('Sum of first',n,'terms of e^x is : ',e_x(1,n))