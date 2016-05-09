#Jake Routh
#menu
#2/29/16

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

def create_widgets(self):
    self.food = BooleanVar()
    Checkbutton(self,
                text = "food",
                variable = food
                ).grid(row = 4, column = 2, sticky = W)






# main
root = Tk()
root.title("Menu")
app = Application(root)
root.mainloop()
