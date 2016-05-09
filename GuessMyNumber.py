# GuessMyNumber.py
# Thorin Schmidt
# 2/18/2016

from tkinter import *
from random import randint

class Application(Frame):
    """ GUI Application for favorite movie types. """
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.remainingTries = 10
        self.number = randint(1,100)
        self.guessedIt = False
        self.create_widgets()
        
        

    def create_widgets(self):
        # create number grid
        self.chosen = StringVar()
        self.chosen.set(None)
        num = 1
        for r in range(0,10):
            for c in range(10):
                Radiobutton(self, text = str(num),
                            variable = self.chosen,
                            value = str(num),
                            command = self.update_guess
                            ).grid(row = r, column = c)
                num += 1

        self.label1 = Label(text = "I've chosen a number from 1 through 100.")
        self.label1.grid(row = 11, column = 0, columnspan = 10, sticky = W)
        self.label2 = Label(text = "You have 10 tries.")
        self.label2.grid(row = 12, column = 0, columnspan = 10, sticky = W)


        
    def update_guess(self):
        if (self.remainingTries > 0) and (not(self.guessedIt)):
            self.remainingTries -= 1    
            message = "You guessed: " + self.chosen.get() + ", "
            currentGuess = int(self.chosen.get())
            if currentGuess < self.number:
                message += "Higher."
            elif currentGuess > self.number:
                message += "Lower."
            else:
                message += "CORRECT!"
                self.guessedIt = True

            self.label1["text"] = message
            self.label2["text"] = "You have "+ str(self.remainingTries) + " tries."





# main
root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()
