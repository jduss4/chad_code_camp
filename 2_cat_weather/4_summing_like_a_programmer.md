# Summing Like a Programmer

- importing a standard module
- fancy list math

Your rainfall script is working great, but when you are reading your Python book you start thinking about the `math` standard library. Surely there must be a better way to sum up a list of numbers, right?

Bingo! While you are looking through the `math` module documentation, you find just the thing:

https://docs.python.org/3/library/math.html#math.fsum

Do you think you can improve your precipitation program using that function?

## Task

- import the math module
- use `math.fsum()` to add up your rainfall totals

Hint:

- the term `iterable` in the documentation for that function means "something that can be iterated" such as a list, a tuple, and even a few things you have yet to discover! So you should be able to pass in any sort of list to that function...although hopefully it has plenty of floating point numbers in it or else it might not be too happy