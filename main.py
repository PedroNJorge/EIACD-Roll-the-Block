from collections import deque
import pygame
from pprint import pprint
import time
import sys
from game import Board
from game import Block
from game import GameLogic
from game import InputHandler
from game import Renderer
from search_algorithms import Problem
from search_algorithms import a_star
from search_algorithms import breadth_first_search
from search_algorithms import depth_first_search
from search_algorithms import depth_limited_search
from search_algorithms import greedy_search
from search_algorithms import iterative_deepening_search
from search_algorithms import uniform_cost_search


def main():
    run = True

    pygame.init()

    board = Board("LEVEL1")
    block = Block(board.level.start[0], board.level.start[1])
    game_logic = GameLogic(block, board)
    input_handler = InputHandler(block, board, game_logic)
    renderer = Renderer(block, board, game_logic, input_handler)

    board.refresh_layout(block)
    pprint(board.level.layout)

    renderer.run()
    pygame.quit()
    sys.exit()
    """
    print("---------------------STARTING-----------------------------")

    if board.level.button:
        layout_only = False
    else:
        layout_only = True

    problem = Problem(block, board, layout_only=layout_only)

    start = time.perf_counter()
    # solution_node = a_star(problem)
    # solution_node = breadth_first_search(problem)
    solution_node = depth_first_search(problem)
    # solution_node = depth_limited_search(problem, 100000)
    # solution_node = greedy_search(problem)
    # solution_node = iterative_deepening_search(problem)
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
    """

    '''
    while run:
        run = input_handler.handle_events()

        if (not run):
            break

        # Fill the screen with a color (optional)
        #renderer.screen.fill((0, 0, 0))  # Black color

        # Update the display
        #pygame.display.flip()

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
    '''


if __name__ == "__main__":
    main()
