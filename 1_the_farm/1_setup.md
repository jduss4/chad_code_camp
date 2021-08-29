# 1.1: Setup

Welcome to Programming for Farmers, lesson 1.1! We're going to start out pretty easy for this first week and just make sure that you have Python installed and a text editor ready to go. Then you'll learn a little about some of the fundamentals of interacting with your computer.

## Programming on your computer

### Python

What is Python and why are we downloading it? Python is a programming language, and your computer needs to understand how to interpret the code you're writing with Python syntax in order to execute, or run it.

You already downloaded Python for your class, so you have it lying around already. Make sure that it is Python 3, or else we may need to work on installing a more modern version.

Previously for your class, you wrote some code and then used a Python graphical user interface to select and run that file. This is not my favorite thing. Ideally, we can run everything from the command line interface, instead. Trust me, it will be a lot easier in the long run. Maybe sit down with me sometime and we'll see if we can figure out how to do that on Windows, because I know 0 things about executing programs in Windows so good luck to both of us there.

### Text editor

You are also going to need a text or code editor for this course. For example, your computer probably already has Notepad or Notepad++, which would work, although it's a little clunky. Unfortunately, you can't use Word for this purpose, as it is meant for formatting documents for printing / publication and not for writing code.

I use [Sublime Text 3](https://www.sublimetext.com/), personally, but a lot of people I know use [Atom](https://atom.io/). Whatever you pick, download it and open it up, change the colors, etc. I can help you customize it for Python development, although most of the time editors are smart enough to do it automatically for you when it sees you're working on a Python file.

### Running Python

I'm going to tell you about two ways to run Python for this course:

- via the Python interpreter
- with `.py` files

The first way is with the interpreter. When you open the Python program on your machine, you get a little terminal that's waiting for Python. You can type in `2+2`, hit enter, and congrats, you wrote and executed some Python! The interpreter is a great way to try out things quickly to see what happens.

The second way is with `.py` files, which are basically just text files, and you're using the file extension to let interested parties know that it contains Python. You can use your text editor to create `.py` files, and then execute them. You'll want to do this for anything more involved than 4 or 5 lines of code.

### How to run things on Windows

Okay, we need to figure out how to run Python files, so that you can write in your editor and just execute programs quickly, rather than use the laborious process from your class of going through the Python interface.  I guess I'll just help with this part, since I don't know how to do it, either.  NO ASSIGNMENT!  Wow what a week, eh Donaghy?

## Basics concepts of programming on your computer

When I first started learning programming, working on the command line and "executing" scripts was all pretty new to me. I'd like to take a little time to mention a few things here that may be helpful as you get started.

### Interface

First off, you need to understand the difference between the interfaces you're using.

- GUI: graphical user interface, how you normally browse Windows, for example
- CLI: command line interface, when you use a terminal to browse like you're in an old text-only adventure game

### Execution

When you tell the computer that you want to run a line of code or a program, this is considered "executing" the code. If it's just typed but you haven't hit return yet, or the file is sitting there but you didn't actually try to run it yet, the code has not been executed.

In this code camp, you will often see the word "execute" and really what this means is "when the code runs." Behind the scenes, it means that Python is translating your instructions into 0s and 1s that your computer can understand (because your computer doesn't know Python).

You will also need to know about the concept of an "executable." An executable is a file or bunch of files that can be run. When you double click Steam to play some games, you're running an executable.

### Standard in, out, and everybody's favorite standard error

When you run a script, you might be putting things in, or outputting something to a screen, or you might even end up with an error! I'm not going to go into the details too much, but you will need to know about the following:

- STDIN:  standard input, the method your environment is using to listen for and capture user input
- STDOUT: standout output, where things like `print` end up! Usually this is your terminal window
- STDERR: standard error, where all the script's errors go to live. Usually this also outputting to the terminal, so I don't worry about it much

That's probably a bit of an oversimplification, but they are good to know about in case you ever come across something that mentions them, or have to work through errors regarding them, etc.

In general, if you're running scripts, you'll want to keep an eye on your terminal because that's where the STDOUT and STDERR are probably printing.

### print()

While we're on the topic of STDOUT, Python has a handy method called `print()` which allows you to print things to STDOUT. This can help if you want to provide a user information / feedback as part of your script, or just if you want to try to see what's going on with something you're working on.
