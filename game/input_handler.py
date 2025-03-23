import pygame
from pprint import pprint


class InputHandler:
    def __init__(self, block, board, game_logic):
        self.block = block
        self.board = board
        self.game_logic = game_logic

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return False    # used to update run in main.py
                case pygame.KEYDOWN:
                    self.handle_keyboard(event)

        return True

    def handle_keyboard(self, event):
        match event.key:
            case pygame.K_w:
                self.block.move("up")
            case pygame.K_s:
                self.block.move("down")
            case pygame.K_a:
                self.block.move("left")
            case pygame.K_d:
                self.block.move("right")

        self.board.refresh_layout(self.block)
        self.game_logic.update()

        pprint(self.board.level.layout)
        print(f"(({self.block.x1}, {self.block.y1}), ({self.block.x2}, {self.block.y2}))")
        print("---------------------------------")
