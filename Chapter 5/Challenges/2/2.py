points = 30
attributes = {
    "Strength" : 0,
    "Health" : 0,
    "Wisdom" : 0,
    "Dexterity" : 0
}

while True:
    choice = input("""
    Type 1 to add points to an attribute
    Type 2 to remove points from an attribute
    Type anything else to end program
    """)
    if choice == "1":
        how_much = input("How many points to add?")
        how_much = int(how_much)
        which = input("""
        Type 1 to add to strength
        Type 2 to add to health
        Type 3 to add to wisdom
        Type 4 to add to dexterity
        """)
        if which == "1":
            attributes["Strength"] += how_much
            points -= how_much
        elif which == "2":
            attributes["Health"] += how_much
            points -= how_much
        elif which == "3":
            attributes["Wisdom"] += how_much
            points -= how_much
        elif which == "4":
            attributes["Dexterity"] += how_much
            points -= how_much
        else:
            print("Incorrect option")
    elif choice == "2":
        how_much = input("How many points to remove?")
        how_much = int(how_much)
        which = input("""
        Type 1 to remove from strength
        Type 2 to remove from health
        Type 3 to remove from wisdom
        Type 4 to remove from dexterity
        """)
        if which == "1":
            attributes["Strength"] -= how_much
            points += how_much
        elif which == "2":
            attributes["Health"] -= how_much
            points += how_much
        elif which == "3":
            attributes["Wisdom"] -= how_much
            points += how_much
        elif which == "4":
            attributes["Dexterity"] -= how_much
            points += how_much
        else:
            print("Incorrect choice")
    else:
        break
    print("Points:", points)
    print()
    print("Strength:", attributes["Strength"])
    print("Health:", attributes["Health"])
    print("Wisdom:", attributes["Wisdom"])
    print("Dexterity:", attributes["Dexterity"])
    
    
        
    
    
            


