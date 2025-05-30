# Question 1
Find roots on an interval with the bisection method for `f(x)==x**2-4*x+exp(-x)`.

# Question 2
Use Newton-Raphson method to find roots for the same function `f(x)==x**2-4*x+exp(-x)`. Compare the iteration numbers for both methods. Which one is efficient? 

Hint : Newton-Raphson method uses the following algorithm to find roots of a function f(x). 
  
`x_{n+1}=x_n-f(x)/f'(x)` where `x0` is the initial guess value and `n` is the number of iterations.

# Question 3
The equation `x**3-1.2*x**2-8.19*x+13.23==0` has a double root close to `x==2`. Determine this root with the Newton-Raphson method within four decimal places.

# Question 4
Determine Wien's Displacement constant by solving the maxima equation from Planck's spectral energy density formula using the Bisection Method.

# Question 5
Find the roots of the equation `924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1==0` using the Newton-Raphson method.

# Question 6
Find the roots of the equation `x**2-4*x+np.exp(-x)==0` using both the Bisection method and the Newton-Raphson method in the same code. Compare the number of iterations required for each method.

# Question 7
Find the roots of the equation `x-np.tan(x)==0` using the Bisection method in the range `0` to `20`.

# Question 8
BK-7 is a type of common optical crown glass. Its index of refraction `n` varies as a function of wavelength; for shorter wavelengths `n` is larger than for longer wavelengths, and thus violet light is refracted more strongly than red light, leading to the phenomenon of dispersion. The index of refraction is tabulated in the attached data file `refractive index.txt`. 

Suppose we wish to find the index of refraction at a wavelength of `5000°Å`. That wavelength is not found in the table, so we must estimate it from the tabular values. Assume that `n` varies smoothly between the tabulated values without wild excursions. 

- Write a function that will linearly interpolate the tabular data for the index of refraction of BK-7 and return a value for `n` for wavelengths between `3511°Å` and `23254°Å`.






