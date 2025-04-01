import pygame


class Renderer:
    def __init__(self, block, board, width=800, height=600, tile_size=50):
        self.block = block
        self.board = board
        self.tile_size = tile_size
        self.screen = pygame.display.set_mode((width, height))
