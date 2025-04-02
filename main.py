from collections import deque
import pygame
from pprint import pprint
import time
from game import Board
from game import Block
from game import GameLogic
from game import InputHandler
from game import Renderer
from search_algorithms import a_star
from search_algorithms import breadth_first_search
from search_algorithms import depth_limited_search
from search_algorithms import greedy_search
from search_algorithms import iterative_deepening_search
from search_algorithms import uniform_cost_search
from search_algorithms import Problem


def main():
    run = True

    pygame.init()
    pygame.display.set_caption("Roll the Block")

    board = Board("LEVEL2")
    block = Block(board.level.start[0], board.level.start[1])
    game_logic = GameLogic(block, board)
    input_handler = InputHandler(block, board, game_logic)
    renderer = Renderer(block, board)

    board.refresh_layout(block)
    pprint(board.level.layout)
    print("---------------------STARTING-----------------------------")

    start = time.perf_counter()
    # solution_node = breadth_first_search(Problem(block, board))
    solution_node = a_star(Problem(block, board))
    # solution_node = greedy_search(Problem(block, board))
    # solution_node = iterative_deepening_search(Problem(block, board))
    end = time.perf_counter()
    print(f"Algorithm took {(end - start)*1000:.6f} ms")

    if solution_node is not None:
        print("---------------------FINISHED-----------------------------")
        pprint(solution_node.state)

        solution = deque()
        prev_node = solution_node.parent
        solution.appendleft(solution_node.action)

        while prev_node is not None:
            pprint(prev_node.state)
            solution.appendleft(prev_node.action)
            prev_node = prev_node.parent
            pygame.time.delay(1000)

        solution.popleft()
        print(solution)
        print(f"Moves made: {len(solution)}")
        run = False
    else:
        print("Couldn't find a solution!")
        pygame.quit()

    while run:
        run = input_handler.handle_events()
        # print(block)

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
            board.switch_level()
            block = Block(board.level.start[0], board.level.start[1])
            board.refresh_layout(block)
            game_logic = GameLogic(block, board)
            input_handler = InputHandler(block, board, game_logic)
            print(board)

    pygame.quit()


if __name__ == "__main__":
    main()
