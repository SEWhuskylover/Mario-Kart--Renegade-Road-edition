# importing the pygame program
import pygame


# Initialize Pygame
pygame.init()

# colors that are going to be used in the program, set with rgb
GREEN = (100, 250, 140)
DARKGREY = (70, 70, 70)
WHITE = (250, 250, 250)

# frames per second that the game will run in
fps = 200
clock = pygame.time.Clock()

# creating the display
display_width = 700
display_height = 900
screen = pygame.display.set_mode((display_width, display_height))
# naming the display
pygame.display.set_caption('Mario Kart: Renegade Road Edition')


# main game loop
# exiting variable allows game loop to run and allows game to close when exiting = true
exiting = False
while not exiting:
    # sets the fps
    clock.tick(fps)

    for event in pygame.event.get():
        # allows the player to quit by pressing q
        if event.type == pygame.QUIT:
            exiting = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exiting = True

    # updating the display so that changes will show up
    pygame.display.update()


# exits the program
pygame.quit()
