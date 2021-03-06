# Euler's Method (4) - Asteroid!

An asteroid has been spotted travelling through our solar system. One astrophysicist has predicted that it will collide with Earth in exactly 215 days, using a new method for modelling trajectories. The researcher has asked you and others to verify their claim using a variety of methods. You have been tasked with modelling the asteroid's trajectory using Euler's method. 

For an asteroid to collide with Earth, it needs to have the same `x`, `y`, and `z` coordinates as the Earth in 215 days (`x`, `y`, and `z` represent the three dimensions. Because solar systems are three dimensional!). If any of the final predicted `x`, `y`, and `z` values are different to the Earth's, then that will mean the asteroid will not collide with Earth in 215 days. 

It has already been proven that the asteroid will have the same `x` and `z` coordinates as Earth in 215 days. So, you only need to worry about the `y` dimension.

The equation for the change in `y` at day `t` after the asteroid was discovered is:

`f'(t) = (-0.05t+5)*exp(0.002t)*0.05`

The starting `y` position of the asteroid is 160.195 million kilometers, which occurs at `t = 0`, so `f(0) = 160.195` million kilometers. The `y` position of Earth in 215 days (`t = 215`) is 150 million kilometers, so `f(215) = 150` million kilometers.

**Task:** Write a function called `will_it_hit(h)`, that returns the number `1` if the asteroid is going to hit Earth in 215 days, and `0` otherwise - along with the Euler's method prediction of the asteroid's `y` poistion. 

The Earth will be considered 'hit' if the asteroid gets within 0.01 million kilometers of Earth (so `abs(earthy - asteroidy)<0.01`). The input for the function is `h`, which indicates the step size in days. The formula for the number of steps is `215/h`. For example, `h = 0.5` indicates that there are two steps of Euler's method per day, resulting in `215/0.5 = 530` steps of Euler's method.

As with the previous exercises, the output for the `fdash` and `onestep` functions should be rounded to 5 decimal places. 

Use your code from the previous exercises. The only thing you will need to change is `fdash`. We have written tests for each of your functions (`fdash`, `onestep`, `eulers`, `will_it_hit`), to help you understand where errors might be. Good luck!

**Note:** All units for the `y` location of the asteroid should be in millions of kilometers - so instead of writing 150000000 for the location of the Earth, use 150. For another example, will_it_hit(5) should give output (0, 151.72445).

**Reminder:** Only use `exp`, not `e**`. You will not pass the exercise if you use `e**`.
