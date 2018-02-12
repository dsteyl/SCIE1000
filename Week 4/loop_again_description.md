### While Loop Practice

While loops are a very important part of programming, so have another go writing a simple while loop.

**Task:** Write a program that estimates and prints out all the average monthly temperatures for Cairns. To do this, construct a while loop that starts at 1 and counts up by 1 all the way to 12 (inclusive). We have given you the print statement (and equation) for you to use. 

Remember, before you run your code in any exercise, tutorial, or other class, make sure your while loops satisfy these three criteria:
1. It has a beginning (for this example, it is 1)
2. It has an end (for this example, it is 12)
3. It has a way of getting from the beginning to the end (for this example, we are counting up by 1 and will be sure to reach 12)

If you miss number 3 you may run into an infinite loop!

### Solution


```
from pylab import *

i = 1
while i <=12:
    print("Average temperature for month", i, "is", 3*sin((i+2)*2*pi/12)+25)
    i = i + 1
    
```
