#Legend of the Dragon
#Jake Routh
#4/25/16

from tkinter import *

# init the games widgets and commands
class Directions(object):
    def __init__(self,options,commands):
        self.options = options
        self.commands = commands
        self.widgets = []
        
    def add(self,widget):
        self.widgets.append(widget)
        
    

# start the game with the 3 starting buttons
class Game(Frame):
  
    def __init__(self, master):
        Frame.__init__(self, master, background="white")   
        self.master = master
        self.master.title("Legend of the Dragon")
        self.master.minsize(400,400)
        self.grid()
        options = 'left right straight'.split()
        options.append('look around')
        self.createCounter = 0
        commands=[self.left1,self.right1,self.straight,self.test]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)
#create the new buttons based on which ones you click
   
    def createwidgets(self,menu):
        row = 1
        for i in menu.options:
            btn = Button(self,text=i,command=menu.commands[row-1])
            menu.add(btn)
            btn.grid(row=row,column=0,sticky=W)
            row += 1        
        if self.createCounter == 0:
            self.scrollbar = Scrollbar(self)
            self.scrollbar.grid(row = 0, column = 2058, rowspan = 700)            
            self.story_txt = Text(self, width = 75, height = 10, 
                                  wrap = WORD, font = ("Blackadder ITC", 16, 
                                                       "bold"),
                                  yscrollcommand=self.scrollbar.set)
            self.story_txt.grid(row =0, column = 2057, columnspan = 1,
                                rowspan = 700, sticky = S)
            self.story_txt.insert(0.0,'A shining star in the dark, the upholder\
 of justice, The White Knight of Gredina. You are on a quest. You must slay the\
 mighty dragon that has been terrorizing the countryside for years now.  It has\
 recently taken roost in a nearby cave system. But infiltrating the cave system\
 is no simple task, many have tried and failed before you. But you are the\
 White knight! Failing is not an option! For if you fail no one else can\
 succeed... You are strong And hold your mighty sword and shield in\
 your hands as you enter your cave. You are always on your guard as you know\
 the tales of dragons roost. There has been sightings of half man half dragon\
 minions! They have scales on their body hard as diamond and there claws are\
 sharp as the sharpest sword. Though they cant breath fire like the dragon they\
 are still just as deadly.  The atrocity of this must be purged. So the dragons\
 evil tainted blood cannot enter that of our human kind. As you enter the cave\
 you come to a split. There is three ways that you can go left, right, or\
 straight. Which way does the mighty knight go?')
            self.scrollbar.config(command=self.story_txt.yview)
        self.createCounter += 1
        #first choice for going left
    
    def left1(self):
        for i in self.directions.widgets:
                    i.grid_forget()        
        self.story_txt.insert(END,"\nYou go left thinking that would be the\
 safest route as it did not have the most foul smell as the others\
 did. You come into the room and in plain view a chest! It looks\
 unlocked you wonder what's inside? But you also think such a easy pick\
 would be taken by now. so you also think it could be a booby trap. What do you\
 do? ")
        self.story_txt.yview('moveto', '1')
        options = ['Search the chest','leave the chest']
        commands = [self.left1_a, self.left1_b]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)
    #first choice for going right
    
    def right1(self):
        for i in self.directions.widgets:
            i.grid_forget()        
        self.story_txt.insert(END,"\nYou go right because the right path is \
always right! Right? As you go along this path you come into a small room \
lighted by a single torch attacted to the wall.you could easily remove this to \
take with you on your quest to find the dragon. There is also a single gold \
coin on the ground. It looks suspicious. Who would leave a golden coin on the \
ground like that? Perhaps the dragon dropped it?  ")   
        self.story_txt.yview('moveto', '1')
        options = ['take the coin','take the torch']
        commands = [self.right1_a, self.right1_b]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)        
    #first choice for going straight
    
    def straight(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"\nYou go straight thinking it will be the\
 Goblins you say as you smell the stench of them. You draw your sword thinking\
 they are close by but as you look around you notice they have moved on a while\
 ago and you sheath your sword and go back to your quest. Before you go you\
 notice a dead man that had been killed by the goblin. Poor guy mustve been\
 ambushed you say. you wonder if he has anything useful.")
        self.story_txt.yview('moveto', '1')
        options = ['search the man', 'Leave him alone']
        commands = [self.straight1_a, self.straight1_b]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)
    #testing button doesnt work quite yet
    
    def test(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"\nyou are observant")
        self.story_txt.yview('moveto', '1')
        options = ['keep going']
        commands = [self.right2]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)
    #one of two choices when going left
    
    def left1_a(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"\nyou decide to search the chest and\
 inside the chest you find a helmet! It fits perfectly and is in much better\
 condition than your current helmet. You leave the room and continue on into\
 the darkness.")
        self.story_txt.yview('moveto', '1')
        options = ['keep going']
        commands = [self.left2]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)
    #second choice for going left
    
    def left1_b(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END, "\nthe chest seems to suspicious for you\
 so you leave it. But what a mistake you have made. The chest was a\
 mimick! It leaps off the ground and tries to eat you! You draw your\
 sword quickly but it consumes it. You have no choice but to turn\
 back out of the cave! Perhaps another day you shall try to fight\
 this but not today! You run away screaming! YOU LOSE THE COWARDLY WAY")
        self.story_txt.yview('moveto', '1')
    #ending for the left route
    
    def left2(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"\nyay stop")
        self.story_txt.yview('moveto', '1')
        options = []
        commands = [self.left3]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)            
        #first choice of 2 for the right path
    
    def right1_a(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"you walk over to the coin and pick it up as\
 you look at it you feel a very strong gust of wind it knocks you to your feet\
 still enough light from various cracks on the ceiling and walls to guide you\
 through the darkness to the next room.")
        self.story_txt.yview('moveto', '1')
        options = ["cool"]
        commands = [self.right2]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)  
    #second choice of 2 for the right path
    
    def right1_b(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"you walk to the torch and take it off its\
 mount you ignore the coin for it is to suspicious for your liking and\
 you move on from the room moving to the next")
        self.story_txt.yview('moveto', '1')
        options = ["Kool"]
        commands = [self.right2]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions)  
