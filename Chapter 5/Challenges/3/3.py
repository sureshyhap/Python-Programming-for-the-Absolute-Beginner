# I don't understand how to replace a son-father pair

father_son = {}

while True:
    choice = input("""
    Type 1 to add a son father pair
    Type 2 to replace a son father pair
    Type 3 to delete a son father pair
    Type anything else to quit
    """)
    if choice == "1":
        son = input("Enter a son: ")
        father = input("Enter his father: ")
        father_son[son] = father
    elif choice == "3":
        son = input("Which son in a son-father pair should be deleted?")
        del father_son[son]
    else:
        break
    for son, father in father_son.items():
        print("{}'s father is {}".format(son, father))
        
