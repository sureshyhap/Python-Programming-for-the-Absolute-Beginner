from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Intro label
        Label(self, text = "Enter information for a new story.").grid(row = 0, column = 0, sticky = W)

        # Label for checks
        Label(self, text = "Pick an adjective.").grid(row = 1, column = 0, sticky = W)
        # Check buttons
        self.itchy_check = BooleanVar()
        Checkbutton(self, text = "itchy", variable = self.itchy_check,
                    command = self.update_text).grid(row = 1, column = 1, sticky = W)
        self.joyous_check = BooleanVar()
        Checkbutton(self, text = "joyous", variable = self.joyous_check,
                    command = self.update_text).grid(row = 1, column = 2, sticky = W)
        self.electric_check = BooleanVar()
        Checkbutton(self, text = "electric", variable = self.electric_check,
                    command = self.update_text).grid(row = 1, column = 3, sticky = W)
        
        # Label for radio buttons
        Label(self, text = "Choose a body part.").grid(row = 2, column = 0, sticky = W)
        # Radio buttons
        self.radio_selection = StringVar(None, "bellybutton")                
        #self.redio_selection.set(None)
        words = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1        
        for word in words:
            Radiobutton(self, text = word, value = word, variable = self.radio_selection,
                        command = self.update_text).grid(row = 2, column = column, sticky = W)
            column += 1

        # Label for text entry 1
        Label(self, text = "Person").grid(row = 3, column = 0, sticky = W)
        # Text entry for person
        self.person_entry = Entry(self)
        self.person_entry.grid(row = 3, column = 1, columnspan = 2, sticky = W)

        # Label for text entry 2
        Label(self, text = "Verb").grid(row = 4, column = 0, sticky = W)
        # Text entry for person
        self.verb_entry = Entry(self)
        self.verb_entry.grid(row = 4, column = 1, columnspan = 2, sticky = W)

        # Label for text entry 3
        Label(self, text = "Plural Noun").grid(row = 5, column = 0, sticky = W)
        # Text entry for person
        self.noun_entry = Entry(self)
        self.noun_entry.grid(row = 5, column = 1, columnspan = 2, sticky = W)

        # Button
        self.bttn = Button(self, text = "Click for story", command = self.update_text)
        self.bttn.grid(row = 6, column = 0, sticky = W)

        # Text field
        self.txt_f = Text(width = 75, height = 10, wrap = WORD)
        self.txt_f.grid(row = 7, column = 0, columnspan = 4, sticky = W)



    def update_text(self):
        message = ""
        
        if self.itchy_check.get():
            message += "itchy "
        if self.joyous_check.get():
            message += "joyous "
        if self.electric_check.get():
            message += "electric "
            
        message += self.radio_selection.get()
        
        message += self.person_entry.get()
        message += self.verb_entry.get()
        message += self.noun_entry.get()

        self.txt_f.delete(0.0, END)
        self.txt_f.insert(0.0, message)

        

def main():
    root = Tk()
    app = Application(root)
    root.title("Mad Libs")
    root.mainloop()

if __name__ == "__main__":
    main()
