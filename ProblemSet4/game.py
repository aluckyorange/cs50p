import random

def get_positive(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            continue
        if number >= 1:
            return number

level = get_positive("Level: ")
rand = random.randint(1, level)

while True:
    guess = get_positive("Guess: ")
    if guess > rand:
        print("Too large!")
    elif guess < rand:
        print("Too small!")
    else:
        print("Just right!")
        break