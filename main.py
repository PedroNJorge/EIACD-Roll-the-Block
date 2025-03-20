import pygame

# Initialize pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Roll the Block")

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((0, 0, 0))  # Black color

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
