import pygame

width, height = 800, 600
run = True
move_counter = 0

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Roll the Block")

while run:
    #use input handler

    # Fill the screen with a color (optional)
    screen.fill((0, 0, 0))  # Black color

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
