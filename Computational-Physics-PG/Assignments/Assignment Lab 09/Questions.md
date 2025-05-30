# Question 1
**Non-linear Pendulum**

The equation of motion for a nonlinear pendulum is :

`d²θ/dt²=-(g/ℓ)*sinθ`______________(1)

1. Write a program to solve the non-linear pendulam equation given in equation 1 by converting
in two first order equations. You can use the fourth-order Runge–Kutta method and assume
the pendulum has a 10 cm arm. Use your program to calculate the angle θ of displacement
for several periods of the pendulum when it is released from a standstill at θ=179° from the
vertical. Make a graph of θ as a function of time.

- Extend your program to create an animation of the motion of the pendulum. Your animation
should, at a minimum, include a representation of the moving pendulum bob and the pendulum
arm. (Hint : For your animation, you may want to make the step size for your Runge–Kutta calculation
smaller than the frame-rate of your animation, i.e., do several Runge–Kutta steps per frame on
screen. This is certainly allowed and may help to make your calculation more accurate.)

Now for example let us drive the above pendulam by exerting a small oscillating force horizontally
on the mass. Then the equation of motion for the pendulum becomes : 

`d²θ/dt²=-(g/ℓ)*sinθ+C*cosθ*sin(Ωt)` where `C` and `Ω` are constants.

2. Write a program to solve this equation for `θ` as a function of time with `ℓ=10cm`, `C=2s^(−2)` and `Ω=5s^(−1)` and make a plot of `θ` as a function of time from `t=0` to `t=100s`. 
Start the pendulum at rest with `θ=0` and `dθ/dt=0`.

- Now change the value of Ω, while keeping C the same, to find a value for which the pendulum
resonates with the driving force and swings widely from side to side. Make a plot for this case
also.

# Question 2
**Trajectory with air resistance**

Many elementary mechanics problems deal with the physics of objects moving or flying through the
air, but they almost always ignore friction and air resistance to make the equations solvable. If we're
using a computer, however, we don't need solvable equations.

Consider, for instance, a spherical cannonball shot from a cannon standing on level ground. The
air resistance on a moving sphere is a force in the opposite direction to the motion with magnitude

`F=½πR²ρCv²`,

where `R` is the sphere's radius, `ρ` is the density of air, `v` is the velocity, and `C` is the so-called
coefficient of drag (a property of the shape of the moving object, in this case a sphere).

The equations of motion for the position `(x,y)` of the cannonball are :

`ẍ=−(πR²ρC)/(2m)*ẋ√(ẋ²+ẏ²)` 
`ÿ=−g−(πR²ρC)/(2m)*ẏ√(ẋ²+ẏ²)`

where m is the mass of the cannonball, g is the acceleration due to gravity, and ẋ and ẍ are the
first and second derivatives of x with respect to time.

- Change these two second-order equations into four first-order equations using the methods you
have learned, then write a program that solves the equations for a cannonball of mass 1 kg and
radius 8 cm, shot at 30° to the horizontal with initial velocity 100 ms^(−1). The density of air is
ρ=1.22 kgm^(−3) and the coefficient of drag for a sphere is C=0.47. Make a plot of the trajectory
of the cannonball (i.e., a graph of y as a function of x).

- When one ignores air resistance, the distance traveled by a projectile does not depend on the
mass of the projectile. In real life, however, mass certainly does make a difference. Use your
program to estimate the total distance traveled (over horizontal ground) by the cannonball above,
and then experiment with the program to determine whether the cannonball travels further if
it is heavier or lighter. You could, for instance, plot a series of trajectories for cannonballs of
different masses, or you could make a graph of distance traveled as a function of mass. Describe
briefly what you discover.

# Question 3
**Cometary orbits**

Many comets travel in highly elongated orbits around the Sun. For much of their lives they are
far out in the solar system, moving very slowly, but on rare occasions their orbit brings them close to
the Sun for a fly-by and for a brief period of time they move very fast indeed.

This is a classic example of a system for which an adaptive step size method is useful, because for the
large periods of time when the comet is moving slowly we can use long time-steps, so that the program
runs quickly, but short time-steps are crucial in the brief but fast-moving period close to the Sun.

The differential equation obeyed by a comet is straightforward to derive. The force between the
Sun, with mass `M` at the origin, and a comet of mass `m` with position vector `r⃗` is `GMm/r²` in direction
`-r⃗/r` (i.e., the direction towards the Sun), and hence Newton's second law tells us that

`m(d²r⃗/dt²)=−(GMm/r²)(r⃗/r)`

Canceling the `m` and taking the `x` component we have `d²x/dt²=−GM(x/r³)`, and similarly for the other two coordinates. 
We can, however, throw out one of the coordinates because the comet stays in a single plane as it orbits. If we orient our axes so that this plane is perpendicular to
the `z`-axis, we can forget about the `z` coordinate and we are left with just two second-order equations
to solve:

`d²x/dt²=−GM(x/r³)`

`d²y/dt²=−GM(y/r³)`

where `r=√(x²+y²)`.

- Write a program to solve your equations using the fourth-order Runge–Kutta method with a fixed
step size. You will need to look up the mass of the Sun and Newton’s gravitational constant G.
As an initial condition, take a comet at coordinates x=4 billion kilometers and y=0 (which
is somewhere out around the orbit of Neptune) with initial velocity vx=0 and vy=500 ms^(−1).
Make a graph showing the trajectory of the comet (i.e., a plot of y against x).
Choose a fixed step size h that allows you to accurately calculate at least two full orbits of the
comet. Since orbits are periodic, a good indicator of an accurate calculation is that successive
orbits of the comet lie on top of one another on your plot. If they do not then you need a smaller
value of h. Give a short description of your findings. What value of h did you use? What did
you observe in your simulation? How long did the calculation take?

- Make a copy of your program and modify the copy to do the calculation using an adaptive step
size. Set a target accuracy of δ=1 kilometer per year in the position of the comet and again plot
the trajectory. What do you see? How do the speed, accuracy, and step size of the calculation
compare with those in previous part? Modify your program to place dots on your graph showing the position of the comet at each
Runge–Kutta step around a single orbit. You should see the steps getting closer together when
the comet is close to the Sun and further apart when it is far out in the solar system.

