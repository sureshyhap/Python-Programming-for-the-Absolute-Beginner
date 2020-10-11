from tkinter import *
import random

num = random.randint(1, 100)    

def main():
    root = Tk()
    app = Application(root)
    root.title("Guess my Number")
    root.geometry("500x200")
    root.mainloop()

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl1 = Label(self, text = "I'm thinking of a number between 1 and 100." \
                          + "Try to guess it in as few attempts as possible.")
        self.lbl1.grid(row = 0, column = 0, sticky = W)

        self.guess = Entry(self)
        self.guess.grid(row = 1, column = 0, sticky = W)

        self.bttn = Button(self, text = "Confirm guess", command = self.response)
        self.bttn.grid(row = 2, column = 0, sticky = W)

        self.txt_f = Text(self, width = 20, height = 1, wrap = WORD)
        self.txt_f.grid(row = 3, column = 0, sticky = W)

    def response(self):
        response = None
        if int(self.guess.get()) == num:
            response = "You got it!"
        elif int(self.guess.get()) > num:
            response = "Lower"
        else:
            response = "Higher"
        self.txt_f.delete(0.0, END)
        self.txt_f.insert(0.0, response)
        

if __name__ == "__main__":
    main()
                                                                      
