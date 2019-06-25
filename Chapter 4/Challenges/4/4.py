import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)

print("Try to guess my word! The word has", len(word), "letters.")

for i in range(5):
    request = input("Choose a letter and I will tell you if it is in thw word: ")
    if request in word:
        print("yes")
    else:
        print("no")

guess = input("Take a guess: ")
while guess != word and guess != "":
    guess = input("Sorry, try again: ")

if guess == word:
    print("You got it!")
