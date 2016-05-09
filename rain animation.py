# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
BLUE = [0, 0, 255] 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREY = [145, 145, 145] 
PALE_TURQUOISE = [175, 238, 238]
YELLOW = [255, 255, 0]
# Set the height and width of the screen
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Rain animation")
 
# Create an empty array for rain drops to be placed into
rain_list = []
 
# Loop 50 times and add a rain drop in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    rain_list.append([x, y])
 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            done = True 
    
    # Set the screen background
    screen.fill(PALE_TURQUOISE)
    pygame.draw.circle(screen,YELLOW,(60,60), 60)
    pygame.draw.circle(screen,GREY,(0,40), 60)
    pygame.draw.circle(screen,GREY,(40,0), 60)
    pygame.draw.circle(screen,GREY,(60,40), 60)
    pygame.draw.circle(screen,GREY,(100,40), 60)
    pygame.draw.circle(screen,GREY,(159,40), 60)
    pygame.draw.circle(screen,GREY,(223,40), 70)
    pygame.draw.circle(screen,GREY,(263,40), 60)
    pygame.draw.circle(screen,GREY,(300,40), 60)
    pygame.draw.circle(screen,GREY,(360,40), 60)
    # Process each rain drop in the list
    for i in range(len(rain_list)):
 
        # Draw the rain drop
        pygame.draw.circle(screen, BLUE, rain_list[i], 2)
 
        # Move the rain drop down one pixel
        rain_list[i][1] += 1
 
        # If the rain drop has moved off the bottom of the screen
        if rain_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            rain_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            rain_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
 
# on exit.
pygame.quit()