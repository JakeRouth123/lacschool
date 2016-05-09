import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653  
 
def draw_my_picture(screen, x, y):
    pygame.draw.circle(screen,GREEN,(325+x, 342+y), 60)
    pygame.draw.circle(screen,GREEN,(547+x, 342+y), 60)
    pygame.draw.rect(screen,BLACK,[234+x, 342+y, 188 ,22],64) 
    pygame.draw.rect(screen,BLACK,[456+x, 342+y, 188 ,22],64)

    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    text = font.render("Deal with it", True, BLACK)
    
    screen.blit(text, [250, 250])    
   
    pygame.draw.arc(screen, BLACK,  [300+x, 290+y,260, 210], 3*PI/2,
                    2*PI, 2)
    pygame.draw.arc(screen, BLACK,  [300+x, 290+y,260, 210], PI,
                    3*PI/2, 2)
def draw_my_picture2(screen, x, y):
    pygame.draw.circle(screen,RED,(325+x, 342+y), 60)
    pygame.draw.circle(screen,RED,(547+x, 342+y), 60)
    pygame.draw.rect(screen,BLACK,[234+x, 342+y, 188 ,22],64) 
    pygame.draw.rect(screen,BLACK,[456+x, 342+y, 188 ,22],64)

    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    text = font.render("Deal with it", True, BLACK)
    
    screen.blit(text, [250, 250])    
   
    pygame.draw.arc(screen, BLACK,  [300+x, 290+y,260, 210], 3*PI/2,
                    2*PI, 2)
    pygame.draw.arc(screen, BLACK,  [300+x, 290+y,260, 210], PI,
                    3*PI/2, 2) 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [1920, 1080]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("User Control")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    draw_my_picture(screen, x_coord, y_coord)
 
    # Game logic
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
     
    # Drawing section
    draw_my_picture2(screen, x, y) 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()