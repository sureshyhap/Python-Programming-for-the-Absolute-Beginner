import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)
correct = word
scrambled = ""

while word:
    position = random.randrange(len(word))
    scrambled += word[position]
    word = word[:position] + word[position + 1:]

print("Here is the word: ", end="")
print(scrambled)
first = correct[0]
last = correct[-1]
asked_for_hint = False

guess = input("Try to guess the word: ")
while guess != correct and guess != "":
    print("Sorry that's not correct.")
    if asked_for_hint == False:
        wants_hint = input("Would you like a hint? (yes or no): ")
        if wants_hint == "yes":
            asked_for_hint = True
            print("The first letter is", first)
            print("The last letter is", last)
    guess = input("Try again: ")

if guess == correct:
    print("Congratulations you got it!")
if asked_for_hint == False:
    print("You get 10 points!")
else:
    print("You get 5 points!")
