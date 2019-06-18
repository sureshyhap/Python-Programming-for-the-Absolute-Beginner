guess_min = 1
guess_max = 100

number = 27

guess = guess_min + ((guess_max - guess_min) // 2)
tries = 1
while guess != number:
    if guess < number:
        guess_min = guess
    elif guess > number:
        guess_max = guess
    print(tries, "guesses so far")
    input()
    tries += 1
    guess = guess_min + ((guess_max - guess_min) // 2)

if guess == number:
    print(f"The computer found it in {tries} tries.")
