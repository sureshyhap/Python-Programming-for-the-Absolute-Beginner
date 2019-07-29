
############ Isn't Challenge 1 already implemented? ################
############ Not exactly working correctly #########################
############ because static data members are not working ###########

# Critter Caretaker
# A virtual pet to care for

import random

class Critter(object):
    """A virtual pet"""
    total_hunger = 0
    total_boredom_ = 0
    total_mood = 0
    
    def __init__(self, name):
        self.name = name
        self.hunger = random.randrange(10)
        self.boredom = random.randrange(10)
        Critter.total_hunger += self.hunger
        Critter.total_boredom_ += self.boredom

    def __str__(self):
        return str(self.name) + " " + \
        str(self.hunger) + " " + \
        str(self.boredom)

    @staticmethod
    def all_eat(food = 4):
        total_hunger -= food
        
    @staticmethod
    def all_play(play = 4):
        total_boredom -= play

    def all_mood(self):
        unhappiness = total_hunger + total_boredom
        if unhappiness < 50:
            m = "happy"
        elif 50 <= unhappiness <= 100:
            m = "okay"
        elif 101 <= unhappiness <= 150:
            m = "frustrated"
        else:
            m = "mad"
        return m        
        

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    #crit_name = input("What do you want to name your critter?: ")
    #crit = Critter(crit_name)
    critters = []
    for letter in "ABCD":
        critters.append(Critter(letter))

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to all critters
        2 - Feed your critters
        3 - Play with your critters
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            Critter.all_eat()
         
        # play with your critter
        elif choice == "3":
            Critter.all_play()

        elif choice == "4":
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
