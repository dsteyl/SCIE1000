
# Exponential vs Compounding

There are many different equations that can be used to model population growth, a few of which you learn about in SCIE1000. One important concept is that often times populations will grow proportional to the current population size. There are multiple simple models we use for this, such as exponential, and compounding. Recall, they look like this:

Expontential: `P(i) = P(0) * e^(k * i)`

Compounding: `P(i) = P(i-1) * (1+k)`

Here's the situation: while you are studying for SCIE1000 outside of class with your study group, your friend argues that these two formulas are interchangeable when k is constant. You aren't quite sure if they're right, because while they are both based on the same concept, why would we even need two different equations if they were essentially the same?

**Task:** Investigate your friend's claim. Graph the two equations on the same axis with the same initial values. If the final values rounded to five decimal places are the same, print "These two equations are interchangeable when k is constant." If they are not, print "These two equations are not interchangeable."

The title of your graph should be 'Exponential vs Compounding". The x-axis should be labelled "Time", and the y-axis should be labelled "Amount". Remember to use a legend with the exponential line labelled "Exponential", and the compounding line labelled "Compounding". Don't change any variable names.

After passing this exercise, take a moment to think about your results. Are the two equations interchangeable? Why or why not? And if not, which equation is most suitable for modelling the growth of a savings account that collects interest monthly, and which is most suitable for modelling a population of bacteria that multiplies rapidly with no limit on resources.

**Hint 1:** The compounding formula can take another form when k is constant: `P(i)= P(0) * (1+k)**i`

**Hint 2:** Don't forget the round() function. Example: round(2.24869231, 2) = 2.25
