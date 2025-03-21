import pygame


class InputHandler:
    def __init__(self, block, board, game_logic):
        self.block = block
        self.game_logic = game_logic
        self.board = board

    def handle_events(self):
        for event in pygame.event.get():
            match(event.type):
                case pygame.QUIT:
                    return False    # used to update run in main.py

        return True
        
    def handle_keyboard(self, event):
        match(event.key):
            case pygame.K_w:
                self.board.level.layout[self.block.x][self.block.y] = 0
                match(self.block.orientation):
                    case "upright":
                        self.board.level.layout[self.block.x - 1][self.block.y] = 2
                        self.board.level.layout[self.block.x - 2][self.block.y] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x + 1][self.block.y] = 0
                        self.board.level.layout[self.block.x - 1][self.block.y] = 1

                    case "vertical":
                        self.board.level.layout[self.block.x][self.block.y + 1] = 0
                        self.board.level.layout[self.block.x - 1][self.block.y] = 2
                        self.board.level.layout[self.block.x - 1][self.block.y + 1] = 2

                self.block.move("up")

            case pygame.K_s:
                self.board.level.layout[self.block.x][self.block.y] = 0
                match(self.block.orientation):
                    case "upright":
                        self.board.level.layout[self.block.x + 1][self.block.y] = 2
                        self.board.level.layout[self.block.x + 2][self.block.y] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x + 1][self.block.y] = 0
                        self.board.level.layout[self.block.x + 2][self.block.y] = 1
                    
                    case "vertical":
                        self.board.level.layout[self.block.x][self.block.y + 1] = 0
                        self.board.level.layout[self.block.x + 1][self.block.y] = 2
                        self.board.level.layout[self.block.x + 1][self.block.y + 1] = 2

                self.block.move("down")

            case pygame.K_a:
                self.board.level.layout[self.block.x][self.block.y] = 0
                match(self.block.orientation):
                    case "upright":
                        self.board.level.layout[self.block.x][self.block.y - 1] = 2
                        self.board.level.layout[self.block.x][self.block.y - 2] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x + 1][self.block.y] = 0
                        self.board.level.layout[self.block.x][self.block.y - 1] = 2
                        self.board.level.layout[self.block.x + 1][self.block.y - 1] = 2
                    
                    case "vertical":
                        self.board.level.layout[self.block.x][self.block.y - 1] = 0
                        self.board.level.layout[self.block.x][self.block.y - 2] = 1

                self.block.move("left")

            case pygame.K_d:
                self.board.level.layout[self.block.x][self.block.y] = 0
                match(self.block.orientation):
                    case "upright":
                        self.board.level.layout[self.block.x][self.block.y + 1] = 2
                        self.board.level.layout[self.block.x][self.block.y + 2] = 2

                    case "horizontal":
                        self.board.level.layout[self.block.x + 1][self.block.y] = 0
                        self.board.level.layout[self.block.x][self.block.y + 1] = 2
                        self.board.level.layout[self.block.x + 1][self.block.y + 1] = 2
                    
                    case "vertical":
                        self.board.level.layout[self.block.x][self.block.y + 1] = 0
                        self.board.level.layout[self.block.x][self.block.y + 2] = 1
                        
                self.block.move("right")

        self.game_logic.update()
