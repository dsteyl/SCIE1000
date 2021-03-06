# Fill in the Functions (2)

You're interested in reaching a savings goal after a number of months, but the calculations to figure out if you will reach your goal are a bit hard. A friend has been kind enough to provide a Python program they wrote that calculates how far they are from their savings goal by calculating the amount of money in their savings account each month. The program adds monthly interest and takes away any money spent on debts.

However, your friend has provided the code without any of the function definitions.

**Task:**
Your task is to write the function definitions that will make the program work.

**Hints:**
1. There are three functions missing, so be sure to write a definition for each of them. Read the code provided carefully to determine 
what they are called, what variables need to be passed to them, and what they need to return.

2. Remember that the amount of money in the account after each month can be found using the compound interest formula, given by `money = (1+r)*money_last_month`, where r is the monthly interest rate as a decimal.

3. Variables defined outside of functions can still be access within the functions without being passed to them. This means that you can access the variables GOAL_NOT_MET and GOAL_MET inside the functions without having them as input to the functions. 

4. To calculate the new savings, the interest should be added to the account first, then the debt taken away.
