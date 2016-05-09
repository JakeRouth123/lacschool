#Jake Routh
#2/18/2016
#Encoder/Decoder

from tkinter import *

class Application(Frame):
    """ GUI application that encodes or decodes a message depending on which they pick """

def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()


def create_widgets(self):
    Label(self,
          text = "Enter information for decoding/encoding"
          ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

    Label(self,
          text = "encode: "
          ).grid(row = 1, column = 0, sticky = W)
    self.encode_ent = Entry(self)
    self.encode_ent.grid(row = 1, column = 1, sticky = W)

def __encode__(self):
    person = self.encode_ent.get()

root = Tk()
root.title("Encoder/Decoder")
app = Application(root)
root.mainloop()
