#!/usr/bin/env python3

# Debugging

# Your dad has asked you to feed the barn cats. And raccoons. And opossum, Alf.
# Each critter eats a certain amount of food, so he has given you a program to
# calculate how much food you need. It's a little complicated because Alf has
# recently been blessed with many opossumlets and needs to eat more than normal!

# Unfortunately, when you run his program, something isn't working!
# You will have to figure it out before the cats get DANGEROUSLY HUNGRY!

# HINT:
# You may want to start with main() since that's where the program starts!
# There are TWO problems with this script

CATS = ["Banjo", "Livy", "Damon", "Rambo", "Charlie"]
RACCOONS = ["No Name", "Name Your Raccoons!!!"]
OPOSSUMS = ["Alf"]

def calc_food(critter, per_critter=1):
    count = len(critter)
    return count * per_critter

# say hello to all of the farm cats
def greet_cats():
    for cat in CATS:
        print("Good evening, " + cat)

def main():
    total_food = 0
    total_food += calc_food(critter=CATS)
    total_food += calc_food()
    # add a little extra food for Alf
    total_food += calc_food(critter=OPOSSUMS, per_critter=5)

    greet_cats()
    print("You are going to need " + total_food + " cups of food")

if __name__ == "__main__":
    main()