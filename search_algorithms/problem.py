from copy import deepcopy
from game import Board
from game import GameLogic
from pprint import pprint


class Problem:
    def __init__(self, block, board):
        self.initial = (block, tuple(map(tuple, board.level.layout)))
        self.level_name = board.level.level_name

    def actions(self, state):
        valid_actions = []
        print("|||||||||||||||Current state||||||||||||||||||")
        print(state[0])
        pprint(state[1])
        for action in ["up", "down", "left", "right"]:
            ghost_block = deepcopy(state[0])
            ghost_block.move(action)
            ghost_board = Board(self.level_name)
            ghost_game_logic = GameLogic(ghost_block, ghost_board)
            print("~~~~ACTION~~~~: ", action)
            print("GHOST: ", ghost_block)
            print("CURR STATE: ", state[0])
            print("~~~~~~~~~~~~~~")

            if not ghost_game_logic.check_lose():
                valid_actions.append(action)

        print("Valid actions:", valid_actions)
        print("||||||||||||||||||||||||||||||||||||||||||||||")
        return valid_actions

    def result(self, state, action):
        block = deepcopy(state[0])
        block.move(action)
        board = Board(self.level_name)
        board_layout = board.refresh_layout(block)

        return (block, tuple(map(tuple, board_layout)))

    def action_cost(self, state, action, next_state):
        return 1

    def is_goal(self, state):
        block = deepcopy(state[0])
        board = Board(self.level_name)
        game_logic = GameLogic(block, board)
        if game_logic.check_win():
            return True

        return False
