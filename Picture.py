#drawn picture
#Jake Routh
#3/4/2016

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#set pi
PI = 3.141592653 
#imtiazlize the picture
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    #pygame.draw.circle(screen, color, (x,y), radius, thickness)
    
    pygame.draw.circle(screen,GREEN,(325,342), 60)
    pygame.draw.circle(screen,GREEN,(547,342), 60)
    pygame.draw.rect(screen,BLACK,[234, 342, 178 ,12], 56) 
    pygame.draw.rect(screen,BLACK,[456, 342, 178 ,12], 56)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
     
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Deal with it", True, BLACK)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])    
    #drwas an arc for the smile
    pygame.draw.arc(screen, BLACK,  [300,290,250,200],3*PI/2,   2*PI, 2)
    pygame.draw.arc(screen, BLACK,  [300,290,250,200],    PI, 3*PI/2, 2)    
    # --- update screen
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()