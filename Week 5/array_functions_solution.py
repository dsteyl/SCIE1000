from pylab import *

# array creation code
A = array([i*3+j**4+i*j-k*20+32 for i in range(10) for j in range(10) for k in range(10)])
# do not edit the code above

average = mean(A)
maximum = max(A)
minimum = min(A)
total = sum(A)
length = len(A)
difference = maximum - minimum
