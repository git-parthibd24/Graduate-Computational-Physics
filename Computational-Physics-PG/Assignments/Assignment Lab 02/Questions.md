# Question 1
In mathematics, the Fibonacci series or Fibonacci sequence are the numbers in the following integer sequence: 0,1,1,2,3,5.... By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. In mathematical terms, the sequence `F_n` of Fibonacci numbers is defined by the recurrence relation `F_n=F_{n-1}+F_{n-2}`. Take n as input. Compute and print the ratio `F_n/F_{n-1}` rounded off up to 2 decimal places. Note: If n is large, this ratio tends to a fixed ratio known as the golden mean.

# Question 2
Write a python program to check if three points are collinear.

# Question 3
Write a python code to add the first ten terms of `e**x` , x being a positive integer.

# Question 4
As an egg cooks, the proteins first denature and then coagulate. When the temperature exceeds a critical point, reactions begin and proceed faster as the temperature increases. In the egg white, the proteins start to coagulate for temperatures above 63°C, while in the yolk the proteins start to coagulate for temperatures above 70°C. For a soft boiled egg, the white needs to have been heated long enough to coagulate at a temperature above 63°C, but the yolk should not be heated above 70°C. For a hard boiled egg, the center of the yolk should be allowed to reach 70°C.

The following formula expresses the time `t` it takes (in seconds) for the center of the yolk to reach the temperature `Ty` (in Celsius degrees) :

`t=(M**(2/3)*c*rho**(1/3))/(K*pi**2*(4*pi/3)**(2/3))*log(0.76*(To-Tw)/(Ty-Tw))`

Here, `M`,`rho`,`c`, and `K` are properties of the egg : 
`M` is the mass , `rho` is the density , `c` is the specific heat capacity , `K` is thermal conductivity.

Relevant values are :
`M=47g` for a small egg and `M=67g` for a large egg , `rho=1.038g/cm**3` , `c=3.7J/g/K` , `K=5.4e-3W/cm/K` .
`Tw` is the temperature (in °C) of the boiling water, and `To` is the original temperature (in °C) of the egg before being put in the water.

Implement the formula in a program, set `Tw=100`, `Ty=70`, and compute `t` for :
- a large egg taken from the fridge (`To=4`) 
- a large egg at room temperature (`To=20`)



