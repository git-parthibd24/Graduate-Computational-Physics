# Question 1
**Quantum oscillators**

Consider the one-dimensional, time-independent Schrödinger equation in a harmonic (i.e., quadratic) 
potential `V(x)=V₀x²/a²`, where `V₀` and `a` are constants.

1. Write down the Schrödinger equation for this problem and convert it from a second-order equation
to two first-order ones, as explained in class. Write a program to find the energies of the ground state
and the first two excited states for these equations when `m` is the electron mass, `V₀=50 eV`, and
`a=10⁻¹¹ m`. Note that in theory the wavefunction goes all the way out to `x=±∞`, but you can get
good answers by using a large but finite interval. Try using `x=−10a` to `+10a`, with the wavefunction
`ψ=0` at both boundaries. (In effect, you are putting the harmonic oscillator in a box with impenetrable
walls.) The wavefunction is real everywhere, so you don't need to use complex variables, and you can use
evenly spaced points for the solution - there is no need to use an adaptive method for this problem.

 The quantum harmonic oscillator is known to have energy states that are equally spaced. Check that this
 is true, to the precision of your calculation, for your answers. (Hint: The ground state has energy in the
 range 100 to 200 eV.)

2. Now modify your program to calculate the same three energies for the anharmonic oscillator with
`V(x)=V₀x⁴/a⁴`, with the same parameter values. Also calculate the properly normalized wavefunctions of the anharmonic
oscillator for a given state and make a plot of them, all on the same axes, as a function of `x` over
a modest range near the origin - say `x = −5a` to `x = 5a`.

To normalize the wavefunctions you will have to evaluate the integral `∫₋∞^∞|ψ(x)|²dx` and then
rescale ψ appropriately to ensure that the area under the square of each of the wavefunctions is 1.
Either the trapezoidal rule or Simpson's rule will give you a reasonable value for the integral.

Note, however, that you may find a few very large values at the end of the array holding the
wavefunction. Where do these large values come from? Are they real, or spurious?

One simple way to deal with the large values is to make use of the fact that the system is
symmetric about its midpoint and calculate the integral of the wavefunction over only the left-
hand half of the system, then double the result. This neatly misses out the large values.

# Question 2
**Gaussian Elimination**

Solve the equation `Ax=v` where

`A=⎡0  0  2  1  2⎤` 
`  ⎢0  1  0  2 -1⎥` 
`  ⎢1  2  0 -2  0⎥` 
`  ⎢0  0  0 -1  1⎥` 
`  ⎣0  1 -1  1 -1⎦`

and,

`v=⎡ 1⎤` 
`  ⎢ 1⎥` 
`  ⎢−4⎥` 
`  ⎢−2⎥` 
`  ⎣ 1⎦`

# Question 3
Solve the previous problem using **LU Decomposition**.

# Question 4
**LU Decomposition and determinant of a matrix**

Solve the equation `AX=V` by LU decompositon method, where
`A=⎡ 3 −1  4⎤` 
`  ⎢−2  0  5⎥` 
`  ⎣ 7  2 -2⎦`

and 
`V=⎡6 −4⎤` 
`  ⎢3  2⎥` 
`  ⎣7 −5⎦`, 

and compute determinant of the matrix `A`. 

**Hints :** Determinant of a matrix is determined by the product of diagonal element of upper triangular matrix `U` after LU decomposition.

# Question 4
**Coupled Mass-Spring System**

Suppose we have a set of `N` identical masses in a row, joined by identical linear springs.
For simplicity, we'll ignore gravity - the masses and springs are floating in outer space. If we jostle this system the masses will vibrate relative to one another under the action of the springs. The motions of the system could be used as a model of the vibration of atoms in a solid, which can be represented with reasonable accuracy in exactly this way. Here we examine the modes of horizontal vibration of the system.

Let us denote the displacement of the `i`th mass relative to its rest position by `sᵢ`. Then the equations of motion for the system are given by Newton's second law :

`m(d²sᵢ/dt²)=k(sᵢ₊₁-sᵢ)+k(sᵢ₋₁-sᵢ)+Fᵢ`

where `m` is the mass and `k` is the spring constant. The left-hand side of this equation is just mass times acceleration, while the right-hand side is the force on mass `i` due to the springs connecting it to the two adjacent masses, plus an extra term `Fᵢ` that represents any external force imposed on mass `i`. 

The only exceptions to the equation are for the masses at the two ends of the line, for which there is only one spring force each, so that they obey the equations :

`m(d²s₁/dt²)=k(s₂-s₁)+F₁`
`m(d²s_N/dt²)=k(s_N₋₁-s_N)+F_N`

Now suppose we drive our system by applying a harmonic (i.e., sinusoidal) force to the first mass: `F₁=Ce^(iωt)`, where `C` is a constant and we use a complex form, as one commonly does in such cases, on the understanding that we will take the real part at the end of the calculation. If we are thinking of this as a model of atoms in a solid, such a force could be created by the charge of the atoms interacting with a varying electric field, such as would be produced by an electromagnetic wave falling on the solid.

The net result of the applied force will be to make all the atoms oscillate in some fashion with angular frequency `ω`, so that the overall solution for the positions of the atoms will take the form:

`sᵢ(t)=xᵢe^(iωt)`

for all `i`. The magnitude of the quantity `xᵢ` controls the amplitude of vibration of mass `i` and its phase controls the phase of the vibration relative to the driving force.

Substituting the solution in the eoms, we find that :

`-mω²x₁=k(x₂-x₁)+C`

`-mω²xᵢ=k(xᵢ₊₁-xᵢ)+k(xᵢ₋₁-xᵢ)`; for all `i` in the range `2 ≤ i ≤ N-1`

`-mω²x_N=k(x_N₋₁-x_N)` 

These equations can be rearranged to read:

`(α-k)x₁-kx₂=C`
`αxᵢ-kxᵢ₋₁-kxᵢ₊₁=0`
`(α-k)x_N-kx_N₋₁=0`

where `α=2k-mω²`.

This is precisely a tridiagonal set of simultaneous equations.
Solve these system of equations using gaussian Elimination and plot the amplitude of vibrations of the atoms along the length of the solid.
