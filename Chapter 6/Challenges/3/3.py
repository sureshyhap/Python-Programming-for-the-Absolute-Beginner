import random

def ask_number(question, low, high, step = 1):
    """ Asks for a number within a range with a given step """
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    print(response)
    return response

number = random.randint(1, 100)
allowed_num_guesses = 5

def main():
    #guess = int(input("Take a guess: "))
    guess = ask_number("Take a guess: ", 1, 100)
    guesses = 1

    while guess != number:
        if guesses > allowed_num_guesses:
            print("I'm sorry. No more guesses.")
            break
        if guess > number:
            print("Lower.")
        elif guess < number:
            print("Higher")
        #guess = int(input("Guess again: "))
        guess = ask_number("Guess again: ", 1, 100)
        guesses += 1

    if guess == number:
        print("You got it!")

main()