#ending for riht AND straight I just used the same ending beecuase it would
#be the same for both
    
    def right2(self):
        for i in self.directions.widgets:
            i.grid_forget()
        self.story_txt.insert(END,"\nyay stop")
        self.story_txt.yview('moveto', '1')
        options = ["\nyay stop"]
        commands = [self.right3]
        self.directions = Directions(options,commands)
        self.createwidgets(self.directions) 
#first choice of 2 for the straight path
    
    def straight1_a(self):
            for i in self.directions.widgets:
                i.grid_forget()
            self.story_txt.insert(END,"\nYou search the man rummaging through\
 his stuff for anything useful. You shake his russack and find a\
 key!  You dont know whats its too but if this man found it here it\
 could perhaps prove useful.")
            self.story_txt.yview('moveto', '1')
            options = ['keep going']
            commands = [self.right2]
            self.directions = Directions(options,commands)
            self.createwidgets(self.directions)
#second choice of 2 for the straight path
    
    def straight1_b(self):
            for i in self.directions.widgets:
                i.grid_forget()
            self.story_txt.insert(END,"\nYou leave the man alone giving him\
 the respect he deserves in death.as you leave the room you can hear\
 the goblins reentering the room. You are glad you left when you\
 did goblins are sneaky and fast and you did not wish to fight\
 them all.")
            self.story_txt.yview('moveto', '1')
            options = ['keep going']
            commands = [self.right2]
            self.directions = Directions(options,commands)
            self.createwidgets(self.directions)

def main():
   
    root = Tk()
    app = Game(root)
    root.mainloop()  


if __name__ == '__main__':
    main()