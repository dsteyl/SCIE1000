# Indexes (2) - Editing Arrays

Now that we can access individual elements in an array, we can learn how to change them. It works the same way variables are changed, except instead of the variable name you need to write the array name and the index in square brackets. Take a look at the following example:

```python
primes = array([354,3,5,7,11])
primes[0] = 2
print(primes)
```
The output is:

```
[2 3 5 7 11]
```

So the format is `arrayname[index] = new value`. In the example given above, we change element 0 of the primes array from 354 to 2. Recall, array indexing starts at 0, so `primes[0]` refers to the first element in the primes array, `primes[1]` refers to the second element in the array, and so on.

**Task:** Modify this program so that it prints the squares array, updates the squares array so it has the correct values, and then prints the squares array again.

