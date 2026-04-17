import random

def greet(name):
    return f"Hello, {name}!"

def roll_dice(sides=6):
    return random.randint(1, sides)

if __name__ == "__main__":
    print(greet("World"))
    print(f"You rolled a {roll_dice()}")
