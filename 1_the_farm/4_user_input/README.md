# 1.4 User input

It's only lesson 4 and I'm already here to talk to you about users. Whenever you work on code, you should keep asking yourself "who is the user? How are they going to use this script? How do I make it as good of an experience as possible?"

"But Jessica, I'm just writing a little script for myself, I don't need to worry much about users." You just said who the user is -- yourself! So you should also try to make your own experience as good as possible :)

Anyway, I'll get off my soapbox now. Today's topic is "user input" which isn't asking for feedback about your script after they use it, rather, it's about user entered info during the script.

## input()

So far, we've talked about `print()`, which lets you print a message to your terminal. `input()` is pretty similar. It prints a message, then waits for the user to enter something and hit return.

```python
age = input("How old are you?")
```

When the above line of code is run, the words `How old are you?` will appear in the terminal and the script will wait until the user puts in something and hits "return."

Their answer will now be stored in the variable `age`. Do you have to store the input results as a variable? Nope. But it's nice to save the answer so you can refer to it later, you know?

__NOTE__: `input()` always returns strings! `age` above is going to be `"32"` not `33`, so you may need to convert it to an integer if you want to use it for mathy stuff.

## A contrived corn harvest example

Here is an example of how you might ask a user for some information and print out something useful for them. Read the code below and make sure you can follow along with what it's doing and see if there are any surprises.

```python
print("Calculate your corn-based earnings")
corn_harvested = input("Corn in bushels: ")
price_per_bushel = input("Current price per bushel ($): ")

amount = int(corn_harvested) * float(price_per_bushel)

print("Your corn was worth $" + str(amount))
```

There are a couple things in the above script which are worth mentioning, so here it is again but with comments!

```python
# first, introduce to the user what the script is going to be doing
print("Calculate your corn-based earnings")

# collect their input, adding a space at the end to help with the formatting
# note the ($) helps the user understand the units expected
corn_harvested = input("Corn in bushels: ")
price_per_bushel = input("Current price per bushel ($): ")

# okay, sorry, I didn't teach you how to do math yet but I think you can figure
# out that this is multiplication!
# 
# notice that we're converting bushels to an int and dollars to a float.
# this means that if a user entered 100.5 bushels, they would receive an
# incorrect amount back....is that okay? It's something to consider as the
# programmer trying to predict how a user might use this script!
amount = int(corn_harvested) * float(price_per_bushel)

# print out the results to the user, and make sure to convert the amount into
# a string, or you'll get an error!
print("Your corn was worth $" + str(amount))
```

## Outro

I think that's probably most of what you need to know to be released out into the world of gathering user input!

Go forth and conquer the exercises and project on this day!
