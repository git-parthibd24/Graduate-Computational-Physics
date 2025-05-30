# Question 1
A well-known quantum mechanics problem involves a particle of mass m that encounters a one-dimensional potential step.
The particle has initial kinetic energy E and wavevector `k1=np.sqrt(2*m*E)/hbar`. 
It enters from the left and encounters a sudden jump in potential energy of height 'V' at position x=0.
When E>V, the particle may:

- (a) Transmit past the step, with reduced kinetic energy E-V and wavevector `k2=np.sqrt(2*m*(E-V))/hbar`.
- (b) Reflect back, with the same kinetic energy and wavevector k1, but in the opposite direction.

The transmission and reflection probabilities are given by:
```
T=(4*k1*k2)/(k1+k2)**2
R=((k1-k2)/(k1+k2))**2
```
Suppose m=9.11e-31 kg, E=10 eV, V=9 eV with hbar=1.0545718e-34 and eV=1.60218e-19. 
Write a Python program to compute and print T and R using the formulas above.

# Question 2
Write a python program to perform a co-ordinate transformation from cartesian to polar
co-ordinate. That is, ask the user for the Cartesian coordinates x,y of a point in two-dimensional
space, and calculate and print the corresponding polar coordinates, with the angle θ given in degrees.

# Question 3
The orbit in space of one body around another, such as a planet around the Sun, need not be circular. In general, it takes the form of an ellipse, with the body sometimes closer in and sometimes further out.
If you are given the distance l1 of closest approach that a planet makes to the Sun (called its perihelion) and its linear velocity v1 at perihelion, then any other property of the orbit can be calculated from these two.
Kepler’s second law tells us that the distance l2 and velocity v2 of the planet at its most distant point, or aphelion, satisfy `l2*v2=l1*v1`.
At the same time, the total energy (kinetic plus gravitational) of a planet with velocity v and distance r from the Sun is given by `E=0.5*m*v**2-G*m*M/r`, where m is the planet’s mass, M=1.9891e30 kg is the mass of the Sun, and `G=6.6738e-11 m**3*kg**(-1)*s**(-2)` is Newton’s gravitational constant.

Given that energy must be conserved, we can calculate v2 as the smaller root of the quadratic equation: 
`v2**2-(2*G*M*v2/(v1*l1))-(v1**2-2*G*M/l1)=0`

Once we have v2, we can calculate l2 using the relation `l2=l1*v1/v2`.

Given the values of v1, l1, and l2, other parameters of the orbit are given by :
Semi-major axis: `a=(l1+l2)/2`
Semi-minor axis: `b=np.sqrt(l1*l2)`
Orbital period: `T=(2*np.pi*a*b)/(l1*v1)`
Orbital eccentricity: `e=(l2-l1)/(l2+l1)`

- Write a program that asks the user to enter the distance to the Sun and velocity at perihelion, then calculates and prints the quantities l2, v2, T, and e.
- Test your program by calculating the properties of the orbits of :
Earth: `l1=1.4710e11 m`, `v1=3.0287e4 m/s`
Halley’s comet: `l1=8.7830e10 m`, `v1=5.4529e4 m/s`
Among other things, you should find that the orbital period of the Earth is one year and that of Halley’s comet is about 76 years.
