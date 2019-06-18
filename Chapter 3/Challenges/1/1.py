import random

fortune1 = "A bird in the hand is worth three in the bush!!"
fortune2 = "For hate is never conquered by hate. Hate is conquered by love."
fortune3 = "You can make your own happiness."
fortune4 = "Stop searching forever. Happiness is just next to you."
fortune5 = "Do not seek so much to find the answer as much as to understand the question better."

choice = random.randint(1, 5)

if choice == 1:
    print(fortune1)
elif choice == 2:
    print(fortune2)
elif choice == 3:
    print(fortune3)
elif choice == 4:
    print(fortune4)
elif choice == 5:
    print(fortune5)
else:
    print("Error")
