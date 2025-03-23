import pygame
from pprint import pprint
from game import Board
from game import Block
from game import GameLogic
from game import InputHandler
from game import Levels
from game import Renderer
from utils import LevelType
from utils import TileType
from utils import Colors


def main():
    # create utils
    width, height = 800, 600
    run = True
    move_counter = 0

    pygame.init()
    pygame.display.set_caption("Roll the Block")

    board = Board("LEVEL1")
    block = Block(board.level.start[0], board.level.start[1])
    game_logic = GameLogic(block, board)
    input_handler = InputHandler(block, board, game_logic)
    renderer = Renderer(block, board, width, height)

    pprint(board.level.layout)
    print("---------------------------------")

    while run:
        run = input_handler.handle_events()

        if (not run):
            break

        # Fill the screen with a color (optional)
        renderer.screen.fill((0, 0, 0))  # Black color

        # Update the display
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
