# Question 1
- Write a program to solve the differential equation:

`d²x/dt²-(dx/dt)²+x+5=0`

using the leapfrog method. Solve from `t=0` to `t=50` in steps of `h=0.001` with initial conditions `x=1` and `dx/dt=0`. Make a plot of your solution showing `x` as a function of `t`.

- Solve the same using Verlet's Method.

# Question 2
**Orbit of the Earth**

Use the Verlet method to calculate the orbit of the Earth around the Sun. The equations of motion
for the position ~r=(x,y) of the planet in its orbital plane are given in the vector form below :

`d²r⃗/dt²=−GMr⃗/r³`

where G=6.6738×10⁻¹¹ m³kg⁻¹s⁻² is Newton's gravitational constant and M=1.9891×10³⁰ kg
is the mass of the Sun.

The orbit of the Earth is not perfectly circular, the planet being sometimes closer to and sometimes
further from the Sun. When it is at its closest point, or perihelion, it is moving precisely tangentially
(i.e., perpendicular to the line between itself and the Sun) and it has distance 1.4710×10¹¹ m from
the Sun and linear velocity 3.0287×10⁴ ms⁻¹.

- Write a program to calculate the orbit of the Earth using the Verlet method, with a time-step
of h=1 hour. Make a plot of the orbit, showing several complete revolutions about the Sun.
The orbit should be very slightly, but visibly, non-circular.

- The gravitational potential energy of the Earth is −GMm/r, where m=5.9722×10²⁴ kg is the
mass of the planet, and its kinetic energy is ½mv² as usual. Modify your program to calculate
both of these quantities at each step, along with their sum (which is the total energy), and
make a plot showing all three as a function of time on the same axes. You should find that the
potential and kinetic energies vary visibly during the course of an orbit, but the total energy
remains constant. Now plot the total energy alone without the others and you should be able to see a slight
variation over the course of an orbit. Because you're using the Verlet method, however, which
conserves energy in the long term, the energy should always return to its starting value at the
end of each complete orbit.
