# 1.2 Data Types

In the land of Python, and indeed most programming languages, you will use basic building blocks like integers, strings, and lists. These are called _data types_.

## Types of data

Let's go through some of the data types used by Python. You'll learn more later, but this is a good list to start with. Keep in mind that while most languages have these same concepts, they may call them something different.

- boolean
- float
- integer
- None
- string

### Boolean

Boolean, or `bool` is an easy data type to remember, because it can only have two values:  `True` or `False`

Booleans are pretty handy, and you should remember them if you are ever dealing with a situation where there are only two options. For example, is the irrigation gate open or closed? Does the pipe contain a skunk or does it not contain a skunk?

Make sure to capitalize `True` and `False`, because that matters to Python!

### Float

A `float` is a fancy "floating point" number. Sometimes it might look like something with a simple decimal, such as `10.17`. Other times, you might be working with very large numbers and end up with a float like `1.7e308`.

### Integer

Integers, or `int`, are less fancy numbers than floats because they cannot be decimals, but they are still very useful! You know, like the number `8` or `183927`.

### None

`None` is something you'll see from time to time which indicates the absence of a value. It can be easy to confuse `None` with `False` or the `int` 0, but they are different! `None` has no value -- use your Jonathan Frakes voice here -- it never happened. Not today. We made it up. 

### String

Strings or `str`, are a very computer-persony name for letters, words, phrases, sentences, etc. You got an English major studying strings all day! You are ready for this data type.

Strings are marked with quotation marks (single or double will do fine):
- "a"
- "A"
- "word"
- "a whole bunch of words"
- "a bunch of words and a new line (return)\n"

## What do you do with them?

What is the point of a data type?  Well, each data type has different things it's good at it. Do you need to do math?  Let's take a look at how integers behave vs how strings behave:

```python
# integers
>>> 2 + 2
4
# strings
>>> "2" + "2"
'22'
```

Let's hope folks at NASA know about data types, or else their calculations are going to send a satellite way out in the middle of nowhere.

Data types exist because, just like in non-programming life, numbers, true / falses, and words exist and you use them differently. I could probably go into more details, but I don't want to right now. Just keep reading, we'll get there.

### type()

Knowledge is power, and it's always nice to know what kind of data type you're working with.  You can use the `type()` method to accomplish this:

```python
>>> type("a")
<type 'str'>

>>> type(8)
<type 'int'>
```

Now you know the dragon's name, you have power over it!

### Conversion

You may need to convert one data type to another at some point. For example, you might have something that looks like a number, but upon closer inspection you realize that it has quotation marks around it. That's not a number, that's a string! Never fear, you can turn it into an integer or float without too much trouble.

```python
bool()
float()
int()
str()
```

For example:

```python
>>> float("10.27")
10.27

>>> str(False)
'False'
```

__A word of warning__: sometimes things don't convert nicely. `"22"` may turn into `22` just fine...but what happens if you convert it to a boolean? What if you convert `.01` to an integer? Just keep an eye on what you're converting and how, is all I'm saying.

### Methods

Okay, remember when I was too lazy to tell you what kind of fun things you can do with items of each data type? Well, I worked up to it. Let's talk about "methods." A method is some kind of procedure you can apply to your string, integer, or whatever you've got.

For example, let's say you have a string:  `"WELCOME GRADS"`. What kind of things might we want to do to this?  Maybe we could make it lowercase, or upcase only the first words? Python has string methods for that: `lower()` and `title()`

```python
>>> "WELCOME GRADS".lower()
'welcome grads'

>>> "WELCOME GRADS".title()
'Welcome Grads'
```

Let's try subbing in your name with `replace()`:

```python
>>> "WELCOME GRADS".replace("GRADS", "CHAD")
'WELCOME CHAD'
```

Those seem cool, but how do you know what kind of methods you can use on all the data types?

### Documentation

Python, and indeed most (all?) programming languages, write down the instructions you need to use them in what we're going to refer to as documentation. You used to be able to buy books of documentation, like baby's first Ruby book, the 1.8 version documentation, but I don't recommend it. You can find what you need online!

- [String type docs](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Int type docs](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types)
- [Float type docs](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float)
- Boolean....let's not worry about those for right now. What, where was something you really wanted to do with True / False?

Go to the string docs and scroll down. Do you see `lower()` and `title()` there? Are there any methods that look interesting?

You don't have to go online to learn what methods are available, however. You can type `help(str)` or `help(int)` directly into your python interpreter to learn about the available string and integer methods, for example.

## Check yourself

At this point, you should have learned:

- [ ] about some basic data types in Python
- [ ] figured out why data types are important
- [ ] learned about methods and where to find them

Head over to the exercises portion to get some practice in!
