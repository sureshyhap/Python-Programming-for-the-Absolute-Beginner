class Television():
    def __init__(self, channel = 1, volume = 10):
        """Initializes data members."""
        self.__channel = channel
        self.__volume = volume
        
    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, new_channel):
        if self.__channel < 1 or self.__channel > 1000:
            print("Incorrect channel choice.")
        else:
            self.__channel = new_channel

    @property
    def volume(self):
        return self.__volume

    def change_volume(self, up):
        if up == True:
            self.__volume += 1
        else:
            self.__volume -= 1

def main():
    tv1 = Television()
    print("Present channel =", tv1.channel, "\nPresent volume =", tv1.volume)
    tv1.channel = 120
    for i in range(50):
        tv1.change_volume(up=True)
    print("Present channel =", tv1.channel, "\nPresent volume =", tv1.volume)

if (__name__ == "__main__"):
    main()
