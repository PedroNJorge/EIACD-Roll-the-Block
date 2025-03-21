import pygame
from game import Board
from game import Block
from game import GameLogic
from game import Renderer
from game import InputHandler


def main():
    width, height = 800, 600
    run = True
    move_counter = 0

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


if __name__ == "__main__":
    main()
