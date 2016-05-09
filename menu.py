 #Jake Routh
#3/1/2016
#mneu

from tkinter import *

class Application(Frame):
    '''menu frame'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    '''creates checkboxes and menu'''
    def create_widgets(self):
        #Foods
        Label(self,
              text = "food "
              ).grid(row = 1,
                     column = 0,
                     sticky = W)
        Checkbutton(self,
                    text = "Steak 10$ "
                    ).grid(row = 2,
                           column = 0,
                           sticky = W)
        Checkbutton(self,
                    text = "Burrito $3 "
                    ).grid(row = 3,
                           column = 0,
                           sticky = W)
        Checkbutton(self,
                    text = "Corndog $2 "
                    ).grid(row = 4,
                           column = 0,
                           sticky = W)
        Checkbutton(self,
                    text = "Mac & Cheese 1$ "
                    ).grid(row = 5,
                           column = 0,
                           sticky = W)
        #Drinks
        Label(self,
              text = "drink "
              ).grid(row = 1,
                     column = 1,
                     sticky = W)
        Checkbutton(self,
                    text = "Water $.50 "
                    ).grid(row = 2,
                           column = 1,
                           sticky = W)
        Checkbutton(self,
                    text = "Pepsi $1 "
                    ).grid(row = 3,
                           column = 1,
                           sticky = W)
        Checkbutton(self,
                    text = "Mtn.Dew $1 "
                    ).grid(row = 4,
                           column = 1,
                           sticky = W)
        Checkbutton(self,
                    text = "Seirra mist $1 "
                    ).grid(row = 5,
                           column = 1,
                           sticky = W)



        self.msg_ent = Entry(self)
        self.msg_ent.grid(row = 6, column = 0, sticky = W)


#main
root = Tk()
root.title("Menu")
app = Application(root)
root.mainloop()
