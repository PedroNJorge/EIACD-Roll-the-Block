class GameLogic:
    def __init__(self, block, board):
        self.block = block
        self.board = board
        self.game_over = False

    def check_win(self):
        return self.board.is_goal((self.block.x, self.block.y))

    def check_lose(self):
        return self.board.is_fatal((self.block.x, self.block.y))

    def update(self):
        if self.check_win():
            print("win")
            self.game_over = True
        elif self.check_lose():
            print("lose")
            self.game_over = False
