#Jake Routh
#2/18/2016
#Encoder/Decoder

from tkinter import *
from CeasarCipher import CeasarCipher

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self.coderRing = CeasarCipher()

    def create_widgets(self):
        #label
        Label(self,
              text = "Enter text to encode/decode:"
              ).grid(row = 0, column = 0, sticky = W)

        self.rbutton1 = StringVar()
        self.rbutton1.set(None)
        self.rbutton2 = StringVar()
        self.rbutton2.set(None)
        #create encoding button
        Radiobutton(self,
                    text = "Encode",
                    variable = self.rbutton1,
                    value = True,
                    command = self.handle_nCode
                    ).grid(row = 2, column = 0, sticky = W)


        #create decoding button
        Radiobutton(self,
                    text = "Decode",
                    variable = self.rbutton1,
                    value = False,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        self.msg_ent = Entry(self)
        self.msg_ent.grid(row = 1, column = 0, sticky = W)

        #create text feild
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 1)

        #reset button
        self.Bttn = Button(self, text = "Reset",
                           command = self.handle_reset)
        self.Bttn.grid(row = 5, column = 1, pady = 10, sticky = W) 

    def update_text(self):
        message = " "
        
            
    def handle_nCode(self):
        contents = self.msg_ent.get()
        result = self.coderRing.encode(contents)
        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,END)
        
    def handle_reset(self):
        self.msg_ent.delete(0,END)
        self.results_txt.delete(0.0,END)
        self.msg_ent.focus_set()
     

# main
root = Tk()
root.title("Basic layout")
app = Application(root)
root.mainloop()
