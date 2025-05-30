#Question 2
#Implement Sieve of Eratosthenes algorithm to generate prime numbers less than or equal a number N


# Creating a list that can hold numbers from 2 to N
N=int(input("Enter the upper limit of number : "))
numbers=[]

if N>=2:
    for i in range(N-1):  #Excluding '1' from the list
        numbers.append(1)

    #Flagging primes as 1 and non-primes as 0 within the created list
    prime=2
    while prime*prime<=N:
        if numbers[prime-2]==1:
            for i in range(prime*prime,N+1,prime):
                numbers[i-2]=0
        prime+=1
    print(numbers)
    # Printing the prime numbers according to the index position of 1 in the list
    print('The prime numbers within',N,'are :')
    for i in range(len(numbers)):
            prime_numbers=[i+2 for i in range(len(numbers)) if numbers[i]==1]      # list comprehension

    for i in range(len(prime_numbers)):
        if i==len(prime_numbers)-1:              # Check if it's the last prime number
            print(prime_numbers[i], end='')      # No comma for the last prime number
        else:
            print(prime_numbers[i], end=',')     # Comma for other prime numbers

else:
    print('No prime numbers within',N)