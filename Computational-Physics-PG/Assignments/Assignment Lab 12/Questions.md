# Question 1
**Relaxation Method for Laplace’s Equation**

Use the **Gauss–Seidel method** to solve **Laplace’s equation** for the two-dimensional problem :

- A square box 1 m on each side.
- Voltage `V=1` volt along the top wall.
- Voltage `V=0` volts along the other three walls.

Use a grid spacing `a=1 cm`, so that there are `100` grid points along each wall, or `101` if you count the points at both ends.

Continue the iteration of the method until the value of the electric potential changes by no more than 
`δ=10⁻⁶ V` at any grid point on any step.

Then make a density plot of the final solution — i.e., the 2D filled contour plot of the potential **`φ`** using Python’s `imshow`.

Experiment with different values of the over-relaxation parameter `ω` to find which value gives the fastest solution. You should find that a value around `ω≈0.9` performs well.

> In general, larger values of `ω` cause the calculation to run faster, but if `ω` is too large, the speed drops off and for `ω>1` the calculation becomes unstable.

# Question 2
**Relaxation Method for Laplace’s Equation (Capacitor Configuration)**

Use the **Gauss–Seidel method** to solve **Laplace’s equation** in two dimensions for a square plane of size **`L=10 m`** representing a **charged capacitor configuration**.

- Use a grid spacing of `Δx=0.1 m`, so that there are `101×101` grid points (`N=101`).
- The capacitor plates are located at `x=2 m` and `x=8 m`, each extending vertically from `y=2 m` to `y=8 m`.
- The plate at `x=2 m` is held at `+1 V`, and the plate at `x=8 m` is held at `−1 V`.
- All other points on the grid are initialized to `0 V`.

Apply the Gauss–Seidel relaxation technique with successive over-relaxation using a relaxation parameter `ω`.

Continue the iteration until the total error in potential values changes by no more than 
`δ=10⁻⁶ V`

After convergence, plot the error as a function of the number of iterations. Make a density plot of the potential **`φ`** to visualize the voltage distribution around the capacitor using `imshow`.

# Question 3
**Thermal diffusion in the Earth’s crust**

A classic example of a diffusion problem with a time-varying boundary condition is the diffusion of 
heat into the crust of the Earth, as surface temperature varies with the seasons. Suppose the mean 
daily temperature at a particular point on the surface varies as: 

`T₀(t)=A+Bsin(2πt/τ)`,

where `τ=365 days`, `A=10°C` and `B=12°C`. At a depth of 20 m below the surface almost all annual 
temperature variation is ironed out and the temperature is, to a good approximation, a constant 11°C 
(which is higher than the mean surface temperature of 10°C—temperature increases with depth, due to 
heating from the hot core of the planet). The thermal diffusivity of the Earth’s crust varies somewhat 
from place to place, but for our purposes we will treat it as constant with value `D=0.1 m²day⁻¹`. 

Write a program to calculate the temperature profile of the crust as a function of depth up to 20 m 
and time up to 10 years. Start with temperature everywhere equal to 10°C, except at the surface and 
the deepest point, choose values for the number of grid points and the time-step h, then run your 
program for the first nine simulated years, to allow it to settle down into whatever pattern it reaches. 
Then for the tenth and final year plot four temperature profiles taken at 3-month intervals on a single 
graph to illustrate how the temperature changes as a function of depth and time.


# Question 4
Use the **Gauss–Seidel Relaxation method** to solve **Poisson’s equation** in two dimensions for a square plane of size **`L=100 m`**, containing **two square charge distributions**.

Use a grid spacing of `Δx=1 m`, so that there are `101×101` grid points (`N=101`).
The top boundary (`y=100 m`) is held at a fixed potential of `100 V`.
All other boundaries are held at `0 V` initially, and the grid is initialized to zero.
A **positive square charge region** with uniform charge density **`+ρ`** is placed in the region `20<x<40`, `60<y<80`.
A **negative square charge region** with uniform charge density **`−ρ`** is placed in the region `60<x<80`, `20<y<40`.
Use `ρ=1` and `ε=1` (arbitrary units).

- Make a **density plot** of the potential **`φ`** to visualize the **voltage distribution due to the charge configuration** using `imshow`.

