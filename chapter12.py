#Jake Routh
#4/5/2016
#chapter 12


import random
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Rectangle():
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.height = random.randint(20, 70)
        self.width = random.randint(20, 70)
        self.changex = random.randint(-3, 3)
        self.changey = random.randint(-3, 3)
    def draw(self):
        pygame.draw.rect(screen,color,[self.x, self.y, self.height ,self.width],
                         0) 
    def move(self):
        if self.x >= 700 or self.x <= 0:
            self.changex *= -1
        self.x += self.changex
        if self.y >=500 or self.y <= 0:
            self.changey *= -1
        self.y += self.changey
        
    def color(self):
        COLOR = random.randint(0, 0, 0) < (255, 255, 255)


class Ellipse(Rectangle):
    def draw(self):
            pygame.draw.ellipse(screen,color,[self.x, self.y, self.height ,
                                              self.width],0)    
    
    
        
        
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for i in range(50):
    my_object = random.choice([Rectangle(),Ellipse()])
    my_list.append(my_object)
    
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # --- Game logic should go here
   
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in my_list:
        i.draw()
        i.move()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
