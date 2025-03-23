class GameLogic:
    def __init__(self, block, board):
        self.block = block
        self.board = board
        self.game_over = False
        self.level_completed = False

    # Need to change everything related to block's position
    def check_win(self):
        if self.block.orientation == "upright":
            return self.board.is_goal((self.block.x1, self.block.y1))

    def check_lose(self):
        return self.board.is_fatal(((self.block.x1, self.block.y1), (self.block.x2, self.block.y2)))

    def update(self):
        if self.check_win():
            print("win")
            self.level_completed = True
            self.board.switch_level()
        elif self.check_lose():
            print("lose")
            self.game_over = True
