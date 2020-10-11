class Village():
    def __init__(self, size = "medium", population = "medium",
                 commerce = "medium", name = "hometown"):
        self.size = size
        self.population = population
        self.commerce = commerce
        self.name = name

    def __str__(self):
        return self.name

class Player():
    def __init__(self):
        self.location = Village()
        
    def walk(self, village):
        self.location = village

def main():
    villages = [
        Village(name = "Kakakiro"),
        Village(name = "Tokyo", commerce = "large")
    ]
    player = Player()
    player.walk(villages[0])
    print("The player is at", player.location)

        
if __name__ == "__main__":
    main()
