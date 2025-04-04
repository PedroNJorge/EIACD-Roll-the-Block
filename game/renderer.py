import pygame
import sys
from game.block import Block
from game.board import Board
from game.game_logic import GameLogic
from game.input_handler import InputHandler

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 50
FPS = 60

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (51, 51, 255) #grid
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255) #new path discovered by button
PURPLE = (128, 0, 128) #button
TRANSPARENT_BLUE = (0, 0, 255, 128) #glass floor
DARK_GRAY = (50, 50, 50)
LIGHT_BLUE = (173, 216, 230) #sky
HOT_PINK = (255, 0, 127) #block
WHITE_CLOUD = (204, 255, 204) #clouds

#Game states
MAIN_MENU=0
RULES = 1
LEVEL_SELECT = 2
PLAYING = 3
GAME_OVER = 4
LEVEL_COMPLETE = 5

#Mouse to play
class Button:
        def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
                self.rect = pygame.Rect(x, y, width, height)
                self.text = text
                self.color = color
                self.hover_color = hover_color
                self.text_color = text_color
                self.is_hovered = False

        def draw(self, screen):
                color = self.hover_color if self.is_hovered else self.color
                pygame.draw.rec(screen, color, self.rect, border_radius=10)
                pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)

                font = pygame.font.Font(None, 32)
                text_surface = font.renderer(self.text, True, self.text_color)
                text_rect = text_surface.get_rect(center=self.rec.center)
                screen.blit(text_surface, text_rect)

        def update(self, mouse_pos):
                self.is_hovered = self.rect.collidepoint(mouse_pos)

        def is_clicked(self, mouse_pos, mouse_click):
                return self.rect.collidepoint(mouse_pos) and mouse_click

#Running the game itself
class Renderer:
        def __init__(self, screen, board, block):
                self.screen = screen
                pygame.display.set_caption("Roll the Block!")
                self.clock = pygame.time.Clock()
                self.game_state = MAIN_MENU
                self.block = None
                self.board = None
                self.game_logic = None
                self.input_handler = None
                self.init_buttons()

                self.animation_active = False
                self.animation_direction = None
                self.animation_progress = 0
                self.animation_speed = 0.1
                self.old_block_position = None
                self.target_block_position = None

        def draw(self):
                self.screen.fill(LIGHT_BLUE)
                self.camera_offset_x = 0
                self.camera_offset_y = 0

                self.transition_alpha = 0
                self.transition_state = None

        def init_buttons(self):
                center_x = SCREEN_WIDTH // 2
                self.play_button = Button(center_x - 100, 200, 200, 50, "Play", WHITE_CLOUD, (>
        
        def run(self):
        #Game loop
                running = True
                while running:
                        self.clock.tick(FPS)
                        #running = self.handle_events()
                        #self.update_animation()
                        #self.draw()

def main():
    game = Renderer()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
