# 1.2 Data Types: Exercises

## Exercises

### type()

This one is an easy one, but throw these in your terminal and see if you can predict what `type()` they all are going to be. Feel free to try some more things out if you want to see what will happen.

1. `"1,892"`
1. `"True"`
1. True
1. `""`
1. `1/10` (this one is interesting)
1. `None`
1. `"None"`
1. `1.2`

### Converting data types

Converting between data types seems pretty straightforward, right? Great, then you should be able to predict the outcome of all of these no problem!

1. `str(False)`
1. `bool("True")`
1. `bool("False")`
1. `bool(10)`
1. `int(True)`
1. `int(False)`
1. `float("hello")`
1. `str(None)`
1. `bool("")`

If anything surprised you, can you work out why it's converting the way it is?

### Methods

This one is on you.  Go check out the links in the lesson for data type methods.  Feel free to ignore any that look confusing, we can come back to those later.  Look for the ones like `.is_integer()` and `.replace()` which make sense to say out loud, and then try them out with this format:

```python
"your string".string_method()
```

Sometimes, methods may take what's called an argument, like replace:

```python
"your string".replace("string you want to replace", "replacement")
```

Just play around with a couple of the things you find, and get used to the idea that you can manipulate integers, floats, and strings, with these Python methods.

## Answer Key

### type()

1. str
1. str
1. bool
1. str
1. int  (`1/10` evaluates to 0!!! WATCH OUT NASA!)
1. NoneType
1. str
1. float

### Converting data types

1. `"False"`
1. `True`
1. `False`
1. `True`
1. `1`
1. `0`
1. (error)
1. `"None"`
1. `False`

### Methods

Guess you gotta ask Jess for help if you're stuck!