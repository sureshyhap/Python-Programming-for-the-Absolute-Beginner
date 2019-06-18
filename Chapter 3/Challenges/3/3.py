import random

number = random.randint(1, 100)
allowed_num_guesses = 5

guess = int(input("Take a guess: "))
guesses = 1

while guess != number:
    if guesses > allowed_num_guesses:
        print("I'm sorry. No more guesses.")
        break
    if guess > number:
        print("Lower.")
    elif guess < number:
        print("Higher")
    guess = int(input("Guess again: "))
    guesses += 1

if guess == number:
    print("You got it!")
