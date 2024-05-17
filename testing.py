import pygame
pygame.init()

# 30 x 20    
WIDTH, HEIGHT = 1000, 600

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
#pipbg = pygame.image.load("bg.jpg") #bg image
   
RATIO_POTATO = 35
SPACING = RATIO_POTATO * 2 + 5  #double the ratio for the next circle
   
#make sure veggies fit on the screen
NUM_VEGGIES_X = WIDTH // SPACING
NUM_VEGGIES_Y = HEIGHT // SPACING


def draw_veggies(location):
    for y in range(NUM_VEGGIES_Y):
        for x in range(NUM_VEGGIES_X):
            #limits and location for veggie
            veggie_x = x * SPACING + RATIO_POTATO
            veggie_y = y * SPACING + RATIO_POTATO
           
            pygame.draw.circle(screen, (150,230,10), (veggie_x,veggie_y), RATIO_POTATO)
            location.append((veggie_x,veggie_y))    #save location on array


def main():    
    # Run until the user asks to quit
    running = True
    while running:  
       
        #vars
        x = 0
        y = 0

        # Fill the background with white
        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))       #add image as the background

        #array to store locations
        matrix = []     #location (x, y)
        draw_veggies(matrix)        #pass the empty matrix to append locations

                   
        # Flip the display
        pygame.display.flip()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
    # Done! Time to quit.
    pygame.quit()

main()
