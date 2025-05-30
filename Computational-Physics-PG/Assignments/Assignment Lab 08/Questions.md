# Question 1
**Differentiation of Unequally Spaced Data**

As shown in Figure, a temperature gradient can be measured down into the soil. The heat flux at the soil-air interface can be computed with Fourier’s law,

`q(z=0)=-k*ρ*C*dT/dz|_(z=0)`

where q=heat flux (W/m2), k=coefficient of thermal diffusivity in soil (∼3.5×10^(−7) m^2/s), ρ=soil density (≈1800 kg/m^3), and C=soil specific heat (≈840 J/(kg°C)). Note that a positive
value for flux means that heat is transferred from the air to the soil. Use numerical differentiation to evaluate the gradient at the soil-air interface and employ this estimate to determine the heat flux into
the ground.

![Soil Temperature Gradient](https://github.com/git-parthibd24/Computational-Physics-PG/blob/main/Assignments/Assignment%20Lab%2008/Assignment%20Lab%2008_Q1.png?raw=true)

# Question 2
It is often the case that the frictional force on an object will increase as the object moves faster. A
fortunate example of this is a parachutist; the role of the parachute is to produce a frictional force due
to air drag, which is larger than would normally be the case without the parachute. Here we consider
1a very simple example in which the frictional force depends on the velocity. Assume that the velocity
of an object obeys an equation of the form :

`dv/dt=a-b*v`______(1) where a and b are constants. 

You could think of a as coming from an applied force, such as gravity,
while b arises from friction. Note that the frictional force is negative (we assume that b>0), so that
it opposes the motion, and that it increases in magnitude as the velocity increases. 

- Use the Euler method to solve equation (1) for v as a function of time. A convenient choice of parameters is a=10
and b=1.0. You should find that v approaches a constant value at long times; this is called the
terminal velocity

# Question 3
Consider a radioactive decay problem involving two types of nuclei, A and B, with populations NA(t)
and NB(t). Suppose that type A nuclei decay to form type B nuclei, which then also decay, according
to the differential equations : 

`dNA/dt=-NA/τ+NB/τ`, `dNB/dt=NA/τ-NB/τ`

where for simplicity we have assumed that the two types of decay are characterized by the same
time constant, τ. Solve this system of equations for the numbers of nuclei, NA and NB, as functions
of time. Consider different initial conditions, such as NA=100, NB=0, etc., and take τ=1s.
Show that your numerical results are consistent with the idea that the system reaches a steady state
in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt
should vanish.

# Question 4
**Numerical Solution of the Lorenz System**

The Lorenz system is defined by the following coupled ordinary differential equations :

`dx/dt=σ(y-x)` 

`dy/dt=x(ρ-z)-y` 

`dz/dt=xy-βz`
where : `σ=10`, `ρ=28`, `β=8/3`.

- Write a Python program that implements the 4th-order Runge-Kutta method (RK4) to solve the system numerically with initial conditions `(x₀,y₀,z₀)=(0,1,0)`
for time range `t∈[0,50]`.

- Generate two plots `y(t)` versus time `t` and `z(t)` versus `x(t)`.


