import random

heads = 0
tails = 0

i = 0
while i < 100:
    flip = random.randrange(2)
    if flip:
        heads += 1
    else:
        tails += 1
    i += 1

print(f"There were {heads} heads and {tails} tails.")
