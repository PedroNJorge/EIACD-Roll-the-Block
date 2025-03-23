import pygame
from pprint import pprint


class InputHandler:
    def __init__(self, block, board, game_logic):
        self.block = block
        self.game_logic = game_logic
        self.board = board

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
                # self.game_logic.is_fatal()

                # Change Board Layout
                match(self.block.orientation):
                    case "upright":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x1 - 2][self.block.y1] = 2
                        self.board.level.layout[self.block.x2 - 1][self.block.y2] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x1 - 1][self.block.y1] = 2
                        self.board.level.layout[self.block.x2 - 1][self.block.y2] = 2

                    case "vertical":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x1 - 1][self.block.y1] = 1

                self.block.move("up")

            case pygame.K_s:
                match self.block.orientation:
                    case "upright":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x1 + 1][self.block.y1] = 2
                        self.board.level.layout[self.block.x2 + 2][self.block.y2] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x1 + 1][self.block.y1] = 2
                        self.board.level.layout[self.block.x2 + 1][self.block.y2] = 2

                    case "vertical":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x2 + 1][self.block.y2] = 1

                self.block.move("down")

            case pygame.K_a:
                match self.block.orientation:
                    case "upright":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x1][self.block.y1 - 2] = 2
                        self.board.level.layout[self.block.x2][self.block.y2 - 1] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x1][self.block.y1 - 1] = 1

                    case "vertical":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x1][self.block.y1 - 1] = 2
                        self.board.level.layout[self.block.x2][self.block.y2 - 1] = 2

                self.block.move("left")

            case pygame.K_d:
                match self.block.orientation:
                    case "upright":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x1][self.block.y1 + 1] = 2
                        self.board.level.layout[self.block.x2][self.block.y2 + 2] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x2][self.block.y2 + 1] = 1

                    case "vertical":
                        self.board.level.layout[self.block.x1][self.block.y1] = 0
                        self.board.level.layout[self.block.x2][self.block.y2] = 0
                        self.board.level.layout[self.block.x1][self.block.y1 + 1] = 2
                        self.board.level.layout[self.block.x2][self.block.y2 + 1] = 2

                self.block.move("right")

        self.game_logic.update()
        pprint(self.board.level.layout)
        print(f"(({self.block.x1}, {self.block.y1}), ({self.block.x2}, {self.block.y2}))")
        print("---------------------------------")
