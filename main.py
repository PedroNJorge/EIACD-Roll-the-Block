import pygame
from game import Board
from game import Block
from game import GameLogic
from game import InputHandler
from game import Levels
from game import Renderer


def main():
    width, height = 800, 600
    run = True
    move_counter = 0

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Roll the Block")

    board = Board("LEVEL1")
    block = Block(board.level.start[0], board.level.start[1])
    game_logic = GameLogic(block, board)
    input_handler = InputHandler(block, board, game_logic)
    renderer = Renderer(block, board)

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
