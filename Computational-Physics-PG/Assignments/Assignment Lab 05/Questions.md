# Question 1
Write a Python function that represents the mathematical function `f(x)=exp(-x**2)*cos(2*pi*x)` on a mesh consisting of q+1 equally spaced points on [-1,1] and return :
- the interpolated function value at x=-0.45
- the error in the interpolated value.

Call the function and write out the error for q=2,4,8,16. Use linear interpolation technique.

# Question 2
Imagine we have `n+1` measurements of some quantity `y` that depends on `x`: `(x0, y0), (x1, y1), ..., (xn, yn)`. We may think of `y` as a function of `x` and ask what `y` is at some arbitrary point `x` not coinciding with any of the points `x0,...,xn`. It is not clear how `y` varies between the measurement points, but we can make assumptions or models for this behavior using interpolation. One way to solve the interpolation problem is to fit a continuous function that goes through all the `n+1` points and then evaluate this function for any desired `x`. A candidate for such a function is the polynomial of degree `n` that goes through all the points. It turns out that this polynomial can be written as :

`p_L(x)=sum(y_k*L_k(x) for k in (0,n)` ______________ Eq.(1)

where:

`L_k(x)=product((x-x_i)/(x_k-x_i) for i in (0,n) if i!= k)` _____________Eq.(2)

The polynomial `p_L(x)` is known as Lagrange's interpolation formula, and the points `(x0,y0),..., (xn,yn)` are called interpolation points.

- Make functions `p_L(x,xp,yp)` and `L_k(x,k,xp,yp)` that evaluate `p_L(x)` and `L_k(x)` by Eq. 1 and Eq. 2, respectively, at the point `x`. The arrays `xp` and `yp` contain the `x` and `y` coordinates of the `n+1` interpolation points, respectively. That is, `xp` holds `[x0,...,xn]`, and `yp` holds `[y0,...,yn]`.

To verify the program, we observe that :
`L_k(x_k)==1`, `L_k(x_i)==0` for `i != k`

This implies that `p_L(x_k)==y_k`. That is, the polynomial `p_L` goes through all the points `(x0,y0), ..., (xn,yn)`.

- Write a function `test_p_L(xp,yp)` that computes `abs(p_L(x_k)-y_k)` at all the interpolation points `(xk,yk)` and checks that the value is approximately zero. Call `test_p_L` with `xp` and `yp` corresponding to 5 equally spaced points along the curve `y=sin(x)` for `x in [0,pi]`. Thereafter, evaluate `p_L(x)` for an `x` in the middle of two interpolation points and compare the value of `p_L(x)` with the exact one.

# Question 3
Use Neville's method to compute `y` at `x=pi/4` from the data :

`x=[0,0.5,1,1.5,2]`

`y=[-1.00,1.75,4.00,5.75,7.00]`

# Question 4
Given the data points :

`x=[1,2,3,4,5]`

`y=[13,15,12,9,13]`

- Calculate the second order derivatives y" analytically in all x points using the condition that first order derivatives are continuous in each boundary.

- Use those second order derivatives y" and determine the natural cubic spline interpolant at x=3.4.
