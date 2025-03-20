import pygame


class Renderer:
    def __init__(self, board, block, tile_size=50):
        self.board = board
        self.block = block
        self.tile_size = tile_size
        # self.screen = pygame.display.set_mode(())
