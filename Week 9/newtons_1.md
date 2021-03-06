# Newton's Method (1)

For the following exercises you will write a program that implements Newton's method. Newton's method can be found in Chapter 8.4 of your lecture notes, which gives a description of why this method works. For our purposes you only need to know the algorithm itself.

Newton's method finds the `x` value where the function is equal to 0, given the function, its derivative, and a starting point. Newton's method can fail when given bad starting points, but we will not worry ourselves with this while implementing this program. Newton's method is as follows:

Given an initial value `x(0)`:

`x(i+1) = x(i) - f(x(i))/f'(x(i))`

In words, the next guess (`x(i+1)`) is the current guess (`x(i)`), minus its y value (`f(x(i))`), divided by the derivative (`f'(x(i))`) at that point. Newton's method is applied until the guesses stop changing too much, or too many guesses have happened. You do not need to fully understand why this algorithm works in order to implement it in Python.

**Task:** To start, write two functions called `f(x)` and `fdash(x)` that calculate the value of the function at `x` and the derivative at `x`, respectively. The function and its derivative that we will be using as a placeholder are as follows:

`f(x) = e^(0.05x)*(0.05x) - 5`

`fdash(x) = e^(0.05x)*(0.0025x + 0.05)`

**Important:** Round the values to 5 decimal places. 

**Reminder:** Only use `exp`, not `e**`, for these exercises.

Don't print anything or ask for any user input. 

