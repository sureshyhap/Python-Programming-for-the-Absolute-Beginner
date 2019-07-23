import random

words = ["Hi", "there", "how", "are", "you"]

while words:
    word = random.choice(words)
    print(word)
    words.remove(word)
