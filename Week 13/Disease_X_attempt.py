from pylab import *

# variables given
weeks = 20
N = 25000000
a = 2.5
b = 0.5
d = 0.0001
stepSize = 0.1

# variables calculated
time = # from 0 to weeks (inclusive) with a step size of 0.1
numSteps = #total number of steps
S = # Susceptible array - initialize as array of 0's with the same length as time
I = # Infected array - initialize as array of 0's with the same length as time
R = # Recovered array - initialize as array of 0's with the same length as time
D = # Deceased array - initialize as array of 0's with the same length as time

# you should initialize the first values of each population array here

# put a while loop here that fills the population arrays


# calculate the index for when the maximum number of infected people occurred
maxIndex = # use the highest(A) function you wrote earlier

# here are the print statements
# you can find the total deaths by getting the last value of the death array
# you can find the maximum number of infected people by using the maxIndex 

print("The total number of deaths is", yourDeathValueHere)
print("The maximum number of people infected at once is", yourMaxValueHere, "which occurred at step", maxIndex)
