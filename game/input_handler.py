import pygame


class InputHandler:
    def __init__(self, block, game_logic):
        self.block = block
        self.game_logic = game_logic

    def handle_events(self):
        for event in pygame.event.get():
            match(event.type):
                case pygame.QUIT:
                    return False    # used to update run in main.py

        return True

    def handle_keyboard(self, event):
        match(event.key):
            case pygame.K_UP:
                pass

        self.game_logic.update()

    def state_block(block, board): #Determines the state the block is in
        for i in range (len(board)):
            for j in range (len(board[i])):
                if block[i][j]==1:
                    return "Upright"
                elif block [i][j]==2:
                    if block [i][j+1]==2:
                        return "Vertical"
                else:
                    return "Horizontal"
                
    movements = ["w", "a", "s", "d"]
    
    def move_upright(block, board, movement): #Movements for when the block is upright
        for i in range (len(board)):
            for j in range (len(board[i])):
                if movement=="w":
                    block[i][j]=0
                    block[i-1][j]=2
                    block[i-2][j]=2
                    return block
                elif movement=="a":
                    block[i][j]=0
                    block[i][j-1]=2
                    block[i][j-2]=2
                    return block
                elif movement=="s":
                    block[i][j]=0
                    block[i+1][j]=2
                    block[i+2][j]=2
                    return block
                elif movement=="d":
                    block[i][j]=0
                    block[i][j+1]=2
                    block[i][j+2]=2
                    return block
    
    def move_horizontal(block, board, movement): #Movements for when the block is horizontal
        for i in range (len(board)):
            for j in range (len(board[i])):
                if movement=="w":
                    block[i][j]=0
                    block[i+1][j]=0
                    block[i-1][j]=1
                    return block
                elif movement=="a":
                    block[i][j]=0
                    block[i+1][j]=0
                    block[i][j-1]=2
                    block[i+1][j-1]=2
                    return block
                elif movement=="s":
                    block[i][j]=0
                    block[i+1][j]=0
                    block[i+2][j]=1
                    return block
                elif movement=="d":
                    block[i][j]=0
                    block[i+1][j]=0
                    block[i][j+1]=2
                    block[i+1][j+1]=2
                    return block
    
    def move_vertical(block, board, movement): #Movements for when the block is vertical
        for i in range (len(board)):
            for j in range (len(board[i])):
                if movement=="w":
                    block[i][j]=0
                    block[i][j+1]=0
                    block[i-1][j]=2
                    block[i-1][j+1]=2
                    return block
                elif movement=="a":
                    block[i][j]=0
                    block[i][j-1]=0
                    block[i][j-2]=1
                    return block
                elif movement=="s":
                    block[i][j]=0
                    block[i][j+1]=0
                    block[i+1][j]=2
                    block[i+1][j+1]=2
                    return block
                elif movement=="d":
                    block[i][j]=0
                    block[i][j+1]=0
                    block[i][j+2]=1
                    return block
