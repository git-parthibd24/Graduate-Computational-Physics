# Question 1
Write a Python program that computes the sum of all the elements of a matrix `C`, where `C=A@B`. Here `A` and `B` are two matrices of size `N×N`. The value of `N` should be taken as input from the keyboard and the user can choose according to their choice. The elements of the matrices are defined as : 
`A[i,j]=i*j/100` 
`B[i,j]=(i+1)*(j+1)/100` 

Round your answer up to three decimal places using `np.round(x,3)` function of Python.

# Question 2
The Sieve of Eratosthenes is an algorithm for finding all prime numbers less than or
equal to a number N . Read about this algorithm on Wikipedia and implement it in a Python program.

# Question 3
Suppose we have recorded GPS coordinates x0, ..., xn at times t0, ..., tn while running or driving along a straight road. We want to compute the velocity vi and acceleration ai from these position coordinates. Using finite difference approximations, one can establish the formulas

`vi≈(x_{i+1}-x_{i-1})/(t_{i+1}-t_{i-1})`

`ai≈((x_{i+1}-x_i)/(t_{i+1}-t_i)-(x_i-x_{i-1})/(t_i-t_{i-1}))/(0.5*(t_{i+1}-t_{i-1}))`

for i=1, ..., n-1 (vi and ai correspond to the velocity and acceleration at point xi at time ti, respectively).

- Write a Python function kinematics(i, x, t) for computing vi and ai, given the arrays x and t of position and time coordinates (x0, ..., xn and t0, ..., tn).

- Write a Python function test_kinematics() for testing the implementation in the case of constant velocity V. Set t0=0, t1=0.5, t2=1.5 and t3=2.2, and xi = V*ti. Call the kinematics function for the legal i values.

# Question 4
- Write a function `count_pairs(dna,pair)` that returns the number of occurrences of a pair of characters (pair) in a DNA string (dna). For example, calling the function with dna as `'ACTGCTATCCATT'` and pair as `'AT'` will return 2.

- Count how many times a certain string appears in another string. For example, the function returns 3 when called with the DNA string `'ACGTTACGGAACG'` and the substring `'ACG'`.

Hint : For each match of the first character of the substring in the main string, check if the next n characters in the main string match the substring, where n is the length of the substring. Use slices like s[3:9] to pick out a substring of s.

