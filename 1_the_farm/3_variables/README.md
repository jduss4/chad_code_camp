# 1.3 Variables + string concatenation

## Variables!

I tried and failed to think of a farming analog to variables, unfortunately, so I'll just have to tell you about them like a normal person.

Remember in algebra how you had variables like x and y, which secretly had a value? Variables are similar in programming, except usually you are using variables in programming to save a value.

Once you've saved something to a variable, you can refer back to it at any time to get that value, or change it if you want to something entirely new.

### Creating a variable

The formula to create a variable is:

```python
example_variable = "some value"
```

On the left of the equal sign is the variable, which in this case is called `example_variable`, although it could be called `x` or `y` or `favorite_string` or really anything you want to call it (within reason).

You can assign all kinds of things to variables. Remember the `None` data type? Sure, stick it in a variable:

```python
my_luck = None
```

Want to keep the result of some calculation around? Use a variable:

```python
age = 2021 - 1986
```

### Naming your variables

I just said you can call your variables anything you want, but that's a lie.  Try to stick to the following:

- start with a lowercase letter
- use snake case (words_separated_by_underscores)
- don't start with a number, but you can have numbers in it!
- feel free to use underscores, but in general avoid special characters
- make it descriptive!!!

Generally, you're assigning some value to a variable because you want to refer back to it later. So make sure you name it something you'll remember. When in doubt, go ahead and embrace the long variable name. `last_pay_period` is a better name than `week`,for example, if you need to save the dates for the last pay period of a month. On the other hand, you don't need to overdo it with something like `current_tractor_attached_to_combine` when `current_tractor` would probably work just fine.

You can save almost anything you want to a variable, which sometimes can get confusing. Was `soybean_humidity` an integer or a float? Was it in fact a boolean because you were using that to store whether the beans were dry enough to harvest? If you are ever having trouble remembering what kind of data a variable is storing, you may want to revisit what it's called and see if something else would make more sense.

It's a little gauche, but especially when you are a beginner, if you are having trouble keeping track of what type of data is in a variable, you can always put that right in the name:

```python
cats_int = 8
rain_float = 0.3
tractor_str = "4640"
```

I probably wouldn't do that in like, my professional programming life most of the time, but hey, if that's what works for you when you're getting started feel free to embrace it!

__CAUTION__: Many programming languages have a concept of "reserved words" which it uses to go about its day to day programming business. If you accidentally stray into trying to use one of these words as a variable name, things could get funky.

A few examples of reserved words:

- and
- class
- continue
- global
- import

### Using your variables

Variables are no good to anybody if you can't use them, so how does that work? Well, before we get to far you should know that whatever you do, DO NOT put quotation marks around your variable. Quotation marks indicate that something is a string, and although the _value_ assigned to the variable might be a string, variables themselves are just hanging out, no quotes, no regrets.

```python
# assign a string to your variable, welcome
>>> welcome = "hello"

# this is a variable, which returns "hello"
>>> welcome
'hello'

# this is a string, it returns itself
>>> "welcome"
'welcome'
```

Okay, you can remember that -- no quotes around variables, easy enough. But how do we actually USE them? Well, remember in the previous lesson where we used `"WELCOME GRADS".lower()` ? You can use a variable anywhere you would have otherwise used the value that you assigned to it!

```python
# create a variable and assign a value
>>> firstname = "Chad"

# make it lowercase!
>>> firstname.lower()
'chad'
```

You can also reuse variables, if something changes by the time you get around to using the variable again:

```python

>>> firstname = "Chad"

# reassign the value of the variable
>>> firstname = "Jess"

# this time, make it uppercase!
>>> firstname.upper()
'JESS'
```

One situation where replacing the value of a variable might be useful is if you are counting something.  Then you might want to be able to have a single variable, `count`, which you change as you go.  At the beginning of the script, the `count` started at 0, but by the end of the script, the count is `18`. It would be pretty confusing if you were trying to make 18 different variables to try to keep the value, so it's easier to just have one you can refer back to whenever you need to see how many items have been counted by that point.

A lot of times, though, it probably makes more sense to just make a second variable than try to reuse the first one, especially if you might need that first value again!

You'll just have to use your judgment, and as you write more code you'll start learning where and when to make variables, and which ones to overwrite.

### You forgot to define your variable

Every once in a while, you're really cooking along, writing some great code. You want to use some variable, so you throw it in...and then you get this error:

```python
NameError: name 'some_variable' is not defined
```
Looks like somebody forgot to actual define their variable, and by that I mean that by this point in the script you have yet to provide Python with a line like this, with something on the right to give it a value.

```python
some_variable = 
```

Python, and indeed many languages, do not enjoy it when you try to use something it has never heard of before. There are some mechanisms you can use if you want a variable around but don't know what the value of it is yet. You can use `None`!

```python
# define a variable, but give it no value. That's not 0, that's not False, it's just literally NO value
some_variable = None
```

Now, Python won't complain that the variable hasn't been defined, but you didn't have to commit to assigning any value yet.

## String concatenation

String concatenation sounds like an intimidating word, but really what it means is "putting together strings." There are a couple ways to do this in Python, but one of the easiest is just to use plus signs:

```python
>>> "example" + "concatenation"
'exampleconcatenation'
```

You've taken two strings, `"example"` and `"concatenation"` and combined them into one string! Great, but how can we save that result?

### Assign results to a variable

Just like when you learned that you could save the results of a math equation to a variable, you can also save things like brand new strings to a variable.  Just remember that on the left of the equal sign is your new variable name, and everything on the right, after it's sorted out, is what ends up assigned to it.

```python
# note the space after John Deere so that the sentence makes sense
>>> equipment = "John Deere " + "tractor"
>>> equipment
'John Deere tractor'
```

### Using variables in your concatenation

You can also use variables in string concatenation! Check it out:

```python
>>> cat = "Banjo"
>>> greeting = "Good evening, "
>>> greeting + cat
'Good evening, Banjo'
```

That example uses two variabls to create a single message, which is pretty cool. You can even save the results to a new variable, if you want:

```python
>>> evening_tidings = greeting + cat
```

### Using non-strings in your strings

Often, you will probably want to be able to use things like numbers along with strings. Maybe you're writing a program about the weather, for example, and you want to output a description along with the temperature. You will first need to convert everything to strings before you can use it!

```python
>>> temp = 98

# you will get an error if you just try to shove an int into a string
>>> "Hot and dry: " + temp
TypeError: cannot concatenate 'str' and 'int' objects

# convert your int to a string, and everybody is happy!
>>> "Hot and dry: " + str(temp)
'Hot and dry: 98'
```

As you will learn about many programming languages, not just Python, oftentimes the key about giving computers instructions with code is that computers do not make assumptions. As a human, we could probably make the logical jump to understand that you want to display that integer as though it were part of the text. Python and your computer, though, don't want to make or can't make assumptions a lot of the time, so you have to be pretty specific about what you want them to do!


### print()

I very briefly touched on `print()` in lesson 1, as a way to output things to the terminal from a script. We can print strings like the ones above, with converted values, with `print()`:

```python
>>> desc = "Hot and dry: " + temp
>>> print(desc)
Hot and dry: 98
```

Note: you can pass `print()` a value like a string, or you can pass in a variable containing the value! It will tell you with an error if there's a problem understanding what you want it to print out.

## Recap

So just to recap, you should have learned:

- what a variable is and how to assign (or reassign) it a value
- some naming advice for variables
- a couple ways you can use variables
- how to concatenate different types of variables as a string
- how to print things to your terminal

Time to head over to the exercises and test your knowledge!
