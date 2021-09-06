# 1.5 Code comments

It's the final lesson of your first week! Hopefully you feel like you learned something, and not like you tried to learn too much too fast!

In the interests of not overloading you right at the beginning, I want to take this time to talk about code comments.

## What's a code comment?

In one of the lessons this week, I mentioned that the `#` symbol begins a comment in Python. What does that mean? It means that anything following the `#` sign won't be "evaluated," aka Python won't try to run it.

```python
# this line won't run
# 2 + 2
# but this next line will v
>>> 2 + 2
4
```

### Block comments

You can also use `"""` three quotation marks in a row to start what's called a block comment.

When you use `#`, you only comment out one line at a time. What if you want to write a long note, though? Then you can use a block comment.

```python
"""
Everything inside of here
is commented out!
Even when it starts on a new line!
"""
```

## Why use comments?

Well, beyond being useful in this tutorial so I can add explanations above lines of code that you should be able to copy paste and run yourself, they can be helpful for yourself and for your future programming friends reading your code to figure out what you were thinking.

Here are some examples where commenting your code might be helpful:

- introduce what the script is for, how to 
- explain something a little confusing / unintuitive
  - "Calculated to accommodate Feb 29 on leap years"
- provide a caution about something you found out that others should know
  - "Going over 1000 causes the database to explode"
  - "Will error if this is a string"
- provide a reference to more discussion
  - "See ticket #127 for more info"
  - "Fixed with solution found at [URL]"
- mark a point in a long script
  - listen, once you have 100+ lines in a file, it might be really helpful to have `### USER INPUTS` marking above where the user input code goes

### Code comments as auto-documentation

Sometimes, you may come across code comments that follow a rigid structure and which appear all over the place. These might be creating documentation. You run a script that goes through all your code and pulls this out to create documentation you can refer to. In that case, you'll probably see comments like:

```python
def getUserById()
"""
Get user by identifier
"""
```

You can do this whenever you want, wherever you want in your code just so long as you aren't OVER doing it. Good code commenting means finding a balance between going overboard describing EVERYTHING and not describing enough!

## Why not use comments?

Not all code comments are awesome, and sometimes they just gum up your code and make it look more confusing. Consider not using the following types of code commenting:

- expressing your frustration
  - "Don't know why this works but it seems to, so giving up for now"
- commenting out a whole section and leaving it forever
  - sometimes, you might comment out code while you're working on something....but then you gotta delete it if you're not using it, dude!!!
- commenting things that don't need explanation
  - sometimes less is more
