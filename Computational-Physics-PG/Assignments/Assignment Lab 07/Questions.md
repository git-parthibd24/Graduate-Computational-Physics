# Question 1
Use Romberg integration to evaluate  `∫_0^πsin(x)dx` with four decimal places accuracy.

# Question 2
Estimate `∫_0^πf(x)dx` as accurately as possible, where `f(x)` is defined by the following data :

`x=[0,π/4,π/2,3π/4,π]`

`f(x)=[1.0000,0.3431,0.2500,0.3431,1.0000]`

Use your favorite integration technique that requires fewer data points.

# Question 3
**Quantum Harmonic Oscillator Problem**

In units where all constants are 1, the wavefunction of the nth energy level of the one-dimensional quantum harmonic oscillator—
i.e., a spinless point particle in a quadratic potential well—is given by :

`ψ_n(x)=1/sqrt(2^n*n!√π)e^(-x^2/2)*H_n(x)`
for `n=0,...,∞`, where `H_n(x)` is the nth Hermite polynomial. Hermite polynomials satisfy a relation
somewhat similar to that for the Fibonacci numbers, although more complex :

`H_{n+1}(x)=2*x*H_n(x)-2*n*H_{n-1}(x)`
with `H_0(x)=1` and `H_1(x)=2x`.

- Write a user-defined function `H(n,x)` that calculates `H_n(x)` for given `x` and any integer `n≥0`. Use your function to plot the wavefunctions for `n=0,1,2,3` on the same graph (`x∈[-4,4]`).

- Make a separate plot of the wavefunction for `n=30` (`x∈[-10,10]`). Hint : If your
program takes too long to run in this case, then you’re doing the calculation wrong—the program
should take only a second or so to run.

- The quantum uncertainty is given by :

`√<x^2>=sqrt(∫_{-∞}^∞ x^2|ψ_n(x)|^2 dx)`

Write a program to evaluate this integral using Gaussian quadrature (100 points) and calculate the uncertainty for `n=5`. Expected result: `√<x^2>≈2.3`.

# Question 4
Evaluate the double integral using Adaptive Trapezoidal Rule :

`∫_-1^1∫_-1^1cos(πx/2)cos(πy/2)dxdy`
