######################## FIX #############################







from tkinter import *

def main():
    entrees = {
        "Spaghetti" : 15,
        "Ravioli" : 10,
        "Pizza" : 5
    }
    drinks = {
        "Soda" : 3,
        "Water" : 1,
        "Lemonade": 2
    }   
    root = Tk()
    app = Application(root)
    app.create_widgets(entrees, drinks)
    root.title("Restaurant Simulator")
    root.geometry("500x100")
    root.mainloop()

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

    def create_widgets(self, dishes, liquids):
        Label(self, text = "Pick an entree and a drink.").grid(row = 0, column = 0, sticky = W)

        self.radio = StringVar(None, "15")
        column = 1
        for dish, price in dishes.items():
            Radiobutton(self, text = dish, value = str(price), variable = self.radio,
                        command = self.calc_price).grid(row = 0, column = column, sticky = W)
            column += 1

        self.radio2 = StringVar(None, "3")
        column = 1
        for drink, price in liquids.items():
            Radiobutton(self, text = drink, value = str(price), variable = self.radio2,
                        command = self.calc_price).grid(row = 1, column = column, sticky = W)
            column += 1

        self.total_text = Text(self, width = 10, height = 1, wrap = WORD)
        self.total_text.grid(row = 2, column = 1, sticky = W)


    def calc_price(self):
        food = int(self.radio.get())
        drink = int(self.radio2.get())
        total = food + drink
        self.total_text.delete(0.0, END)
        self.total_text.insert(0.0, "$" + str(total) + ".00")

                                                                                                            
        
if __name__ == "__main__":
    main()
