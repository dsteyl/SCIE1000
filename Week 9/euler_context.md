Light emitting diodes (commonly referred to as LEDs) are a key component in electrical circuits. The relationship between the voltage and current through a diode is exponential, such that the current through the diode exponentially increases with its corresponding voltage. If the current passing through a diode is too high, the diode can rupture and break. This particular current value is known as the maximum forward diode current.

You have a diode that has the following equation to represent the **derivative** of its current:
```python
cdash = 0.006*exp(3.2*v)
```

You wish to write a program that will apply Euler's method to estimate the diode current. The program will take the following inputs from the user:
1. The maximum forward diode current
2. The voltage to iterate up to when performing Euler's method
3. The step size to implement when using Euler's method
The program will print the following message if the maximum forward diode current is reached:
"The diode has ruptured at a voltage of (ANSWER HERE) volts."
If the maximum forward diode current is not reached, then the program will print:
"The diode has not ruptured."

This will require you to implement the following steps when writing your program:
1. Prompting the user for the appropriate input.
2. Calculating the number of steps the program will iterate over from the user input.
3. Implementing Euler's method at each step. It is recommended make use of some functions from the previous Euler's method exercises, particularly the fdash function (modified to use cdash for this question) and the one_step function.
4. Use a while loop to implement multiple steps of Euler's method, similar to the eulers function. At **each** step, check if the current is greater than or equal to the maximum forward diode current. If it is, you need to print the appropriate message, and also stop the program from running. It is recommended you write a function called 'check_rupture' 
to implement at each step of your Euler's method, that will either return a result of RUPTURED or NOT_RUPTURED. The result from this function 
can then be checked using a conditional. If rupture has occurred, to stop the program from running after this point, 
you can change your current step to a value greater than the total number of steps needed. This will prevent any while loop implementing your Euler's method to stop.
5. You will also need a condition to check that after Euler's method is completed, if there was no rupture, then you will print the appropriate message.

The program includes the following variables already:
currentStep - The first step of your Euler's method
c - The initial current to implement in your first Euler's method step
v - The initial voltage to implement in your first Euler's method step