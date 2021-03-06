from pylab import *

# Since we are randomly generating the questions, we need to use the random library
import random

# this function will randomly generate an m value between -0.15 and 0.15 (but not too small)
def generate_k():
    k = round(random.random()*0.3-0.15, 3)
    if abs(k)<0.04:
        return generate_k()     
    return(k)

# this function will randomly generate an A0 value between 0 and 20 (but not too small)
def generate_A0():
    A0 = round(random.random()*20)
    if abs(A0) <= 0.05:
        return generate_A0()
    return(A0)

# this function will generate a data set using the A0 and k values provided
def generate_data(k, A0):
    # the x values will be randomly chosen from 0 to 25
    x = array([random.randrange(25) for i in range(25)])
    # the y values will be calculated using y = A0*exp(k*x) * a random number to scatter
    y = array([A0*exp(k*i)*(0.9+random.random()*0.2) for i in x])
    return x, y
    
# the k and A0 values are randomly generated
k = generate_k()
A0 = generate_A0()

# the x and y arrays are randomly generated using k and A0
x, y = generate_data(k, A0)

# the data is plotted using black circles
plot(x, y, 'ko')
grid(True)
xlabel("x")
ylabel("y")
title("Exponential Model")
show()

# the user guesses the A0 and k values
A0_guess = float(input("Enter your A0 value: "))
k_guess = float(input("Enter your k value: "))


# let the user know if their guesses are close enough  
if A0-3<=A0_guess<= A0+3:
    print("The A0 value is close enough.")
else:
    print("The A0 value is incorrect.")

if k-0.03<=k_guess<= k+0.03:
    print("The k value is close enough.")
else:
    print("The k value is incorrect.")



        
# tell the user the actual values
print("The actual A0 value is", A0, "and the actual k value is", k)
