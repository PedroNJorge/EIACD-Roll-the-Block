import pygame
from pprint import pprint
from game import Board
from game import Block
from game import GameLogic
from game import InputHandler
from game import Renderer


def main():
    # create utils
    width, height = 800, 600
    run = True

    pygame.init()
    pygame.display.set_caption("Roll the Block")

    board = Board("LEVEL1")
    block = Block(board.level.start[0], board.level.start[1])
    game_logic = GameLogic(block, board)
    input_handler = InputHandler(block, board, game_logic)
    renderer = Renderer(block, board, width, height)

    board.refresh_layout(block)
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

        if game_logic.game_over:
            # press r to restart
            # Idea: make z undo button
            break

        if game_logic.level_completed:
            print(f"Total moves made: {block.move_counter}")
            game_logic.level_completed = False
            block = Block(board.level.start[0], board.level.start[1])
            pprint(board.level.layout)
            print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

    pygame.quit()


if __name__ == "__main__":
    main()
