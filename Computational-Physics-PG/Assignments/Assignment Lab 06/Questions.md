# Question 1
The spectrum of a star is well approximated as a blackbody. While studying the blackbody radiation most of you have encountered the Planck function. Integration of the Planck function over wavelength essentially gives the stellar brightness which is given below :

`B=2*h*c**2∫_0^∞(1/λ**5)*(1/(exp(h*c/(λ*k_B*T))-1))dλ`

Assuming `x=h*c/(λ*k_B*T)`, the integration changes to

`B=(2*(k_B*T)**4)/(h**3c**2)∫_0^∞(x**3)/(e**x-1)dx`

- Calculate the Integration part of this function using trapezoidal rule. Note that this integral has an analytic solution

`∫_0^∞(x**3)/(e**x-1)dx=π**4/15`

Compare your numerically estimated result with the analytical solution.

Hints : Consider a transformation from `x` to `z` by assuming `z=x/(c+x)` to make the integral finite. Here `c` is chosen to be close to the maximum of the integrand. This transformation maps the interval `x∈[0,∞]` to `z∈[0,1]`

# Question 2
Consider the integral 
`E(x)=∫_0^x e**(-t**2)dt`.

1. Write a program to calculate `E(x)` for values of `x` from `0` to `3` in steps of `0.1`. Choose for yourself what method you will use for performing the integral and a suitable number of slices.

2. When you are convinced your program is working, extend it further to make a graph of `E(x)` as a function of `x`.

Note that there is no known way to perform this particular integral analytically, so numerical approaches are the only way forward.
